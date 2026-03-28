# arXiv:2602.15019v2[cs.AI]17 Feb 2026

## Hunt Globally: Wide Search AI Agents for Drug Asset Scouting in Investing, Business Development, and Competitive Intelligence

### Alisa Vinogradova1*, Vlad Vinogradov1*, Luba Greenwood1,3, Ilya Yasny1,2, Dmitry Kobyzev1,2, Shoman Kasbekar, Kong Nguyen1, Dmitrii Radkevich1, Roman Doronin1, Andrey Doronichev1

1 Bioptic.io, San Francisco, CA 2 LanceBio Ventures 3 Harvard Business School info@optic.inc

##### Abstract

Bio-pharmaceutical innovation has shifted: many new drug assets now originate outside the United States and are disclosed primarily via regional, non-English channels. Recent data suggests over 85% of patent filings originate outside the U.S., with China accounting for nearly half of the global total; a growing share of scholarly output is also non-U.S. Industry estimates put China at ∼ 30% of global drug development, spanning 1,200+ novel candidates. In this highstakes environment, failing to surface "under-the-radar" assets creates multi-billion-dollar risk for investors and business development teams, making asset scouting a coveragecritical competition where speed and completeness drive value. Yet today’s Deep Research AI agents still lag human experts in achieving high-recall discovery across heterogeneous, multilingual sources without hallucinations. We propose a benchmarking methodology for drug asset scouting and a tuned, tree-based self-learning Bioptic Agent aimed at complete, non-hallucinated scouting. We construct a challenging completeness benchmark using a multilingual multiagent pipeline: complex user queries paired with ground-truth assets that are largely outside U.S.-centric radar. To reflect real deal complexity, we collected screening queries from expert investors, BD, and VC professionals, and used them as priors to conditionally generate benchmark queries. For grading, we use LLM-as-judge evaluation calibrated to expert opinions. On this benchmark, our Bioptic Agent achieves 79.7% F1 score, outperforming Claude Opus 4.6 (56.2%), Gemini 3 Pro + Deep Research (50.6%), OpenAI GPT-5.2 Pro (46.6%), Perplexity Deep Research (44.2%), and Exa Websets (26.9%). Performance improves steeply with additional compute, supporting the view that more compute yields better results.

Platform — https://bioptic.io

### Introduction

Large pharmaceutical companies rely heavily on external innovation to sustain and expand their pipelines, with the majority of new drugs sourced externally through Business Development and Search & Evaluation (BD and S&E) functions. While pharmaceutical companies have invested significantly in AI to accelerate internal discovery and develop-

*These authors contributed equally.

![image 1](Vinogradova et al._2026_Hunt Globally Wide Search AI Agents for Drug Asset Scouting in Investing, Business Development, and_images/imageFile1.png)

Figure 1: Quality–time tradeoff for asset scouting. y-axis: F1-score (harmonic mean of precision and recall; higher is better). x-axis: wall-clock time (log scale; larger indicates longer compute). DR here stands for deep research; langfree stands for no language parallelism.

ment, these efforts represent only a small fraction of pipeline development. In contrast, very little progress has been made in applying AI to drug asset scouting, where a substantial share of strategic value lies. In this high-stakes environment, missing a single qualifying program/asset can mean losing a top partnering or acquisition opportunity worth billions of US dollars, making BD and S&E competition where speed and completeness matter [1, 2].

Crucially, this scouting problem is increasingly global and often disclosed through regional channels, with a substantial amount of innovation coming from outside of the US. For example, WIPO patent applications by origin (origin data) underscore how widely innovation is distributed. Recent data indicates that ~86.5% of global patent applications originate outside the US, with China being the largest country of origin, accounting for ~48.2% of worldwide applications [3]. In biopharma, public leadership commentary has similarly emphasized that major portions of development activity now sit outside traditional U.S./EU hubs. For instance, as reported, Pfizer CEO Albert Bourla cited China as ~30% of global drug development with ~1,200 novel drug candidates [4]. Together, these signals motivate a practical shift

![image 2](Vinogradova et al._2026_Hunt Globally Wide Search AI Agents for Drug Asset Scouting in Investing, Business Development, and_images/imageFile2.png)

Figure 2: Completeness Benchmark construction pipeline Top: Assets Mining the Regional News Miner Agent surfaces regional-stage drug assets from non-English sources; the Attributes Enrichment Agent validates and structures each asset; the Google Search Agent prioritizes under-the-radar assets via an English vs. origin-language discoverability check. Bottom: Query Generation real Investor Queries are clustered by intent and distilled by the Template Generator Agent into intent2templates; conditioned on these templates, the Query Generation Agent produces benchmark queries paired with ground-truth (GT) assets, and the Query Validator Agent along with human expert validators ensure each query–GT pair is valid and investor-realistic.

for scouting where competitive advantage can depend on identifying qualifying programs from heterogeneous, multilingual sources before they are broadly amplified. In such settings, even modest omission rates can be high-cost, which makes completeness and verification central evaluation targets.

- As a result, BD and S&E activities are limited to largely


manual and time-consuming tasks, relying on human expertise. To maintain a competitive edge and secure top assets, what is needed are wide-research AI agents for global asset scouting: systems that can systematically identify best-inclass assets across languages and sources faster than rivals and optimize for completeness and match or surpass human expert quality.

Existing deep-research tools are typically optimized for fast web fact-finding and citation-backed report synthesis, and common benchmarks reflect this objective. Benchmarks like BrowseComp [5] emphasize short browsing tasks with a single verifiable answer, while rubric-based benchmarks such as ResearchRubrics [6] and DRACO [7] evaluate grounding, reasoning, clarity, and citation quality in long-form outputs. Consequently, these evaluation targets favor depth over breadth, where breadth here means completeness-first, open-world set discovery. In BD-style

“find-all” searches, this can lead to superficial retrieval and the most novel and valuable programs being missed, including those under the radar or disclosed primarily in nonEnglish ecosystems. DeepSearchQA moves toward exhaustive answer sets, but it typically evaluates tasks where the correct set is smaller, whereas our setting emphasizes longtail enumeration with larger cardinality, where valid outputs can reach hundreds or thousands of entities [8]. Widecoverage collection benchmarks further show that exhaustive enumeration is a distinct capability that remains difficult even for strong agents in open-world “enumerate-all” settings [9], and complementary evaluation work cautions that apparent progress on curated tasks can mask persistent omission and shallow-coverage failure modes in realistic browsing and extraction [10]. Hence, current Deep Research agents are still less reliable than human experts at consistently identifying all assets that meet complex, multiconstraint criteria.

One of the reasons why this remains unresolved is that much of the required evidence is public but scattered across heterogeneous, fast-moving, and often non-English sources such as company pages, local press, regional trial registries, conference materials, regulatory and legal filings, and corporate PDFs, which forces scouts to traverse many documents

to confirm tight criteria while maintaining provenance and completeness under limited time and budget. The same asset frequently appears under multiple aliases through codename changes, transliterations, and subsidiary disclosures, and early-stage under-disclosure to protect Intellectual Property (IP) is common, so “what exists” and “what can be found reliably” diverge in real workflows. Some notable data vendors, such as Clarivate and GlobalData, have begun using LLMs to curate drug assets. However, their databases still lack real-time updates and coverage, and they cannot handle complex queries. Another point is that the challenge is not only to build an index of all the assets in the world, but also to translate an investor- or diligence-style query into the complete set of matching assets, a step that requires expert interpretation of the technical criteria baked into the query. This intelligence gap is one of the main focuses of

