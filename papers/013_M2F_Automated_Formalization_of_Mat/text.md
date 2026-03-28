# arXiv:2602.17016v1[cs.AI]19 Feb 2026

## M2F: Automated Formalization of Mathematical Literature at Scale

Zichen Wang1, Wanli Ma2, Zhenyu Ming3, Gong Zhang3, Kun Yuan4, Zaiwen Wen2∗

1School of Mathematical Sciences, Peking University 2Beijing International Center for Mathematical Research, Peking University 3Huawei Technologies 4 Center for Machine Learning Research, Peking University zichenwang25@stu.pku.edu.cn, wlma@pku.edu.cn, mingzhenyu1@huawei.com, nicholas.zhang@huawei.com kunyuan@pku.edu.cn, wenzw@pku.edu.cn

###### Abstract

Automated formalization of mathematics enables mechanical verification but remains limited to isolated theorems and short snippets. Scaling to textbooks and research papers is largely unaddressed, as it requires managing cross-file dependencies, resolving imports, and ensuring that entire projects compile end-to-end. We present M2F (Math-to-Formal), the first agentic framework for end-to-end, project-scale autoformalization in Lean. The framework operates in two stages. The statement compilation stage splits the document into atomic blocks, orders them via inferred dependencies, and repairs declaration skeletons until the project compiles, allowing placeholders in proofs. The proof repair stage closes these holes under fixed signatures using goal-conditioned local edits. Throughout both stages, M2F keeps the verifier in the loop, committing edits only when toolchain feedback confirms improvement. In approximately three weeks, M2F converts long-form mathematical sources into a project-scale Lean library of 153,853 lines from 479 pages textbooks on real analysis and convex analysis, fully formalized as Lean declarations with accompanying proofs. This represents textbook-scale formalization at a pace that would typically require months or years of expert effort. On FATE-H, we achieve 96% proof success (vs. 80% for a strong baseline). Together, these results demonstrate that practical, large-scale automated formalization of mathematical literature is within reach. The full generated Lean code from our runs is available at https://github.com/optsuite/ReasBook.git.

### 1 Introduction

Most mathematical knowledge resides in textbooks and research papers. Formalizing even a single section of such material in Lean [6, 5] remains labor-intensive, typically demanding domain experts and, at scale, coordinated curation and annotation by teams. The bottleneck is project-level compilation, not any individual proof: imports and namespaces must be chosen consistently, definitions must typecheck under a pinned library snapshot, dependencies must be stabilized across files, and the code must be iteratively repaired until the project elaborates. This work dominates the cost of formalization and slows the growth of libraries such as mathlib [24] and OptLib [12, 14, 15]. Prior work provides key ingredients but does not directly address this project-scale compilation problem. Neural theorem provers and agentic systems focus on closing goals given well-formed statements within a buildable project; autoformalization translates informal text and LaTeX into formal snippets but struggles to maintain global buildability as documents grow and structural errors accumulate. We review these lines of work in §2. Our focus is the upstream task: turning textbook- and paper-scale sources into a consistent Lean project that elaborates end-to-end.

We address this gap with M2F (short for Math-to-Formal), a framework for automated formalization of mathematical literature at project scale. We formulate the task as knowledge compilation under a fixed Lean environment E: given a textbook or paper as input, produce a Lean project that elaborates end-to-end and

∗Corresponding author

provides span-level provenance linking declarations back to the source text. Our core methodology is verifiercertified refinement (VeriRefine): M2F proposes localized edits and commits only when Lean’s toolchain feedback certifies strict progress on compilation, or—once compilation holds—on closing remaining proof holes. This accept-if-improves rule makes progress measurable and prevents regressions from accumulating over long runs. M2F instantiates VeriRefine in two stages. Stage 1 (statement compilation) decomposes documents into atomic blocks, infers and refines a dependency schedule, emits declaration skeletons, and repairs them until the project elaborates, permitting sorry placeholders in proofs. Stage 2 (proof repair) freezes statement signatures and closes remaining holes via goal-conditioned local edits. We evaluate Stage 2 under matched statements and matched compute using verifier-normalized budgets (verifier calls). Our experiments demonstrate both document-scale compilation and strong prover behavior. Across long-form sources spanning 312 pages of real analysis, 140 pages of convex analysis, and 27 pages of research-paper exposition, M2F produces end-to-end buildable Lean artifacts under E in a single end-to-end run, reaching 241 files, 4,116 declarations, and 153,853 lines of Lean (Table 2); under matched statements, Stage 2 closes all proof holes on these compiled projects (PSR= 100%, proof success rate under matched statements). We additionally evaluate Stage 2 on FATE-H because it provides fully formal Lean statements and serves as a standard anchor for controlled prover comparison; replacing each target proof with sorry yields a clean matched-statement protocol that isolates proof repair. Under this protocol, Stage 2 achieves 96% PSR on FATE-H, outperforming a state-of-the-art prover baseline (Seed-Prover 1.5 at 80%, a +16-point gain; Table 5). Our contributions are summarized as follows.

- • Autoformalization at scale as knowledge compilation. We formulate textbook-/paper-scale formalization as compiling a buildable Lean project under a pinned environment, producing span-level provenance and enabling end-to-end evaluation beyond per-snippet correctness.
- • VeriRefine. We introduce an accept/revert refinement primitive governed solely by Lean toolchain feedback: edits are committed only when they reduce elaboration errors or, once elaboration succeeds, close proof holes. This ensures reliable progress under verifier-normalized compute budgets.
- • M2F as a strong prover. We show that Stage 2 of M2F can serve as a strong prover under matched statements: using a CLI+MCP toolchain-in-the-loop with goal-conditioned local proof edits, it achieves state-of-the-art success on FATE-H among the compared provers, providing an external validation of the methodology.


Taken together, the three contributions above constitute M2F: a project-level knowledge-compilation formulation with provenance, a verifier-certified refinement primitive (VeriRefine), and a two-stage instantiation that scales to textbook- and paper-length sources while yielding strong prover behavior under matched statements. By keeping the Lean toolchain in the loop and using verifier feedback as the sole acceptance signal, M2F produces buildable Lean projects end-to-end and systematically reduces remaining proof holes without accumulating regressions, demonstrating that large-scale formalization is practically feasible under pinned environments. The M2F pipeline from end-to-end is shown in Figure 1. More information on the M2F system is available in https://github.com/optsuite/M2F.git, and the Lean projects generated from our runs can be checked in https://github.com/optsuite/ReasBook.git. This positions proof assistants as reliable verifier infrastructure and suggests a path to accelerating the growth of formal mathematics libraries and downstream mathematical reasoning in AI systems.

### 2 Related Work

Neural theorem proving in Lean. A large line of work studies automated proving when given goals that already elaborate in Lean, typically combining retrieval, search, and verifier feedback. Representative tool interfaces and benchmarks include MiniF2F and LeanDojo [32, 29], and recent systems scale performance via stronger models and increasingly agentic search loops [28, 21, 4, 10, 19]. These approaches commonly assume a buildable project and well-typed statements under a pinned snapshot; in contrast, M2F targets an upstream regime where failures are dominated by project- and library-level structure (imports, name resolution, dependency ordering, and type-mismatch cascades) that arise before proof search is meaningful.

![image 1](Wang et al._2026_M2F Automated Formalization of Mathematical Literature at Scale_images/imageFile1.png)

Figure 1: The M2F pipeline for project-scale automated formalization.

Autoformalization with tool feedback and structural guidance. LLM-based autoformalization translates informal sources into formal statements and proofs [27], and Lean-centric pipelines increasingly incorporate compiler/tool feedback during generation and refinement [17]. Recent work further exploits structural cues and dependency information, including compiler-feedback refinement and consistency validation (ATF) [9], DAG/dependency-aware proof workflows (ProofFlow) [3], retrieval with dependency-graph driven iterative autoformalization (Aria) [26], and structure-to-instance theorem autoformalization (SITA) [13]. M2F is complementary: we make end-to-end project buildability under E the primary objective and operationalize refinement through a verifier-certified accept/revert rule defined directly over toolchain feedback and remaining proof holes.

Faithfulness, evaluation, and diagnostic-conditioned repair. Datasets and evaluation protocols for autoformalization include aligned corpora and alignment metrics [7, 31, 1, 8, 16, 20]. We complement these directions with a project-level evaluation protocol that tracks end-to-end buildability, uses provenance links to support faithfulness auditing beyond typechecking, and evaluates proof repair under matched statements while reporting compute in verifier-normalized units. Methodologically, our accept/revert refinement loop is related to diagnostic-conditioned program repair, where candidate edits are proposed and validated by executing a checker and inspecting diagnostics [18, 30, 25, 2, 23]; proof assistants add structure because

“compilation” corresponds to type-theoretic elaboration under a pinned snapshot, and proof repair can further condition on elaborated goal states.

### 3 Problem Setup and Pipeline Overview

Figure 1 summarizes M2F as a project-scale, verifier-in-the-loop pipeline for automated formalization. The input is a long-form LaTeX document (or a collection of textbook/paper sections) D, and the output is a Lean project P that elaborates end-to-end under a pinned dependency revision. M2F is organized as a two-stage pipeline (statements then proofs) executed inside a refinement protocol: the Lean toolchain returns range-annotated feedback, and each bounded edit is accepted only when verifier feedback certifies objective improvement.

#### 3.1 Input, Environment, and Output

The input is a long-form source D (a LaTeX document or a collection of textbook/paper sections), normalized into an ordered sequence of JSON items by the PDF/LaTeX-to-JSON preprocessing in Figure 1 (page-aligned extraction, structure anchoring, and dependency recovery). This representation supports deterministic iteration over items and stable provenance linking. We use provenance spans to trace generated declarations back to the source; let Span(D) denote the set of character spans in D. All verification is performed under a fixed Lean environment E, consisting of a Lean toolchain version and a pinned dependency revision (e.g., a specific mathlib commit). Fixing E makes build outcomes and diagnostics comparable across runs; we assume determinism under E, i.e., repeated verification produces identical diagnostics up to irrelevant ordering.

We expose the toolchain through project-level and file-level verification oracles: VerifyProjE(P) → (ok,∆),VerifyFileE(P,f) → (ok,∆f).

Here ∆ and ∆f are finite multisets of diagnostics annotated with source ranges in the corresponding Lean project or file; each diagnostic includes a severity tag (error/warning/info) and a message string. We write err(·) for the number of error-level diagnostics (defined for both ∆ and ∆f), and treat ok as shorthand for err(∆) = 0 (project) or err(∆f) = 0 (file); warnings do not affect success. Note that provenance spans Span(D) live in the source coordinate system, while diagnostic ranges live in Lean file coordinates.

The output is a Lean project P together with a provenance map π : Decl(P) → 2Span(D), where Decl(P) is the set of globally named declarations introduced across modules/files. Stage 1 permits sorry in proof bodies but requires that all modules/imports elaborate successfully (zero error-level diagnostics); Stage 2 optionally targets a placeholder-free project with no remaining sorry.

Although we expose VerifyProj for reporting end-to-end buildability (e.g., lake build), the refinement loop itself is certified at file granularity: each attempted edit re-invokes VerifyFile on the touched file and is accepted/reverted based solely on toolchain outputs. This separation makes the pipeline portable across agents and runtimes: patch proposal can use LLMs and tool queries, while certification depends only on E and verifier feedback.

#### 3.2 Two-Stage Pipeline

M2F separates knowledge import from discharging proof obligations: at document scale, proof repair is meaningful only after imports, namespaces, typing, and dependencies have been stabilized at the project level.

