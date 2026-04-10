"""PaperBanana wrapper: path management, agent initialization, and diagram generation."""
import asyncio
import base64
import logging
import os
import shutil
import sys
from io import BytesIO
from pathlib import Path

logger = logging.getLogger(__name__)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config_loader import get_paperbanana_dir

_pb_dir = get_paperbanana_dir()
if not _pb_dir:
    raise ValueError(
        "paperbanana_dir not set. "
        "Set it in config.json or PAPERBANANA_DIR env var. "
        "Clone from: https://github.com/dwzhu-pku/PaperBanana"
    )
PAPERBANANA_DIR = Path(_pb_dir)


def _ensure_path():
    """Add PaperBanana to sys.path if not already there."""
    if str(PAPERBANANA_DIR) not in sys.path:
        sys.path.insert(0, str(PAPERBANANA_DIR))


def _ensure_config():
    """Copy model_config.template.yaml to model_config.yaml if missing."""
    configs_dir = PAPERBANANA_DIR / "configs"
    config_path = configs_dir / "model_config.yaml"
    template_path = configs_dir / "model_config.template.yaml"
    if not config_path.exists() and template_path.exists():
        shutil.copy2(template_path, config_path)


def _ensure_dataset(task_name: str = "diagram"):
    """Download PaperBananaBench reference data from HuggingFace if not present."""
    data_dir = PAPERBANANA_DIR / "data" / "PaperBananaBench" / task_name
    ref_path = data_dir / "ref.json"
    images_dir = data_dir / "images"
    if ref_path.exists() and images_dir.exists():
        return
    try:
        from huggingface_hub import snapshot_download
        logger.info(f"Downloading PaperBananaBench/{task_name} from HuggingFace...")
        snapshot_download(
            "dwzhu/PaperBananaBench",
            repo_type="dataset",
            allow_patterns=[f"{task_name}/*"],
            local_dir=str(PAPERBANANA_DIR / "data" / "PaperBananaBench"),
        )
    except ImportError:
        logger.warning("huggingface_hub not installed — skipping dataset download, "
                       "falling back to retrieval_setting=none")
    except Exception as e:
        logger.warning(f"Dataset download failed: {e} — using retrieval_setting=none")


def _extract_final_image_b64(result: dict, exp_mode: str) -> str | None:
    """Return the base64-encoded final image from a pipeline result dict."""
    task_name = "diagram"

    # Try critic rounds 3 → 0
    for round_idx in range(3, -1, -1):
        key = f"target_{task_name}_critic_desc{round_idx}_base64_jpg"
        if key in result and result[key]:
            return result[key]

    # Fallback: stylist (demo_full) or planner
    if exp_mode == "demo_full":
        key = f"target_{task_name}_stylist_desc0_base64_jpg"
    else:
        key = f"target_{task_name}_desc0_base64_jpg"
    return result.get(key)


def generate_diagram(method: str, caption: str,
                     aspect_ratio: str = "16:9",
                     critic_rounds: int = 3,
                     exp_mode: str = "demo_full",
                     retrieval_setting: str = "auto",
                     output_path: str | Path | None = None) -> bytes | None:
    """Generate a diagram image via PaperBanana.

    Args:
        method: Markdown description of the diagram content.
        caption: Figure caption / visual intent string.
        aspect_ratio: Image aspect ratio (e.g. "16:9", "21:9", "3:2").
        critic_rounds: Number of PaperBanana critic iterations.
        exp_mode: "demo_full" (with Stylist) or "demo_planner_critic" (without).
        retrieval_setting: "auto" (reference learning), "none" (no refs).
        output_path: If provided, save the PNG bytes to this path.

    Returns:
        PNG image bytes, or None if generation failed.
    """
    prev_cwd = os.getcwd()
    try:
        _ensure_path()
        os.chdir(str(PAPERBANANA_DIR))
        _ensure_config()

        # Download reference dataset for auto retrieval
        if retrieval_setting == "auto":
            _ensure_dataset("diagram")
            # If dataset still not available, fall back to none
            ref_path = PAPERBANANA_DIR / "data" / "PaperBananaBench" / "diagram" / "ref.json"
            if not ref_path.exists():
                retrieval_setting = "none"
                logger.info("Reference data not available, using retrieval_setting=none")

        from agents.planner_agent import PlannerAgent
        from agents.visualizer_agent import VisualizerAgent
        from agents.critic_agent import CriticAgent
        from agents.retriever_agent import RetrieverAgent
        from agents.stylist_agent import StylistAgent
        from agents.vanilla_agent import VanillaAgent
        from agents.polish_agent import PolishAgent
        from utils import config
        from utils.paperviz_processor import PaperVizProcessor

        exp_config = config.ExpConfig(
            dataset_name="Demo",
            split_name="demo",
            exp_mode=exp_mode,
            retrieval_setting=retrieval_setting,
            work_dir=PAPERBANANA_DIR,
        )

        processor = PaperVizProcessor(
            exp_config=exp_config,
            vanilla_agent=VanillaAgent(exp_config=exp_config),
            planner_agent=PlannerAgent(exp_config=exp_config),
            visualizer_agent=VisualizerAgent(exp_config=exp_config),
            stylist_agent=StylistAgent(exp_config=exp_config),
            critic_agent=CriticAgent(exp_config=exp_config),
            retriever_agent=RetrieverAgent(exp_config=exp_config),
            polish_agent=PolishAgent(exp_config=exp_config),
        )

        data = {
            "filename": "diagram",
            "caption": caption,
            "content": method,
            "visual_intent": caption,
            "additional_info": {"rounded_ratio": aspect_ratio},
            "max_critic_rounds": critic_rounds,
            "candidate_id": 0,
        }

        logger.info(f"Generating diagram via PaperBanana "
                     f"(mode={exp_mode}, retrieval={retrieval_setting})...")

        async def _run():
            results = []
            async for result in processor.process_queries_batch(
                [data], max_concurrent=1, do_eval=False
            ):
                results.append(result)
            return results

        results = asyncio.run(_run())

        if not results:
            logger.error("PaperBanana returned no results")
            return None

        b64 = _extract_final_image_b64(results[0], exp_mode)
        if not b64:
            logger.error("No image found in PaperBanana result")
            return None

        from PIL import Image

        if "," in b64:
            b64 = b64.split(",")[1]
        img_data = base64.b64decode(b64)

        img = Image.open(BytesIO(img_data))
        png_buf = BytesIO()
        img.save(png_buf, "PNG")
        png_bytes = png_buf.getvalue()

        if output_path is not None:
            out = Path(output_path)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(png_bytes)
            logger.info(f"Diagram saved: {out}")

        return png_bytes

    except Exception as e:
        logger.error(f"PaperBanana diagram generation failed: {e}")
        return None
    finally:
        os.chdir(prev_cwd)