- our method and evaluation, with precision and coverage as the core metrics.


To make completeness measurable under realistic BD and S&E conditions, we introduce a completeness-first benchmark for drug asset scouting that is constructed backward from validated program records rather than forward from the query. In particular, we mine predominantly nonUS regional assets from non-English ecosystems using a multilingual, multi-agent mining configuration that explicitly spans region, language, source type, and development stage. We reduce method-induced coverage bias via entity-agnostic query templates and by aggregating candidates across multiple provider deep-research systems. We then validate and enrich candidates into structured program records with provenance, while normalizing aliases and prioritizing under-the-radar discoverability patterns. To ensure the benchmark reflects real screening intent, we ground query construction in expert screening behavior by using BD/VC-style multi-constraint screening queries as priors. This way, success requires evidence aggregation and constraint satisfaction. Because “find-all” evaluation is dominated by entity normalization and attribute verification, the benchmark further operationalizes expert-aligned grading with LLM-as-judge components for alias resolution and upto-date attribute extraction.

Building on this benchmark, we present Bioptic Agent, a tree-based, self-learning scouting system engineered around completeness and non-hallucination. Instead of compressing exploration into a single evolving narrative, the agent preserves the candidate set and its evidence as persistent artifacts, allocates compute to under-explored branches, and uses expert-aligned critic and validator signals to surface constraint violations and coverage gaps, converting these failure modes into targeted child directives that drive sustained recall growth. This is the key place where general “self-correction” loops remain insufficient in practice, because self-critique can improve internal consistency while still silently failing task-specific constraints without validators tailored to the end screening objective.

This paper expands our previous work on benchmarking LLM-based agents for competitive landscape mapping in drug asset due diligence [11] by moving from competitor discovery within a single diligence context to open-

world, multilingual, “find-all” asset scouting with controlled query intent and difficulty. In a head-to-head evaluation against state-of-the-art commercial deep-research baselines, Bioptic Agent achieves 79.7% F1-score (harmonic mean of precision and recall; higher is better) and substantially outperforms Claude Opus 4.6 high at 56.2%, Gemini 3 Pro with Deep Research at 50.6%, OpenAI GPT-5.2 Pro high at 46.6%, Perplexity Deep Research at 44.2%, and Exa Websets at 26.9%, supporting the conclusion that investor-grade and BD-grade scouting requires completeness-oriented search control, lossless candidate tracking, and expert-aligned validation rather than increased browsing compute or better synthesis alone.

### Completeness Benchmark

Constructing benchmarks for open-world find-all asset scouting is prone to method-induced coverage bias: if candidate assets are collected by an agent or expert given the query, the resulting ground truth systematically overrepresents what that same method can discover. To reduce this bias and make the benchmark hard enough, we invert the process. We start with independently observed drug assets curated from regional news sources in local languages. We validate and enrich them with evidence-grounded attributes. We then generate investor-native queries for which the sampled seed asset is a correct answer, while forbidding direct identifiers (names/codes, trial IDs, unique URLs, rare aliases). Each benchmark sample is a multi-constraint query with a single ground-truth (GT) asset that is intentionally difficult to surface via English-centric search, so success requires evidence aggregation and multi-hop reasoning rather than string matching.

This design may introduce inherent residual bias, that is, seed selection is not uniform across all assets, with news favoring entities with wide media coverage, specific geographies, drug modalities, and certain development stages. Our pipeline mitigates these effects and ensures controlled distribution by (i) filtering out PR noise, (ii) mining across regional news sources using local languages, (iii) filtering out globally amplified assets using an English-vs-local discoverability signal, and (iv) conditioning query generation on a seed corpus of real investor/BD queries to match the empirical intent and constraint-composition distribution, ensuring query realism and GT correctness. Figure 2 represents an overview of the pipeline that creates the benchmark.

#### Regional News Miner Agent

To counter the tendency of unconstrained web discovery to overweight English/US announcements and to surface locally announced programs earlier in their public lifecycle, we introduce a Regional News Miner that iterates over tuples ⟨region, language, source, stage⟩ from a curated region– language–source store (Table 1). For each tuple, it executes a deep-research retrieval loop in the local language of the target market and returns extracted program (asset) names with canonical links to the underlying announcements.

We construct the store in Table 1 by manually curating 10 regions and 2–5 high-signal biotech news sources per region, prioritizing outlets that routinely publish primary local

announcements before they appear in global English coverage. The miner runs a round-robin schedule over the full configuration set R × L × S(r) × T , where R is the set of curated regions, L is the set of supported local languages, S(r) is the curated set of sources source for region r, and T = {preclinical,clinical}, ensuring that every ⟨r,ℓ,s,t⟩ combination is visited. Specifically, the miner (i) selects the next region–language pair, (ii) selects a curated source within that region, (iii) selects a development stage to control stage coverage, and (iv) runs a search agent that queries two deep-research agents in parallel, OpenAI o4-mini-deepresearch and Gemini Deep Research, and aggregates their candidates to mitigate provider-specific blind spots.

The Search Agent constrains Deep Research Agents to query in language ℓ and to extract program/asset announcements written in ℓ from the designated source s. Crucially, the search agent is instructed to avoid seeding searches with specific company or drug names and instead use entityagnostic templates (e.g., new clinical trial authorization, licensing agreement, IND filed, government grant, phase I initiated) combined with the sampled region r, local language ℓ, and source constraints s. This reduces popularity and incumbency bias, increases discovery of previously unseen programs, and ensures the benchmark is not anchored to a fixed watchlist. After enumerating all ⟨region, language, source, stage⟩ combinations, the miner produces 1255 validated regional news assets. All attributes and supporting artifacts are preserved in the original announcement language ℓ and then propagated to the downstream modules of the benchmark pipeline for filtering and validation.

#### Attributes Enrichment Agent

Regional News Miner Agent is recall-oriented by design and therefore admits noisy candidates, including false positives and stale metadata (e.g., platform/initiative names misidentified as assets, misspellings and aliases, or outdated information such as ownership and development stage). We therefore validate and enrich with attributes each mined candidate with an Attributes Enrichment Agent based on deep-research web retrieval built on top of OpenAI o4-mini-deep-research. The agent additionally performs usage-aware cross-lingual entity resolution, retaining the original mention while reconciling local aliases and transliterations and linking them to the commonly used English canonical names observed in global sources.

Given an input asset bundle (the program name as extracted from the announcement, a canonical URL to the announcement page, and the miner context ⟨r,ℓ,s,t⟩), the agent runs an iterative search–browse–refine loop in both the local language ℓ and English to: (i) verify that the candidate corresponds to a real drug program; (ii) correct misspellings and resolve aliases, including cross-lingual variants and development codes; (iii) determine whether development is currently active; (iv) retrieve and reconcile the most recent development evidence across regions, languages, and source types, preserving multiplicity; (v) extract an up-to-date attributes used downstream for query construction, spanning program-level descriptors and trial-level details, using iterative query expansion to approach evidence saturation; and

![image 3](Vinogradova et al._2026_Hunt Globally Wide Search AI Agents for Drug Asset Scouting in Investing, Business Development, and_images/imageFile3.png)

Figure 3: Distribution of asset origin language and therapeutic areas in the benchmark test split. Left: proportion of assets by origin language. Right: proportion of therapeutic-area labels assigned across assets.

(vi) find strong global amplification signals (e.g., major US trade-press coverage or large-pharma deal announcements) used to filter out non-challenging for agent’s retrieval and over covered in US media assets.

