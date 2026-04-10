"""Topic별 카테고리 동적 로딩 + 공통 slug 변환.

카테고리 목록은 _new_classification.json에서 읽어옴 (topic_modeling.py가 생성).
하드코딩 없이 bottom-up 클러스터링 결과를 그대로 사용.
"""
import json
import os
from functools import lru_cache

# config_loader는 순환 import 방지를 위해 지연 로딩
_config_loaded = False
_papers_dir = None
_get_topic_dir = None


def _ensure_config():
    global _config_loaded, _papers_dir, _get_topic_dir
    if not _config_loaded:
        import sys
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from config_loader import PAPERS_DIR, get_topic_dir
        _papers_dir = str(PAPERS_DIR)
        _get_topic_dir = get_topic_dir
        _config_loaded = True


def category_slug(cat_name):
    """카테고리 이름 → 파일명용 slug. 모든 스크립트에서 이 함수를 사용할 것."""
    return cat_name.replace(" ", "_").replace("&", "and").replace(",", "")


def get_categories(topic):
    """topic의 카테고리 목록을 _new_classification.json에서 동적으로 로드.

    Returns:
        list[str]: 카테고리 이름 목록 (항상 "Other" 포함)
    """
    _ensure_config()
    topic_dir = str(_get_topic_dir(topic))
    cls_path = os.path.join(topic_dir, "_new_classification.json")

    if os.path.exists(cls_path):
        with open(cls_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        cats = [c["name"] for c in data.get("categories", [])]
        if "Other" not in cats:
            cats.append("Other")
        return cats

    # fallback: _papers_index.json에서 추출
    idx_path = os.path.join(_papers_dir, "_papers_index.json")
    if os.path.exists(idx_path):
        with open(idx_path, "r", encoding="utf-8") as f:
            papers = json.load(f)
        cats = sorted(set(
            p.get("classifications", {}).get(topic, {}).get("primary_category", "Other")
            for p in papers if topic in p.get("topics", [])
        ))
        if "Other" not in cats:
            cats.append("Other")
        return cats

    return ["Other"]


# 하위 호환: 기존 코드가 CATEGORIES_BY_TOPIC["ai4s"] 형태로 접근하는 경우 지원
class _CategoriesProxy(dict):
    """dict-like proxy that loads categories on demand."""
    def __missing__(self, topic):
        cats = get_categories(topic)
        self[topic] = cats
        return cats

    def get(self, topic, default=None):
        try:
            return self[topic]
        except Exception:
            return default if default is not None else ["Other"]


CATEGORIES_BY_TOPIC = _CategoriesProxy()
