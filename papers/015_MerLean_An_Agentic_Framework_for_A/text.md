# arXiv:2602.16554v1[cs.LO]18 Feb 2026

## MERLEAN: AN AGENTIC FRAMEWORK FOR AUTOFORMALIZATION IN QUANTUM COMPUTATION

Yuanjie Ren∗ Massachusetts Institute of Technology Cambridge, MA 02139 yuanjie@mit.edu

Yidi Qi∗ Northeastern University Boston, MA 02115 y.qi@northeastern.edu

Jinzheng Li∗ Northeastern University Boston, MA 02115 li.jinzh@northeastern.edu

ABSTRACT

We introduce MerLean, a fully automated agentic framework for autoformalization in quantum computation. MerLean extracts mathematical statements from LATEX source files, formalizes them into verified Lean 4 code built on Mathlib, and translates the result back into human-readable LATEX for semantic review. We evaluate MerLean on three theoretical quantum computing papers producing 2,050 Lean declarations from 114 statements in total. MerLean achieves end-to-end formalization on all three papers, reducing the verification burden to only the newly introduced definitions and axioms. Our results demonstrate that agentic autoformalization can scale to frontier research, offering both a practical tool for machine-verified peer review and a scalable engine for mining high-quality synthetic data to train future reasoning models. Our approach can also be generalized to any other rigorous research in mathematics and theoretical physics.

1 INTRODUCTION

The goal of autoformalization (Szegedy, 2020) is to automatically translate mathematical statements from natural language into formal code verifiable by systems such as Isabelle (Paulson, 1994), Coq (Team, 2024), and Lean (Moura & Ullrich, 2021). Recent work has shown that Large Language Models (LLMs) are well suited to this task due to their semantic processing capabilities (Wu et al., 2022; Jiang et al., 2022; Tarrach et al., 2024; Weng et al., 2025).

While most research in autoformalization focuses on pure mathematics, applications in physics have also attracted significant attention: Lean libraries such as PhysLean/HepLean (Tooby-Smith, 2024) and Lean-QuantumInfo (Meiburg et al., 2025) are currently under development, with the latter specifically utilizing autoformalization tools to accelerate the process. Theoretical quantum computation serves as an ideal testbed for this workflow. The volume of submissions to the arXiv quant-ph category reached 11,891 articles in 2025 (arXiv, 2025), creating a verification bottleneck that threatens to outpace the peer-review system. Functionally, the field operates as a subfield of applied mathematics, exhibiting deep connections to linear algebra, graph theory, and algebraic topology. The rigorous nature of these results makes them suitable for neuro-symbolic verification, while strong industrial interest ensures practical impact.

∗Equal contribution.

In this work, we introduce MerLean, a fully automated agentic framework designed to extract, organize, and formalize mathematical statements from LATEX source files, operating without human-inthe-loop intervention during the formalization process. After formalization succeeds, we run a second agent that “autoinformalizes” the verified code back into natural language, generating a blueprint for human experts to review the semantic alignment between the formal code and the original intent. We evaluate MerLean on three papers in theoretical quantum computing: one unpublished manuscript (guaranteeing zero data contamination) and two previously published works. MerLean achieved end-to-end formalization on all three papers, introducing necessary definitions and axioms where results depend on mathematical machinery not yet available in Mathlib. An interactive example of the formalization output is available at https://doxtor6.github.io/MerLean-examples/. The scope of this framework extends beyond quantum computation. Any discipline that relies on formal mathematical proofs can use this neuro-symbolic approach to scale verification and accelerate discovery.

- 2 RELATED WORKS

LLM-based autoformalization and automated theorem provers demonstrated promising capabilities on competition-level problems (Wu et al., 2022; Jiang et al., 2022). Subsequent work improved upon these foundations by addressing proof detail expansion (Tarrach et al., 2024) and faithfulness verification (Li et al., 2024; Liu et al., 2025; Peng et al., 2025). Extensions to domain-specific applications include Euclidean geometry (Murphy et al., 2024), biomedical text (Zhang et al., 2025), and physics (Zhang et al., 2026).

Recent work has shifted toward agentic systems that couple frontier LLMs with tool integration for interactive theorem proving. Breen et al. (2025) demonstrated Ax-Prover, an MCP-based multi-agent system using Claude Sonnet that outperforms specialized provers on out-of-domain benchmarks. Xu & Odersky (2026) demonstrated “agentic proof automation” by mechanizing System Capless (14,000+ lines of Lean 4) with 87% task success rate across 189 annotated tasks; their workflow is human-guided, with humans providing definitions, theorems, and proof strategies while agents handle mechanical proof engineering. Liu et al. (2026) proposed Numina-Lean-Agent, combining Claude Code with MCP-based Lean tools including Lean-LSP-MCP for goal querying and theorem search; it solved all 12 Putnam 2025 problems without model training and formalized the Brascamp–Lieb theorem (8,000+ lines), though again requiring substantial human guidance.

Architecturally, MerLean closely resembles both systems—sharing the paradigm of agentic interaction with Lean 4 in a generate-check-refine loop, frontier LLMs as the reasoning backbone, and the ambition of formalizing research-level mathematics. The primary feature is that MerLean achieves full-paper and fully automated end-to-end formalization without human guidance on the domain we tested.