The agent is enforced to emit a hierarchically structured attribute record in which every atomic claim is paired with explicit provenance (a list of source URL and verbatim supporting quote pairs). The enriched record contains the following asset attributes:

- • Validation and status: whether the candidate is a valid drug asset, whether development is currently active, whether it is preclinical or clinical, and the current stage
- • Program descriptors: developer(s), modality, target(s), short mechanism of action, detailed mechanism of action, indication(s), and patent(s)
- • Trial-level records: a list of trials, where each trial includes indication, development phase, regimen, efficacy data, safety data, line of therapy, biomarker(s), countries of sites, and endpoints
- • Regulatory fields: approved geography and regulatory labels


Following enrichment, we apply a filtering pass to remove (a) non-drug/invalid/hallucinated entities, (b) globally approved and widely covered drugs (unless approval is local and there is meaningful ongoing development that remains under-amplified in English), and (c) candidates with strong global amplification signals (major US trade press or largepharma deal announcements). As shown in the pipeline schematic, this step reduces 1255 mined candidates to 798 enriched assets, which are propagated to the next module (Google Search Agent).

#### Google Search Agent

For each validated asset we construct a number of queries in English and language l, drug’s origination country’s language. Using a SERP tool, we count the maximum number of google search result pages for (A) English queries and the max number of pages for (B) queries in the original local language. This yields an English-vs-local discoverability profile used in downstream filtering.

#### Conditioned Query Generation

Starting from the filtered enriched asset records produced by the Regional News Miner, Attributes Enrichment Agent and

###### Region Language Curated sources (2–5 per region)

United States English FierceBiotech, FiercePharma, Endpoints News China Chinese Yaozhi, Pharmcube, VBData/Artery Network Japan Japanese Nikkei Biotech, Pharma Japan Korea Korean Medigate, ETNews, BioSpectator Brazil Portuguese Portal da Saúde, Agência Brasil, Estadão Saúde, Valor Econômico–Saúde, JOTA Saúde Australia English PharmaDispatch, BiotechDispatch, MTPConnect News Germany German Ärzteblatt, transkript.de, CHEManager Life Sciences France French Pharmaceutiques, Le Quotidien du Médecin, Biotech Finances Spain Spanish Diario Médico, Redacción Médica, El Global CIS countries Russian/Ukrainian Vademecum, Pharmvestnik, Apteka.ua

Table 1: Manually curated regional sources used by the regional news miner to increase coverage of locally announced programs.

![image 4](Vinogradova et al._2026_Hunt Globally Wide Search AI Agents for Drug Asset Scouting in Investing, Business Development, and_images/imageFile4.png)

- Figure 4: Benchmark query composition. Left: distribution of queries across difficulty tiers (Broad, Tight, Complex/multi-hop). Right: prevalence of high-level constraint categories across queries (multi-label). A single query can trigger multiple categories; therefore, a category is counted once per query if the query contains that type of constraint.


Google Search Agent, we generate queries via an inverted procedure (asset → query). Given a ground-truth (GT) asset and its validated attributes, we construct a query for which the GT asset is one of the correct answers. We forbid GT identifiers and high-identifiability lexical fingerprints (drug names/codes, trial IDs, asset-unique URLs, rare aliases, and announcement-specific phrasing). We also rewrite constraints (like MoA/target class, modality family, indication with population/line-of-therapy slice, maturity window, geography/ownership, evidence signals) into class-level abstractions where relevant. This ensures that the query returns a candidate cohort that contains the GT asset rather than returning the GT asset as a singleton result. As a result, resolution requires evidence aggregation, multi-hop browsing, and domain reasoning rather than lexical matching.

To produce investor-native queries under a constrained generation process, we curate a seed corpus of real biotech investor/BD queries and use it as an empirical prior, ensuring the generated queries match the seed distribution. This corpus consists of 48 real investor/BD queries that have been reviewed in the coverage pass by expert biopharma investors to ensure the set spans core diligence workflows. This cor-

pus serves as an empirical prior over (i) intent (the business question being asked) and (ii) difficulty tier (how investors combine filters such as modality/platform, target/MoA, indication and population slice, maturity/stage, geography/origin, ownership/licensing, and evidence signals). Operationally, query generation is conditioned on these corpusderived dimensions and sampled to match the investor corpus frequency profile, yielding a synthetic query distribution closer to real diligence workloads than unconstrained prompt synthesis.

Corpus-derived axes From the seed corpus of investor queries, we induce a stable set of intent dimensions using an LLM-assisted clustering procedure. We set the number of intent clusters to k = 10 to balance granularity and interpretability, and then reassign all 48 investor queries to these intents. The resulting intent dimensions are:

- • Program attrition and suspended or terminated programs
- • Business development screening for in-licensing or acquisition
- • Indication landscape mapping
- • Target-first landscape mapping
- • Precision oncology sub-landscapes
- • White-space and low-competition target hunting
- • Geography and origin constraints
- • Platform and modality scouting
- • Catalysts and upcoming readouts
- • Combination regimen opportunity discovery


Within each intent, we group the investor queries into three corpus-consistent difficulty tiers (see Figure 4 for their distribution across the final benchmark):

- • Broad: low constraint, primarily enumerative landscape building over a wide search space
- • Tight: conjunctive screening queries with multiple simultaneous constraints on entity class and attributes, designed to filter to a narrow candidate set
- • Complex / multi-hop: tight screening plus at least one derived constraint that typically cannot be validated from a single source and therefore requires integrating evidence across multiple sources, such as lifecycle changes over


- Figure 5: Example prompt specifications (intent × template) used for benchmark query generation. Each query group is defined by an intent, difficulty tier, and a template. Here Gi denotes the i-th query group.


|[G1] Intent: White-space and low-competition target hunting Difficulty tier: Complex Template: Find all [stage(s)] [modality] assets targeting [target class] for [therapy area/indication], reporting [biomarkers/endpoints/early efficacy/safety] and no more than [N] competitors ahead in [stage(s)]; exclude tool compounds not intended for patient use.<br><br>[G2] Intent: Target-first landscape mapping Difficulty tier: Complex Template: Find assets that [target] [target A], across any modality, any indication, and any development phase, focusing exclusively on [target A] (do not include multi-target assets unless [target A] is clearly a primary target).<br><br>[G3] Intent: Geography and origin constraints Difficulty tier: Tight Template: Find [region activity: origin/licensing/trials] [modality] assets [stage] for [disease] targeting the [pathway/axis].<br><br>[G4] Intent: Indication landscape mapping Difficulty tier: Broad Template: Find all assets in development for [indication] [stage].<br>|
|---|


time, readout or signal aggregation, competitor ceilings (i.e., targeting hot targets; having at most N competing programs), or nuanced include/exclude mechanistic rules.

Template induction (intent × difficulty tier) and instantiation. For each (intent, difficulty tier) group in the investor corpus, a GPT-5.2 template-induction agent abstracts the group’s real investor queries into a set of structural templates that capture their recurring constraint structure. Intent, difficulty tier, and template collectively define a query group used in the conditioned query generation. See Figure 5 for representative examples of the query groups used.

Query Generation Given a sampled GT asset, GPT-5.2based query generation agent (i) selects suitable (intent, difficulty tier) group based on the asset specifics and available attributes (for example if this is the only asset for a specific rare cancer mutation, then it will not pick the group which requires this specifics), (ii) selects a compatible template from that group associated with the difficulty tier, and (iii) generates a query following that template and mapping validated attributes into non-identifying constraints.