- In Stage 1 (statements), M2F maps D to a project P1 that elaborates end-to-end under E while allowing proof placeholders. Each JSON item is assigned a target file; an LLM proposes a Lean declaration skeleton (possibly containing sorry); and when compilation fails the system proposes bounded patches guided by localized diagnostics. After each patch, it re-runs VerifyFile and commits the edit only if verifier feedback certifies objective improvement; otherwise it reverts.
- In Stage 2 (proofs), M2F takes P1 and reduces remaining proof holes to obtain P2 under matched statements (statement signatures are held fixed; edits are restricted to proofs and optional local helpers that do not change existing signatures). Given the next proof item, the system locates the corresponding Lean declaration and its hole location (typically the inserted sorry) to establish the target file/range for repair. It then iterates a proof planner/prover to propose candidate proof patches; failed attempts trigger bounded repair via an error fixer and replanning. To keep verification stable at scale, the pipeline includes a deterministic guard for oversized files that triggers splitting before continuing. Both stages share the same refinement primitive (VeriRefine): propose a localized edit, re-run VerifyFile, and accept/revert based on verifier-certified objective improvement. We report compute in verifier-normalized units (the number of VerifyFile calls), which reduces sensitivity to wall-clock variability and provides a uniform budget across long-running compilation and proof repair.


### 4 Method: VeriRefine for M2F

VeriRefine is an operator for Lean projects under a fixed environment E (toolchain + pinned dependencies). A state is a project P. Each refinement step proposes a bounded patch p to a file region and commits it only

if Lean verification certifies a strict improvement of an explicit objective; otherwise the step is rolled back. This accept/revert contract decouples how patches are proposed (which may use language models, retrieval, and structured tool feedback) from how progress is certified (which depends only on verifier outputs), making long-run refinement stable under verifier-call budgets.

- 4.1 Oracles, Diagnostics, and Scopes Fix a Lean environment E. For a project state P and file f, the file-level verifier returns

VerifyFileE(P,f) → (ok,∆f),

where ∆f is a finite multiset of diagnostics and we treat ok = true as shorthand for err(∆f) = 0 (warnings ignored), i.e., f elaborates under E. We model each diagnostic as d = (r,κ,µ) with source range r in f, severity κ ∈ {error,warning,info}, and message string µ; writing rng(d), kind(d), and msg(d) for projections, the error count is err(∆f) = |{d ∈ ∆f : kind(d) = error}|.

A scope S is a finite union of ranges in f, and diagnostic localization is Localize(∆f,S) = {d ∈ ∆f : rng(d) ∩ S ̸= ∅}

with errS(∆f,S) = err(Localize(∆f,S)). Let Hdr(f) be a bounded header region (imports/namespace/section) and Decl(c) the declaration range of a newly inserted skeleton c. We use Scope(c,f) = Decl(c) ∪ Hdr(f) and, for a diagnostic or hole x, Scope(x,f) = rng(x) ∪ Hdr(f).

When err(∆f) = 0, we optionally query an elaborated goal state at a hole h via GoalStateE(P,f,h) ∈ {(g,Γ),⊥}, returning goal type g and local context Γ = (x1 : T1,...,xm : Tm), or ⊥ if unavailable.

- 4.2 Objectives and Verifier-Certified Accept/Revert

We compare objective pairs by a priority order: (a,b) ≺ (a′,b′) iff a < a′ or (a = a′∧b < b′). For file diagnostics ∆f, define the primary metric E(∆f) = err(∆f). Stage 1 uses the secondary metric L(∆f,S) = errS(∆f,S) for the current scope S; Stage 2 uses the secondary metric H(f) = |H(f)|, where H(f) are occurrences of sorry outside comments/strings. This ordering ensures that we never accept a patch that increases compilation errors, even if it would reduce locality errors or hole count. Target scheduling is external to acceptance. Stage 1 (resp. Stage 2) processes statement (resp. proof) items in increasing JSON index order, and each proof item may include a reference answer used only to condition patch proposals.

All edits are executed through TryPatchs. Given s ∈ {1,2}, state P, file f, scope S, a candidate patch p, and current diagnostics ∆f, it snapshots f, applies p restricted to S, and re-runs VerifyFileE(P,f) to obtain ∆′f. It commits iff the stage objective strictly improves in the priority order: Stage 1 accepts iff (E(∆′f),L(∆′f,S)) ≺ (E(∆f),L(∆f,S)) and Stage 2 accepts iff (E(∆′f),H′(f)) ≺ (E(∆f),H(f)), where H′(f) is the hole count after applying p. Otherwise it rolls back. Because acceptance requires strict improvement, the sequence of accepted patches is monotone with respect to the stage objective, preventing oscillation and making verifier-call budgets a direct bound on attempted edits.

- 4.3 Patch-Proposal Operators (Instantiation Layer)


VeriRefine separates proposal from certification. We describe proposal as a family of operators that may use tool feedback (diagnostics, goal states) and auxiliary context (e.g., reference proof text), while certification is always enforced by TryPatchs. Concretely, M2F uses the following operator types:

- • GenSkeleton: (u,P,f)  → c inserts a declaration skeleton for a statement item u.
- • RepairPatch: (P,f,δ)  → p proposes a localized patch conditioned on localized diagnostics δ = Localize(∆,S).


- • FixCompileError: (P,f,d)  → p proposes a patch targeting a selected error diagnostic d when err(∆) > 0.
- • Plan/Replan: (u,g,Γ)  → π proposes (and updates) a proof plan; u may include a reference answer.
- • ProposeProofPatch: (P,f,h,π,u,g,Γ)  → p proposes a hole-closing proof patch within Scope(h,f).
- • SplitIfLargeAndResolve (optional): given a long file, split at declaration boundaries while preserving namespace/section context and a linear import chain among parts, then re-resolve the target location by label.


#### 4.4 Preprocessing: Input as Ordered JSON Items

M2F takes as input an ordered stream of JSON items derived from long-form sources. Statement items provide a label and a LaTeX span describing the statement/definition environment; proof items share the same index space and additionally carry an proof field containing the source proof text (LaTeX/NL). In this paper we treat preprocessing as producing these ordered, provenance-carrying JSON items; the semantic schema and invariants of these items are specified in Appendix B.

#### 4.5 Statement Compilation and Proof Repair

- Stage 1 compiles ordered statement items into a Lean project P1 that elaborates under E while allowing proof placeholders. For each statement item, the system inserts a Lean skeleton into its target file and iteratively applies localized repairs until the file elaborates (or the per-item budget is exhausted); all candidate edits


are mediated by TryPatch1 and are committed only when verifier feedback certifies improvement. When a required name and type must be made available before its body is stabilized (e.g., ordering constraints or latent cycles in long-form exposition), Stage 1 admits typed stubs that introduce the intended constant with its intended type while deferring the actual body, so that downstream items can elaborate. Concretely, we use stub templates of the following form, where nb and Tb denote the intended name and type for the current block:

theorem n_b : T_b := by sorry lemma n_b : T_b := by sorry def n_b : T_b := sorry abbrev n_b : T_b := by sorry example : T_b := by sorry instance n_b : T_b := by sorry

Algorithm 1 summarizes the verifier-certified statement compilation procedure.

Stage 2 starts from the compilable project P1 and reduces the number of remaining proof holes while preserving elaboration. We evaluate Stage 2 under matched statements: statement signatures are held fixed and only proofs (and optional local helpers that do not change existing signatures) may be edited. Stage 2 processes proof items in increasing JSON index order; each item locates its target hole in the current Lean project (typically a labeled sorry) and may provide a reference answer (source proof text) used only to condition planning and patch proposal. Proof repair alternates between compile-error recovery (if err(∆) > 0) and hole-focused proof patching with optional goal/context queries, with bounded retries and replanning under verifier-call budgets. Algorithm 2 specifies the verifier-certified proof repair procedure for a single proof item.

### 5 M2F: Interface Contract

M2F exposes document-scale autoformalization as a verifier-certified refinement loop (VeriRefine) over a pinned Lean environment E (Lean toolchain plus pinned dependency revision). Patch proposal can be implemented by any agent (LLM, retrieval, tool calls); certification is determined solely by toolchain outputs.

- Algorithm 1 Verifier-certified statement compilation


Input: Ordered statement items Istmt (JSON); environment E; per-item budget K Output: Compilable project P1; provenance map π

P ← InitProject(E); π ← ∅ for u ∈ Istmt in increasing index order do

f ← TargetFile(u); snap0 ← Snapshot(P, f) (c, πu) ← GenSkeleton(u, P, f); Insert(P, f, c); π ← π ∪ πu S ← Scope(c, f); ( , ∆) ← VerifyFileE(P, f); t ← 0 while err(∆) > 0 ∧ t < K do

δ ← Localize(∆, S) if δ = ∅ then

S ← ExpandScope(S, ∆)

else p ← RepairPatch(P, f, δ) ( , ∆) ← TryPatch1(P, f, S, p, ∆)

t ← t + 1

if err(∆) > 0 then

Restore(P, f, snap0) return P, π

For a project state P and file f, the minimal oracle is file verification VerifyFileE(P,f) → (ok,∆f), returning a finite multiset of range-annotated diagnostics; we treat ok as shorthand for err(∆f) = 0 (warnings ignored). When err(∆f) = 0, we optionally query an elaborated goal state at a hole h via GoalStateE(P,f,h) ∈ {(g,Γ),⊥}, which is used only to condition patch proposals and never to decide acceptance. Edits are range-bounded. A patch is applied only within a scope S (a finite union of ranges). We use the uniform constructor from §4: for a newly inserted skeleton c, S = Decl(c) ∪ Hdr(f); for a diagnostic or hole x, S = rng(x) ∪ Hdr(f). If Localize(∆f,S) = ∅ but err(∆f) > 0, we allow bounded scope expansion as a fallback. All edits are executed through a single commit/rollback wrapper: snapshot → apply within S → re-verify → accept iff the stage objective strictly improves; otherwise rollback. Using the priority order from §4, Stage 1 accepts iff (err(∆′f),errS(∆′f,S)) ≺ (err(∆f),errS(∆f,S)), and Stage 2 accepts iff (err(∆′f),|H′(f)|) ≺ (err(∆f),|H(f)|), where H(f) counts remaining proof holes (e.g., sorry). Each attempted patch triggers exactly one call to VerifyFileE, so verifier-call budgets directly bound the number of attempted edits.

### 6 Experiments

We evaluate M2F on long-form mathematical sources and on the external benchmark FATE-H. On long-form sources, evaluation is end-to-end and fully checkable under a pinned Lean environment E: M2F produces a Lean project that passes lake build, yielding a textbook-scale artifact of 241 files, 4,116 declarations, and 153,853 lines of Lean code from 479 pages of source material (Table 2). We then evaluate proof repair under matched statements on an audited statement layer whose signatures are manually verified against provenance-linked spans (Appendix A.3); under this protocol, Stage 2 closes 875/875 audited proof holes while preserving elaboration (Table 2 and Table 4). We additionally report results on FATE-H (100 problems), where statements already elaborate in Lean, so Stage 2 can be evaluated in isolation as a prover and compared by success rate.

#### 6.1 Setup

We evaluate on (a) textbooks: sections from Real Analysis by Lebl [11]1 and Convex Analysis by Rockafellar [22]; (b) research papers: full sections with heterogeneous exposition and implicit assumptions; and (c) an external prover benchmark: FATE-H2. We include FATE-H for three reasons. First, its statements already elaborate in Lean, so Stage 1 is bypassed and Stage 2 can be evaluated under matched statements without confounding from statement generation. Second, FATE-H is widely used in recent Lean prover evaluations,

- 1https://github.com/jirilebl/real-analysis.
- 2https://github.com/frenzymath/FATE-H.git


###### Algorithm 2 Verifier-certified proof repair for a proof item

Input: Project P1; proof item u (label + optional answer); budgets T (verifier calls), R (retries), C (replans) Output: Updated project state

P ← P1 f ← TargetFile(u); f ← SplitIfLargeAndResolve(f, u) ( , ∆) ← VerifyFileE(P, f); t ← 0 while t < T do

if err(∆) > 0 then d ← SelectError(∆); S ← Scope(d, f) p ← FixCompileError(P, f, d) ( , ∆) ← TryPatch2(P, f, S, p, ∆); t ← t + 1 continue

h ← LocateTargetHole(f, u) if h = ⊥ then return P

(g, Γ) ← GoalStateE(P, f, h) (optional)

π ← Plan(u, g, Γ) for c = 1 to C do

for r = 1 to R do q ← ProposeProofPatch(P, f, h, π, u, g, Γ) (acc, ∆) ← TryPatch2(P, f, Scope(h, f), q, ∆); t ← t + 1 if acc then