- 3 FRAMEWORK


MerLean is a bidirectional autoformalization framework comprising two complementary pipelines: autoformalization translates mathematical research papers from LATEX into verified Lean 4 libraries built on Mathlib, while autoinformalization converts the formal code back into human-readable LATEX for expert review. This round-trip design ensures both machine-verified correctness and humanverifiable semantic alignment. The framework employs a frontier LLM agent based on Claude Code that engages multi-turn agentic interactions—iteratively refining outputs based on compiler feedback, faithfulness checks, and tool-augmented exploration of Mathlib. Figure 1 illustrates the overall architecture.

- 3.1 AUTOFORMALIZATION


Statement Extraction. Given a LATEX paper, the agent first extracts all mathematical statements, including definitions, theorems, lemmas, propositions, corollaries, and remarks into a structured JSON representation. Each statement corresponds to a single mathematical result from the paper. It includes a unique identifier (e.g., Def 1, Thm 2), the mathematical content in natural language, explicit dependencies on other statements, and proof sketches when available. The extraction runs

LATEX Paper Extract Formalize Verify

LATEX Blueprint

Autoinformalization

![image 1](Ren et al._2026_MerLean An Agentic Framework for Autoformalization in Quantum Computation_images/imageFile1.png)

Auto-formalization

- Figure 1: MerLean architecture. Autoformalization extracts statements from a LATEX paper, formalizes them into Lean 4, and verifies faithfulness. Autoinformalization translates the verified code back into a human-readable LATEX blueprint or file.


for multiple iterations, where each pass reviews and refines the previous output: expanding vague phrases like “by standard arguments” into concrete proof steps, adding missing intermediate lemmas, and ensuring statements are ordered so that dependencies precede dependents.

Iterative Formalization. For each extracted statement, the agent enters a compile-fix loop. It generates Lean 4 code consisting of one or more declarations, writes them to the appropriate file in the library structure, and compiles it. Each statement typically produces multiple declarations, as the agent autonomously introduces auxiliary definitions, helper lemmas, and typeclass instances to support the target result. If compilation fails, the error messages (type mismatches, unknown identifiers, tactic failures, etc.) will be parsed and fed back to the agent, which analyzes the errors and produces a corrected version. This loop continues until either the code compiles without errors and warnings, or until it reaches a maximum attempt limit. During this process, the agent has access to several diagnostic tools provided via lean-lsp-mcp, a Model Context Protocol server that exposes Lean’s language server capabilities directly to the agent, lean goal for inspecting proof states at specific positions, lean hover info for type signatures and documentation, and semantic search tools (leansearch, loogle) for discovering relevant Mathlib lemmas. The agent can also grep through Mathlib source code to find usage patterns and verify that referenced lemmas actually exist.

Faithfulness Checking. Compilation alone is insufficient: an LLM can produce code that typechecks but misrepresents the mathematics (e.g., proving a trivial statement instead of the intended theorem) (Lin et al., 2025). After a successful build, MerLean reflects on whether the result matches the original meaning. If yes, the program continues to the next statement; otherwise it continues to attempt.

Axiom Handling. Frontier research often depends on results not yet in Mathlib (e.g., the K¨unneth formula for certain coefficient rings). MerLean handles this through explicit axiom declarations, clearly distinguishing intentional assumptions from incomplete proofs (sorry). When formalization fails after maximum attempts, an “axiom phase” converts blocking subgoals to axioms, producing partial formalizations with transparent assumptions that can be filled in as Mathlib expands.

- 3.2 AUTOINFORMALIZATION


The decoder reverses the formalization process, converting a verified Lean 4 library back into human-readable LATEX. While existing tools such as doc-gen4 can produce reasonably readable documentation from Lean source code, the output remains deeply tied to Lean’s type-theoretic syntax and is difficult to interpret for readers without formal methods expertise. Therefore, MerLean utilizes the same LLM model that performed the formalization to do the informalization: since the model has demonstrated its ability to formalize content in the specific research area, it should also be capable of translating each declaration into natural language, making it accessible to domain experts with no prior knowledge of Lean. Of course, no original statement or paper content is provided to the informalization agent to prevent data leaks. The pipeline parses all Lean files, constructs a dependency graph, and produces two complementary outputs: an interactive blueprint compatible with leanblueprint for web-based exploration of the dependency structure, and a standalone textbook-style narrative for readers unfamiliar with formal methods. Any unverified assumptions (axiom declarations) are prominently highlighted, ensuring full transparency about the boundaries of the formalization.

- 4 EXPERIMENTS


We evaluate MerLean on three papers in theoretical quantum computing: one unpublished manuscript to guarantee zero data contamination, and two published papers to assess performance on existing literature.