#### Query Validator Agent

To reduce undetected query–GT inconsistencies and minimize human review load, we run an automated verifica-

tion loop that flags and corrects likely mismatches before expert inspection. A Criteria Match Validator Agent (the same as the one used in the Bioptic Agent, later discussed in a dedicated subsection of the "Bioptic Agent" section) takes a generated query and a GT asset and predicts whether the asset satisfies the query. The validator decomposes the query into atomic criteria with explicit logical operators (AND/OR/NOT) and comparators, and at each node extracts supporting attributes/evidence from the structured asset schema. If the asset does not satisfy the query, the validator returns a failure rationale. A Query Generator agent (based on gpt-5.2) then revises the query based on the rationale (tightening/loosening constraints, fixing modality/target/stage mismatches, and removing accidental leakage tokens) returned by the validator. Revised query–asset pairs are re-validated and revised iteratively until the validator confirms that the asset satisfies the query, after which those pairs are submitted for the expert review.

#### Final filtering and human validation

As a final benchmark construction step, we curate query–asset pairs to enforce benchmark hardness while mitigating selection bias toward globally amplified programs. For the fraction of the assets in the resultant set, we require the asset to have at most 9 pages of English search results and more than 0 pages in the origination language. We further validate assets against regional “white sources” and conduct final human expert checks and expert query editing.

For an overview of the final benchmark’s properties, see Figures 3, 4, 6. Figure 3 reports coverage by asset origin language and therapeutic area. Figure 4 characterizes query composition by showing both the distribution across constraint tiers and the prevalence of atomic constraint categories. The constraint categories plot is built by tagging each query with the atomic constraint categories, because a query can contain multiple constraints, it can contribute to multiple category bars. Figure 6 shows three randomly sampled queries from the resulting benchmark.

### Bioptic Agent

Bioptic Agent is designed as a tree-based self-learning agentic system optimized for complete, non-hallucinated biomedical asset scouting. The system addresses the recall stagnation problem common in sequential search agents by combining multi-language parallel investigation, treebased search ideas generation, and search-quality-weighted rewards. This section provides a detailed technical description of the system architecture, components, and algorithmic mechanisms.

Bioptic Agent employs the following main components:

- • Investigator Agents execute thousands of web searches to retrieve candidate assets matching the user query, optionally guided by a Coach Agent directive that narrows the search space.
- • Criteria Match Validator Agent checks each candidate asset against the query criteria and outputs a match verdict plus a detailed, traceable, supported by evidence pass/fail rationale.


- Figure 6: Example queries from the final benchmark, conditionally generated for relevant query groups (G1–G4 in Figure 5).


|• [G1] Find small-molecule antigen presentation modulators in oncology (preclinical through Phase 2). Include only assets with in vivo tumor efficacy and ≤ 3 more-advanced direct same-target competitors globally.<br>• [G2] Find all drug assets targeting LAT1, across any modality, any indication, and any development phase, focusing exclusively on LAT1 (do not include multi-target assets unless LAT1 is clearly a primary target).<br>• [G3] Find China-developed/licensed (or have China trial activity) biologic assets (mAbs/bispecifics) in development for autoimmune diseases that modulate the TSHR–IGF-1R axis.<br>• [G4] Find all drug assets currently in preclinical or clinical development for treatment of DMD.<br>|
|---|


- • Deduplication Agent ensures a global set of validated assets contains only unique assets by removing duplicates and resolving aliases.
- • Coach Agent generates new exploration directives based on accumulated context: assets found, errors detected, actions performed, queries executed and domains visited so far, etc.


The system maintains stores that are regularly updated (at each Rollout, Evaluate and Aggregate steps) and accumulate across epochs:

- 1. Cglobal: Holds all candidate drugs discovered before validation;
- 2. A˜global: Holds all validated, deduplicated assets;
- 3. Evidence stores: all executed web queries - Qglobal; all visited domains - Dglobal;


Bioptic Agent treats web exploration as a tree, where each node n stores: (1) dn - an exploration directive produced by Coach Agent, (2) δn - additional instructions produced by Coach Agent related to the directive (these are prompt modifications to the Investigator Agent’s prompts to explore the directive and override some errors in the initial prompt), (3) parent(n) - parent node reference, (4) children(n) - the list of all child node references, (5) N(n) - number of total visits to the node, and (6) W(n) - the total cumulative reward score for the node’s directive.

The algorithm runs in a loop for a number of epochs, and for each epoch e, the following steps are executed:

- 1. Initialize (once): Create the root node n0 with empty di-

rective dn

0

add it to the directive tree, which was empty at this point.

- 2. Select: Select m nodes {ni}mi=1 via Upper Confidence Bound (UCB) rule (see subsection "Selection") from the tree of directives, where m is the number of parallel explorations per epoch. At the first epoch, when root node node has no children, yet, the root node with an empty directive will be chosen at this step.


- 3. Rollout: For each selected node n:

- (a) Instantiate one Investigator Agent per each language (apply language parallelism); In total there will be (number of languages) agents;
- (b) Provide each agent: (1) the user query, (2) aggregated

prior asset findings (A˜global and Cglobal discovered so far), and (3) the node’s directive dn plus directive’s additional instructions δn.

- (c) Each Investigator Agent executes web searches in the specified language and returns candidate drugs; Candidates are then merged across agents/languages.
- (d) Update Cglobal with merged candidates and append executed queries/domains to the evidence stores (Qglobal, Dglobal).


- 4. Evaluate: For each selected node n:

- (a) The Criteria Match Validator Agent validates each candidate asset against query criteria, producing (match verdict, pass/fail rationale) per candidate.
- (b) Then precision p(ne) is computed as the fraction of returned candidates that the Criteria Match Validator Agent marks as valid matches to the query;
- (c) Then we run Deduplication Agent on the list of assets that validator agent marked as matching the query; Deduplicator agent resolves duplicates and aliases and

returns ∆A˜(ne) a set of valid new unique assets that were not yet discovered before and thus not present

in the global assets store A˜global.

- (d) Then using p(ne) and ∆A˜(ne) we compute the Node Reward rn(e) (see subsection "Evaluate: Node Reward")

and update the node’s W(n) with it (W(n)+ = rn(e)) and also increment the number of visits N(n)

- (e) Puts failure rationales for assets with match verdict that are in ∆A˜(ne) to the list Fn.


- 5. Backpropagate: For each node n, backpropagate the reward and number of node visits to the root, updating number of total visits to the node N(·) and W(·) along the path (see subsection "Backpropogation").
- 6. Aggregate: Merge new unique validated items ∆A˜(ne) across all explored nodes; deduplicate/resolve aliases and append only new unique assets to A˜global.
- 7. Expand: If not the last epoch, then for each node n:


- (a) Coach Expansion: Conditioned on the current node (dn,δn), directive lineage (path to root), global memory (e.g., A˜global, Cglobal), evidence logs (Qglobal,Dglobal), and the node’s validation failures Fn produced by Criteria Match Validator Agent in the current epoch (Step 4), the Coach Agent generates (i) k non-overlapping child directives for the next epoch

chdn and (ii) chδn per-directive additional instructions / prompt updates to Investigator/Actor prompts.

- (b) Tree Update: Then Coach agent updates the tree of directives, by adding to the node n as children to the children(n), new nodes initialized by chdn as dn and chδn as δn.


8. Repeat from Step 2.

#### Language Parallelism

- At each epoch, Bioptic runs multiple investigator instances in parallel across languages. The system supports:


• Language Parallelism: English plus additional configured languages (e.g., Chinese in our evaluation). Each investigator is instructed to search primarily in its target language, increasing coverage over regional sources, transliterations, and non-English pipeline disclosures.

#### Criteria Match Validator Agent

After Investigator Agents produce the candidate list of assets matching the user query in the Rollout step, those candidate items are filtered by a Criteria Match Validator llm-as-ajudge aligned with domain experts with the 88% precision as discussed in a subsection "Multi-Agent Debate-Based Tuning". It accepts a single candidate asset and a query and predicts whether the asset matches the query. For each candidate, the validator agent performs hundreds of web searches to perform targeted evidence checks against the query’s hard requirements, respecting logical structure (AND/OR) when present. It returns a structured verdict containing:

- • Match verdict: Boolean indicating whether the candidate matches all criteria.
- • Evidence provenance: Per-criterion fields containing supporting snippets and source URLs when available.
- • Failure rationale: A concise reason (confirmation or failure summary) grounded in the evidence fields.
- • Normalized attributes: Extracted attributes (e.g., phase, modality, indication, MoA, developers) along with citations.


Validator outputs are retained for error analysis and summarized by Coach Agent into compact failure patterns that guide subsequent exploration. Also, verdicts it produces are

used to compute the local precision score p(ne) for the node. Also note that, unlike the Precision Grader, that is fixed across all experiments, the Criteria Match Validator prompts may change during tuning because they are part of the search agent rather than the evaluation grader.

#### Deduplication Agent

Deduplication Agent identifies and removes duplicate assets that may appear under different names, aliases, or synonyms. This step is critical for maintaining data quality in the global asset store A˜global, as pharmaceutical assets are frequently referred to by multiple identifiers: generic names, brand names, development codes, cross-lingual variants, and historical names that change during development.

The agent accepts A˜global and Vn(e), the validated list of candidate assets Investigator Agent returned for the given node after Criteria Match Validator Agent filtering, but before deduplication. The agent operates in two modes, differing in their computational approach and search intensity:

Light Deduplication: This mode processes all Vn(e) items in a single LLM pass or, depending on the size of the full

item list, in a few passes by splitting the list into batches, sending each batch to the LLM in one pass, then merging the outputs and passing the merged list to the deduplicator again for a final deduplication pass. The agent performs hundreds of web searches to discover aliases, alternative names, development codes, and cross-lingual variants for all items simultaneously, then groups duplicates and selects canonical representatives. In our experiments, light deduplication achieves deduplication quality comparable to the heavy mode in the vast majority of cases.

Heavy Deduplication: This mode processes each candidate item ∈ Vn(e) sequentially, each in a separate LLM pass, checking it against all existing items in A˜global with exhaustive web search verification. The agent performs extensive web searches to discover all possible aliases, previous names, development codes, and cross-lingual variants. It results in hundreds of thousands of searches for large candidate sets, but provides higher confidence in deduplication accuracy.

In our benchmark evaluations, we use light deduplication as the default, achieving state-of-the-art performance with an F1-score of 79.7%. The heavy mode is available for scenarios requiring exhaustive verification.

#### Coach Agent

In the Expand step, Coach Agent implements the tree: for each node n explored in the current epoch, it proposes k child directives for the next epoch based on the continuously updated memory consisting of the the research history, research gaps present and errors produced by the Investigator Agent when it was computing for the parent’s directive, as well as the entire path of directives from the root to the current node, the Investigator Agent’s initial instructions. Each child directive consists of a short, high-level description of what angle the Investigator Agent should pursue next, what types of sources to prioritize and additional instructions that specify how Investigator Agent should execute that angle. In effect, dn focuses the investigators on a particular slice of the original query;

More specifically, the Coach Agent consumes: (1) the query; (2) the node-path directives (i.e., all directives along the path from the current node to the root); (3) the current node’s directive dn/δn; (4) all executed web queries Qglobal and visited domains Dglobal (including those attributable to the current node); (5) Fn(e) - list of failure rationales for all the false positive assets returned by the Criteria Match Validator Agent for the given node; (6) the current A˜global (and, when available, Cglobal to avoid rediscovery); and (7) the Investigator Agent’s initial task prompt.

Using this context, then Coach Agent generates:

• dn - child directives for the next epoch, which are (1) non-overlapping concrete refinements (mutations) of the current node’s directive, (2) target under-explored search angles suggested by prior outcomes, (3) each strictly narrower than the parent by introducing explicit additional constraints, and (4) collectively exhaustive over the parent’s remaining search space so no major gap is left unassigned.

• δn - additional instructions (prompt updates to the Investigator Agent) that reflect observed errors, override ambiguous or incorrect Investigator instructions, and address directive-specific blind spots.

The coach is instructed to propose directives that target angles that were missed or only weakly explored, based on the executed-query and domain history (Qglobal, Dglobal) and recent outcomes, while also exploiting partially explored but promising directions. It uses the compressed validator failure summary (see bellow in Failure Summarization) to refine strategy and reduce recurring rejection reasons in subsequent rollouts. The produced directives must be mutually disjoint (non-overlapping in scope) yet collectively cover the search space defined by the current directive (or the original query when the current directive is empty). Figure 7 shows a part of the tree of directives Coach Agent has built for the randomly sampled query from the benchmark.

Failure Summarization To keep its context clean, the

Coach Agent calls an LLM to compress Fn(e), the long list of detailed validator failure rationales for all candidates returned by the Investigator agents, into a short set of recurring failure patterns. This is done to mitigate the context rot of the Coach Agent.

#### Evaluate: Node Reward

This step turns the outcome of the Investigator Agent exploring a directive into the statistics that affect how the Selection step will look at each node. So, here we update the node associated with the directive with the score related to the directive’s performance.

The node reward is computed as:

rn(e) = p(ne) ∆A˜(ne) . (1)

Here p(ne) is the local precision for node n at epoch e, the fraction of candidates returned by Investigator Agent that the Criteria Match Validator Agent marks as valid

matches to the query; ∆A˜(ne) denotes the set of newly added validated and deduplicated assets credited to node n at epoch

e. These are assets that were not in the global asset set A˜global before epoch e and were added due to the rollout under di-

rective dn.

This reward is designed around the asset scouting objective. We want to prioritize directives that reliably add new valid assets to the global results, rather than directives that only produce many candidates. The precision gate enforces this by reducing the credit given to low-quality rollouts, so high-volume but noisy directives do not attract more compute.

#### Backpropagation

After computing rn(e), we backpropagate it by updating node statistics for node n and all of its ancestors in the directive tree:

N(k) ← N(k) + 1, (2) W(k) ← W(k) + rn(e), ∀k ∈ An, (3)

where An is the set of ancestors of node n including n itself. The resulting values N(·) and W(·) are the quantities used by the UCB rule in Selection step, so directives that repeatedly add new validated assets receive higher scores in future epochs.

#### Selection

At the selection stage, our goal is to decide which search directive to try next so that we keep discovering new valid assets rather than repeatedly visiting the same sources. The Coach agent organizes search into a tree of directives, where each node corresponds to one directive and edges represent refinements proposed during expansion. At any point, the eligible choices are the current leaf nodes, meaning directives that have been generated but do not yet have child directives. In each epoch, we select up to m (m - maximum number of parallel explorations) eligible leaf nodes for parallel rollout, where the Investigator agents execute web searches guided by the selected directive.

We rank eligible leaf nodes using an Upper Confidence Bound rule:

