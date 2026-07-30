"""PaperBanana wrapper: path management, agent initialization, and diagram generation.

Prefers Hermes gateway for image generation when configured; falls back to
PaperBanana (vendor image APIs) only if Hermes is unset or fails.
"""
import asyncio
import base64
import json
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
PAPERBANANA_DIR = Path(_pb_dir) if _pb_dir else None


def _ensure_path():
    """Add PaperBanana to sys.path if not already there."""
    if PAPERBANANA_DIR is None:
        raise ValueError(
            "paperbanana_dir not set. "
            "Set it in config.json or PAPERBANANA_DIR env var, "
            "or configure Hermes (HERMES_GATEWAY_*) for diagram generation. "
            "Clone from: https://github.com/dwzhu-pku/PaperBanana"
        )
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
        _prune_ref_to_available(data_dir)
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
    _prune_ref_to_available(data_dir)


def _prune_ref_to_available(data_dir: Path):
    """ref.json 에서 GT 이미지가 디스크에 없는 reference 엔트리를 제거한다."""
    ref_path = data_dir / "ref.json"
    images_dir = data_dir / "images"
    if not ref_path.exists() or not images_dir.is_dir():
        return
    try:
        with open(ref_path, encoding="utf-8") as f:
            entries = json.load(f)
        if not isinstance(entries, list):
            return

        def _img_ok(e):
            p = e.get("path_to_gt_image") or ""
            if not p:
                return False
            cand = Path(p)
            for q in (cand, data_dir / p, images_dir / cand.name):
                if q.exists():
                    return True
            return False

        kept = [e for e in entries if _img_ok(e)]
        dropped = len(entries) - len(kept)
        if dropped <= 0:
            return
        backup = data_dir / "ref.orig.json"
        if not backup.exists():
            shutil.copy2(ref_path, backup)
        tmp = ref_path.with_suffix(".json.tmp")
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(kept, f, ensure_ascii=False)
        os.replace(tmp, ref_path)
        logger.warning(
            f"[paperbanana] ref.json: dropped {dropped} reference(s) with "
            f"missing GT images, kept {len(kept)} (backup: ref.orig.json)")
    except Exception as e:
        logger.warning(f"[paperbanana] ref.json prune skipped: {e}")


def _extract_final_image_b64(result: dict, exp_mode: str) -> str | None:
    """Return the base64-encoded final image from a pipeline result dict."""
    task_name = "diagram"

    for round_idx in range(3, -1, -1):
        key = f"target_{task_name}_critic_desc{round_idx}_base64_jpg"
        if key in result and result[key]:
            return result[key]

    if exp_mode == "demo_full":
        key = f"target_{task_name}_stylist_desc0_base64_jpg"
    else:
        key = f"target_{task_name}_desc0_base64_jpg"
    return result.get(key)


def _generate_via_paperbanana(method: str, caption: str,
                              aspect_ratio: str = "16:9",
                              critic_rounds: int = 3,
                              exp_mode: str = "demo_full",
                              retrieval_setting: str = "auto",
                              output_path: str | Path | None = None) -> bytes | None:
    """Legacy PaperBanana path (vendor image APIs)."""
    prev_cwd = os.getcwd()
    try:
        _ensure_path()
        os.chdir(str(PAPERBANANA_DIR))
        _ensure_config()

        if retrieval_setting == "auto":
            _ensure_dataset("diagram")
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

        try:
            from utils import generation_utils as _gu
            _gu.reinitialize_clients()
        except Exception as _e:
            logger.warning(f"reinitialize_clients skipped: {_e}")
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
        logger.exception(f"PaperBanana diagram generation failed: {e}")
        raise
    finally:
        os.chdir(prev_cwd)


def generate_diagram(method: str, caption: str,
                     aspect_ratio: str = "16:9",
                     critic_rounds: int = 3,
                     exp_mode: str = "demo_full",
                     retrieval_setting: str = "auto",
                     output_path: str | Path | None = None) -> bytes | None:
    """Generate a diagram image — Hermes first, PaperBanana fallback.

    Args:
        method: Markdown description of the diagram content.
        caption: Figure caption / visual intent string.
        aspect_ratio: Image aspect ratio (e.g. "16:9", "21:9", "3:2").
        critic_rounds: Number of PaperBanana critic iterations (fallback only).
        exp_mode: PaperBanana mode (fallback only).
        retrieval_setting: PaperBanana retrieval (fallback only).
        output_path: If provided, save the PNG bytes to this path.

    Returns:
        PNG image bytes, or None if generation failed.
    """
    # 1) Hermes preferred path
    try:
        from lib import hermes_image
        if hermes_image.available():
            logger.info("Generating diagram via Hermes gateway...")
            png = hermes_image.generate_diagram(
                method, caption, aspect_ratio=aspect_ratio,
                output_path=output_path)
            if png:
                return png
            logger.warning("Hermes returned no image — falling back to PaperBanana")
    except Exception as e:
        logger.warning("Hermes diagram path failed (%s) — PaperBanana fallback", e)

    # 2) PaperBanana fallback
    if PAPERBANANA_DIR is None:
        logger.error(
            "No Hermes image and paperbanana_dir unset — cannot generate diagram")
        return None
    return _generate_via_paperbanana(
        method, caption, aspect_ratio=aspect_ratio,
        critic_rounds=critic_rounds, exp_mode=exp_mode,
        retrieval_setting=retrieval_setting, output_path=output_path)