- • Paper A: Balanced Product Codes (Breuckmann & Eberhardt, 2021). This paper studies quantum codes constructed from tensor products and fiber bundles of chain complexes. The mathematical machinery includes homological algebra, tensor product of complexes, expander graphs and spectral expansion.
- • Paper B: Fault-Tolerant Quantum Computation (Williamson & Yoder, 2024). This paper provides a comprehensive treatment of stabilizer codes and fault-tolerant protocols. The mathematical content includes stabilizer formalism and Pauli algebra, transversal gates, gauging graphs, fault-tolerant state preparation and measurement.
- • Paper C: Quantum Topology. This is an unpublished manuscript, ensuring the content has never appeared in any LLM training data. The manuscript proves several algebraic and group-theoretic properties of some map on quantum computational systems. Details will be released later.


These three projects demonstrate the agent’s capability to formalize and bridge logical gaps in frontier rigorous research, regardless of whether the content is present in the base LLM’s training data. An interactive example of the Fault-Tolerant QC formalization output is available at https:

//doxtor6.github.io/MerLean-examples/.

- 4.1 RESULTS


Table 1: Summary of formalization experiments per paper.

### Paper Statements Lines of Lean Declarations Time

Balanced Product 44 14,997 730 20h 4m Fault-Tolerant QC 47 18,557 923 11h 41m Quantum Topology 23 7,761 397 7h 51m

Table 2: Formalization statistics by statement type across all three papers. Type Count Avg. Time Avg. Compiles

Definition 49 18m 0s 11.7 Theorem 15 39m 41s 22.4 Lemma 20 33m 22s 18.3 Remark 26 10m 34s 7.1 Corollary 4 19m 23s 5.5

Total/Avg 114 21m 54s 13.0

Across all three papers, MerLean formalized 114 statements totaling 2,050 Lean declarations in under 42 hours of wall-clock time. Supported by manual review to ensure all new definitions and axioms are mathematically accurate and rigorously constructed, MerLean successfully formalized all three papers, demonstrating its capability on both novel and published content. The Balanced Product Codes paper required explicit axioms for 9.1% of statements, corresponding to results depending on machinery not yet in Mathlib (e.g., spectral sequences, K¨unneth isomorphisms for F2-chain complexes). Theorems were the hardest to formalize, averaging 39m 41s and 22.4 compile attempts, while remarks were the easiest at 10m 34s and 7.1 compiles with no axioms required. A representative fully-proved theorem is shown in Appendix A.1.

- Figure 2 shows the distribution of compile attempts per statement, broken down by type and paper. The distribution is heavily right-skewed across all three papers: most statements compile within


|| |
|---|
<br><br>| |
|---|
<br><br>| |
|---|
<br><br>| |
|---|
|
|---|


n n n

Figure 2: Distribution of compile attempts by statement type for each paper (maximum 30 attempts before axiom phase). Most statements resolve within 1–10 attempts; theorems and lemmas require significantly more iterations.

1–10 attempts, but a long tail of “hard” statements requires 21+ iterations. Balanced Product Codes exhibits the widest spread, reflecting its reliance on advanced algebraic machinery (spectral sequences, K¨unneth formulas) not yet in Mathlib. Fault-Tolerant QC is heavily concentrated in the low-compile regime, with 23 of 47 statements resolving within 5–10 attempts; its two theorems are the only statements exceeding 20 compiles. Quantum Topology shows a more uniform distribution, consistent with its smaller but technically diverse statement set. Across all papers, theorems and lemmas dominate the high-compile bins, while definitions and remarks cluster in the lower range.

- 4.2 QUALITATIVE OBSERVATIONS


Compile-Fix Loop Behavior. The hard statements that require 20+ compile attempts typically involve:

- 1. Dependent type arithmetic (e.g., proving i − 1 + 1 = i at the type level)
- 2. Missing lemmas that require creative workarounds
- 3. Tactic timeouts requiring proof restructuring


Agent-Discovered Lemmas. MerLean frequently introduces auxiliary lemmas not stated in the original paper. These helper lemmas are natural intermediate steps that a human mathematician would typically leave implicit (see Appendix A.2 for a full example). For instance, the agent introduced:

- • edgeBoundary card eq edgeCount (Balanced Product Codes): Bridges the gap between the geometric definition of expansion (boundary size) and algebraic adjacency counts, enabling the formal derivation of the Relative Cheeger Inequality.

- • pauliPair anticommuting ct satisfied (Fault-Tolerant QC): Algebraically verifies that anticommuting spacetime faults cancel out disjointly in the detector model, a necessary intermediate result for proving the Global Correctness of Spacetime Syndrome Extraction.

- • weight inequality core (Fault-Tolerant QC): Establishes that w′ − |S| + |∂S| ≥ min(h(G),1)·d by case-splitting on the Cheeger parameter h(G) ≥ 1, bridging the cleaning lemma and the space distance lower bound (see Appendix A.2).


Axiom Declarations. The Balanced Product Codes formalization required explicit axiom declarations where the underlying mathematical machinery is not yet available in Mathlib. Notably, the original paper invokes these classical theorems directly without proof, as they are well-known results in the literature; the informal proofs are therefore absent from the source material from the very beginning, making axiomatization the natural counterpart in the formal setting. These axioms reveal concrete gaps relevant to physics applications:

- • K¨unneth Formula: The isomorphism Hn(C ⊗ D) ∼= p+q=n Hp(C) ⊗ Hq(D) for chain complexes over F2 is not available in Mathlib (kunnethMap injective aux, kunnethMap surjective aux).