log max(1,N(parent(n))) N(n)

W(n) N(n)

UCB(n) =

+ c

,

(4) where c = 1.2 is the exploration constant, N(n) is the number of times node n has been selected, N(parent(n)) is the parent’s visit count and W(n) is the cumulative reward attributed to node n over past epochs. The first term is the empirical mean reward of the directive, that prioritizes nodes whose directives have historically produced higher reward, and the second term is an exploration bonus that prioritizes nodes that have been selected fewer times. Any node that has never been selected receives an infinite score UCB(n) = +∞, which guarantees it will be tried at least once.

Selection proceeds top-down from the root of the directive tree produced by the Coach Agent. At each internal node, we select the child with the highest UCB score and repeat until reaching a leaf node. When multiple children have the same visit count, we break ties by preferring the child with the higher mean reward; if ties still remain, we break them arbitrarily. This traversal implicitly prioritizes promising branches: directives deeper in the subtree of a highscoring child are promoted earlier in our evaluation queue, so they are rolled out, scored, aggregated, backpropagated, and expanded sooner than lower-scoring alternatives.

### Experiments

We evaluate whether a specialized scouting scaffold (Bioptic Agent) outperforms general-purpose generic deep research / find-all systems on the task of asset scouting. All methods are evaluated on a held-out gold test split consisting of 22 pairs of query-asset from the Completeness Benchmark (see Figures 3, 4 for distribution) using recall, precision, and F1score.

#### Precision & Recall Graders

To evaluate agent performance on the completeness benchmark, we employ LLM-based graders that assess precision and recall against ground-truth assets, in a similar way we did in [11]. Both graders use GPT-5.1 with temperature 0.2 and a fixed seed for reproducibility, and are equipped with web search tools to verify drug attributes and resolve aliases.

Both graders are designed to be evidence-grounded: all decisions are supported by verbatim quotes and source URLs from authoritative sources, ensuring reproducibility and auditability of the evaluation process.

Recall Grader: The recall grader determines whether the expected ground-truth asset is present in the agent’s predicted list of assets. Given the query, the predicted asset list, and the expected asset’s attributes (drug name, English name, indication, mechanism of action, modality, developers, stage, country), the grader performs web searches to discover all aliases, alternative names, and cross-lingual variants for both the expected asset and each predicted asset. It then determines equivalence by matching attributes and aliases, accounting for naming variations such as brand names, generic names, development codes, and synonyms. The grader returns a binary verdict: the expected asset is present in the predicted list if any predicted asset matches the expected asset after alias resolution, and absent otherwise.

For each benchmark query–asset example i, the Recall Grader outputs a binary verdict Ri ∈ {0,1} indicating whether the expected asset is present in the agent’s predicted list after alias/cross-lingual resolution. The reported recall is the mean of these verdicts over the benchmark:

Nbench

1 Nbench

Recall =

Ri,

i=1

where Nbench is the number of benchmark query–asset examples in the evaluated split.

Precision Grader: The precision grader validates each predicted asset against the search criteria to determine whether it should be included in the results. The grader employs a structured decomposition approach: it breaks the query into logical components, then further decomposes each dimension into atomic components. For each atomic component, the grader forms a verification query, performs web searches to retrieve the asset’s corresponding attribute value, and documents all steps taken to retrieve this value with verbatim quotes and source URLs. The grader then produces a verdict for each dimension indicating whether the asset meets the criterion defined in that dimension. Finally, the grader assembles all dimension-level verdicts, preserving the query’s logical operators (AND/OR), strictness, and overall logic, to produce a final answer of whether the asset matches the query, supported by detailed justification text.

The Precision Grader is applied to every predicted

(query,asset) pair produced by the agent. Let Aall predicted be the set of all such predicted pairs across the benchmark,

and let Acorrectly predicted ⊆ Aall predicted be the subset that the Precision Grader validates as match (i.e., satisfies the query constraints). We report precision as the fraction of predicted

assets that are validated as matches: Precision = |Acorrectly predicted|

###### .

|Aall predicted|

Multi-Agent Debate-Based Precision Grader Tuning The Precision Grader was tuned through an iterative refinement process involving multi-agent debate and expert alignment. Each refinement iteration involves the following components and steps:

- • Generator Agent: given a query, generate a list of candidate drugs that may satisfy the query constraints. The Bioptic Agent is an example of a generator agent.
- • Precision Grader (tuned): for each (query,drug) pair, output a match/non-match verdict with structured justification and provenance.
- • Critic Agent: evaluate the Precision Grader’s justification, flag disagreements and ambiguous cases, and challenge inconsistent decisions.
- • Debate step: the Precision Grader and the Critic Agent exchange structured reasons (with provenance) until they converge on a consensus match/non-match verdict (a pseudo-label) for each (query,drug) pair.
- • Prompt-fix step: conditioned on the Precision Grader prompt and the post-debate pseudo-labels, the Critic Agent produces a structured summary of prompt fixes explaining the root cause of mismatches; these fixes are manually curated and applied to update the Precision Grader prompt before the next iteration.


Because we did not have an initial expert-labeled set large enough to support prompt tuning, we employed a debatebased weak-supervision in which the Precision Grader and the Critic Agent converge on pseudo-labels for each (query,drug) pair. We operationalize each (query,drug) as a binary classification instance with the positive class defined as match, i.e., the drug satisfies the query constraints. The system also checks for cross-policy consistency, ensuring the Precision Grader applies consistent criteria for previously identified matches and non-matches.

On a calibration subset of 57 query-drug pairs, the grader achieved 87% accuracy, 100% precision, 82.8% recall, and 90.6% F1-score with respect to the debate-converged pseudo-labels (internal Precision Grader and Critic Agent agreement). After these pseudo-metrics stabilized, domain experts performed a one-time audit of the grader’s predicted match pairs to estimate the trustworthiness of positive decisions in practice; this yielded 88% precision under expert labels. Overall, this design concentrates scarce expert time on the most error-prone cases while still providing a human-grounded calibration of the final grader’s positive predictions.

#### Models & Agents Tested

We compare Bioptic Agent against State-of-the-Art search agents:

- 1. Find-all agents: Exa Websets (num_matches = 500)
- 2. Deep research agents: systems optimized for prolonged browsing + synthesis (e.g., Gemini 3 Pro Deep Research, Perplexity Deep Research).


- 3. Powerful single-pass model: GPT-5.2 Pro in a high search context and reasoning regimes; Claude Opus 4.6 in a high search context regime and with 1M tokens context window enabled for the fraction of the benchmark, for which 200k tokens context window was not enough.
- 4. Sequential scaffold ablations: o4-mini-deep-research and GPT-5.2 run as a simple iterative loop: given previously-found assets, prompt to find more, append new candidates, repeat.
- 5. Bioptic Agent (no-tree, lang-free) ablation: removes tree-structured exploration and disables language parallelism, while keeping the remaining components unchanged.


#### Experimental Settings

Unless stated otherwise, all agents from above are used in their highest supported compute setting, and same prompts (main task prompt and the previous findings prompt that preprompts previous found assets) as that was used to initialize the Investigator in the Bioptic Agent are used for all the agents for fair comparison.

Sequential scaffold ablations o4-mini-deep-research and GPT-5.2 are wrapped in a vanilla sequential-epoch ensemble. Epoch 1 runs the raw query; each subsequent epoch appends a pre-promted all previously found assets (at previ-

- ous epochs) and explicitly instructs the agent to return only new items not already listed.