return P if t ≥ T then return P

π ← Replan(π, u, g, Γ, ∆) return P

providing a standard anchor for success-rate comparisons when external systems do not expose comparable verifier-call accounting. Third, it decouples evaluation from our document preprocessing and compilation stack, serving as a portability check that the same VeriRefine loop can be dropped into an existing Lean benchmark without corpus-specific heuristics. Table 1 summarizes scale; for long-form corpora, the Holes column counts all candidate proof locations after replacing proofs with sorry, and Stage 2 is evaluated on these matched-statement obligations after statement-signature audit.

- Table 1: Corpora and scale. Blocks is the number of Stage 1 atomic blocks. Decls is the number of generated declarations after Stage 1. Holes is the number of candidate matched-statement proof obligations for Stage 2.


Corpus Sections Pages Blocks Decls Holes

Real Analysis 36 312 416 1195 339 Convex Analysis 15 140 560 2620 499 Paper 6 27 67 301 37

FATE-H – – – 100 100

All runs use the same Lean environment E (Lean: leanprover/lean4:v4.26.0-rc2) on the same hardware (Intel(R) Xeon(R) 6982P-C, 16 cores / 32 threads, 128 GiB RAM), and a file/project is considered verified iff Lean reports zero error-level diagnostics under E. LLM interactions are executed via Codex CLI with model reasoning effort="high", and we interface with Lean through an LSP-based MCP server3 for lightweight tool queries during refinement (e.g., goal/context inspection when available); prompting philosophy and instrumentation are reported in Appendix A. A key implication for infrastructure is that our pipeline does not require large-scale human annotation to run: we do not assume human-labeled proof traces, dependency labels, or step-by-step demonstrations, and the primary signal is the Lean toolchain itself. Finally, statement faithfulness is enforced by a provenance-linked manual audit that acts as an evaluation gate rather than a posthoc sanity check: every theorem/lemma statement included in Stage 2 evaluation is compared by a domain expert against its provenance-linked source span, verifying preservation of quantifier structure, hypotheses (including implicit assumptions made explicit in prose), the conclusion, and essential typeclass/domain

3https://github.com/oOo0oOo/lean-lsp-mcp.git

- Table 2: End-to-end artifacts and proof progress under matched statements. PB indicates that the final project builds under E. A concrete workflow walkthrough and code overview are provided in Appendix D.


End-to-end artifact Matched-statement Stage 2 Corpus Blocks PB Files Decls LoC Holes Closed PSR (%)

Real Analysis 416 ✓ 49 1195 34327 339 339 100 Convex Analysis (Sec. 1–15) 560 ✓ 164 2620 105682 499 499 100 Paper 67 ✓ 28 301 13844 37 37 100

Total (long-form) 1043 ✓ 241 4116 153853 875 875 100

constraints; any statement that fails this checklist is excluded from the audited evaluation set (Appendix A.3). We do not use model-based statement checking as a correctness oracle because the statement layer is itself model-generated and model reviewers can share correlated failure modes (silently rubber-stamping subtle semantic drift); automated alignment is used only for triage, while human audit is the correctness criterion for the statement layer used in matched-statement proof repair.

#### 6.2 Project Artifacts and Statement Compilation

The primary output of M2F is a buildable Lean library artifact rather than isolated proofs. Table 2 reports end-to-end artifacts after running the full pipeline on textbook- and paper-scale sources: for Lebl’s Real Analysis (312 pages) M2F produces 49 files, 1,195 declarations, and 34,327 lines of Lean code; for Rockafellar’s Convex Analysis it produces 164 files, 2,620 declarations, and 105,682 lines of Lean code. Across all long-form corpora combined (479 pages), the output is 241 files and 153,853 lines of Lean code that build end-to-end under E, indicating that imports, namespaces, and file/module structure have been stabilized at project scale without axiom declarations. The same table reports Stage2 progress under matched statements on the proof targets whose statement signatures pass the human audit. Table1 reports corpus scale and the full set of candidate matched-statement proof obligations obtained by blanking proofs with sorry; in our current evaluation, all candidates pass audit, so the Hole counts coincide. For a qualitative view of artifact navigability and governance—workflow overview, ToC-faithful source-to-module alignment, and representative verified Lean excerpts—see Appendix D.

We quantify Stage 1 using three metrics: SCC (statement compile coverage), the fraction of atomic blocks whose insertion and repair yields a file with zero error-level diagnostics; ARR (average repair rounds), the mean number of repair attempts per block (zero for blocks that elaborate immediately); and PB (project buildability). Compute is reported in verifier calls (one call is one invocation of file elaboration/typechecking via lake env lean); Stage 1 uses a per-block cap K = 3 verify→repair attempts. Table 3 shows SCC = 100% and PB true on all long-form corpora, with ARR far below 1.0 (0.42/0.08/0.20), meaning that the refinement loop rarely needs to intervene beyond the generated skeletons; in particular, ARR < 0.5 implies that strictly more than half of blocks require zero patch attempt, and the observed ARR values yield conservative lower bounds that at least 58%/92%/80% of blocks elaborate immediately after insertion. Overall, these results support a practical view of textbook-scale import as an infrastructure problem: most of the work is carried by toolchain-certified generation plus localized repair, while human effort is concentrated on lightweight review rather than dense manual authoring.

- Table 3: Stage 1 statement compilation. PB indicates whether the final project builds under E (allowing sorry). Metric Real Analysis Convex Analysis Paper


SCC (%) 100 100 100 ARR (rounds) 0.42 0.08 0.20 PB ✓ ✓ ✓

#### 6.3 Proof Repair under Matched Statements

- Stage 2 evaluates proving capability isolated from statement generation under matched statements: starting from the same statement layer, each target proof is replaced by sorry, and methods may edit only proofs; PSR is the fraction of holes closed while preserving elaboration under E. To avoid conflating wall-clock variability with algorithmic behavior, we report compute in verifier calls; Stage 2 uses bounded retries and replanning (R = 10, C = 21), with totals reported in Appendix C, and non-verifier oracle calls are not counted by default (Appendix C). The full Stage 2 closes all audited holes on all three long-form corpora (PSR = 100%; Table 2). To isolate which components matter under a fixed statement layer, we run ablations on a representative slice of each long-form corpus:one fixed slice defined by a single dataset file per corpus from each of Real Analysis, Convex Analysis, and Paper, and PSR is computed on the audited holes within that slice. Table 4 reports the resulting PSR. Because the sampled Real Analysis slice contains mostly routine obligations, several variants saturate at 100% there; the slice is still informative for stress-testing the refinement loop itself, as one-shot repair drops sharply. In contrast, the Paper slice is substantially more sensitive: diagnostics-only collapses (13.85%), and disabling replanning also degrades performance, indicating that structured goal/context conditioning and plan revision are critical beyond local diagnostic repair when exposition is heterogeneous and dependencies are implicit.


- Table 4: Stage 2 ablations under matched statements on fixed slices (one dataset file per long-form corpus, selected and then fixed; slice identifiers are reported in Appendix A.4). PSR is computed on holes within each slice; full-corpus results are in Table 2.


Method Real Analysis Convex Analysis Paper One-shot 45.45 63.94 46.15 Diagnostics-only 100 95.45 13.85 No replanning (C=1) 100 90.91 46.97 M2F (full Stage 2) 100 100 100

On FATE-H, Stage 2 is evaluated in isolation (statements already elaborate): we replace each target proof with sorry and run proof repair under matched statements. Because external systems do not expose comparable verifier-call accounting, we compare PSR rather than verifier-normalized efficiency. Table 5 shows that M2F reaches 96% fully automatically, improving by 16 points over the strongest reported Seed-Prover variant (80%). We further define a reproducible light-supervision condition as an additional input artifact: a JSON lemma map with 31 entries, each consisting of (i) a fully-qualified Lean declaration name available under E and (ii) a one-sentence natural-language role description; no proof scripts, tactics, or intermediate derivations are provided. With the Stage 2 algorithm, budgets, and prompts unchanged (the lemma map is used only as extra conditioning context), the same pipeline solves one additional instance, reaching 97%.

35

Seed-Prover 1.0

80

Seed-Prover 1.5

- 96
- 97


M2F (fully automatic)

M2F (with human assistance)

0 20 40 60 80 100

PSR (%)

Figure 2: PSR on FATE-H across provers.

Table 5: Stage 2 on FATE-H (100 problems) under matched statements. Entries are PSR (%). “+31 decl lemma map” is a reproducible light-supervision condition: a JSON lemma map with 31 fullyqualified Lean declaration names, each annotated by a one-sentence natural-language role description; no proof scripts or step-by-step traces are provided.

Method FATE-H

Seed-Prover 1.0 (medium) 35 Seed-Prover 1.5 (agentic prover only) 57 Seed-Prover 1.5 80 M2F (fully automatic) 96 M2F (+31 decl lemma map) 97

#### 6.4 Failure Analysis

On FATE-H, the four instances not solved automatically decompose cleanly by cause: one is solved under the reproducible +31-decl lemma-map condition; one is a benchmark issue whose formal Lean statement is inconsistent and therefore unprovable under E; and two remain unsolved in our current runs without expert lemma maps. The benchmark issue was surfaced during M2F-assisted investigation: verifier-in-the-loop traces localized the inconsistency and enabled expert review to confirm the statement-level error, while the LLMbased semantic checks we tried (including GPT-5.2 Pro and other frontier models) did not flag the problem. This case illustrates how formal languages and proof-assistant verifiers complement large models: beyond proving, verifier-guided workflows can detect subtle statement errors and provide high-precision, mechanizable feedback signals that are useful for improving model reasoning and for curating reliable benchmarks.

### 7 Conclusion

We presented M2F, a verifier-in-the-loop pipeline that compiles textbook- and paper-scale sources into Lean projects that build end-to-end under a pinned environment while preserving span-level provenance. M2F combines dependency-aware statement compilation with matched-statement proof repair via goal-conditioned edits under a toolchain-certified accept/revert rule. On 479 pages, it produces a 153,853-LoC buildable library and closes all audited obligations; on FATE-H it solves 96% fully automatically and 97% with a 31-declaration natural-language lemma map. M2F also surfaced a FATE-H statement error missed by state-of-the-art LLM-based semantic checks (including GPT-5.2 Pro), underscoring the value of formal verification as both a prover oracle and a high-precision signal for evaluating and improving large-model mathematical reasoning. Overall, the remaining bottleneck shifts to natural-language grounding and library navigation.

### References

- [1] Azerbayev, Z., Piotrowski, B., Schoelkopf, H., Ayers, E. W., Radev, D., and Avigad, J. Proofnet: Autoformalizing and formally proving undergraduate-level mathematics, 2023. URL https://arxiv. org/abs/2302.12433.
- [2] Bouzenia, I., Devanbu, P., and Pradel, M. Repairagent: An autonomous, LLM-based agent for program repair, 2024. URL https://arxiv.org/abs/2403.17134.
- [3] Cabral, R., Do, T. M., Xuejun, Y., Tai, W. M., Feng, Z., and Shen, X. Proofflow: A dependency graph approach to faithful proof autoformalization, 2025.
- [4] Chen, J., Chen, W., Du, J., Hu, J., Jiang, Z., Jie, A., Jin, X., Jin, X., Li, C., Shi, W., Wang, Z., Wang, M., Wei, C., Wei, S., Xin, H., Yang, F., Gao, W., Yuan, Z., Zhan, T., Zheng, Z., Zhou, T., and Zhu, T. H. Seed-prover 1.5: Mastering undergraduate-level theorem proving via learning from experience,

2025. URL https://arxiv.org/abs/2512.17260.

- [5] de Moura, L. and Ullrich, S. The Lean 4 theorem prover and programming language. In Platzer, A. and Sutcliffe, G. (eds.), Automated Deduction – CADE 28, volume 12699 of Lecture Notes in Computer Science, pp. 625–635. Springer, 2021. doi: 10.1007/978-3-030-79876-5\ 37. URL https: //doi.org/10.1007/978-3-030-79876-5_37.