- • Tensor-Homology Commutativity: The isomorphism Hq(V ⊗ C) ∼= V ⊗ Hq(C) for a flat module V is assumed via the combined axiom e2PageIsoHomologyTensor ax. This conceptually bundles the vertical and horizontal homology steps to identifying the spectral sequence E2 pages with tensor products of base and fiber homologies in Theorem 3. The separate axioms verticalHomologyIsoTensor ax and horizHomologyIsoTensor ax are defined but superseded by this combined form in the main proof.

- • Spectral Sequences: The machinery for computing homology of total complexes via spectral sequences is incomplete (spectralSequenceIsomorphism nontrivial). This is used in Theorem 3’s proof of the Fiber Bundle K¨unneth Theorem to relate the E2 page to the total homology.


These axioms are transparently marked in both the Lean code and the generated blueprint, so that readers immediately see which results rest on unverified assumptions. Appendix A.3 shows the full K¨unneth formula formalization as a concrete example.

- 5 DISCUSSION


- 5.1 CHALLENGES IN MERLEAN

Mathlib Gaps and Axiom-Based Formalization. Our evaluation highlighted gaps in Mathlib regarding specialized physics concepts, for instance, the K¨unneth formula was unavailable. MerLean handles this by explicitly declaring axiom nodes in the dependency graph. More broadly, many physics concepts are not rigorously defined in the language of mathematics (e.g., notions in quantum field theory). Yet, it is out of the scope of this work (and similar ones) to build lean code of full prior knowledge. Consequently, it is reasonable to develop libraries based on “axioms”. Such choices of axioms should not be too elementary for the reason explained above, and not too advanced either, trivializing the derivation of the main results.

Faithfulness Checking. A critical challenge is ensuring that formalized code accurately reflects the original text, rather than merely compiling without errors. MerLean’s faithfulness checking pipeline is used to address this problem, while the autoinformalized blueprint exposes the logical structure for human review. Together, these mechanisms eliminate hallucinations as much as possible, making it immediately apparent if the agent has proven a trivial variation or fabricated a definition to satisfy the compiler.

- 5.2 FUTURE APPLICATIONS OF MERLEAN


Research Assistant. During our initial formalization of the unpublished Quantum Topology paper, one lemma persistently required an axiom. Examining the autoinformalized blueprint revealed that an ambiguous definition, where a constraint the author had implicitly assumed was lacking, caused the problem. After fixing the LATEX source, MerLean produced a complete formalization. This illustrates how the bidirectional pipeline can help researchers improve the rigor of their setups, definitions, and proofs.

Formalized Peer Review. Our validation on an unpublished manuscript confirms that MerLean operates without pre-training on the specific content. We envision a workflow where autoformalization occurs locally during drafting. Just as LATEX became the standard for mathematical typesetting, agentic frameworks could make formal repositories a standard companion to static PDFs, transforming peer review dynamics: reviewers could rely on machine-verified guarantees, focusing strictly on novelty and scientific significance.

Synthetic Data Flywheel. Autoformalization also plays a critical role in training specialized theorem provers, as the quality of large-scale synthetic data depends directly on accurate formalization (Xin et al., 2024; Kumarappan et al., 2025). MerLean facilitates a virtuous cycle for LLM training by mining high-quality (natural language, formal code) pairs grounded in the scientific research they are based on. Feeding it back into base models will improve the next generation of agents.

Contributing to Physics Libraries. The Lean ecosystem has seen growing efforts to formalize physics, including PhysLean/HepLean (Tooby-Smith, 2024) for general physics and LeanQuantumInfo (Meiburg et al., 2025) for quantum information theory. MerLean can accelerate contributions to these libraries by formalizing relevant research papers and extracting reusable definitions and lemmas. Alternatively, researchers can use MerLean to create domain-specific libraries by formalizing a collection of strongly related papers, building a coherent formal foundation for their research area that captures the interconnected definitions, lemmas, and theorems spanning multiple works.

- 6 CONCLUSION


We have presented MerLean, a fully automated bidirectional framework for formalizing mathematical research papers from LATEX into verified Lean 4 libraries. Our evaluation on three papers in theoretical quantum computation, covering stabilizer codes, fault-tolerant protocols, balanced product codes, and homological algebra, produced over 2,000 Lean declarations across 41,000+ lines of verified code, demonstrating that fully automated formalization of frontier research is feasible. The iterative compile-fix-verify loop effectively produces faithful formalizations without human intervention, while the autoinformalization pipeline enables domain experts to review semantic alignment without formal methods expertise.

Looking ahead, while theoretical quantum computing serves as an effective testbed, its mathematical substrate, being primarily linear algebra and functional analysis, benefits from mature Mathlib support. We plan to extend our evaluation to other scientific domains and branches of pure mathematics characterized by deeper dependency chains or different foundational structures, such as algebraic geometry and number theory, to fully establish the framework’s generalizability.

