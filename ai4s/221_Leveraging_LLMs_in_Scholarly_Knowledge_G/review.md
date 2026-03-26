# Leveraging LLMs in Scholarly Knowledge Graph Question Answering

> **저자**: Tilahun Abedissa Taffa, Ricardo Usbeck | **날짜**: 2023-11-16 | **Journal**: arXiv | **Link**: [https://arxiv.org/abs/2311.09841](https://arxiv.org/abs/2311.09841)

---

## Essence

This paper presents a scholarly Knowledge Graph Question Answering (KGQA) that answers bibliographic natural language questions by leveraging a large language model (LLM) in a few-shot manner.

## Motivation

- **Gap**: Our system achieves an F1 score of 99.0%, on SciQA - one of the Scholarly-QALD-23 challenge benchmarks.

## Achievement

1. Our system achieves an F1 score of 99.0%, on SciQA - one of the Scholarly-QALD-23 challenge benchmarks.

## How

- This paper presents a scholarly Knowledge Graph Question Answering (KGQA) that answers bibliographic natural language questions by leveraging a large language model (LLM) in a few-shot manner.
- The model initially identifies the top-n similar training questions related to a given test question via a BERT-based sentence encoder and retrieves their corresponding SPARQL.
- Using the top-n similar question-SPARQL pairs as an example and the test question creates a prompt.
- Our system achieves an F1 score of 99.0%, on SciQA - one of the Scholarly-QALD-23 challenge benchmarks.

## Originality


**Trigger-based extraction**: This paper presents a scholarly Knowledge Graph Question Answering (KGQA) that answers bibliographic natural language questions by leveraging a large language model (LLM) in a few-shot manner.. The model initially identifies the top-n similar training questions related to a given test question via a BERT-based sentence encoder and retrieves their corresponding SPARQL.. Using the top-n similar question-SPARQL pairs as an example and the test question creates a prompt.. Then pass the prompt to the LLM and generate a SPARQL.. Finally, runs the SPARQL against the underlying KG - ORKG (Open Research KG) endpoint and returns an answer.. Our system achieves an F1 score of 99.0%, on SciQA - one of the Scholarly-QALD-23 challenge benchmarks.

## Limitation & Further Study

### 저자들이 언급한 한계

- Abstract에서 명시적 한계 언급 없음

### 후속 연구

- 해당 연구의 확장 및 다른 도메인 적용 가능성 탐구

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 4/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: This paper presents a scholarly Knowledge Graph Question Answering (KGQA) that answers bibliographic natural language questions by leveraging a large language model (LLM) in a few-shot manner을 다룬 연구로, AI for Science 관점에서 의미 있는 기여를 한다.