- [6] de Moura, L. M., Kong, S., Avigad, J., van Doorn, F., and von Raumer, J. The Lean theorem prover (system description). In Felty, A. P. and Middeldorp, A. (eds.), Automated Deduction – CADE-25, volume 9195 of Lecture Notes in Computer Science, pp. 378–388. Springer, 2015. doi: 10.1007/978-3-319-21401-6\

26. URL https://doi.org/10.1007/978-3-319-21401-6_26.

- [7] Gao, G., Wang, Y., Jiang, J., Gao, Q., Qin, Z., Xu, T., and Dong, B. Herald: A natural language annotated Lean 4 dataset. In The Thirteenth International Conference on Learning Representations (ICLR), 2025. doi: 10.48550/arXiv.2410.10878. URL https://openreview.net/forum?id=Se6MgCtRhz.


- [8] Gulati, A., Ladsaria, D., Mishra, S., Sidhu, J., and Miranda, B. An evaluation benchmark for autoformalization in Lean4, 2024. URL https://arxiv.org/abs/2406.06555.
- [9] Guo, Q., Wang, J., Zhang, J., Kong, D., Huang, X., Xi, X., Wang, W., Wang, J., Cai, X., Zhang, S., and Ye, W. Autoformalizer with tool feedback, 2025.
- [10] Jiang, J., He, W., Wang, Y., Gao, G., Hu, Y., Wang, J., Guan, N., Wu, P., Dai, C., Xiao, L., and Dong, B. Fate: A formal benchmark series for frontier algebra of multiple difficulty levels, 2025. URL https://arxiv.org/abs/2511.02872.
- [11] Lebl, J. Real Analysis. 2016. Available online at https://www.jirka.org/ra/.
- [12] Li, C., Wang, Z., He, W., Wu, Y., Xu, S., and Wen, Z. Formalization of complexity analysis of the first-order algorithms for convex optimization, 2024. URL https://arxiv.org/abs/2403.11437.
- [13] Li, C., Ma, W., Wang, Z., and Wen, Z. Sita: A framework for structure-to-instance theorem autoformalization, 2025.
- [14] Li, C., Wang, Z., Bai, Y., Duan, Y., Gao, Y., Hao, P., and Wen, Z. Formalization of algorithms for optimization with block structures, 2025. URL https://arxiv.org/abs/2503.18806.
- [15] Li, C., Xu, S., Sun, C., Zhou, L., and Wen, Z. Formalization of optimality conditions for smooth constrained optimization problems, 2025. URL https://arxiv.org/abs/2503.18821.
- [16] Lu, J., Wan, Y., Huang, Y., Xiong, J., Liu, Z., and Guo, Z. Formalalign: Automated alignment evaluation for autoformalization, 2024. URL https://arxiv.org/abs/2410.10135.
- [17] Lu, J., Wan, Y., Liu, Z., Huang, Y., Xiong, J., Liu, C., Shen, J., Jin, H., Zhang, J., Wang, H., Yang, Z., Tang, J., and Guo, Z. Process-driven autoformalization in Lean 4, 2024. URL https: //arxiv.org/abs/2406.01940.
- [18] Monperrus, M. Automatic software repair: A bibliography. ACM Computing Surveys, 51(1):17:1–17:24,

2018. doi: 10.1145/3105906. URL https://doi.org/10.1145/3105906.

- [19] Ospanov, A. and Yousefzadeh, R. APOLLO: Automated LLM and Lean collaboration for advanced formal reasoning, 2025. URL https://arxiv.org/abs/2505.05758.
- [20] Poiroux, A., Weiss, G., Kuncˇak, V., and Bosselut, A. Reliable evaluation and benchmarks for statement autoformalization, 2024. URL https://arxiv.org/abs/2406.07222. Also appeared at EMNLP 2025.
- [21] Ren, Z. Z., Shao, Z., Song, J., Xin, H., Wang, H., Zhao, W., Zhang, L., Fu, Z., Zhu, Q., Yang, D., Wu, Z. F., Gou, Z., Ma, S., Tang, H., Liu, Y., Gao, W., Guo, D., and Ruan, C. Deepseek-prover-v2: Advancing formal mathematical reasoning via reinforcement learning for subgoal decomposition, 2025. URL https://arxiv.org/abs/2504.21801.
- [22] Rockafellar, R. T. Convex Analysis, volume 28 of Princeton Mathematical Series. Princeton University Press, Princeton, NJ, 1970.
- [23] Tang, H., Hu, K., Zhou, J. P., Zhong, S., Zheng, W.-L., Si, X., and Ellis, K. Code repair with LLMs gives an exploration-exploitation tradeoff, 2024. URL https://arxiv.org/abs/2405.17503. NeurIPS 2024.
- [24] The mathlib Community. The Lean mathematical library. In Proceedings of the 9th ACM SIGPLAN International Conference on Certified Programs and Proofs (CPP ’20). Association for Computing Machinery, 2020. doi: 10.1145/3372885.3373824. URL https://doi.org/10.1145/3372885.3373824.
- [25] Wang, H., Liu, Z., Wang, S., Cui, G., Ding, N., Liu, Z., and Yu, G. INTERVENOR: Prompting the coding ability of large language models with the interactive chain of repair. In Findings of the Association for Computational Linguistics: ACL 2024, 2024. doi: 10.18653/v1/2024.findings-acl.124. URL https://aclanthology.org/2024.findings-acl.124/.


- [26] Wang, H., Xie, R., Wang, Y., Gao, G., Yu, X., and Dong, B. Aria: An agent for retrieval and iterative auto-formalization via dependency graph, 2025.
- [27] Wu, Y., Jiang, A. Q., Li, W., Rabe, M. N., Staats, C., Jamnik, M., and Szegedy, C. Autoformalization with large language models. arXiv preprint arXiv:2205.12615, 2022. URL https://arxiv.org/abs/ 2205.12615.
- [28] Xin, H., Ren, Z. Z., Song, J., Shao, Z., Zhao, W., Wang, H., Liu, B., Zhang, L., Lu, X., Du, Q., Gao, W., Zhu, Q., Yang, D., Gou, Z., Wu, Z. F., Luo, F., and Ruan, C. Deepseek-prover-v1.5: Harnessing proof assistant feedback for reinforcement learning and monte-carlo tree search, 2024. URL https://arxiv.org/abs/2408.08152.
- [29] Yang, K., Swope, A. M., Gu, A., Chalamala, R., Song, P., Yu, S., Godil, S., Prenger, R., and Anandkumar, A. LeanDojo: Theorem proving with retrieval-augmented language models. arXiv preprint arXiv:2306.15626, 2023. URL https://arxiv.org/abs/2306.15626. NeurIPS 2023 (Datasets and Benchmarks Track).
- [30] Yasunaga, M. and Liang, P. Graph-based, self-supervised program repair from diagnostic feedback. In Proceedings of the 37th International Conference on Machine Learning (ICML), volume 119 of Proceedings of Machine Learning Research. PMLR, 2020. URL https://proceedings.mlr.press/ v119/yasunaga20a.html.
- [31] Ying, H., Wu, Z., Geng, Y., Wang, J., Lin, D., and Chen, K. Lean workbook: A large-scale Lean problem set formalized from natural language math problems, 2024. URL https://arxiv.org/abs/2406.03847.
- [32] Zheng, K., Han, J. M., and Polu, S. Minif2f: a cross-system benchmark for formal olympiad-level mathematics. In International Conference on Learning Representations (ICLR), 2022. doi: 10.48550/ arXiv.2109.00110. URL https://openreview.net/forum?id=9ZPegFuFTFv.


### A Prompting Philosophy and Instrumentation Details

This appendix documents two cross-cutting design choices that shape our system across all stages. First, we summarize the prompting philosophy that we use to make the model produce canonical, mathlib-aligned Lean statements and stable proofs. Second, we describe the instrumentation semantics that make the pipeline auditable and enable the verifier-normalized compute accounting in Appendix C. We intentionally do not include literal prompt templates; instead we describe the design principles that guided prompt construction and the semantics of what is logged.

#### A.1 Prompting philosophy

Our prompting philosophy is organized around one principle: statement-first formalization. Across stages, we treat “writing the right statement” as the most important driver of downstream success. In practice, a statement that is minimal, canonical, and aligned with existing mathlib interfaces can dramatically reduce proof difficulty by avoiding accidental typeclass obligations, brittle goal shapes, and unnecessary rewriting overhead.

Choosing the right declaration form. Prompts are designed to make the model choose standard Lean and mathlib declaration forms with canonical binders. We encourage def for definitions of data/functions/predicates, abbrev when lightweight unfolding behavior is desirable, and structure for packaging fields when typeclass inference is not intended. We use class only when downstream code should consume the structure via typeclass inference; otherwise structure is preferred. For propositions, we use theorem for results explicitly presented as theorems in the source and default to lemma otherwise. Finally, we reserve instance for canonical typeclass instances that should be found by inference, and we avoid inventing instances solely to make automation or rewriting easier.

Avoid inline proofs inside terms. A stability rule in our prompts is to avoid embedding proofs inside larger terms. Concretely, prompts discourage (and in some stages forbid) writing proof snippets such as (by ...) or ⟨...,by ...⟩ inside a term-level construction. When a construction requires proof obligations (for example, closure properties for subtypes or structure fields), we design prompts to first introduce a separate helper lemma with a clean, minimal statement and then reference that lemma by name in the larger term. This yields flatter goal structure, improves readability, and makes later repair and proof search more modular. Additional constraints for definitions. Definitions are handled more strictly than propositions. Prompts are designed so that the model do not use tactic-mode proofs inside a def body; definitions should be expressed as short term constructions. If a definition appears to require substantial proof work, prompts steer the model toward splitting: define the object/predicate with a clean def or abbrev, and move properties or obligations into separate lemmas. When a definition must be left incomplete, prompts prefer := sorry (not by sorry) to avoid introducing tactic blocks into definitions.

Placeholders in Stage 1. Stage 1 allows placeholders to obtain a compilable statement layer. Prompts enforce a consistent policy: proposition-valued declarations use := sorry as a proof placeholder, and definitions use := sorry if a placeholder is necessary. We avoid using axiom to bypass obligations unless the global project rules explicitly allow it.

- A checklist for “good statements”. Prompts implicitly encode (and our human review follows) a checklist that encourages canonical statements. We reuse existing mathlib structures and predicates whenever possible instead of introducing ad-hoc ones, minimize binders and keep them canonical, separate object definitions from properties, avoid inline proofs inside terms by factoring helpers, and avoid non-canonical instances. Docstrings are required. Prompts require a short natural-language docstring immediately above each new declaration (/-- ... -/ in Lean). Docstrings are intended to improve maintainability and future reuse: they should briefly describe what the declaration is, why it exists, and (when applicable) how it relates to the source material. We avoid copying long verbatim text from the source; concise descriptions are preferred. Proof stability and timeout robustness. When writing proofs (especially in Stage 2), prompts prioritize stable proof scripts and discourage forms that frequently trigger deterministic slowdowns. We avoid long, deeply nested chains of have statements and prefer flatter structures using standard combinators such as intro, refine, calc, rw, and simp. When a proof repeatedly requires many intermediate facts, prompts treat this as a signal that the statement or helper-lemma shape may be suboptimal; the model is encouraged to revise the statement layer or factor additional helpers rather than continuing a brittle proof search.


Table 6: Instrumentation artifacts: content and primary use. Artifact Contents Primary use Per-call model log Full stdout/stderr for one model invocation, including

Per-call auditing/debugging; token backfill from stable markers

effective prompt, tool-wrapper outputs, and emitted diffs; may also include token markers

Progress checkpoint (JSON)

A single resume cursor (e.g., next item or next file) plus minimal run identifiers

Crash-safe resumability without reprocessing completed targets

History store (JSONL)

Compact per-target records across retries (plan summaries, key errors, selected fields)

Debugging and optional continuity context for later attempts

Primary source for paper metrics and verifier/oracle call accounting

Metrics event log (JSONL)

Append-only event stream with run/item/file boundaries, verifier checks, and oracle/model-call outcomes

Metrics summary (JSON)

