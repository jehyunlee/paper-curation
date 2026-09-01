"""공개용 기관 표의 유출 방지 계약 (2026-09-01).

한 번 푸시하면 되돌릴 수 없는 종류라, 무엇을 싣는지가 아니라 **무엇이 절대
새면 안 되는지**를 고정한다.

원본 서지 DB 에서 공개 금지인 것:
  * 운영자 Google Drive 절대경로 — 계정 이메일이 `metadata_json` 4,184행에 있다
  * PDF 앞머리(`header_raw`) — 교신저자 이메일 2,074개가 추출된다
  * 개인 Zotero 라이브러리 키
  * `paper_institutions.raw_name` 에 섞인 이메일 143건과 저자 나열

raw_name 을 블랙리스트로 거르려던 두 시도는 실측에서 모두 실패했다:
  * 이름 나열 패턴 → `Oak Ridge National Laboratory,` 같은 실재 기관이 죽었다
  * 기관어 필수 → `Tencent`·`Genentech`·`DeepMind Technologies Limited` 가 죽었다
그래서 화이트리스트다. 안전이 확실하지 않으면 그 칸을 비우고, 기관·상위·국가는
남긴다. 여기 있는 문자열은 전부 실제 코퍼스에서 뽑은 것이다.

Run:
  PYTHONUTF8=1 /opt/homebrew/Caskroom/miniconda/base/envs/py312/bin/python \
      pipeline/tests/test_export_institutions_public.py
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from export_institutions_public import (  # noqa: E402
    clean_raw_name, is_publishable_raw,
)


def publishable(raw):
    """실제 파이프라인과 같은 순서: 정리 → 판정."""
    return is_publishable_raw(clean_raw_name(raw))


class PiiMustNeverSurviveTests(unittest.TestCase):

    def test_correspondence_tail_is_stripped(self):
        raw = "3University of Waterloo. Correspondence to: Tianshu Yu <tianshuyu@cuhk.edu.cn>"
        out = clean_raw_name(raw)
        self.assertNotIn("@", out)
        self.assertNotIn("Tianshu", out)
        self.assertEqual(out, "University of Waterloo")

    def test_hyphenated_correspondence_tail_is_stripped(self):
        raw = "3ECNU Corre- spondence to: Guangtao Zhai <zhaiguangtao@pjlab.org.cn>"
        out = clean_raw_name(raw)
        self.assertNotIn("@", out)
        self.assertNotIn("Guangtao", out)

    def test_orcid_is_stripped(self):
        raw = ("Assoc. Prof. Dr., Ordu University, Ulubey VS, "
               "nalantastan@odu.edu.tr, ORCID: 0000-0002-5833-4498")
        out = clean_raw_name(raw)
        self.assertNotIn("@", out)
        self.assertNotIn("0000-0002-5833-4498", out)

    def test_author_lists_are_not_published(self):
        for raw in (
            "Zhengwei Tao, Dingchu Zhang, Zekun Xi, Gang Fu, Yong Jiang(), "
            "Pengjun Xie, Fei Huang, Jingren Zhou Tongyi Lab , Alibaba Group",
            "Montse Gonzalez Arenas, Hao-Tien Lewis Chiang, Tom Erez, "
            "Leonard Hasenclever, Jan Humplik, Brian Ichter",
            "Pete Florence, Andy Zeng, Jonathan Tompson, Igor Mordatch, "
            "Yevgen Chebotar, Pierre Sermanet, Noah Brown",
            "Savas Tsikis, Boston Children's Hospital and Harvard Medical "
            "School, United States Jianghua Zhan, Tianjin",
            "Zenglin Xu Fudan University, Shanghai Academy of AI for Science "
            "Yuan Cheng Fudan University",
        ):
            self.assertFalse(publishable(raw), raw[:60])

    def test_no_email_survives_publication(self):
        for raw in (
            "3University of Waterloo. Correspondence to: Tianshu Yu <t@cuhk.edu.cn>",
            "Ordu University, nalantastan@odu.edu.tr",
        ):
            out = clean_raw_name(raw)
            if is_publishable_raw(out):
                self.assertNotIn("@", out, raw[:50])


class RealInstitutionsMustSurviveTests(unittest.TestCase):
    """과잉 차단이 표를 쓸모없게 만든다. 실측으로 죽었던 것들을 고정한다."""

    def test_companies_without_an_org_word(self):
        """기관어 필수 규칙이 죽였던 것들."""
        for raw in ("NVIDIA", "Tencent", "Genentech", "Google DeepMind",
                    "ETH Zurich", "ByteDance Seed", "Galbot"):
            self.assertTrue(publishable(raw), raw)

    def test_place_named_institutions(self):
        """이름 나열 패턴이 죽였던 것들 — 지명이 사람 이름처럼 보인다."""
        for raw in ("Oak Ridge National Laboratory, Oak Ridge, TN, USA",
                    "New York Genome Center, New York, NY, USA",
                    "The Alan Turing Institute, London, United Kingdom",
                    "Cooperative Medianet Innovation Center, Shanghai Jiao Tong University"):
            self.assertTrue(publishable(raw), raw)

    def test_person_named_buildings_are_institutions(self):
        for raw in ("John A. Paulson School of Engineering and Applied Sciences, "
                    "Harvard University, Boston, MA",
                    "IBM Thomas J. Watson Research Center"):
            self.assertTrue(publishable(raw), raw)

    def test_leading_affiliation_marker_is_removed(self):
        self.assertEqual(clean_raw_name("23Max-Planck Institute for Sustainable Materials"),
                         "Max-Planck Institute for Sustainable Materials")
        self.assertEqual(clean_raw_name("2University of Missouri-Columbia"),
                         "University of Missouri-Columbia")

    def test_acronym_with_at_sign_is_not_mistaken_for_email(self):
        """`IIT@MIT` 는 이메일이 아니다 — @ 뒤에 점이 있어야 이메일이다."""
        self.assertTrue(publishable("IIT@MIT"))


class ExportShapeTests(unittest.TestCase):

    def test_control_characters_are_removed(self):
        """xlsx 는 제어문자를 거부한다 — 실측 9건 있었다."""
        self.assertNotIn("\x07", clean_raw_name("Alibaba\x07Group"))

    def test_overlong_strings_are_not_published(self):
        self.assertFalse(publishable("A University of " + "x" * 300))

    def test_empty_and_marker_only_strings_are_not_published(self):
        for raw in ("", "   ", "12", "3,", "*†"):
            self.assertFalse(publishable(raw), repr(raw))


if __name__ == "__main__":
    unittest.main(verbosity=2)
