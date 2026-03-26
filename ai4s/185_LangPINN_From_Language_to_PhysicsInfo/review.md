# Lang-PINN: From Language to Physics-Informed Neural Networks via a Multi-Agent Framework

> **저자**: Xin He, Liangliang You, Hongduan Tian, Bo Han, Ivor Tsang, Yew-Soon Ong | **날짜**: 2025-10-03 | **DOI**: 10.48550/arXiv.2510.05158
> **리뷰 모드**: PDF

---

## Essence
We present Lang-PINN, an LLM-driven multi-agent system that builds trainable PINNs directly from natural language task descriptions.

## Originality (Abstract 기반)
- [authorship, action] We present Lang-PINN, an LLM-driven multi-agent system that builds trainable PINNs directly from natural language task descriptions.
- [action, approach] Lang-PINN coordinates four complementary agents: a PDE Agent that parses task descriptions into symbolic PDEs, a PINN Agent that selects architectures, a Code Agent that generates modular implementations, and a Feedback Agent that executes and diagnoses errors for iterative refinement.
- [action, finding] This design transforms informal task statements into executable and verifiable PINN code.
- [finding, result] Experiments show that Lang-PINN achieves substantially lower errors and greater robustness than competitive baselines: mean squared error (MSE) is reduced by up to 3--5 orders of magnitude, end-to-end execution success improves by more than 50\%, and reduces time overhead by up to 74\%.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 2 |
| Technical Soundness | 4 |
| Overall | 3 |

**총평**: 의미 있는 기여를 하나, 독창성 또는 실험적 검증의 보강이 필요한 연구.