Run-end aggregates that mirror the final run end event payload

Quick run-level accounting without scanning JSONL logs

Token backfill (JSONL)

Per-target token totals reconstructed from stable token markers in per-call logs

Robust token accounting when metrics events omit per-call token fields

Failure rollup (optional)

Append-only human-readable list of persistent item/file failures with pointers

Fast triage and rerun planning

Stage-specific intent. Stage 1 aims to produce a Lean project that elaborates under the pinned environment while allowing proof placeholders, so prompts emphasize canonical signatures, minimal assumptions, consistent placeholder policy, and diagnostics-driven repairs with small, local edits. Stage 2 aims to eliminate target proof holes while preserving the audited statement layer, so prompts emphasize respecting matched statements (no signature edits), goal-directed proof search when goal/context is available, stable proof structure, and factoring nontrivial obligations into helper lemmas rather than embedding proofs inside terms.

How we package context to the model. A central tradeoff is over-conditioning (too much context causing unnecessary refactors) versus under-conditioning (too little context causing missing assumptions or wrong types). We adopt a minimal sufficient context principle: each prompt includes only the information needed for the current local decision. Across stages, prompt inputs may include the focal content (an atomic block or a small neighborhood around a target hole), explicit edit-scope constraints, localized verifier diagnostics or goal/context information, and a compact shared header/import/notation context. Windowing and truncation rules are fixed to keep prompts within model limits and to ensure repeatability; the corresponding artifact schemas that store prompt inputs are described in Appendix B.

#### A.2 Instrumentation semantics

Instrumentation is designed so that reported metrics can be reconstructed from machine-readable logs rather than manual bookkeeping. We log at attempt granularity: each model invocation and each verifier check produces a structured record, and runs also emit an append-only metrics stream. This section describes what we log and how it is used; Appendix B gives the corresponding JSON/JSONL schemas.

##### A.2.1 Artifact types and their semantics

We distinguish three levels of artifacts. First, per-call logs provide a full audit trail for each model call (inputs/outputs/diffs/tokens) and are primarily used for debugging and token backfill. Second, compact JSON/JSONL stores provide structured, queryable traces: progress checkpoints for resumability, history stores for “memory” and debugging, and a metrics event log for analytics. Third, optional rollups provide human-friendly summaries of persistent failures.

Table 6 summarizes the semantic role of each artifact category. We emphasize semantic intent rather than on-disk paths; Appendix B specifies the corresponding machine-readable formats.

##### A.2.2 Recoverability: checkpoints and resumable runs

Long runs can be interrupted by timeouts, infrastructure instability, or budget limits. To make experiments recoverable, each pipeline maintains a single-key JSON checkpoint that stores the next target to process. We treat the exact key name and schema as part of the JSON artifact specification and describe it in Appendix B.3; Appendix A.2.2 explains the operational semantics (when the cursor advances, when it stops, and how runs resume deterministically).

Why checkpointing matters for accounting. Checkpointing guarantees that totals computed from logs can be reconstructed without ambiguity. When a run is resumed, the resumed segment emits a new run id in the metrics stream, so corpus-level totals are computed by summing over the run ids included in the reported experiment. This design prevents double counting and makes it clear which targets were attempted in each segment.

##### A.2.3 Per-call logs: auditability and token extraction

Per-call logs are produced for every model invocation. They are human-readable and capture the full transcript needed to reproduce what the model saw and did, including any diffs applied to the Lean project.

Per-call log delimiters and token footer. Per-call logs begin with a literal STDOUT: section and then a literal STDERR: section. Token usage is recorded as a two-line footer containing the literal marker tokens used followed by a decimal integer (commas may appear). Our tooling parses this with a robust regex equivalent to tokens used\s*([0-9][0-9,]*).

Audit scope. Because the per-call log contains the effective prompt (as printed by the Codex wrapper) and the corresponding stdout/stderr transcript, it provides a complete audit trail for debugging and for reconstructing token usage even when metrics events omit per-call token fields. Per-call logs are also used to diagnose failures that involve toolchain behavior (e.g., unexpected verifier output or wrapper exceptions) that may not be captured in compact JSON summaries.

##### A.2.4 Structured stores: history and metrics

History store (JSONL). The history store is an append-only JSONL stream of compact per-task records. Each record includes a timestamp, a run id, a task identifier, a kind tag (plan, replan request, fix attempt, warning cleanup, etc.), and a payload object. The payload is designed to be lightweight and may truncate long strings to keep the store compact. When history augmentation is enabled, a small window of recent records for the current file/task is loaded and included in later prompts to improve continuity across retries without requiring the full per-call logs.

Metrics event log (JSONL). The metrics event log is the primary machine-readable instrumentation for paper metrics and accounting. It is an append-only JSONL stream where each line is a JSON object with a timestamp, a run id, an event label, and an event payload. Event labels cover run start/end, item/file start/end, verifier checks, and model-call results. When present, event payloads may additionally include file snapshot summaries (size, modification time, line counts) that allow change-size analyses without reading full diffs.

MCP/LSP tool queries are logged but not counted. During statement, proof, and final editing, the wrapper may issue Lean LSP/MCP queries (for example: diagnostics refreshes, goal inspection, hover/type information, local search, completions, and running small Lean snippets) to support interactive refinement. These tool queries are recorded only in the raw per-call transcripts and are not emitted as structured metrics events. As a result, the oracle-call totals in Appendix C—which are derived from model-invocation events—do not include the frequency of LSP/MCP queries, and token totals do not include any cost attributable to these local tool queries. In practice, LSP/MCP usage can contribute to wall-clock time and local compute, but it is excluded from our verifier-normalized and token-based accounting.

##### A.2.5 Implementation notes: resumability and file-local verification

All pipelines iterate deterministically over their target inventory (dataset indices for item-level stages, or a fixed file list for file-level cleanup). To support interruption and restart, each pipeline maintains a single JSON checkpoint that stores the next target cursor; on restart, the pipeline reloads this checkpoint and

resumes without re-processing completed targets. This design avoids manual bookkeeping and enables reliable aggregation across runs: if a corpus/stage setting is completed across multiple resumptions, the reported totals simply sum across the corresponding run ids.

Verification is performed file-locally using a pinned Lean environment: the pipeline repeatedly runs a single-file compile check (e.g., lake env lean <file>) on the currently edited file rather than rebuilding the entire project after every local edit. This is both a performance choice and an accounting choice: each such single-file compile check is exactly one verifier call in our cost model (Appendix C.1), and the corresponding diagnostics provide the accept/reject signal for commit/rollback in all stages.

For very large generated sections, an optional splitter can refactor a file into multiple parts connected by a deterministic import chain (e.g., sectionYY partK.lean files imported by a thin aggregate module). When splitting is enabled, proof repair targets only the containing part file, keeping both verification and patch scope local and reducing instability caused by overly large files.

##### A.2.6 Mapping metrics events to paper metrics

The paper reports (i) success rates, (ii) verifier-normalized compute, (iii) oracle-call frequency, and (iv) token usage (as a complementary cost proxy). All of these can be derived from the metrics event log and (for tokens) optionally corroborated via token backfill.

Success and completion. For item-level pipelines, completion status is defined by item-end events that record whether the target item was processed successfully under budget. For file-level final cleanup, completion status is defined by file-end and task-end events that record whether a file verified and how many sorry occurrences were eliminated.

Verifier calls. Verifier-call totals are computed by counting verifier-check events (labeled lean check in our logs) and aggregating across the run ids included in a reported corpus/stage setting. For some Stage 1 runs produced with an older metrics schema, verifier-check events may not be emitted explicitly; in that case we reconstruct verifier-call totals from per-item retry counters as described in Appendix C.3. Appendix C defines verifier calls as our primary compute unit and describes the aggregation procedure.

Oracle calls and token usage. Oracle-call totals are computed by counting model-result events (agent result events) and summing across run ids, again matching the aggregation used for verifier calls. For some

- Stage 1 runs produced with an older metrics schema, explicit repair-call events may not be emitted; in that case we reconstruct oracle-call totals from the same per-item retry counters used for verifier-call reconstruction (Appendix C.6). When per-call token counts are present in metrics, token totals can be computed by summing those fields. To make accounting robust across logging variants, we also provide a token-backfill procedure that parses stable token markers from per-call logs and emits structured per-task token totals; Appendix B.7 specifies this artifact and Appendix C explains how it is used for reporting.

A.3 Human statement-audit protocol (faithfulness gate)

- Stage 2 evaluation relies on a statement layer whose faithfulness is checked against the original source. For each long-form corpus (our textbook corpora and the paper corpus), theorem/lemma statements used in Stage 2 evaluation are manually audited by a human expert against the provenance-linked source excerpt shown during statement compilation. This audit is the only correctness gate for statement faithfulness: model-based reviewers may be used for triage, but they are not treated as a guarantee because the statement layer is itself model-generated and reviewer models can share correlated failure modes. Audit checklist. Auditors compare the Lean declaration (binder structure, hypotheses, conclusion) against the corresponding source excerpt under standard informal conventions. In particular, they check (i) quantifier structure and binder order, including implicit “for all” in prose; (ii) side conditions and domain restrictions (e.g., non-emptiness, measurability, integrability, boundedness); (iii) the logical strength of the conclusion; and (iv) whether any additional Lean-side assumptions were silently introduced (e.g., extra typeclass constraints) or omitted. A statement is accepted iff the Lean signature is judged equivalent in mathematical content to the source excerpt. Coverage and corrections. For the textbook corpora used in our matched-statement Stage 2 evaluation, we manually audit every theorem/lemma statement that serves as a proof target. In the current revision, this audit did not require statement-level edits: after checking the generated Lean signatures against the source


excerpts, we found them faithful and therefore froze the matched statement layer as generated. Because early runs did not maintain a separate per-statement audit ledger, we do not report a separate audited-statement count here; instead, the evaluation target counts (numbers of proof targets/holes) are reported in the main text (Table 2) and are the same targets used for the accounting totals in Appendix C.

Audit provenance and identifiers. Each audited statement is identified by the tuple (data file, index, label): data file is recorded at run start, and index and textttlabel are recorded at item start/end. The source excerpt used for audit is exactly the dataset record payload (the content field together with any accompanying section context and dependencies when present) that was shown to the model during statement compilation; this payload is serialized into prompt metadata and preserved verbatim in the per-call model logs. The audited Lean declaration is linked back to the same item via its index and textttlabel, which also appears in the docstring/comment immediately preceding the generated declaration in the Lean file. In our current datasets and logs, the excerpt is stored as a LaTeX string.

#### A.4 Stage 2 ablation slices (section identifiers)

For Table 4, each long-form corpus uses a fixed ablation slice defined by a single dataset file (recorded as data file). All ablation methods for that corpus are run on the same fixed slice. We report slice identifiers by data file together with the observed number components coverage (where number components = [chapter, section, ...]).

- • Real Analysis (Lebl). data/proof/ch-real-nums.json; observed coverage: chapter = 1, section ∈ {1,2,3,5}.
- • Convex Analysis (Rockafellar). data/section04.json; observed coverage: chapter = 4, section ∈ {1,2,3,4,5,6,7,8}. Note that despite the filename section04.json, this slice spans multiple sections within Chapter 4.
- • Paper. data/nesterov05_full.json; observed coverage: chapter = 1, section ∈ {1,2,3,4,5}. Paper-only micro-ablation. We additionally ran a paper-only micro-ablation restricted to Chapter 1, Section 5 with slice id filtered__nesterov05_full__chap01_sec05.json (observed coverage: chapter = 1, section = 5).


### B Semantic-First JSON Schemas for Intermediate Artifacts

This appendix specifies the machine-readable intermediate artifacts used for preprocessing inputs, resumability, debugging, and metrics reconstruction. Appendix A.2 describes the semantic role of these artifacts; here we focus on stable schema structure and invariants. We intentionally avoid committing to any on-disk directory layout or filename convention. Instead, we define each artifact by its semantic category (dataset record, checkpoint, history record, metrics event record, metrics summary, token backfill).

#### B.1 Dataset record: a natural-language item