We also plan to evaluate MerLean on existing autoformalization benchmarks to enable direct comparison with prior work. However, current benchmarks (e.g., miniF2F, ProofNet) focus primarily on isolated theorem statements rather than full paper formalization with interconnected definitions, lemmas, and theorems. In the future, we intend to create a dedicated benchmark comprising diverse research papers across multiple mathematical domains, enabling systematic evaluation of autoformalization systems at the level of frontier research.

LLM USAGE DISCLOSURE

In accordance with ICLR 2026 policy, we disclose the following uses of large language models in this work:

Research. MerLean uses Claude (Opus 4.5) as its core reasoning engine for both autoformalization and autoinformalization. The LLM performs statement extraction from LATEX, Lean code generation, error diagnosis and repair, and natural language translation of formal code. All experimental results reported in this paper were produced by this LLM-based system. The authors have verified and validated all research contributions.

Writing. Claude Code was used as a writing assistant for editing portions of this manuscript, including fixing typos and improving grammar. All content was reviewed, verified, and revised by the human authors, who take full responsibility for the accuracy and integrity of the final submission.

REFERENCES

arXiv. arXiv quantum physics submission statistics. https://arxiv.org/year/quant-ph, 2025.

Benjamin Breen, Marco Del Tredici, Jacob McCarran, Javier Aspuru Mijares, Weichen Winston Yin, Kfir Sulimany, Jacob M. Taylor, Frank H. L. Koppens, and Dirk Englund. Ax-Prover: A Deep Reasoning Agentic Framework for Theorem Proving in Mathematics and Quantum Physics, November 2025. URL http://arxiv.org/abs/2510.12787. arXiv:2510.12787 [cs].

Nikolas P Breuckmann and Jens Niklas Eberhardt. Balanced product quantum codes. IEEE Transactions on Information Theory, 67(10):6653–6674, 2021.

Albert Q. Jiang, Sean Welleck, Jin Peng Zhou, Wenda Li, Jiacheng Liu, Mateja Jamnik, Timoth´ee Lacroix, Yuhuai Wu, and Guillaume Lample. Draft, Sketch, and Prove: Guiding Formal Theorem Provers with Informal Proofs, November 2022. URL http://arxiv.org/abs/2210.

12283. arXiv:2210.12283 [cs].

Adarsh Kumarappan, Mo Tiwari, Peiyang Song, Robert Joseph George, Chaowei Xiao, and Anima Anandkumar. LeanAgent: Lifelong Learning for Formal Theorem Proving, March 2025. URL http://arxiv.org/abs/2410.06209. arXiv:2410.06209 [cs].

Zenan Li, Yifan Wu, Zhaoyu Li, Xinming Wei, Xian Zhang, Fan Yang, and Xiaoxing Ma. Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency. November

2024. URL https://openreview.net/forum?id=8ihVBYpMV4.

Yong Lin, Shange Tang, Bohan Lyu, Ziran Yang, Jui-Hui Chung, Haoyu Zhao, Lai Jiang, Yihan Geng, Jiawei Ge, Jingruo Sun, Jiayun Wu, Jiri Gesi, Ximing Lu, David Acuna, Kaiyu Yang, Hongzhou Lin, Yejin Choi, Danqi Chen, Sanjeev Arora, and Chi Jin. Goedel-prover-v2: Scaling formal theorem proving with scaffolded data synthesis and self-correction, 2025. URL https:

//arxiv.org/abs/2508.03613.

Junqi Liu, Zihao Zhou, Zekai Zhu, Marco Dos Santos, Weikun He, Jiawei Liu, Ran Wang, Yunzhou Xie, Junqiao Zhao, Qiufeng Wang, Lihong Zhi, Jia Li, and Wenda Li. Numina-lean-agent: An open and general agentic reasoning system for formal mathematics, 2026. URL https: //arxiv.org/abs/2601.14027.

Qi Liu, Xinhao Zheng, Xudong Lu, Qinxiang Cao, and Junchi Yan. RETHINKING AND IMPROVING AUTOFORMALIZATION: TOWARDS A FAITHFUL METRIC AND A DEPENDENCY RETRIEVAL-BASED APPROACH. 2025.

Alex Meiburg, Leonardo A Lessa, and Rodolfo R Soldati. A formalization of the generalized quantum stein’s lemma in lean. arXiv preprint arXiv:2510.08672, 2025.

Leonardo de Moura and Sebastian Ullrich. The Lean 4 Theorem Prover and Programming Language. In Automated Deduction – CADE 28: 28th International Conference on Automated Deduction, Virtual Event, July 12–15, 2021, Proceedings, pp. 625–635, Berlin, Heidelberg, July 2021. SpringerVerlag. ISBN 978-3-030-79875-8. doi: 10.1007/978-3-030-79876-5 37. URL https://doi.

org/10.1007/978-3-030-79876-5_37.

Logan Murphy, Kaiyu Yang, Jialiang Sun, Zhaoyu Li, Anima Anandkumar, and Xujie Si. Autoformalizing Euclidean Geometry, May 2024. URL http://arxiv.org/abs/2405.17216. arXiv:2405.17216 [cs].

Lawrence C. Paulson (ed.). Isabelle, volume 828 of Lecture Notes in Computer Science. SpringerVerlag, Berlin/Heidelberg, 1994. ISBN 978-3-540-58244-1. doi: 10.1007/BFb0030541. URL http://link.springer.com/10.1007/BFb0030541.

