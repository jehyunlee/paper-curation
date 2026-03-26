# Uncertainty quantification in scientific machine learning: Methods, metrics, and comparisons

> **저자**: Apostolos F. Psaros, Xuhui Meng, Zongren Zou, Ling Guo, George Em Karniadakis | **날짜**: 03/2023 | **DOI**: 10.1016/j.jcp.2022.111902
> **리뷰 모드**: PDF

---

## Essence
In this work, we present a comprehensive framework that includes uncertainty modeling, new and existing solution methods, as well as evaluation metrics and post-hoc improvement approaches. To demonstrate the applicability and reliability of our framework, we present an extensive comparative study in which various methods are tested on prototype problems, including problems with mixed input-output data, and stochastic problems in high dimensions.

## Originality (Abstract 기반)
- [context] However, quantifying errors and uncertainties in NN-based inference is more complicated than in traditional methods.
- [approach, conclusion] This is because in addition to aleatoric uncertainty associated with noisy data, there is also uncertainty due to limited data, but also due to NN hyperparameters, overparametrization, optimization and sampling errors as well as model misspecification.
- [finding, result, conclusion] Although there are some recent works on uncertainty quantification (UQ) in NNs, there is no systematic investigation of suitable methods towards quantifying the total uncertainty effectively and efficiently even for function approximation, and there is even less work on solving partial differential equations and learning operator mappings between infinite-dimensional function spaces using NNs.
- [authorship, novelty, action, finding, approach] In this work, we present a comprehensive framework that includes uncertainty modeling, new and existing solution methods, as well as evaluation metrics and post-hoc improvement approaches.
- [authorship, action, finding, learned] To demonstrate the applicability and reliability of our framework, we present an extensive comparative study in which various methods are tested on prototype problems, including problems with mixed input-output data, and stochastic problems in high dimensions.
- [authorship, approach] In the Appendix, we include a comprehensive description of all the UQ methods employed.
- [authorship, action] Further, to help facilitate the deployment of UQ in Scientific Machine Learning research and practice, we present and develop in [1] an open-source Python library (github.com/Crunch-UQ4MI/neuraluq), termed NeuralUQ, that is accompanied by an educational tutorial and additional computational experiments.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 3 |
| Technical Soundness | 4 |
| Overall | 4 |

**총평**: 높은 수준의 기여와 탄탄한 실험적 검증을 보여주는 연구.