A dataset record is the canonical task input describing one extracted mathematical unit (definition/lemma/theorem/etc.) in natural language (LaTeX-like). The statement pipeline consumes the statement text to generate a Lean declaration skeleton. The proof pipeline consumes the proof text (when present) to attempt proof completion for items that are meaningful proof targets (e.g., skipping definition-only records).

Container format and ordering. A dataset is stored as a JSON array; each element is a record. Consumers iterate deterministically by sorting records on index, even if the input is already sorted. This makes partial runs resumable and ensures that logs are comparable across machines.

Record schema (semantic view). Each record combines (i) stable identity, (ii) source position metadata, and (iii) the extracted content used for prompting. Table 7 summarizes the keys and their meaning.

Section metadata (context). The context object records where the item appears in the source. In our runs it includes chapter/section titles together with numeric indices (chapter/section/subsection). Values may be empty strings when the source lacks a corresponding heading. Consumers use this metadata for deterministic target positioning and, in some configurations, for mapping items to a file/namespace layout.

Table 7: Dataset record keys (semantic schema). Key Meaning / used for index Stable integer identifier; defines iteration order and is used as the primary

resume cursor. label Human-readable label (e.g., “Lemma 1.1”); used in logs and for locating targets. env Coarse type tag (e.g., definition vs. proposition); used for filtering which items are proof targets. number components Numbering decomposition used as a fallback for deterministic target position-

ing.

extracted labels Source-level labels attached to the item; helpful for traceability and context. context Structured section metadata (chapter/section titles and indices) used for

deterministic file/position inference. content Extracted statement text; primary input to statement compilation prompts. dependencies Lightweight dependency labels used as optional local context (consumer-

specific). proof Extracted proof text; may be empty. Proof runs that require proof content skip empty-proof items.

Invariants. The dataset file is a JSON array, index is unique, and consumers treat index order as the canonical iteration order. If proof is empty, proof-stage consumers may skip the record depending on configuration (e.g., when proof text is required as reference context).

##### Example record (redacted).

{ "index": 1, "label": "Definition 1.1.1", "env": "def", "number_components": [1, 1, 1], "extracted_labels": ["def:1.1", "eq:1.1"], "context": {

"chapter_number": 1, "chapter": "___", "section_number": "1", "section": "___", "subsection_number": "", "subsection": ""

}, "content": "\\begin{definition} . . . \\end{definition}", "dependencies": [], "proof": "" }

#### B.2 Lemma-map supervision artifact (declaration-level hints)

In the lightly supervised FATE-H setting, we use an optional lemma map to provide minimal expert guidance for library navigation. A lemma map consists only of declaration-level hints (names or short natural-language descriptions) and explicitly excludes any formal proof scripts, intermediate proof steps, or tactic traces. It conditions planning/retrieval, but it does not affect acceptance: every edit is still accepted or rejected solely by verifier feedback under E.

Schema (semantic view). A lemma map can be represented as a JSON object keyed by problem id (or dataset index). Each entry stores a list of relevant Lean declarations and an optional short note explaining why they are relevant. The exact key names are not important; the semantics are.

{

"problem_id": "FATEH_XX", "decl_hints": [

"Mathlib.Analysis. . ..", "Mathlib.Topology. . .."

], "notes": "optional natural-language rationale"

}

Consumption invariant. Downstream prompts are instructed to treat these hints as navigation cues (which existing theorems/definitions to look at), not as proof steps. In particular, the system may import, unfold, or apply the hinted declarations, but it must still produce a verifier-certified proof without relying on any unverified intermediate claims.

#### B.3 Progress checkpoint: resumable cursor

A progress checkpoint stores the resume cursor for a pipeline. It is a single JSON object with exactly one integer key. Item-level pipelines store the next dataset index to process; file-level pipelines store the next file index to process. Checkpoints are overwritten in-place and are intended to support resuming after interruption.

Schema. Item-indexed pipelines use a key of the form next index. File-indexed pipelines use a key of the form next file index. The value is always the next target to process.

#### B.4 History record: compact per-task trace

A history store is an append-only JSONL stream of compact records used for debugging and (optionally) prompt augmentation. Each line is a single JSON object. As described in Appendix A.2, the purpose of history is to provide lightweight “memory” without reading full per-call logs; here we specify the stable top-level schema and the most common record kinds.

Top-level schema. Each history record includes a timestamp, a pipeline tag, a run id (for cross-reference into the metrics log), a Lean file identifier, a task identifier, a kind tag, an optional short summary, an optional log pointer, and a kind-specific payload object. Table 8 summarizes the keys and their meaning.

Table 8: History record fields (top-level schema). Field Meaning

ts UTC timestamp (ISO8601). pipeline Pipeline tag (e.g., proof or final). run id Run identifier linking to the metrics event log. lean file Lean file identifier (relative path or logical name). task id Task identifier (item index, file-index+line target, compile/warnings task, etc.). kind Kind tag indicating payload interpretation (plan, fix, replan request, warning cleanup,

etc.). summary Optional short summary (may be truncated). log path Optional pointer to a per-call log for deep inspection. payload Kind-specific payload object (may truncate large strings).

Common kinds. In our runs, common kinds include planner outputs, executor replan requests, repair attempts, and (in final cleanup) compilation-fix and warning-cleanup records. Planner records typically store both a structured plan object (when parsable) and a raw plan text block; fix records typically store the motivating Lean error output (as a string) together with basic metadata such as attempt number and token usage.

Truncation invariants. To keep history compact, the history writer may truncate long string fields (for example, summaries and large error logs). Truncation is applied to top-level strings (including selected

payload strings) and is intended as a space-saving mechanism; full raw text remains available in per-call logs when needed. Example history record (redacted).

{ "ts": "2026-01-19T09:55:23.567889+00:00", "pipeline": "proof", "run_id": "proof_stage2_. . ._e70e21ee", "lean_file": "FormalPaper/. . ./section04_part1.lean", "task_id": "34", "kind": "agent_c_plan", "summary": "status=ok | main=smoothedObjective_lipschitz_gradient", "log_path": ". . ./proof_agent_c_. . .log", "payload": {

"round": 1, "code": 0, "tokens_used": 12345, "model": "___", "reasoning_effort": "___", "plan": { ". . .": ". . ." }, "plan_raw": "{. . .}"

} }

#### B.5 Metrics event log: append-only run instrumentation

The metrics event log is the primary machine-readable instrumentation used for paper metrics and compute accounting. It is an append-only JSONL stream where each line is a JSON object with four top-level fields: timestamp, run id, event label, and event payload.

Top-level schema. Every event record has the same top-level structure: ts (UTC timestamp), run id (identifier), event (event label), and data (payload object). This invariant makes logs easy to parse and supports schema evolution by adding fields to data while preserving the top-level form.

Event taxonomy. The precise set of event labels is implementation-defined but stable within a logging schema version. For parsing and analysis, it is sufficient to group events into a small number of families: run boundaries, item/file boundaries, verifier checks, per-agent oracle-call results, and (for plan-driven runs) planning-loop bookkeeping events. Appendix A.2.6 explains how these families are used to derive paper metrics; the key schema invariant here is that every line shares the same top-level structure and the data object contains enough identifiers to attribute the event to a target.

Optional change-size snapshots. Some oracle-result events may include file snapshot summaries before and after applying an edit. These snapshots record whether a file exists and, if it does, its size and a line-count summary. They enable change-size analyses without parsing full diffs.

Example metrics record.

{ "ts": "2026-01-14T17:23:57.451963+00:00", "run_id": "proof_stage2_. . .", "event": "item_start", "data": { "index": 1, "label": "Lemma 1.1", "chapter": 1, "section": 1, "local_index": 1 } }

#### B.6 Metrics summary: end-of-run totals

For convenience, each run writes a metrics summary as a single JSON object. The summary mirrors the run end event payload and provides run-level totals without scanning the full JSONL stream.

Common fields. All summaries include a pipeline identifier and a small set of run-level totals such as processed targets, resume cursor, total elapsed seconds, and aggregated attempt counters. The exact set of counters depends on the pipeline, but the intent is consistent: the summary provides a concise accounting view for that run segment.

##### Example summary (redacted).

{ "pipeline": "final",

"processed_files": 2, "next_file_index": 2, "total_seconds": 951.1927,

- "total_b_attempts": 1,
- "total_c_plans": 1, "total_a_attempts": 1, "total_sorries_eliminated": 1, "total_tokens_used": 123456 }


#### B.7 Token backfill: per-task token totals from per-call logs

Token usage can be reconstructed either from metrics events (when per-call token fields are present) or by parsing stable token markers from per-call logs. To make accounting robust to logging variants, we provide a token-backfill procedure that parses per-call logs, aggregates token totals per task, and emits these totals as a dedicated metrics run.

Backfill event schema. Backfill emits metrics records with event label task tokens. Each record includes a stage tag, a task identifier, total tokens for that task, and a per-agent breakdown when multiple agents contribute to the same task. The record may also include optional convenience fields such as the human label and Lean file identifier when available.

##### Example backfill record (redacted).

{ "event": "task_tokens",

"data": { "stage": "final", "task": "0_L119", "tokens_used_total": 65831, "tokens_used_by_agent": { "a": 34170, "c": 31661 }, "log_file_count": 2, "lean_file": "FormalBook/. . ./section01.lean" } }

### C Verifier-Normalized Compute and Cost Accounting

This appendix defines the compute and cost quantities reported in our experiments and explains how they are reconstructed from the structured artifacts described in Appendix B. Our primary compute unit is the number of Lean single-file compilation checks (verifier calls), because all stages repeatedly apply candidate edits and then re-check the affected Lean file via a uniform pinned environment. In addition, we report the frequency and token usage of model invocations (“oracle calls”) and include a conservative robustness check that charges each oracle call as a fixed fraction of a verifier call.

#### C.1 Compute unit: verifier calls

We measure compute in terms of verifier calls. A verifier call is one invocation of Lean elaboration/typechecking for a single file under the pinned environment E. Operationally, this corresponds to running a single-file compile check (e.g., lake env lean <file>) and collecting the resulting diagnostics.

What is counted. We count every verifier invocation performed by the method, including verifier calls inside repair/search loops and those triggered by any optional stabilization procedures. Concretely, whenever a stage applies a candidate patch and then re-checks the file to decide accept/reject (or to advance to the next target), that re-check contributes one verifier call.

Success criterion for accounting. A file is considered verified iff Lean reports zero error-level diagnostics under E. Warnings are ignored for verification accounting unless they are explicitly promoted to errors by the toolchain or by a pipeline configuration.

Why this unit matches the pipeline design. All stages rely on repeated single-file compilation checks as the ground-truth accept/reject signal. In the statement stage, the system appends a skeleton and compiles

the target file; if compilation fails, it applies a small repair and compiles again. In the proof and final stages, the system alternates between proposing proof edits and compiling to confirm that the file still elaborates (and that the targeted sorry is removed when required). Because these checks are performed in a uniform pinned environment, verifier-call counts are comparable across corpora and stages.

#### C.2 Budgets and per-target caps

Our pipelines are budgeted by placing explicit caps on the number of propose→verify loops and on the number of fallback repairs, so that total compute is predictable and runs are resumable. This subsection restates the caps used in our experiments and fixes notation for the accounting formulas below.

- Stage 1 (statement compilation). For each dataset item processed in Stage 1, the pipeline first generates a Lean statement skeleton (allowing proof placeholders) and then runs a verifier call on the affected file. If verification fails, a local repair routine is invoked and the file is re-verified. We cap the number of local repair rounds per item by a small constant K (a fixed hyperparameter in the experiment configuration). As a result, each Stage 1 item triggers at least one verifier call and at most 1 + K verifier calls, with early termination when the file verifies.
- Stage 2 (proof completion). Stage 2 is organized as a bounded planning-and-execution loop. A planning step proposes a structured proof strategy, and an execution step applies proof edits for the target hole; the file is then verified. If execution fails in a way that suggests a flawed plan, the system may request replanning; if verification fails due to local compilation issues, the system may attempt bounded local repairs. To make accounting explicit, we use two caps: C is the maximum number of planning rounds (including the initial plan), and R is the maximum number of executor attempts per plan. This yields the conservative upper bound B = R · C on the number of executor-driven candidate proof patches for a single target. This is an upper limit; in practice, targets often terminate early once solved or once a stopping condition is reached. Optional file splitting overhead. In some proof runs, a file may be split into multiple parts when it exceeds a line-count threshold, and additional verification checks may be triggered as part of that process. When splitting is enabled, we count the splitter’s model calls as oracle calls (see §C.6) and we count any compilation checks performed during or after splitting as verifier calls.