Bioptic Agent In Figure 1, as wall-clock time increases, the Bioptic Agent explores deeper levels of the directive tree. For all experiments reported in Table 2 and Figure 1, we used gpt-5.2 with high search context and high reasoning effort as the LLM for the Investigator Agents; gpt-5-mini with medium search context and medium reasoning effort for the Criteria Match Validator Agent; and gpt-5 with medium search context and medium reasoning effort for both the Deduplication Agent and the Coach Agent. During the Roll-

- out step, we enabled multilingual parallelism by running Investigator Agents in English and Chinese. In the Expand step, the Coach Agent generated (k = 3) non-overlapping child directives per node, and we used light deduplication throughout. For cost optimization purporses we run Bioptic Agent with 1 parallel exploration on the full benchmark, so in fact, there are 10 and Investigator agents executed by the end of the 5th epochs and 20 if Bioptic Agent run for 10 epochs.


Bioptic Agent (no-tree, lang-free) ablation This ablation preserves Bioptic Agent’s components (Coach reflection, validators, and deduplication) but removes treestructured exploration. At each epoch, the Coach produces a flat set of k directives; all directives are executed in parallel, their artifacts are merged into a single pool, and the merged pool is passed to the next epoch to generate the next batch of directives. We also disable multilingual parallelism (we do not spawn separate Investigator instances per language and we do not constrain queries to a specific language). We set k = 5 parallel directives per epoch. Therefore, running for 5 epochs executes 25 Investigator calls, and running for 10 epochs executes 50 Investigator calls.

Model Recall Precision F1

Bioptic Agent (GPT-5.2, high) 0.730 0.877 0.797 Claude Opus 4.6 (high) 0.454 0.736 0.562 Gemini 3 Pro Deep Research 0.500 0.512 0.506 OpenAI Deep Research (o4-mini) 0.372 0.713 0.489 GPT-5.2 Pro (high) 0.364 0.648 0.466 Perplexity Sonar Deep Research (high) 0.409 0.481 0.442 GPT-5.2 (high) 0.182 0.683 0.287 Exa Websets (num_matches=500) 0.182 0.515 0.269

Table 2: Assets discovery performance. Recall/Precision/F1 on the asset scouting eval, sorted by F1 score (all metrics higher are better).

#### Results and Discussion

Table 2 shows that Bioptic Agent achieves the best overall performance, with an F1-score of 0.797, substantially outperforming all tested state-of-the-art search agents. The strongest baseline is Claude Opus 4.6 with an F1-score of 0.562, followed by Gemini 3 Pro Deep Research with an F1-score of 0.506, o4-mini-deep-research with 0.489, GPT5.2 Pro high with 0.466, Perplexity Sonar Deep Research high with 0.442, GPT-5.2 high with 0.287, and Exa Websets with 0.269. Bioptic Agent’s advantage is driven by simultaneously high precision of 0.877 and high recall of 0.730, whereas competing systems exhibit markedly lower recall and more limiting precision–recall tradeoff.

Figure 1 further indicates that Bioptic Agent improves rapidly in the early regime and then approaches a plateau near ∼ 0.80 F1-score. Notably, Bioptic Agent uses GPT-5.2 as its underlying model, making it cheaper than having a scaffold on top of Opus 4.6, which is a much heavier model.

The sequential scaffold ablations with o4-mini-deepresearch and gpt-5.2 improve more slowly and plateau earlier at markedly lower F1-score. The sequential scaffold over the gpt-5.2 (the blue plot in the Figure 1) uses the same underlying model and the same prompts as our Bioptic Agent Investigator. The results, therefore, indicate that simply iterating to find more assets with a growing list of prior candidates is insufficient for sustained coverage: once obvious sources and search angles are exhausted, the sequential loop tends to revisit similar evidence and exhibits diminishing returns. By comparison, Bioptic Agent’s higher and more sustained gains suggest that its scaffold architecture is the primary driver of improved completeness rather than model strength and prolonged executions alone.

We include OpenAI Deep Research (o4-mini) in the sequential scaffold ablation to test a natural hypothesis suggested by Table 2: since Gemini 3 Pro Deep Research is the second strongest after Bioptic Agent, perhaps simply running a state-of-the-art Deep Research agent longer—by iterating a sequential “find more” loop—could close the gap to Bioptic Agent. Directly applying many sequential epochs to Gemini 3 Pro Deep Research is costly, so we use o4-mini-deep-research as a cost-efficient alternative that is comparable in terms of F1-score and itself a Deep Research scaffolded agent. Empirically, however, the sequen-

tially wrapped o4-mini-deep-research still improves more slowly and saturates earlier than Bioptic Agent, similarly to how the gpt-5.2-based scaffold is saturated, consistent with diminishing returns once the most obvious sources and search angles are exhausted. This demonstrates that the gains are not in simply running a state-of-the-art general agent longer; rather, Bioptic Agent’s advantage comes from its specialized tree-based exploration, self-reflection, and self-learning scaffolding beyond naive sequential iteration.

Finally, we compare the Bioptic Agent against the Bioptic Agent (no-tree, no-multilingual) ablation. Removing the directive tree and disabling multilingual parallelism yields comparable quality through roughly the 5th epoch, but the ablation saturates thereafter. Importantly, this saturation occurs despite higher compute: at 10 epochs, the no-tree variant executes 50 Investigator calls versus 20 Investigator calls for the full Bioptic Agent setting shown in Figure 1. This suggests that (i) tree-based exploration helps prevent early saturation by systematically allocating compute to under-explored branches, and (ii) multilingual rollout provides additional coverage on locally announced and nonEnglish-first assets. This experiment also shows how much of the performance gain comes from self-reflection and selflearning, implemented via the internal evaluation step, the Coach Agent’s use of search history and error and gap analysis, and the Investigator Agent’s automatic prompt refinement with parallel execution of conditioned directives, compared to vanilla sequential GPT-5.2 execution.

### Conclusion

In this paper we present (i) a challenging Completeness Benchmark for drug asset scouting and (ii) Bioptic Agent, a tree-based, multilingual wide-research system optimized for complete, non-hallucinated “find-all” scouting. The benchmark is constructed backward from validated program records, mined predominantly from non-U.S., nonEnglish ecosystems, and paired with investor-native, multiconstraint screening queries.

On this benchmark, Bioptic Agent achieves the best overall performance with F1-score of 79.7% and substantially outperforms state-of-the-art commercial deepresearch baselines (Table 2), including Claude Opus 4.6 high (56.2%), Gemini 3 Pro Deep Research (50.6%), o4-minideep-research (48.9%), GPT-5.2 Pro high (46.6%), Perplexity Sonar Deep Research high (44.2%), and Exa Websets (26.9%). Figure 1 shows a clear quality–time tradeoff: Bioptic Agent improves rapidly early and then approaches a plateau near ∼ 0.80 F1, while sequential “run longer” scaffolds improve more slowly and plateau earlier at lower quality.

### References

[1] Alexander Schuhmacher, Oliver Gassmann, Sebastian Kwisda, Malte Kremer, Markus Hinder, and Dominik Hartl. The R&D productivity challenge: transforming the pharmaceutical ecosystem. Drug Discovery Today, 2025. ISSN 1359-6446.