Zhongyuan Peng, Yifan Yao, Kaijing Ma, Shuyue Guo, Yizhe Li, Yichi Zhang, Chenchen Zhang, Yifan Zhang, Zhouliang Yu, Luming Li, Minghao Liu, Yihang Xia, Jiawei Shen, Yuchen Wu, Yixin Cao, Zhaoxiang Zhang, Wenhao Huang, Jiaheng Liu, and Ge Zhang. CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization, July 2025. URL http://arxiv.

org/abs/2507.06181. arXiv:2507.06181 [cs]. Christian Szegedy (ed.). A Promising Path Towards Autoformalization and General Artificial Intelligence, 2020.

Guillem Tarrach, Albert Q. Jiang, Daniel Raggi, Wenda Li, and Mateja Jamnik. More Details, Please: Improving Autoformalization with More Detailed Proofs. June 2024. URL https: //openreview.net/forum?id=AkJvzpYMvK.

The Coq Development Team. The Coq Proof Assistant, June 2024. URL https://zenodo. org/records/11551307. Language: eng.

Joseph Tooby-Smith. Heplean: Digitalising high energy physics, 2024. URL https://arxiv. org/abs/2405.08863.

Ke Weng, Lun Du, Sirui Li, Wangyue Lu, Haozhe Sun, Hengyu Liu, and Tiancheng Zhang. Autoformalization in the Era of Large Language Models: A Survey, May 2025. URL http: //arxiv.org/abs/2505.23486. arXiv:2505.23486 [cs].

Dominic J. Williamson and Theodore J. Yoder. Low-overhead fault-tolerant quantum computation by gauging logical operators, 2024. URL https://arxiv.org/abs/2410.02213.

Yuhuai Wu, Albert Q. Jiang, Wenda Li, Markus N. Rabe, Charles Staats, Mateja Jamnik, and Christian Szegedy. Autoformalization with Large Language Models, May 2022. URL http: //arxiv.org/abs/2205.12615. arXiv:2205.12615 [cs].

Huajian Xin, Daya Guo, Zhihong Shao, Zhizhou Ren, Qihao Zhu, Bo Liu, Chong Ruan, Wenda Li, and Xiaodan Liang. Deepseek-prover: Advancing theorem proving in llms through large-scale synthetic data, 2024. URL https://arxiv.org/abs/2405.14333.

Yichen Xu and Martin Odersky. Agentic Proof Automation: A Case Study, January 2026. URL http://arxiv.org/abs/2601.03768. arXiv:2601.03768 [cs].

Hanning Zhang, Ruida Wang, Rui Pan, Wenyuan Wang, Bingxu Meng, and Tong Zhang. PhysProver: Advancing Automatic Theorem Proving for Physics, January 2026. URL http://arxiv.org/ abs/2601.15737. arXiv:2601.15737 [cs].

Lan Zhang, Marco Valentino, and Andre Freitas. Autoformalization in the Wild: Assessing LLMs on Real-World Mathematical Definitions, September 2025. URL http://arxiv.org/abs/ 2502.12065. arXiv:2502.12065 [cs].

A FORMALIZATION EXAMPLES

We provide representative examples from the Fault-Tolerant QC formalization to illustrate the quality of MerLean’s output.

- A.1 THEOREM: FAULT TOLERANCE OF GAUGING MEASUREMENT


Theorem 2 of Williamson & Yoder (2024) (adapted): The fault-tolerant implementation of Algorithm 1 with a suitable graph G has spacetime fault-distance dST = d, where d is the distance of the original code. Specifically, if (1) the Cheeger constant satisfies h(G) ≥ 1, and (2) the number of measurement rounds satisfies to − ti ≥ d, then any spacetime logical fault has weight at least d.

/-- Main Theorem (Fault Tolerance): The spacetime fault-distance equals d. Under the conditions:

- 1. h(G) >= 1 (Cheeger constant at least 1)
- 2. (t_o - t_i) >= d (sufficient measurement rounds) The spacetime fault-distance d_ST equals exactly d. -/


theorem FaultToleranceTheorem [Fintype V] [Fintype E] [Fintype M] [Nonempty M] (DC : DetectorCollection V E M) (baseOutcomes : OutcomeAssignment M) (logicalEffect : SpacetimeFault V E M -> Prop) (cfg : FaultToleranceConfig) (h_all_decompose : forall F,

IsSpacetimeLogicalFault DC baseOutcomes logicalEffect F -> LowerBoundCase DC baseOutcomes logicalEffect cfg F)

(h_exists_d : exists F, IsSpacetimeLogicalFault DC baseOutcomes logicalEffect F /\ F.weight (intervalRounds cfg) = cfg.d) :

spacetimeFaultDistance DC baseOutcomes logicalEffect (intervalRounds cfg) = cfg.d := by

-- Get the weight-d logical fault for existence obtain <F_d, hF_d_log, hF_d_weight> := h_exists_d

-- Upper bound: d_ST <= d have h_le : spacetimeFaultDistance DC baseOutcomes