#### C.3 Reporting total verifier calls

Per-run totals from metrics events. Verifier calls are reconstructed from the metrics event log described in Appendix B.5. Each verifier invocation emits exactly one verifier-check event (in our logs this event is labeled lean check). For a single run r, let Events(r) be the multiset of metrics records for that run, and define

Vr = #{e ∈ Events(r) : e.event = lean check}. When a run is interrupted and resumed, each resumed segment produces its own run id; the corpus-level total is computed by summing Vr across all run ids included in the reported experiment.

Stage 1 metrics variant. Some Stage 1 runs in our archived artifacts were produced with a metrics schema that does not emit explicit lean check events. For these runs, verifier-call totals can still be reconstructed because each processed item triggers one initial file verification, and each bounded repair attempt triggers one additional verification. Let I(r) be the set of Stage 1 items completed in run r (equivalently, the set of item end events), and let b attempts(i) be the recorded number of bounded repair attempts for item i. We then compute

Vr = |I(r)| +

b attempts(i).

i∈I(r)

When lean check events are present (as in Stage 2 runs), we use the direct event-count definition above.

Aggregating by corpus and stage. For each corpus/stage pair reported in the main paper, we aggregate (i) the number of targets processed, (ii) the number solved, and (iii) the total verifier calls. For Stage 1, “targets” refers to the number of dataset items processed in the aggregated runs; “solved” may either be the

number of items whose target file verified at item end, or simply equal to targets if the pipeline configuration guarantees a verified output per item. For Stage 2, “targets” refers to the number of proof targets attempted

Table 9: Total verifier calls and verifier-normalized cost.

Corpus Stage Targets Solved Total verifier calls Calls/solved Notes Textbooks: Real Analysis

- 1 416 416 592 1.42

SCC = 100% sorry allowed

- 2 339 339 628 1.85


Matched statements PSR = 100%

Textbooks: Convex Analysis

- 1 560 560 605 1.08

SCC = 100% sorry allowed

- 2 499 499 1065 2.13


Matched statements PSR = 100%

- 1 67 67 81 1.20

SCC = 100% sorry allowed

- 2 37 37 77 2.08


Paper

Matched statements PSR = 100%

Benchmark: FATE-H (auto) 2 100 96 283 2.95

One instance is incorrect see §6.4

Benchmark: FATE-H (+ lemma map) 2 100 97 368 3.79

31 decl hints see Table 5

under the reported setting, and “solved” refers to the number of targets whose designated proof hole was successfully closed under budget.

- Summary table. Table 9 reports the aggregated target counts, solve counts, and total verifier calls for each corpus/stage setting used in the main paper.


#### C.4 Paper metrics: definitions and log reconstruction

This subsection defines the primary paper metrics and explains how they are reconstructed from the structured logs in Appendix B. Throughout, we treat the Lean toolchain under the pinned environment E as the only acceptance signal: a proposed change “counts” only if it is committed by the pipeline and the subsequent verifier check reports zero error-level diagnostics.

PB (project buildability). PB is true iff the final generated project builds under E (allowing sorry in Stage 1). Operationally, PB is assessed on the end-to-end project state produced by the pipeline, not on an individual item or file. In our instrumentation, PB is recorded as a run-level outcome and can also be reproduced by running a project build in the pinned environment.

SCC (statement compile coverage). Let B be the set of Stage 1 atomic blocks processed in a corpus run. A block is counted as compiled iff its enclosing Lean file elaborates under E after the block insertion/repair loop terminates. We report SCC = |Bok|/|B|. In logs, B is reconstructed from the processed item inventory; success is reconstructed from item-end status markers and the final verifier outcome for the affected file.

ARR (average repair rounds per block). For each block b ∈ B, let a(b) be the number of candidate repair patches attempted after the initial insertion (blocks that elaborate immediately contribute a(b) = 0). We report ARR = |B1

ok| b∈Bok a(b), i.e., the mean repair-attempt count over successfully processed blocks. In logs, a(b) can be reconstructed either by counting repair-result events attributable to that block or by counting the verifier checks that occur inside the bounded verify→repair loop for the block (minus the initial post-insertion check).

PSR (proof success rate under matched statements). Let H be the evaluated set of proof obligations under matched statements (the statement layer is frozen and not edited during proof search). A hole counts

- as closed iff (i) the designated sorry is eliminated in the target file and (ii) the verifier still reports zero


error-level diagnostics for that file under E. We define PSR = |Hclosed|/|H|. In logs, H is reconstructed from the evaluated task inventory together with per-target identifiers, and closure is reconstructed from the first verifier check that both verifies and decreases the hole count for that target.

Auxiliary reporting on FATE-H. Because one FATE-H instance is a benchmark issue whose Lean statement is already incorrect (and thus not provable as stated), we sometimes additionally report success excluding this instance. Concretely, the fully automatic setting solves 96/100 instances (Table 5), while excluding the incorrect instance yields 96/99 ≈ 97.0% solved; see §6.4.

Not solved

Human-assisted

Solved

Error

| |
|---|


| |
|---|


| |
|---|


Linesofcode(logscale)

- 101

- 102

- 103


0 10 20 30 40 50 60 70 80 90 100

File ID

- Figure 3: FATE-H per-problem code length (non-empty lines) and outcome category. Colors indicate outcome: green


= solved automatically, yellow = solved with lemma-map supervision, red = unsolved; the single wrong-statement instance is shown with a distinct style (see §6.4).

#### C.5 FATE-H per-problem length and solved status

To contextualize aggregate success rates on FATE-H, Figure 3 reports, for each of the 100 problems, a simple code-length proxy together with the outcome category under our Stage 2 runs. We define the length of a problem as the number of non-empty lines of Lean code in its source file, measured after preprocessing and proof blanking but before any successful proof patch is applied. Because FATE-H contains many problems, we plot a bar chart: each bar corresponds to one problem (x-axis), and bar length is the line count (y-axis). Outcome categories. Bars are colored by outcome: solved fully automatically (green), solved with light expert help via the lemma map (yellow), and unsolved (red). One additional category marks the single wrong-statement instance (“Error”), discussed in the Failure Analysis (§6.4); this instance is not solvable under E as stated and is visualized with a distinct styling (e.g., a separate color or hatch pattern). In our reported runs, this yields 96 solved automatically, 1 solved with the lemma map, 2 remaining open, and 1 wrong instance (Table 5).

#### C.6 Non-verifier oracle calls and their frequency

In addition to verifier calls, the system makes non-verifier oracle calls to the model through Codex CLI. These calls produce candidate Lean edits (statement skeletons, proof patches, repairs) or structured plans that guide subsequent edits. Oracle calls are not counted as verifier calls, but they can dominate wall-clock time and token usage, so we report their frequency and use them in robustness checks.

What counts as an oracle call. An oracle call is any model invocation whose output can directly change the Lean project or the plan used to change it. In Stage 1, oracle calls include the initial statement-synthesis call and any bounded repair calls used to make the file compile. In Stage 2, oracle calls include planning calls, executor calls that apply proof edits, repair calls that address compilation failures after edits, and (when enabled) splitter calls that refactor large files into multiple parts. In the final cleanup stage (when used), oracle calls include compilation-fix and warning-cleanup calls as well as plan/execution calls that eliminate remaining sorry tokens.

How oracle calls are counted in logs. Oracle calls are reconstructed from the metrics event log (Appendix B.5). Each model invocation emits one oracle-result event whose label identifies the agent role (planner/executor/repair/splitter). We count oracle calls by counting these oracle-result events within each run. If a reported corpus/stage aggregates multiple run ids (e.g., due to resumption), we sum oracle-call counts across those run ids, matching the aggregation used for verifier calls.

Stage 1 metrics variant. Some Stage 1 runs in our archived artifacts were produced with a metrics schema that does not emit explicit repair-call events for the bounded repair agent. However, the Stage 1 control flow makes oracle-call totals reconstructible from the same per-item repair counter: each processed item always triggers one statement-synthesis model call, and each bounded repair attempt corresponds to one additional

###### Table 10: Oracle-call frequency.

Corpus Stage Verifier calls Oracle calls Calls/target Notes Textbooks: Real Analysis Textbooks: Convex Analysis Paper Benchmark: FATE-H (auto) 2 283 339 3.39 Proof-only; statements already elaborate Benchmark: FATE-H (+ lemma map) 2 368 479 4.79 Proof-only; conditioned on decl hints

- 1 592 592 1.42 Statement synthesis + bounded repairs
- 2 628 1263 3.73 Planner/executor/repair calls


- 1 605 605 1.08 Statement synthesis + bounded repairs
- 2 1065 2001 4.01 Planner/executor/repair (+ optional split)


- 1 81 81 1.21 Statement synthesis + bounded repairs
- 2 77 148 4.00 Planner/executor/repair calls


repair model call. Let I(r) and b attempts be as above; we compute

Qr = |I(r)| +

b attempts(i),

i∈I(r)

which matches the verifier-call reconstruction for Stage 1.

Note on Lean LSP/MCP tool queries. Some runs issue lightweight Lean IDE queries during editing (goal inspection, hover/type information, local search, completions, and small snippet execution). These are not model invocations and are not emitted as metrics events, so they are excluded from the oracle-call totals above. They may contribute to wall-clock time and local compute, but they are outside the verifier-normalized and token-based accounting reported in this appendix.

- Summary table. Table 10 reports oracle-call frequency alongside verifier calls, and normalizes by the number of targets to make stages and corpora comparable.

C.7 Token-based cost for oracle calls

Oracle-call frequency measures how many model invocations are made, but it does not capture their size. We therefore additionally report token usage as a proxy for model-side cost.

Token totals. When per-call token counts are recorded directly in metrics events, total tokens can be computed by summing those per-call fields over oracle-result events in the run. To make accounting robust to logging variants, we treat the token-backfill artifact described in Appendix B.7 as the canonical source of token totals when available, because it reconstructs per-task token usage directly from stable token markers in the per-call agent logs.

- Summary table. Table 11 reports total token usage for oracle calls as a complementary proxy for model-side cost, together with a per-solved normalization for the Stage 2 settings.


Table 11: Token usage for oracle calls. Corpus Stage Oracle calls Total tokens Tokens/solved

- 1 592 20429061 49108
- 2 1263 140040564 413099


Textbooks: Real Analysis

- 1 605 28421469 50753
- 2 2001 307966089 617167


Textbooks: Convex Analysis

1 81 2875173 42913 2 148 16362141 442220

Paper

Benchmark: FATE-H (auto) 2 339 44177658 460184 Benchmark: FATE-H (+ lemma map) 2 479 53766276 554292

#### C.8 Fractional accounting robustness check

Verifier calls are our primary compute unit, but model invocations can also contribute nontrivial cost. To check that our conclusions are not sensitive to how oracle calls are priced, we report a conservative fractional accounting view that charges each oracle call as a fixed fraction of a verifier call.

Definition. For a run (or an aggregation of runs), let V be the total number of verifier calls and let Q be the total number of oracle calls (as defined above). For a chosen fraction α ∈ [0,1], we define a verifier-equivalent compute total

Costα = V + α · Q.

We report Costα (and optionally Costα/solved) for a small set of α values that cover “oracle is cheap” to “oracle is comparable” regimes.

Reporting. Unless otherwise stated, we use α ∈ {0.05, 0.10, 0.25}. The corresponding totals are computed from the same reconstructed V and Q used in Tables 9 and 10.

- Summary table. Table 12 reports verifier-equivalent compute totals under fractional accounting for representative choices of α, using the same V and Q aggregates reported above.