- [2] McKinsey & Company. External innovation: Biopharma dealmaking to boost r&d productivity, 2025. URL https://www.mckinsey.com/industries/lifesciences/our-insights/external-innovation-biopharmadealmaking-to-boost-r-and-d-productivity.
- [3] World Intellectual Property Organization. World intellectual property indicators 2025. https://www.wipo.int/edocs/pubdocs/en/wipopub-941-17-2025-en-world-intellectual-propertyindicators-2025.pdf, 2025.
- [4] Reuters. Pfizer CEO Says U.S. Pharma Industry Needs to Collaborate with China. https://www.reuters.com/business/healthcarepharmaceuticals/pfizer-ceo-says-us-pharma-industryneeds-collaborate-with-china-2025-10-15/, October 2025.
- [5] Jason Wei, Zhiqing Sun, Spencer Papay, Scott McKinney, Jeffrey Han, Isa Fulford, Hyung Won Chung, Alex Tachard Passos, William Fedus, and Amelia Glaese. BrowseComp: A simple yet challenging benchmark for browsing agents, 2025. URL https: //arxiv.org/abs/2504.12516.
- [6] Manasi Sharma, Chen Bo Calvin Zhang, Chaithanya Bandi, Clinton Wang, Ankit Aich, Huy Nghiem, Tahseen Rabbani, Ye Htet, Brian Jang, Sumana Basu, Aishwarya Balwani, Denis Peskoff, Marcos Ayestaran, Sean M. Hendryx, Brad Kenstler, and Bing Liu. ResearchRubrics: A benchmark of prompts and rubrics for evaluating deep research agents, 2025. URL https: //arxiv.org/abs/2511.07685.
- [7] Joey Zhong, Hao Zhang, Clare Southern, Jeremy Yang, Thomas Wang, Kate Jung, Shu Zhang, Denis Yarats, Johnny Ho, and Jerry Ma. DRACO: a cross-domain benchmark for deep research accuracy, completeness, and objectivity, 2026. URL https://arxiv.org/abs/2602. 11685.
- [8] Nikita Gupta, Riju Chatterjee, Lukas Haas, Connie Tao, Andrew Wang, Chang Liu, Hidekazu Oiwa, Elena Gribovskaya, Jan Ackermann, John Blitzer, Sasha Goldshtein, and Dipanjan Das. DeepSearchQA: Bridging the Comprehensiveness Gap for Deep Research Agents, 2026. URL https://arxiv.org/abs/2601.20975.
- [9] Ryan Wong, Jiawei Wang, Junjie Zhao, Li Chen, Yan Gao, Long Zhang, Xuan Zhou, Zuo Wang, Kai Xiang, Ge Zhang, Wenhao Huang, Yang Wang, and Ke Wang. WideSearch: Benchmarking Agentic Broad Info-Seeking, 2025.
- [10] Tianci Xue, Weijian Qi, Tianneng Shi, Chan Hee Song, Boyu Gou, Dawn Song, Huan Sun, and Yu Su. An Illusion of Progress? Assessing the Current State of Web Agents, 2025. URL https://arxiv.org/abs/2504.01382.
- [11] Alisa Vinogradova, Vlad Vinogradov, Dmitrii Radkevich, Ilya Yasny, Dmitry Kobyzev, Ivan Izmailov, Katsiaryna Yanchanka, Roman Doronin, and Andrey Doronichev. LLM-Based Agents for Competitive Landscape Mapping in Drug Asset Due Diligence,


2025. URL https://arxiv.org/abs/2508.16571.

Find RNA-targeting therapeutics for chronic hepatitis B. HBV oligonucleotide programs (siRNA/ASO/ddRNAi/shRNA) in undercover APAC markets surfaced via national registries and local pipeline disclosures

SiRNA assets (GalNAc or LNP) surfaced via national registries and local pipeline disclosures. GalNAc-delivered siRNA assets in Japan and Taiwan surfaced via national registries and local pipeline disclosures. GalNAc-delivered siRNA assets in South Korea, Singapore, Hong Kong, and Australia/New Zealand surfaced via national registries and local pipeline disclosures. LNP-delivered siRNA assets in Japan, Taiwan, South Korea, Singapore, Hong Kong, and Australia/New Zealand surfaced via national registries and local pipeline disclosures.

Antisense oligonucleotide assets (RNase-H/gapmer/LNA) surfaced via national registries and local pipeline disclosures. Japan and Taiwan academic- or spinout-origin RNase-H gapmer/LNA ASO HBV assets surfaced via registries and local pipeline disclosures.

South Korea and Hong Kong industry- or translational-origin RNase-H gapmer/LNA ASO HBV assets surfaced via registries and local pipeline disclosures.

Singapore and Australia/New Zealand early-stage RNase-H gapmer/LNA ASO HBV assets surfaced via registries and local pipeline disclosures.

Vectorized RNAi assets (ddRNAi/shRNA, e.g., AAV-based) surfaced via national registries and local pipeline disclosures.

Stealth early-stage HBV oligonucleotides surfaced via regulatory and legal documentation before public pipeline disclosure CHB siRNA/ASO/ddRNAi injections disclosed in regulator notices and statutory trial registries before any public pipeline mention.

CHB siRNA/ASO/ddRNAi injections disclosed in institutional ethics/IRB/REC records before statutory trial registry listing. CHB siRNA/ASO/ddRNAi injections disclosed in procurement/insurance/contracts or corporate legal transfer/assignment filings before regulator/registry or ethics disclosure.

Small-molecule HBV RNA expression/stability/processing inhibitors (non-oligonucleotide) with evidence of HBsAg or HBV RNA reduction.

PAPD5/7 (TENT4A/B) enzymatic inhibitors with HBsAg or HBV RNA reduction evidence. Non-DHQ, 2022–2025 + APAC regulator notices and statutory trial registries (primary records only). Non-DHQ, 2022–2025 + patent disclosures with explicit PAPD5/7 enzymatic data and HBV RNA/HBsAg reduction. Non-DHQ, 2022–2025 + congress abstracts and sponsor gray literature with advancement signals and HBV RNA/HBsAg reduction.

ZCCHC14-engagers or PAPD5/7–ZCCHC14 complex disruptors, excluding PAPD5/7 enzymatic inhibitors, with HBsAg or HBV RNA reduction evidence.

ZCCHC14 direct binders (non-PAPD5/7 enzymatic) with HBV RNA/antigen reduction evidence. ZCCHC14 targeted degraders or molecular glues (non-PAPD5/7 enzymatic) with HBV RNA/antigen reduction evidence. Non-binder PAPD5/7–ZCCHC14 complex disruptors (non-PAPD5/7 enzymatic) with HBV RNA/antigen reduction evidence.

Non-PAPD5/7 and non-ZCCHC14 mechanisms (e.g., PRE/export or other RNA-processing pathways) with HBsAg or HBV RNA reduction evidence.

HBV PRE cis-element binders blocking RNA export/processing, excluding ϵ mechanisms and excluding trans-acting RNA-pathway modulators.

HBV ϵ (epsilon) RNA binders disrupting ϵ–polymerase priming or pgRNA packaging, excluding PRE mechanisms and excluding trans-acting RNA-pathway modulators.

Trans-acting HBV RNA export/processing/decay pathway modulators, excluding PRE mechanisms and excluding ϵ mechanisms.

- Figure 7: Part of the Coach Agent generated tree of directives for the query "Find RNA-targeting therapeutics for chronic


hepatitis B". Nodes given here are summaries of coach generated directive dn and directive additional instruction δn, we do not include them here in full for readability purposes. It was built for k = 3. Each node represents an incremental refinement of its parent; the effective search intent at node n is given by the root-to-n path, so child directives omit repeated parent phrasing and specify only the additional constraints or angle.