logicalEffect (intervalRounds cfg) <= cfg.d := by calc spacetimeFaultDistance DC baseOutcomes

logicalEffect (intervalRounds cfg) <= F_d.weight (intervalRounds cfg) := spacetimeFaultDistance_le_weight DC baseOutcomes

logicalEffect (intervalRounds cfg) F_d hF_d_log _ = cfg.d := hF_d_weight

-- Lower bound: d_ST >= d have h_ge : spacetimeFaultDistance DC baseOutcomes

logicalEffect (intervalRounds cfg) >= cfg.d := by

-- Get the minimum-achieving fault have h_has : hasLogicalFault DC baseOutcomes

logicalEffect := <F_d, hF_d_log>

obtain <F_min, hF_min_log, hF_min_weight> :=

spacetimeFaultDistance_is_min DC baseOutcomes logicalEffect (intervalRounds cfg) h_has

-- Apply lower bound to F_min have h_min_ge := spacetimeFaultDistance_ge_d DC

baseOutcomes logicalEffect cfg F_min hF_min_log (h_all_decompose F_min hF_min_log)

calc cfg.d

<= F_min.weight (intervalRounds cfg) := h_min_ge _ = spacetimeFaultDistance DC baseOutcomes

logicalEffect (intervalRounds cfg) := hF_min_weight

-- Combine omega

- A.2 AGENT-DISCOVERED HELPER LEMMA


This lemma is part of the formalization of Williamson & Yoder (2024), specifically addressing the lower bound on space distance. The agent introduced this intermediate lemma on its own to complete the proof of the space distance lower bound in the fault-tolerant quantum computation formalization. Given a Cheeger-like expansion parameter h(G), a cleaning set of size at most the cleaned operator weight, and a boundary satisfying the isoperimetric inequality, the lemma establishes:

#### w′ − |S| + |∂S| ≥ min(h(G), 1) · d,

where w′ is the cleaned weight, |S| the cleaning set size, |∂S| the boundary size, and d the code distance. The proof splits on whether h(G) ≥ 1, using a calc chain with nlinarith in each branch.

theorem weight_inequality_core (hG : R) (hG_nonneg : 0 <= hG) (d : N) (_hd_pos : 0 < d) (cleanedWeight : N) (hCleaned : cleanedWeight >= d) (cleaningSetSize : N) (hCleaningBound : cleaningSetSize <= cleanedWeight) (boundarySize : N) (hCheeger : (boundarySize : R) >= hG * cleaningSetSize) : (cleanedWeight : R) - cleaningSetSize + boundarySize

>= minCheegerOne hG * d := by simp only [minCheegerOne] by_cases hG_ge_1 : hG >= 1

. -- Case h(G) >= 1: boundarySize >= cleaningSetSize, so result >= cleanedWeight >= d

rw [min_eq_right hG_ge_1] have hBound : (boundarySize : R) >= cleaningSetSize := by

calc (boundarySize : R) >= hG * cleaningSetSize := hCheeger _ >= 1 * cleaningSetSize := by nlinarith _ = cleaningSetSize := one_mul _

have hCleaned’ : (cleanedWeight : R) >= d :=

Nat.cast_le.mpr hCleaned linarith

. -- Case h(G) < 1 push_neg at hG_ge_1 rw [min_eq_left (le_of_lt hG_ge_1)] have hClean : (cleanedWeight : R) >= d :=

Nat.cast_le.mpr hCleaned

have hS’ : (cleaningSetSize : R) <= cleanedWeight :=

Nat.cast_le.mpr hCleaningBound

calc (cleanedWeight : R) - cleaningSetSize + boundarySize

>= cleanedWeight - cleaningSetSize

+ hG * cleaningSetSize := by linarith _ = cleanedWeight

+ (hG - 1) * cleaningSetSize := by ring _ >= cleanedWeight

+ (hG - 1) * cleanedWeight := by nlinarith _ = hG * cleanedWeight := by ring _ >= hG * d := by nlinarith

- A.3 AXIOM EXAMPLE: KUNNETH¨ FORMULA


This example is drawn from the formalization of Breuckmann & Eberhardt (2021), where the K¨unneth formula is essential for calculating the homology of balanced product codes. The K¨unneth formula is a fundamental result in homological algebra that relates the homology of a tensor product of two chain complexes to the tensor products of their individual homologies. Given chain complexes C = (C•,∂C) and D = (D•,∂D) over F2, the formula states:

Hn(C ⊗ D) ∼=

Hp(C) ⊗ Hq(D).

p+q=n

Over a field such as F2, all modules are flat, so the Tor correction terms vanish and the K¨unneth map is an isomorphism. The isomorphism sends a pair of homology classes [z] ∈ Hp(C) and [w] ∈ Hq(D) to the class [z ⊗ w] ∈ Hp+q(C ⊗ D). Proving this in Lean 4 requires (i) showing the tensor product of cycles is a cycle, (ii) showing boundaries are preserved so the map descends to homology, and (iii) establishing bijectivity. Steps (i)–(iii) involve unfolding the internal colimit structure of Mathlib’s total complex, which is not yet supported; these are axiomatized. The full formalization is shown below.