Table 12: Fractional accounting: verifier-equivalent compute Costα = V + αQ Corpus/setting V Q Cost0.10 Cost0.25 Textbooks (Real Analysis, Stage 2) 628 1263 754.30 943.75 Textbooks (Convex Analysis, Stage 2) 1065 2001 1265.10 1565.25 Paper (Stage 2) 77 148 91.80 114.00 FATE-H (auto, Stage 2) 283 339 316.90 367.75

### D Qualitative Showcase: Navigable Artifacts with Provenance andDependency Governance

This appendix provides a qualitative view of what the end-to-end system produces as a library artifact, complementing the quantitative results in the main text. While Table 2 already reports the primary scale statistics (files/decls/LoC and end-to-end buildability), we focus here on three properties that are hard to convey with a single success rate: (i) a closed-loop workflow with explicit governance points, (ii) ToCfaithful navigability from a source section to a small, checkable edit scope in Lean, and (iii) provenance- and dependency-centric indicators that support auditing and maintenance.

#### D.1 Workflow overview: a closed loop, not one-shot generation

The system treats project-scale formalization as a closed loop driven by the Lean toolchain: edits are accepted only when the verifier certifies a strict improvement in a build- and hole-based objective. This design gives two practical guarantees that matter at scale. First, failures are localized (file/section/part granularity), enabling fast revert-and-retry without corrupting the rest of the project. Second, outputs are not merely a pile of proofs, but a structured repository with explicit provenance anchors and a controlled import footprint, so that downstream users can audit and maintain the artifact. Figure 4 provides a compact, governance-oriented view of this loop, complementing the end-to-end pipeline diagram in Figure 1.

#### D.2 Source-to-project alignment at section granularity

A central “project-scale” requirement is navigability: readers should be able to move from a source section to the corresponding Lean files with minimal cognitive overhead. For Rockafellar’s Convex Analysis, we mirror the source section numbering (§1–§15) at the module level and display the generated Lean file tree with indentation (not full paths). When a section is too large to edit and verify reliably, the workflow performs a structure-preserving split into partK modules, while keeping a stable section-level entry module as the public import target.

![image 2](Wang et al._2026_M2F Automated Formalization of Mathematical Literature at Scale_images/imageFile2.png)

- Figure 4: System capability manifesto (workflow). A verifier-in-the-loop pipeline that turns PDF-derived structure into a buildable Lean project with (i) provenance anchoring for statement auditability, (ii) human gatekeeping


- at governance points, and (iii) accept/revert refinement driven solely by Lean diagnostics, yielding a queryable repository of verified declarations rather than isolated one-off proofs.


Table 13: System capability manifesto (governance at scale). Indicators that emphasize (i) edit locality via structure-preserving splitting, (ii) dependency governance via an inspectable import footprint, and (iii) auditability via provenance anchors attached to declarations. Scale (files/decls/LoC, PB/PSR) is reported in Table 2.

Indicator Real Analysis Convex Analysis (§1–§15) Paper Max structure-preserving split factor 6-way 23-way 10-way Unique imported modules (approx.) 50 160+ 25+ Provenance anchors in docstrings (approx.) 400+ 600+ 70+ Remaining sorry (closure) 0 0 0

#### D.3 Workflow capability indicators beyond raw scale

The main text already reports corpus scale and buildability (Table 2). Here we focus on governance indicators that are more directly tied to whether the workflow remains controllable as projects grow: how aggressively the system can split a single section without breaking the public module interface, how large the import surface becomes, and whether the artifact carries enough provenance anchors to support auditing. The counts below are computed from our artifact snapshot; where appropriate we report coarse magnitudes (e.g.,

“160+”).

Highlights. In the Convex Analysis artifact, the workflow cleanly executes a 23-way structure-preserving split of a single section, attaches 600+ provenance anchors, and manages 160+ unique imports—a concrete demonstration of dependency governance and auditability at textbook scale. These indicators reflect the system’s ability to keep edit scopes small and dependencies inspectable while still producing end-to-end verified projects.

#### D.4 Representative verified code excerpts

We include three excerpts that illustrate complementary sources of complexity in project-scale formalization. First, we show a textbook-level interface definition from Convex Analysis that is imported across multiple

![image 3](Wang et al._2026_M2F Automated Formalization of Mathematical Literature at Scale_images/imageFile3.png)

![image 4](Wang et al._2026_M2F Automated Formalization of Mathematical Literature at Scale_images/imageFile4.png)

![image 5](Wang et al._2026_M2F Automated Formalization of Mathematical Literature at Scale_images/imageFile5.png)

######                 —       –   

▸

                                       –      

▸

                     –   ▸                      –   

                      –    ▸                      –   

                        –    ▸                      –   

- Figure 5: System capability manifesto (navigability and locality). Rockafellar Convex Analysis (§1–§15) is re-indexed into a ToC-faithful Lean project. The right panel is an indented file tree (not full paths) illustrating structure-preserving splitting (e.g., a single source section expanded into many partK modules) while keeping a stable section module for downstream imports and verifier-local edits.


chapters, illustrating how the artifact exposes reusable notions behind a small, stable API surface (here, the definition of a supporting hyperplane). Second, we include a classical result from Real Analysis (the mean value theorem) as a representative example of a long proof whose correctness must remain stable under localized edits and refactoring; for space, we elide internal steps with ellipses. Third, we present a paper-style theorem with heavy parameterization and layered hypotheses (Algorithm 3.11 / Theorem 1.4.1), which stresses scoping, abbreviation management, and long-range dependencies across the library. For robustness under pdfLaTeX, the listings are lightly normalized (e.g., we use ASCII fallbacks or omit nonessential proof details where appropriate); this affects only presentation and not the underlying Lean development.

/- Convex Analysis (textbook): multi-file dependency surface + interface lemma. -/ import Mathlib

- import FormalBook.Chapters.Chap01.section01_part1
- import FormalBook.Chapters.Chap02.section09_part3
- import FormalBook.Chapters.Chap03.section11_part4


/-- Text 11.3.2: A supporting hyperplane to ‘C‘ is a hyperplane which is the boundary of a supporting half-space to ‘C‘. Equivalently, a supporting hyperplane has the form ‘H = {x | x ·v b = beta}‘ with ‘b ̸= 0‘, such that ‘x ·v b ≤ beta‘ for every ‘x ∈ C‘ and ‘x ·v b = beta‘ for at least one ‘x ∈ C‘. -/ def IsSupportingHyperplane (n : Nat) (C H : Set (Fin n -> Real)) : Prop :=

∃ (b : Fin n → Real) (beta : Real), b ̸= 0 ∧ H = {x : Fin n → Real | x ·v b = beta} ∧ (∀ x, x ∈ C → x ·v b ≤ beta) ∧ ∃ x, x ∈ C ∧ x ·v b = beta

/-- Theorem 4.2.4 (Mean value theorem): If ‘f : [a, b] → R‘ is continuous on the closed interval and differentiable on the open interval, then some ‘c ∈ (a, b)‘ satisfies ‘f b - f a = deriv f c * (b - a)‘. -/ theorem mean_value_theorem

{f : R → R} {a b : R} (h1 : a < b) (hcont : ContinuousOn f (Set.Icc a b)) (hdiff : DifferentiableOn R f (Set.Ioo a b)) : ∃ c ∈ Set.Ioo a b, f b - f a = deriv f c * (b - a) := by

...

/-- Theorem 1.4.1. Assume the structural model (2.2) and that ‘fhat‘ is differentiable with M-Lipschitz gradient on ‘Q1‘. Let ‘d1‘ be a prox-function of ‘Q1‘ with parameter ‘σ1 > 0‘ and prox-diameter ‘D1‘ as in (4.3_D1). Let ‘d2‘ be a prox-function of ‘Q2‘ with strong convexity parameter ‘σ2 > 0‘ and define ‘D2 := max_{u ∈ Q2} d2 u‘ as in Proposition 2.7. Apply Algorithm 3.11 to the smoothed problem (4.1) with ‘µ = µ(N) = (2∥A∥_{1,2}/(N+1)) * sqrt(D1/(σ1 σ2 D2))‘ (equation (thm3_muN)). After ‘N‘ iterations define ‘\hat x := y_N‘ and ‘\hat u := _{i=0}^N 2(i+1)/((N+1)(N+2)) u_µ(x_i)‘ (4.2). Then ‘0 ≤ f(\hat x) - ϕ(\hat u)‘ and the duality-gap bound (4.3) holds, and consequently the ϵ-solution bound (4.4) holds. -/ theorem algorithm311_duality_gap_bound {E1 E2 : Type*} [NormedAddCommGroup E1]

[NormedSpace R E1] [FiniteDimensional R E1] [NormedAddCommGroup E2] [NormedSpace R E2] [FiniteDimensional R E2] (Q1 : Set E1) (Q2 : Set E2) (A : E1 →L[R] (E2 →L[R] R)) (fhat : E1 → R) (phihat : E2 → R) (d1 : E1 → R) (d2 : E2 → R) (σ1 σ2 M D1 : R) (xSeq ySeq : N → Q1) (uµ : E1 → E2) (N : N) (hatu : Q2) : let A’ : E1 →ℓ[R] Module.Dual R E2 :=

{ toFun := fun x => (A x).toLinearMap map_add’ := by

intro x y;ext u;simp map_smul’ := by

intro c x;ext u;simp } let D2 : R := sSup (d2 ’’ Q2) let µ : R := (2 * OperatorNormDef A’ / ((N : R) + 1)) *

Real.sqrt (D1 / (σ1 * σ2 * D2)) let fbar : E1 → R := SmoothedObjective Q2 A phihat d2 µ fhat let f : E1 → R := fun x => fhat x + sSup ((fun u => A x u - phihat u) ’’ Q2) let ϕ : Q2 → R := AdjointFormPotential Q1 Q2 A fhat phihat LipschitzOnWith (Real.toNNReal M) (fun x => fderiv R fhat x) Q1 → 0 < σ1 → 0 < σ2 → StrongConvexOn Q1 σ1 d1 → StrongConvexOn Q2 σ2 d2 → IsProxDiameterBound Q1 d1 D1 → OptimalSchemeAlgorithm Q1 fbar d1

(M + (1 / (µ * σ2)) * (OperatorNormDef A’) ^ 2) σ1 xSeq ySeq → (∀ x, IsSmoothedMaximizer Q2 A phihat d2 µ x (uµ x)) → (hatu : E2) = Finset.sum (Finset.range (N + 1)) (fun i =>

(2 * ((i : R) + 1) / (((N : R) + 1) * ((N : R) + 2))) • uµ (xSeq i : E1)) →

- ConvexOn R Q1 fhat → DifferentiableOn R fhat Q1 →
- ConvexOn R Q2 phihat → (∀ x,


fderiv R (SmoothedMaxFunction Q2 A phihat d2 µ) x =

(AdjointOperator A’ (uµ x)).toContinuousLinearMap) → 0 ≤ M → 0 ≤ D1 → 0 < M + (1 / (µ * σ2)) * (OperatorNormDef A’) ^ 2 → IsClosed Q1 → IsOpen Q1 → ConvexOn R Q1 fbar → DifferentiableOn R fbar Q1 → 0 ≤ µ → (∀ u ∈ Q2, 0 ≤ d2 u) → (∀ x, BddAbove ((fun u => A x u - phihat u) ’’ Q2)) → BddAbove (d2 ’’ Q2) → Q2.Nonempty → (∀ u, BddBelow ((fun x => A x u + fhat x) ’’ Q1)) → 0 ≤ f (ySeq N : E1) - ϕ hatu ∧ f (ySeq N : E1) - ϕ hatu ≤

(4 * OperatorNormDef A’ / ((N : R) + 1)) * Real.sqrt (D1 * D2 / (σ1 * σ2)) +

(4 * M * D1) / (σ1 * ((N : R) + 1) ^ (2 : N)) ∧ ∀ ϵ > 0, (N : R) ≥

(4 * OperatorNormDef A’ / ϵ) * Real.sqrt (D1 * D2 / (σ1 * σ2)) + 2 * Real.sqrt (M * D1 / (σ1 * ϵ)) → f (ySeq N : E1) - ϕ hatu ≤ ϵ := by

...

