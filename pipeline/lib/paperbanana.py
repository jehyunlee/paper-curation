"""PaperBanana wrapper: path management, agent initialization, and diagram generation."""
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
    """ref.json 에서 GT 이미지가 디스크에 없는 reference 엔트리를 제거한다.

    왜 (2026-06-12 실측): HF LFS 부분 다운로드로 ref.json 이 참조하는 이미지 중
    소수(예 298 중 4)가 누락될 수 있다. RetrieverAgent 가 그중 하나를 reference
    로 고르면 ``FileNotFoundError`` 로 *해당 카테고리 다이어그램 생성이 통째로
    실패* 한다(비결정적). 디렉토리 존재만 보던 기존 가드는 이를 못 잡았다.
    누락 엔트리만 외과적으로 제거하면 남은 다수(예 294)로 retrieval 품질을
    유지하면서 landmine 을 없앤다. 원본은 .orig 로 1회 백업, 멱등.
    """
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


def _resolve_output_path(output_path: str | Path | None) -> Path | None:
    """Resolve caller-relative output before PaperBanana changes process cwd."""
    if output_path is None:
        return None
    return Path(output_path).expanduser().resolve()


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
    # PaperBanana temporarily changes cwd below. Resolve a caller-relative target
    # before that transition so generated images stay in the requested project path.
    resolved_output = _resolve_output_path(output_path)
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

        # Each generate_diagram call uses a fresh asyncio.run() event loop.
        # PaperBanana caches its async LLM clients (google-genai / AsyncAnthropic)
        # as module globals bound to the FIRST loop, so the 2nd+ call dies with
        # "Event loop is closed". Recreate the clients so they rebind to this loop.
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

        if resolved_output is not None:
            resolved_output.parent.mkdir(parents=True, exist_ok=True)
            resolved_output.write_bytes(png_bytes)
            logger.info(f"Diagram saved: {resolved_output}")

        return png_bytes

    except Exception as e:
        # Log full traceback so root causes (e.g. ModuleNotFoundError for
        # PaperBanana's own deps) surface in the wrapper's stderr instead of
        # being swallowed into a generic "returned None". Then re-raise so the
        # outer watchdog/retry layer can decide whether it's transient.
        logger.exception(f"PaperBanana diagram generation failed: {e}")
        raise
    finally:
        os.chdir(prev_cwd)