The 4 snippets below correspond to the definition of types, followed by the three proof steps (i)–(iii). First, we define the source type (direct sum of tensor products of homologies) and the target type (homology of the tensor product):

variable (C D : F2ChainComplex) /-- All F2-modules are flat (free modules are flat). -/ instance flat_F2_module (M : Type*) [AddCommGroup M]

[Module F2 M] : Module.Flat F2 M := Module.Flat.of_free

/-- Tensor product of homology spaces. -/ noncomputable def HomologyTensor (p q : Z) : Type :=

(C.Homology p) (x)[F2] (D.Homology q)

... /-- Index set: pairs (p,q) with p + q = n. -/ def KunnethIndex (n : Z) : Type :=

{ pq : Z x Z // pq.1 + pq.2 = n }

/-- The direct sum (+)_{p+q=n} H_p(C) (x) H_q(D). -/ noncomputable def KunnethDirectSum (n : Z) : Type :=

Pi_0 (i : KunnethIndex n), HomologyTensor C D i.val.1 i.val.2

... /-- Homology of the tensor product complex at degree n. -/ noncomputable abbrev TensorHomology (n : Z) : Type :=

(TensorProductComplex C D).Homology n

- Step (i): Constructing the map on cycles. We show that the tensor product of cycles is a cycle, allowing us to define the cross product on cycles:

/-- Map from C_p (x) D_q to (C (x) D)_{p+q}. -/ noncomputable def tensorInclusion (p q : Z) :

(C.X p) (x)[F2] (D.X q) ->l[F2]

(TensorProductComplex C D).X (p + q) := (TensorProductComplex.i C D p q).hom

/-- Axiom: z (x) w is a cycle when both z, w are cycles. d(z (x) w) = dz (x) w +- z (x) dw = 0. -/ axiom cycle_tensor_cycle_is_cycle’_aux

(C D : F2ChainComplex) (p q : Z) (z : C.X p) (hz : z in C.Cycles p) (w : D.X q) (hw : w in D.Cycles q) : tensorInclusion C D p q (z (xt) w) in

(TensorProductComplex C D).Cycles (p + q)

/-- Map from C.Cycles p (x) D.Cycles q to total cycles. -/ noncomputable def cyclesCrossProduct (p q : Z) :

(C.Cycles p) (x)[F2] (D.Cycles q) ->l[F2] (TensorProductComplex C D).Cycles (p + q) := by

... -- bilinear map lifting cycle_tensor_cycle_is_cycle’

- Step (ii): Descent to homology. We axiomatize that boundaries are preserved under the cross product, ensuring the map descends to a well-defined map on homology:


/-- Axiom: boundary (x) cycle is a boundary. If z = dz’, then z (x) w = d(z’ (x) w) since dw = 0. -/ axiom boundary_tensor_cycle_is_boundary’_aux

(C D : F2ChainComplex) (p q : Z) (z : C.Cycles p) (hz : z.val in C.Boundaries p) (w : D.Cycles q) : (cyclesCrossProduct C D p q (z (xt) w)).val in

(TensorProductComplex C D).Boundaries (p + q)

/-- Axiom: cycle (x) boundary is a boundary. If w = dw’, then z (x) w = d(z (x) w’) since dz = 0. -/ axiom cycle_tensor_boundary_is_boundary’_aux

(C D : F2ChainComplex) (p q : Z) (z : C.Cycles p)

(w : D.Cycles q) (hw : w.val in D.Boundaries q) : (cyclesCrossProduct C D p q (z (xt) w)).val in

(TensorProductComplex C D).Boundaries (p + q)

- Step (iii): Bijectivity and the Main Theorem. Finally, we construct the K¨unneth map and axiomatize its bijectivity to establish the isomorphism:


... /-- Cross product descends to homology: [z] (x) [w] |-> [z (x) w].

-/ noncomputable def kunnethComponentMap (p q : Z) : HomologyTensor C D p q ->l[F2] TensorHomology C D (p + q) := TensorProduct.lift (kunnethComponentMapAux2 C D p q)

/-- The Kunneth map from (+)_{p+q=n} H_p(C) (x) H_q(D) to H_n(C (x) D). -/ noncomputable def kunnethMap (n : Z) : KunnethDirectSum C D n ->l[F2] TensorHomology C D n := by refine DFinsupp.lsum N ?_ intro <<p, q>, hpq> subst hpq exact kunnethComponentMap C D p q

/-- Axiom: the Kunneth map is injective over F2. -/ axiom kunnethMap_injective_aux

(C D : F2ChainComplex) (n : Z) : Function.Injective (kunnethMap C D n)

/-- Axiom: the Kunneth map is surjective over F2. -/ axiom kunnethMap_surjective_aux

(C D : F2ChainComplex) (n : Z) : Function.Surjective (kunnethMap C D n)

/-- Kunneth Formula: (+)_{p+q=n} H_p(C) (x) H_q(D) ˜= H_n(C (x) D). -/ noncomputable def kunnethEquiv (n : Z) :

KunnethDirectSum C D n ˜=l[F2] TensorHomology C D n := LinearEquiv.ofBijective (kunnethMap C D n) <kunnethMap_injective C D n, kunnethMap_surjective C D n>

