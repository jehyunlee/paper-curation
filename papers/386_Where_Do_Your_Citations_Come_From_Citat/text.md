# arXiv:2603.24216v1[cs.DL]25 Mar 2026

![image 1](Where Do Your Citations Come From Citation-Constellation A Free Open-Source No-C_images/imageFile1.png)

WHERE DO YOUR CITATIONS COME FROM? CITATION-CONSTELLATION: A FREE, OPEN-SOURCE, NO-CODE, AND AUDITABLE TOOL FOR CITATION NETWORK DECOMPOSITION WITH COMPLEMENTARY BARON AND HEROCON SCORES ∗

Mahbub Ul Alam SciLifeLab Data Centre, Uppsala University, Sweden mahbub.ul.alam@scilifelab.uu.se, mahbub.ul.alam.anondo@gmail.com

## ABSTRACT

In this paper, I introduce Citation-Constellation, a fully operational and freely available tool2 for citation network analysis. Every claim presented here can be verified directly by the reader, with no installation, registration, or payment required. Users may enter an ORCID or OpenAlex ID to receive a complete citation network decomposition within minutes. The source code is publicly available3.

Standard citation metrics treat all citations as equal, thereby obscuring the social and structural pathways through which scholarly influence actually propagates [1, 2]. A citation from an independent researcher who discovers a paper through literature search carries a different epistemic weight than one from a direct co-author, a departmental colleague, or an editorial board member [3, 4]. Yet conventional metrics such as the h-index, raw citation counts, and journal impact factors collapse these important distinctions into a single number.

I introduce two complementary bibliometric scores that decompose a researcher’s citation profile according to network proximity between citing and cited authors. BARON (Boundary-Anchored Research Outreach Network score) provides a strict binary metric that counts only citations from outside the detected collaborative network, while HEROCON (Holistic Equilibrated Research Outreach CONstellation score) applies configurable graduated weights that assign partial credit to in-group

∗The acronyms BARON and HEROCON serve as metaphors that encode the conceptual relationship between the scores, as detailed in Section 5.

- 2Citation-Constellation No-Code Tool: citation-constellation.serve.scilifelab.se
- 3Citation-Constellation Source Code: github.com/citation-cosmograph/citation-constellation


citations based on relationship proximity. The gap between these two scores serves as a diagnostic indicator of inner-circle dependence.

The accompanying open-source tool implements this decomposition through a phased detection architecture comprising (1) self-citation analysis, (2) co-authorship graph traversal, (3) temporal institutional affiliation matching via the Research Organization Registry (ROR), and (4) AI-agentdriven venue governance extraction using a locally deployed large language model4. The first three phases are fully operational and accessible via the provided web tool, while Phase 4 is currently under active implementation. The implementation places particular emphasis on ORCID-validated author identity resolution, an UNKNOWN classification for citations with insufficient metadata, and comprehensive audit trails that document every classification decision. The venue governance phase demonstrates how recent advances in locally deployable generative AI can automate bibliometric infrastructure tasks, such as editorial board extraction and entity resolution, that were previously intractable without dedicated research teams. A no-code web interface deployed on SciLifeLab Serve enables researchers to compute and visualize their scores without programming knowledge, installation, or registration.

I present these scores as structural diagnostics that describe where in the social graph citations originate, explicitly not as quality indicators for research evaluation, and discuss their alignment with the responsible research assessment movement [5, 2]. The graduated HEROCON weights remain experimental and require empirical calibration; I identify sensitivity analysis and cross-validation with citation motivation studies as priorities for future work.

Keywords bibliometrics · citation analysis · citation network structure · co-authorship network · self-citation · author disambiguation · research impact measurement · network proximity · responsible research assessment · open science · research evaluation · scientometrics · scholarly communication · venue governance · institutional affiliation · ORCID · audit trail · reproducibility · large language model · generative AI · AI agent · AI infrastructure · automated information extraction · natural language processing

## 1 Introduction

The quantification of research impact represents a central concern of modern science policy, institutional evaluation, and individual career assessment. Metrics such as the h-index [6], citation count, and journal impact factor have become deeply embedded in academic hiring, promotion, and funding decisions. Yet these metrics share a fundamental limitation: they treat all citations as equivalent signals of impact, regardless of the relationship between the citing and cited researchers. This limitation has been noted by numerous scholars [7, 8, 9, 2, 1].

A citation from an independent researcher who discovers a paper through literature search carries a different epistemic weight than a citation from a direct co-author, a colleague in the same department, or one that arrives through a venue where the cited researcher holds an editorial or governance role. The former represents genuine external reach, providing evidence that the work has found relevance beyond its originating community. The latter, while not illegitimate, reflects the natural amplification effects of collaborative networks, institutional proximity, and professional relationships. This phenomenon, the tendency for citation patterns to follow social network structure, has been extensively studied in the literature on invisible colleges [10, 11], co-authorship networks [12, 13, 14, 15], and citation homophily [4, 16].

The core insight, that citation patterns are shaped by social network proximity, is well-established in network science and scientometrics. However, operationalizing this insight into a practical, auditable tool has been hindered by persistent challenges in author disambiguation, metadata quality, and the complexity of building comprehensive network detection layers that span self-citation, co-authorship, institutional affiliation, and venue governance. I address these challenges with an open-source tool that makes several key engineering contributions.

First, I present Citation-Constellation, a phased detection architecture that progressively deepens network analysis from self-citation through co-authorship graphs, temporal affiliation matching, and venue governance detection, with each phase producing an independently meaningful and usable score.

Second, the tool incorporates ORCID-validated author identity resolution to address the critical challenge of disambiguation error contaminating citation analysis.

Third, an UNKNOWN classification honestly reports citations with insufficient metadata rather than silently defaulting them to EXTERNAL, preventing systematic bias against researchers with poor metadata coverage.

4Citation-Astrolabe Source Code (venue governance database, under construction): citation-cosmograph/citation-astrolabe

Fourth, comprehensive audit transparency ensures that every classification decision is documented with a humanreadable rationale in a structured JSON file, enabling full reproducibility and contestability.

Fifth, the Phase 4 pipeline employs an AI-agent-driven venue governance extraction system using a locally deployed language model to build a persistent, incrementally expanding database of editorial board and program committee membership across disciplines.

Finally, the dual-score framework, comprising BARON (Boundary-Anchored Research Outreach Network score, a strict binary metric) and HEROCON (Holistic Equilibrated Research Outreach CONstellation score, a graduated weighted metric), provides an interpretable summary in which the gap between scores serves as a structural diagnostic of inner-circle dependence.

To ensure full accessibility for researchers regardless of their technical background, Citation-Constellation is available

- as both a command-line application and a no-code web interface (see Table 2 for links).

I emphasize that the HEROCON weights are experimental defaults informed by reasoning about relationship proximity, not empirically calibrated values. I present these tools as structural diagnostics, not quality indicators. BARON and HEROCON describe where in the social graph citations originate. They should not be used for hiring, promotion, or funding decisions.

2 Positioning My Contribution

The core insight, that citation patterns reflect network structure, is well-established, from Crane’s invisible colleges [10] through Wallace et al.’s network-distance analysis [4] and beyond. My contribution lies in synthesizing these disparate lines of inquiry into a unified, operational framework. By combining co-authorship analysis [12, 13], institutional proximity detection [17, 18], and editorial governance connections (novel in this context) with robust ORCID-based identity resolution [19], honest data quality reporting, and full audit transparency, I transform a theoretical lens into a practical diagnostic instrument.

This is not merely engineering. The history of scientometrics shows that the gap between theoretical insight and practical deployment is where most value is lost [20, 1], and that this gap is not neutral. When powerful analytical tools exist only as conceptual frameworks in journal articles, they benefit only those with the technical resources to reimplement them [21]. When they exist as accessible, free, open-source software, they become democratic infrastructure [22].

- 2.1 Accessibility as a Contribution


I deploy the Citation-Constellation tool as a web application on SciLifeLab Serve (citationconstellation.serve.scilifelab.se), freely accessible to anyone with a web browser. It requires no installation, no programming knowledge, no institutional subscription, no registration, and no payment. A researcher may navigate to the URL, enter an ORCID or OpenAlex identifier, and receive a full multi-layer citation network decomposition with interactive visualizations and a downloadable audit report within minutes.

This matters because many researchers understand, in principle, that citation patterns reflect network structure. Far fewer have access to a tool that decomposes their own profile across multiple network layers, validates author identity, honestly reports data limitations, and documents every decision in a contestable audit trail. Bibliometric self-knowledge has historically been a privilege of researchers with access to expensive proprietary databases such as Scopus and Web of Science [23, 24] and the technical skills to query them. A researcher at a well-funded university and a researcher

- at a teaching-intensive institution in the Global South face very different barriers to understanding their own citation structure, barriers that are economic and technical, not intellectual [25, 26]. By building entirely on open data sources, OpenAlex [22], ORCID [19], and ROR [27], and by providing both a command-line tool and a no-code web interface, I lower the barrier to citation profile analysis to near zero.


The comparison feature, which allows side-by-side visualization of multiple researcher profiles from uploaded audit files, further enables peer learning: colleagues within a department, a field, or a cohort may examine their structural patterns together, generating insights about disciplinary norms, collaboration effects, and career trajectories that no individual analysis could reveal. A department head could compare the citation constellations of their team to understand structural differences; a doctoral student could benchmark their emerging profile against established researchers in their field. These are not evaluative comparisons. They are structural explorations, made possible only when the tool is freely and universally accessible. This aligns with the broader open science movement’s emphasis on making research infrastructure equitable and transparent [28, 29, 30, 31].

### 2.2 The Audit Trail as Curated Evidence

The BARON/HEROCON dual-score framework provides an interpretable summary, but I consider the audit trail to be the deeper contribution. Each audit file is a structured, timestamped, machine-readable record of every citation link and every classification decision for a specific researcher at a specific moment in time. This is not merely a transparency mechanism. It is a curated data product. Aggregated across researchers, fields, and institutions, these audit files constitute a novel dataset for science-of-science research [32]: one that captures not merely how many citations a researcher received, but the network relationship underlying each one.

The hardest barrier in bibliometric research has always been the curation of trustworthy, structured data sources linking citations to their social context [1, 33, 24]. Existing large-scale citation databases [34, 22] capture citation counts and field classifications but do not decompose individual citations by the network relationship between citing and cited authors. My audit trail addresses this gap directly: each file is self-contained, reproducible, and carries its own provenance metadata. Future analyses, whether on collaboration norms across fields, on the evolution of collaboration networks and productivity [35], citation networks over career stages [36, 37], or on institutional effects on citation composition [17], can build on this curated foundation without repeating the expensive data collection and classification pipeline.

My emphasis on auditability also responds to growing calls for transparency in research evaluation [38, 39]. Traditional metrics are opaque: a researcher receives an h-index but cannot inspect how each citation was counted or whether misattributed works inflated the number. The Citation-Constellation audit trail, by contrast, makes every assumption contestable.

### 2.3 AI-Agent-Driven Bibliometric Infrastructure

Several components of this tool, particularly the venue governance extraction in Phase 4, would have been considered impractically labor-intensive even a year ago. Manually identifying editorial board members and program committee members across hundreds of academic venues, resolving their identities against bibliometric databases, and maintaining a persistent, incrementally growing governance database would require a dedicated research team. The rapid maturation of locally deployable large language models [40, 41] and efficient inference engines such as llama.cpp [42] has fundamentally changed this calculus. A quantized 8-billion-parameter model running on commodity CPU hardware can now perform structured information extraction from heterogeneous HTML pages with sufficient accuracy for entity resolution against bibliometric databases, a task that previously required either expensive commercial APIs, brittle rule-based scrapers, or dedicated human annotation [43].

The resulting venue governance database is not merely useful for BARON/HEROCON scoring. It is an independent scholarly resource. It could support studies of editorial board diversity across disciplines [44, 45], analyses of the relationship between editorial roles and citation patterns [46], investigations of how governance structures evolve over time, or simply serve as a lookup tool for researchers curious about who governs the venues they publish in.

More broadly, I consider this work a proof of concept for AI-agent-driven bibliometric infrastructure. The combination of web scraping, LLM-based structured extraction, entity resolution against open bibliometric databases, and persistent incremental storage represents a reusable architectural pattern. The same pipeline that extracts editorial boards could be adapted to extract funding acknowledgements, author contribution statements, or conflict-of-interest declarations. This is all structured data that exists on journal websites but is not systematically captured or reliably structured in existing commercial databases [47, 48].

## 3 How to Use Citation-Constellation

The tool is available in two forms: a no-code web interface (recommended for most users) and a command-line interface (for advanced users and automation). Both produce identical scores and audit trails.

### 3.1 No-Code Web Interface

The web interface is deployed on SciLifeLab Serve and requires no installation, no programming knowledge, and no account creation. Navigate to the application URL and use one of six tabs:

- 1. Run Analysis — Compute new BARON & HEROCON scores.
- 2. View Existing Audits — Upload audit JSON files for visualization and comparison.
- 3. How to Run Here & Install Locally — Step-by-step instructions.


- 4. How BARON & HEROCON Work — Plain-language methodology.
- 5. Future Features — Planned Phase 4, 5, and 6 capabilities.
- 6. Full Research Paper — This paper, embedded for reference.


- 3.1.1 Running a New Analysis Navigate to the Run Analysis tab.

- 1. Enter a researcher identifier. Provide an ORCID (e.g., 0000-0000-0000-0000) or an OpenAlex ID (e.g., A0000000000). Full URLs are accepted; the tool extracts the ID automatically. ORCID format validation includes ISO 7064 Mod 11,2 checksum verification; invalid checksums produce a clear error message.
- 2. Optional: Set a career start year (default: 2000). If OpenAlex has merged works from a different researcher with a similar name, enter the year your career began. All earlier works will be excluded. This is often the simplest fix for name collision.
- 3. Optional: Adjust co-author graph depth (default: 2). Depth 1 counts only direct co-authors as in-group. Depth 2 (recommended) includes co-authors of co-authors. Depth 3 extends to three hops.
- 4. Optional: Enable manual validation. Check “Wait for my validation before discarding flagged papers” to review ORCID-flagged papers as checkboxes before scoring proceeds.
- 5. Optional: Upload custom HEROCON weights. Under the “Advanced” accordion, upload a JSON file to override default weights. Unspecified classifications use defaults.
- 6. Click “Run Analysis.” For a researcher with approximately 50–100 publications, expect 1–4 minutes. A progress message is displayed throughout.


- 3.1.2 Understanding the Results

- • Score Summary — BARON, HEROCON, gap, total citations, classifiable citations, reliability rating.
- • Classification Donut Chart — Proportional breakdown of citation origins with scores in the center.
- • Classification Summary Table — Each category with count, percentage, and HEROCON weight.
- • Co-Author Network Graph — Interactive force-directed network. Target researcher as gold node; direct co-authors in crimson (sized by shared papers); transitive co-authors in blue. Hover for details. Networks above 150 nodes are automatically pruned.
- • Career Trajectory Chart — Dual-line BARON and HEROCON over time, shaded gap area, cumulative citation bars.
- • Full Classification Table — Every citation with classification, confidence, phase, and human-readable rationale. Collapsible, with “Export Citations as JSON” option.
- • Interpreting the BARON–HEROCON gap — A small gap (below 3%) indicates overwhelmingly external impact. A moderate gap (3–10%) suggests meaningful inner-circle contribution alongside dominant external reach. A large gap (above 10%) indicates that a significant portion of measured impact comes from the collaborative network. This is neither good nor bad; it characterizes citation structure, not quality.
- • Download Audit Report — Complete JSON audit for offline analysis or re-visualization.


- 3.1.3 Comparing Multiple Researchers


In the View Existing Audits tab, upload previously generated audit JSON files. A single file produces full visualization. Multiple files produce a comparison table, separate overlaid BARON and HEROCON trajectory charts, and expandable individual reports. Up to 115 simultaneous comparisons are supported. Files are validated against the expected schema; invalid files are rejected with clear messages.

Rate limit: 10 analyses per hour per session. Visualization has no limit.

- 3.2 Command-Line Interface


- 3.2.1 Installation


git clone https://github.com/citation-cosmograph/citation-constellation.git cd citation-constellation pip install -r requirements.txt

Requirements: Python 3.11+. No database needed for Phases 1–3.

### 3.2.2 Basic Usage

- # Phase 1: Self-citation baseline only

- python phase1.py --orcid 0000-0000-0000-0000

# Phase 2: Self-citation + co-author network

- python phase2.py --orcid 0000-0000-0000-0000 --trajectory

# Phase 3: Full analysis (recommended — includes Phases 1 + 2)

- python phase3.py --orcid 0000-0000-0000-0000 --trajectory




# Also accepts OpenAlex IDs python phase3.py --openalex-id A0000000000 --trajectory

### 3.2.3 Common Flags (Table 1)

Flag Description

- –export results.json Export summary to JSON
- –trajectory or -t Show cumulative career trajectory by year
- –since 2010 Only include works from 2010 onward
- –depth 1|2|3 Co-author graph depth (default 2)
- –herocon-weights file.json Custom HEROCON weight configuration
- –confirm or -c Review ORCID-flagged works interactively before scoring
- –no-orcid-check Skip ORCID cross-validation
- –no-audit Skip audit file generation (not recommended)
- –verbose or -v Verbose output Table 1: Common flags for command-line interface


#### 3.2.4 Interactive Confirmation Modepython phase3.py --orcid 0000-0000-0000-0000 --confirm

The tool displays flagged works with reasons and prompts for a decision. Input options: all (exclude all), none (keep all), 1,3,5 (exclude specific items), or 1-3,5 (ranges). The audit trail records all exclusion decisions.

### 3.2.5 Audit Trail

Every run generates a timestamped JSON audit file in ./audits/ by default. CLI-generated audit files can be uploaded to the web interface for interactive visualization without re-running computation. Note: the –trajectory or -t flag must be included during generation for the career trajectory chart to be available in the web interface. All other visualizations work regardless of this flag.

- 3.3 Running Locally


- Option A: Python.

cd citation-constellation/ pip install -r requirements.txt python app/main.py # Open http://localhost:7860

- Option B: Docker from source.


docker build --platform linux/amd64 -t citation-constellation:v0.3 . docker run --rm -it -p 7860:7860 citation-constellation:v0.3 # Open http://localhost:7860

### Option C: Prebuilt image.

docker pull mahbub1969/citation-constellation:v1 docker run --rm -it -p 7860:7860 mahbub1969/citation-constellation:v1 # Open http://localhost:7860

### 3.4 Citation-Cosmograph Ecosystem (Table 2)

#### pulsar → astrolabe → constellation

the signal the instrument the map

###### Component Purpose Link

Citation-Constellation BARON & HEROCON scoring No-Code Tool | Code Citation-Pulsar-Helm LLM inference on Kubernetes Code Citation-Astrolabe Venue governance database Code

Table 2: The Citation-Cosmograph ecosystem on GitHub.

## 4 Demonstration and Illustrative Output

- 4.1 Score Progression Across Phases As detection layers deepen (Table 3), BARON decreases as more in-group relationships are identified:


### Phase Detection Layers Classes BARON HEROCON

- 1 Self-citation 2 High —
- 2 + Co-author network 4 Moderate Moderate-High
- 3 + Affiliation matching 7 Lower Moderate Table 3: Score progression across phases


Ethical Notice Every analysis output begins with a prominent ethical disclaimer (Figure 1), reinforcing that BARON and HEROCON measure citation network structure, not research quality, impact, or integrity, and should not be used for hiring, promotion, or funding decisions.

![image 2](Where Do Your Citations Come From Citation-Constellation A Free Open-Source No-C_images/imageFile2.png)

Figure 1: Ethical notice displayed at the top of every analysis output.

Full Score Panel The score panel (Figure 2) presents the BARON and HEROCON scores alongside key summary statistics: total citations, classifiable citations, the BARON–HEROCON gap, and a data quality reliability rating. Both the web interface and command-line interface produce equivalent information, formatted for their respective contexts.

![image 3](Where Do Your Citations Come From Citation-Constellation A Free Open-Source No-C_images/imageFile3.png)

(a) Web Interface

![image 4](Where Do Your Citations Come From Citation-Constellation A Free Open-Source No-C_images/imageFile4.png)

(b) Command Line Interface

Figure 2: Score panel in both interfaces.

Classification Breakdown Donut Chart The donut chart (Figure 3) provides a proportional breakdown of citation origins across all classification categories, with the BARON and HEROCON scores displayed in the center. This gives an immediate visual sense of how a researcher’s citations distribute across network layers.

![image 5](Where Do Your Citations Come From Citation-Constellation A Free Open-Source No-C_images/imageFile5.png)

- Figure 3: Classification breakdown donut chart.

Co-author Network Graph The interactive co-author network graph (Figures 4 and 5) renders the target researcher

- as a gold node, direct co-authors in crimson (sized proportionally to the number of shared publications), and transitive co-authors in blue. Hovering over any node reveals the author name, shared paper count, and co-authorship recency. Networks exceeding 150 nodes are automatically pruned for readability.


![image 6](Where Do Your Citations Come From Citation-Constellation A Free Open-Source No-C_images/imageFile6.png)

- Figure 4: Co-author network graph (overview).


![image 7](Where Do Your Citations Come From Citation-Constellation A Free Open-Source No-C_images/imageFile7.png)

- Figure 5: Co-author network graph (detail).


Classification Summary The classification summary table (Figure 6) lists each citation category with its count, percentage of classifiable citations, and the HEROCON weight applied. This tabular view complements the donut chart by providing exact numbers for each network layer.

![image 8](Where Do Your Citations Come From Citation-Constellation A Free Open-Source No-C_images/imageFile8.png)

(a) Web Interface

![image 9](Where Do Your Citations Come From Citation-Constellation A Free Open-Source No-C_images/imageFile9.png)

(b) Command Line Interface

- Figure 6: Classification summary in both interfaces.


Career Trajectory Chart The career trajectory chart (Figure 7) plots cumulative BARON and HEROCON scores over time as dual lines, with a shaded region between them representing the gap. Stacked bars beneath show annual citation volume. This visualization reveals how a researcher’s external reach evolves across career stages, whether it grows after an institutional move, narrows as a lab expands, or remains stable over time.

![image 10](Where Do Your Citations Come From Citation-Constellation A Free Open-Source No-C_images/imageFile10.png)

(a) Web Interface

![image 11](Where Do Your Citations Come From Citation-Constellation A Free Open-Source No-C_images/imageFile11.png)

(b) Command Line Interface

- Figure 7: Career trajectory chart in both interfaces.

Citation Table from Audit Trail The full citation table (Figure 8) exposes every individual citation with its classification, confidence level, detection phase, and a human-readable rationale explaining why that classification was assigned. This is the audit trail made visible: any classification can be inspected, questioned, and contested.

![image 12](Where Do Your Citations Come From Citation-Constellation A Free Open-Source No-C_images/imageFile12.png)

- Figure 8: Full citation table from the audit trail.


Comparison View The comparison view enables side-by-side structural analysis of multiple researchers from uploaded audit files. The tables and figures (Figures 9, 10, and 11) presented here are derived from actual empirical data; however, researcher names have been anonymized to ensure confidentiality.

The overlaid trajectory charts allow structural comparison of how external reach evolves across different researchers’ careers. A department head could use these to understand whether early-career researchers in their group are building external visibility at a pace consistent with field norms, or whether a mid-career shift in collaboration patterns coincided with a change in citation composition. When researchers from different fields or institution types are compared, the trajectories can reveal whether apparent differences in raw citation counts mask similar underlying structural patterns, or whether nominally similar profiles diverge sharply in their network dependence over time. These are not evaluative rankings; they are structural narratives placed side by side.

![image 13](Where Do Your Citations Come From Citation-Constellation A Free Open-Source No-C_images/imageFile13.png)

Figure 9: Comparison table.

![image 14](Where Do Your Citations Come From Citation-Constellation A Free Open-Source No-C_images/imageFile14.png)

- Figure 10: BARON trajectory comparison.

![image 15](Where Do Your Citations Come From Citation-Constellation A Free Open-Source No-C_images/imageFile15.png)

- Figure 11: HEROCON trajectory comparison.


![image 16](Where Do Your Citations Come From Citation-Constellation A Free Open-Source No-C_images/imageFile16.png)

Figure 12: Individual reports within the comparison view.

In addition to the comparative overlays, the visualization expands into full individual reports (Figure 12) for each uploaded researcher, identical in format to those produced by the Run Analysis tab. Each expandable section contains the score panel, classification donut chart, co-author network graph, career trajectory, and full citation table for that researcher. This allows a viewer to move seamlessly between the bird’s-eye comparative view and the detailed per-citation audit of any individual profile, without needing to re-run any computation.

### 4.2 ORCID Cross-Validation Impact

In testing, OpenAlex had merged works from a different researcher with a similar name. The ORCID layer correctly excluded those misattributed works, preventing contamination of the co-author graph and affiliation timeline. DOI-based matching resolved 70–85% of works; title-based fuzzy matching recovered an additional 10–15%.

### 4.3 Limitations of Current Validation

I acknowledge that the current demonstration is descriptive rather than validational. I have not yet established that BARON/HEROCON scores correlate with (or meaningfully diverge from) independent measures of citation motivation, research quality, or integrity. I identify such validation as a critical priority for future work (see Section 10).

## 5 Nomenclature as Framework: The Metaphors of BARON and HEROCON

Before describing the technical methodology, I pause to explain the names of the two scores, because the metaphors they invoke are not decorative. They encode the conceptual relationship (Figure 13) between the scores and frame how they should be interpreted.

### 5.1 BARON: The Boundary Guardian

The Boundary-Anchored Research Outreach Network (BARON) score takes its name from the historical Marcher Barons, the feudal lords charged with securing and governing the outer borders of a realm. In medieval England and Wales, the Marcher Lords held the frontier: the boundary where a kingdom’s influence either held or dissolved. Their role was to anchor legitimacy at the edges.

The BARON score plays an analogous role for a researcher’s citation profile. It deliberately filters out the natural amplification of local networks, co-authors, institutional peers, and editorial connections, and measures only what crosses the boundary: citations from researchers with no detected relationship to the author. In doing so, BARON anchors the maximum defensible reach of a scholar’s metrics. It asks a simple, strict question: how much of this researcher’s citation impact survives when we remove every citation that could plausibly have been mediated by social proximity?

![image 17](Where Do Your Citations Come From Citation-Constellation A Free Open-Source No-C_images/imageFile17.png)

Figure 13: The Citation-Constellation emblem

This is a conservative measure by design. Just as a Marcher Baron’s strength was tested not by the loyalty of subjects within the walls but by the respect commanded beyond them, BARON tests a citation profile not by in-group endorsement but by external validation. A high BARON score does not mean a researcher is better; it means their work has demonstrably reached beyond their immediate scholarly community. A low BARON score does not mean a researcher is worse; it may reflect a small field, a productive lab, or a disciplinary norm of close collaboration.

By establishing this foundational threshold of strict external outreach, the BARON score provides the crucial boundary that gives the broader HEROCON score its shape. Without demonstrated reach beyond the immediate circle, the constellation cannot form.

### 5.2 HEROCON: The Constellation

The Holistic Equilibrated Research Outreach CONstellation (HEROCON) score is named for the constellation Hercules. In Greek mythology, Hercules was placed among the stars after his death as an eternal monument to strength, perseverance, and labors that transcended mortal limits.

Where BARON draws a binary line at the boundary, HEROCON maps the full figure. It treats a researcher’s total scholarly influence as a constellation: localized collaborations, co-authors, departmental colleagues, and institutional peers form bright, dense clusters of stars, much like the tightly bound star systems at the heart of Hercules. These clusters are valuable; they represent the close intellectual community that sustains and nourishes research. But a constellation cannot be confined to a single cluster. It must stretch across the sky to earn its name.

The BARON score provides the anchoring boundary stars that define the constellation’s outer limits and give it its legendary shape. A dense local cluster without distant anchor points is not a constellation; it is an asterism, a local pattern that does not extend to the broader sky. Conversely, scattered distant points without a bright local core lack the structure that makes a constellation recognizable. The interplay between the two, dense local community (HEROCON’s partial credit for in-group citations) and broad external reach (BARON’s boundary anchoring), is what gives a citation profile its constellation shape.

One of the constellation’s most prominent star systems, Rasalgethi (Alpha Herculis, from the Arabic ra’s al-j¯ath¯ı, "the kneeler’s head"), carries a further resonance.

The figure of Hercules in the sky is depicted kneeling, a posture not of defeat but of humility. True scholarly leadership, like the kneeling Hercules, requires humility: acknowledging the contributions of one’s immediate community, recognizing that co-author citations and institutional support are the bright core that sustains a career. A high HEROCON score demonstrates precisely this, that a researcher unites a bright local foundation with the vast external outreach that illuminates the broader academic universe.

Ultimately, the gap between HEROCON and BARON reveals the shape of the constellation itself. A small gap means the constellation is diffuse, citations come from everywhere. A large gap means the constellation has a bright, dense core surrounded by more distant anchor points. Neither pattern is inherently better; they are different shapes in the scholarly sky, and the Citation-Constellation tool makes those shapes visible.

## 6 Methodology

### 6.1 Conceptual Framework

I conceptualize a researcher’s citation profile as concentric network layers (Table 4), from most proximate (self) to most distant (external). Each layer represents a relationship type that could mediate citation behavior:

- • Layer 0 — Self: Citing own prior work.
- • Layer 1 — Direct co-authors: Shared at least one publication.
- • Layer 2 — Transitive co-authors: Co-authors of co-authors (configurable depth, default 2).
- • Layer 3 — Institutional colleagues: Same institution/department, even without co-authorship.
- • Layer 4 — Venue governance: Editorial board or program committee overlap with citing venue.
- • Layer 5 — External: No detected relationship.


BARON treats all layers 0–4 as in-group (weight = 0) and only counts fully external citations (weight = 1). HEROCON assigns graduated weights:

Layer Relationship BARON HEROCON Rationale

- 0 Self-citation 0 0.0 No credit; researcher is citing themselves
- 1 Direct co-author 0 0.2 Low credit; strongest collaborative tie
- 2 Transitive co-author 0 0.5 Moderate credit; indirect tie, weaker influence pathway
- 3a Same department 0 0.1 Very low credit; strongest proximity without co-authorship

- 3b Same institution, different dept 0 0.4 Moderate credit; cross-departmental
- 3c Same parent organization 0 0.7 High credit; tenuous institutional link


- 4a Venue self-governance 0 0.05 Near-zero; researcher directly governs the venue

- 4b Venue editor is co-author 0 0.15 Low credit; compound relationship
- 4c Venue editor at same institution 0 0.3 Moderate credit; institutional link through editorial channel
- 4d Committee member in network 0 0.4 Moderate credit; weaker governance connection


- 5 External 1 1.0 Full credit; no detected relationship Table 4: Conceptualizing scoring for a researcher’s citation profile as concentric network layers.


Score computation.

external citations

BARON =

- classifiable citations × 100 (1)

HEROCON = i

wi

- classifiable citations × 100 (2)


where wi is the HEROCON weight for citation i’s classification, and “classifiable” excludes UNKNOWN citations (see Section 6.6).

Diagnostic gap = HEROCON − BARON (3) The diagnostic gap represents the proportion of impact attributable to in-group citations under graduated weighting.

### 6.1.1 The HEROCON weights as a testable hypothesis

The HEROCON weights represent a formal hypothesis about the relative strength of different network pathways in mediating citation. I hypothesize that a direct co-authorship tie (weight 0.2) is a stronger predictor of networkmediated citation than mere departmental colocation (weight 0.1), because the former represents a deliberate intellectual collaboration while the latter may be purely administrative. I hypothesize that a tie through a co-author of a co-author (weight 0.5) is weaker than a direct tie but still represents a meaningful intellectual community, whereas a differentdepartment colleague at the same institution (weight 0.4) might have even less direct intellectual overlap despite closer physical proximity. These hypotheses are eminently testable, and I identify their empirical calibration as my primary future work (see Section 10).

I acknowledge these weights are experimental defaults, not empirically calibrated values. Researchers who wish to test alternative weightings may do so through full weight customization, available both via the CLI (–herocon-weights path/to/weights.json, see Section 3.2.3 for details) and through the web interface’s Advanced settings, where a custom weights JSON file can be uploaded before running an analysis (see Section 3.1.1, step 5 for details).

- 6.2 Phased Implementation Architecture (Figure 14) Each phase adds a detection layer and produces a usable score. Later phases incorporate earlier layers.


![image 18](Where Do Your Citations Come From Citation-Constellation A Free Open-Source No-C_images/imageFile18.png)

- Figure 14: Phased implementation architecture. Phases 1–3 are complete and available via CLI and web interface. Phase 4 (venue governance via local LLM) is under development. Phase 5 (field normalization) is planned.


### 6.2.1 Phase 1: Self-Citation Baseline

For each researcher publication, I fetch all incoming citations from OpenAlex. I check whether any author ID on the citing work matches the target researcher and classify as SELF or NON_SELF.

BARONv0.1 = percentage of NON_SELF citations (4)

### 6.2.2 Phase 2: Co-Author Network Detection

I construct a co-authorship graph from the target researcher’s publications. Each author pair sharing a paper creates a weighted edge:

strength(a,b) = shared_papers(a,b) × exp(−0.1 × years_since_last_collaboration) (5)

The exponential decay with rate 0.1 yields a half-life of approximately 7 years (ln(2)/0.1 ≈ 6.93). This reflects the hypothesis that recent collaborators are more “in-group” than distant ones. I note that the specific decay rate is not empirically grounded; alternative rates would be equally defensible. The decay function currently modulates co-authorship strength metadata logged in audit files but does not affect BARON classification (which uses binary in/out).

Starting from the target researcher, the tool performs a Breadth-First Search (BFS) traversal of the co-authorship graph to a configurable depth d (default 2). Every author encountered during this traversal is considered part of the researcher’s collaborative network. Citations are then classified by graph distance: distance 0 (the researcher themselves) maps to SELF, distance 1 (direct co-authors) maps to DIRECT_COAUTHOR, distance 2 (co-authors of co-authors) maps to TRANSITIVE_COAUTHOR, and any citing author beyond depth d or not found in the graph is classified as EXTERNAL.

HEROCON is introduced in this phase with the 4-class taxonomy.

### 6.2.3 Phase 3: Temporal Affiliation Matching

Citations not classified as SELF or co-author are checked for institutional affiliation overlap at the time of citation. I build an affiliation timeline from work-level affiliation data in OpenAlex. Institutional relationships are resolved using ROR parent-child hierarchy and OpenAlex lineage data, producing four tiers: SAME_DEPT, SAME_INSTITUTION, SAME_PARENT_ORG, DIFFERENT.

When affiliation data is insufficient for classification, citations are labeled UNKNOWN (see Section 6.6).

### 6.2.4 Phase 4: Venue Governance Detection

This phase detects citations flowing through venues where the target researcher or their network holds governance roles. I use a locally deployed language model (Qwen 3.5 8B, Q4_K_M quantized) to extract structured governance data from venue editorial board pages.

- Stage 1 — Database construction. For each venue, the system fetches the editorial board page (via httpx or Cloudflare Crawl API for JS-rendered sites), feeds the raw HTML to the local LLM for structured extraction (member name, role, institution, ORCID), and performs entity resolution against OpenAlex author profiles. Results are cached with confidence scores and timestamps.
- Stage 2 — Citation reclassification. For each citation currently classified as EXTERNAL, I check whether the citing venue has governance overlap with the target researcher or their network. Classifications: VENUE_SELF_GOVERNANCE, VENUE_EDITOR_COAUTHOR, VENUE_EDITOR_AFFIL, or VENUE_COMMITTEE.


The venue governance database is designed for incremental growth: each new analysis contributes new venues. A nightly job refreshes stale entries.

### 6.2.5 Phase 5: Field Normalization and Percentiles (Proposed)

Field-normalized percentile ranks comparing a researcher’s scores against peer cohorts (same field, similar career length, comparable publication volume). This phase is not yet implemented.

### 6.3 Author Identity Validation via ORCID

A critical challenge I encountered during development was author disambiguation error in OpenAlex. Researchers with common names may have works misattributed to their profile. I address this through ORCID cross-validation using a smart two-mode system:

- • High ORCID coverage (≥70%): ORCID is used as a hard filter; only works in both ORCID and OpenAlex enter scoring.
- • Low ORCID coverage (<70%): All OpenAlex works are kept, but affiliation anomaly detection flags works from institutions never associated with the researcher.


If the publication span exceeds 25 years, a warning suggests using –since YEAR to set the career start explicitly.

### 6.4 Transparency and Audit Trail

Every run produces a timestamped JSON audit file documenting: the researcher profile, every work analyzed, every citation link, every classification decision with a human-readable rationale, the co-author graph, the affiliation timeline and institution hierarchy, data quality metrics, and the score computation.

Every output carries an inline disclaimer: “BARON and HEROCON measure citation network structure, not research quality, impact, or integrity.”

### 6.5 Technology Stack

Python 3.11+ CLI application using Typer, Rich, and httpx. No database required for Phases 1–3. Phase 4 adds a persistent venue governance database (SQLite/PostgreSQL) and a locally deployed Qwen 3.5 8B language model (Q4_K_M quantized, served via llama.cpp on Kubernetes). A Gradio-based web interface provides no-code access for all Phase 1–3 functionality.

Data sources (all free and open): OpenAlex, 260M+ works, 100M+ authors, 2.8B+ citation links; ORCID Public API v3.0; ROR API v2; Cloudflare Crawl API (Phase 4 only).

Performance. For approximately 80 publications and 1500 citations, Phase 3 completes in under 90 seconds with approximately 100–150 OpenAlex API calls.

### 6.6 The UNKNOWN Classification and Data Quality Reporting

OpenAlex work-level affiliations are present for approximately 75% of recent works, with lower coverage for older publications. When affiliation data is missing, the system cannot determine whether a citation is genuinely external or institutional.

Early versions defaulted such citations to EXTERNAL, creating systematic bias: researchers with poor metadata received artificially inflated BARON scores. This is both technically incorrect and ethically problematic.

I address this with UNKNOWN: citations are classified UNKNOWN when (a) the target researcher has no affiliation data for the relevant time period, or (b) no citing author has affiliation data for the citation year. UNKNOWN citations are excluded from both BARON and HEROCON calculations.

Data quality metrics: Classifiable citations count and percentage. Reliability rating: HIGH (≥85%), MODERATE (≥70%), LOW (≥50%), VERY LOW (<50%).

I acknowledge that excluding UNKNOWN citations from the denominator creates a different form of selection bias. If UNKNOWN citations are systematically different from classifiable ones, disproportionately from developing countries with poor metadata, or from older publications, then the computed scores may not represent the true citation distribution. I identify a sensitivity analysis comparing different UNKNOWN imputation strategies as a priority for future work.

## 7 Conceptual Foundations and Tool Landscape

I position Citation-Constellation within the existing landscape by looking in two directions. The first is the conceptual literature that has established, over decades, that citation patterns are shaped by social network structure, that selfcitation is a spectrum rather than a binary, and that metrics can distort the practices they aim to measure. The second is the practical tool landscape, the software that researchers actually use today to analyze citations, map networks,

and evaluate scholarly output. The conceptual literature tells me why citation network decomposition matters. The tool landscape tells me that despite decades of theoretical insight, no existing instrument translates that insight into an individual-level, auditable diagnostic. This section maps both dimensions to make that gap precise.

- 7.1 Conceptual Foundations


- 7.1.1 Citation-Based Research Impact Metrics


The h-index [6] remains the most widely recognized single-number measure of research impact. While elegant in its simplicity, the h-index has well-documented limitations: it is field-dependent, penalizes early-career researchers, and cannot distinguish between different types of citations [49, 8, 9]. Seglen [7] made the classic argument that journal impact factors should not be used for evaluating individual research.

The g-index [50] and field-weighted citation impact [51] address some limitations but share the fundamental problem of treating all citations equally regardless of source. Waltman [1] provides a comprehensive review, concluding that existing approaches remain inadequate for capturing the multidimensional nature of research influence. Leydesdorff and Bornmann [52] demonstrated how fractional counting of citations affects impact measurement across fields.

### 7.1.2 Self-Citation Analysis

Aksnes [53] demonstrated that self-citations constitute a significant fraction of total citations. Kacem et al. [54] provided a comprehensive analysis of self-citation patterns across disciplines. Critically, Ioannidis [3] introduced a generalized view of self-citation extending beyond direct author self-citation to include co-author self-citation, collaborative selfcitation, and coercive induced self-citation. This taxonomy is directly relevant to my multi-layer approach. My BARON and HEROCON scores operationalize a similar decomposition, extending Ioannidis’s conceptual framework into a computable, auditable system.

Fowler and Aksnes [55] demonstrated that self-citation increases subsequent citation from others. Seeber et al. [56] explicitly framed self-citations as strategic responses to the use of metrics for career decisions, directly connecting to my Goodhart’s Law concerns (see Section 8.3).

### 7.1.3 Network-Aware Citation Analysis

Invisible colleges. Crane [10] introduced informal networks of scientists who influence each other’s work outside formal institutional structures. Zuccala [11] developed a formal model reconciling structural and processual perspectives. These invisible colleges are precisely the "hidden networks" that my tool makes visible.

Co-authorship and citation. Newman [12, 13] established foundational methods for analyzing scientific collaboration networks. Glänzel and Schubert [14] found that collaborative papers receive more citations. Moody [15] traced increasing disciplinary cohesion. My Phase 2 co-author graph detection operationalizes these findings.

Citation proximity. Most directly relevant to my work, Wallace, Larivière, and Gingras [4] examined citation proximity using degrees of separation in co-author networks, finding that direct self-citations are relatively constant across fields (hovering around 20% in natural and medical sciences, and 10% in social sciences and humanities), while citations to co-author network members vary substantially. Their approach is conceptually identical to my BARON/HEROCON decomposition. My contribution extends their analysis with temporal affiliation matching, venue governance detection, ORCID identity validation, and a tool that any researcher can run on their own profile.

Institutional and geographic effects. Larivière and Gingras [17] demonstrated the Matthew Effect in citation. Wagner and Leydesdorff [16] analyzed international collaboration network structure. Pan, Kaski, and Fortunato [18] uncovered the role of geography in shaping citation and collaboration networks.

Citation homophily and diversity. Hofstra et al. [57] documented the diversity–innovation paradox: underrepresented groups innovate at higher rates but their contributions are discounted. This suggests that citation network structure may systematically disadvantage researchers less embedded in dominant citation communities. My UNKNOWN classification and data quality reporting attempt to make such biases visible.

### 7.1.4 Citation Cartels and Gaming

Baccini, De Nicolao, and Petrovich [46] documented citation gaming at national scale. Edwards and Roy [58] described perverse incentives. Smaldino and McElreath [59] modeled the evolutionary pressure for bad science driven by metric optimization. Meho [60] found institutions with publication surges of up to 965% driven by strategic optimization. These patterns illustrate Goodhart’s Law as articulated by Fire and Guestrin [61].

My tool does not detect gaming per se; rather, it detects network structure. The distinction matters because in-group citation is normal and often appropriate. Nevertheless, making network composition visible creates accountability infrastructure.

### 7.1.5 Author Disambiguation and Identity

Ferreira, Gonçalves, and Laender [43] surveyed automatic methods for disambiguation. OpenAlex [22] uses machine learning. Schulz et al. [62] exploited citation networks for large-scale disambiguation, validating my use of co-author graphs as identity evidence. ORCID [19] provides researcher-maintained persistent identifiers. I use ORCID as a trust anchor for validating algorithmically assigned works.

### 7.1.6 Responsible Research Assessment

DORA [5] calls for moving away from single-number metrics. The Leiden Manifesto [2] requires that quantitative evaluation support qualitative expert judgment. Wilsdon et al. [38] provided a comprehensive UK policy framework. De Rijcke et al. [39] documented how indicator use distorts research behavior. Brembs [63] demonstrated that prestigious journals struggle to reach even average reliability, which is relevant to my venue governance detection, as it separates the structural fact of editorial connection from any quality judgment.

### 7.2 Existing Tools and Platforms

The conceptual foundations reviewed above have been established for decades, yet the practical tool landscape reveals a striking absence. No existing instrument translates these insights into an individual-level citation network decomposition with auditable, per-citation classifications. I survey the most prominent tools below to make this gap concrete.

### 7.2.1 Bibliometric Network Visualization

VOSviewer (vosviewer.com; [64]) is a widely used free tool for constructing and visualizing bibliometric networks, including co-authorship maps, citation coupling, co-citation clusters, and keyword co-occurrence networks. Developed at CWTS, Leiden University, it excels at mapping the structure of a research field at the macro level. VOSviewer visualizes relationships between entities (authors, journals, institutions) but does not analyze the citation profile of a single researcher. It does not classify individual citations by network proximity, does not compute per-researcher scores, and does not produce audit trails. VOSviewer answers what does this field look like?, whereas Citation-Constellation answers where do my citations come from?

CiteSpace (citespace.podia.com; [65]) is a Java-based tool for visualizing and analyzing trends and patterns in scientific literature, with particular strength in detecting research fronts, burst detection, and temporal co-citation analysis. Like VOSviewer, CiteSpace operates at the field level rather than the individual researcher level. It maps how a body of literature evolves, not how a single researcher’s citations decompose by network proximity.

Bibliometrix / Biblioshiny (bibliometrix.org; [66]) is an R package (with a Shiny web interface called Biblioshiny) for comprehensive science mapping analysis. It supports co-authorship networks, keyword co-occurrence, thematic evolution, and three-field plots. Bibliometrix is powerful and flexible for field-level bibliometric analysis but, like VOSviewer and CiteSpace, it does not perform per-citation network proximity classification for an individual researcher. It can compute co-authorship statistics and self-citation rates but does not build a multi-layer classification system (self → co-author → institutional → venue governance → external) with graduated scoring and per-citation audit trails.

### 7.2.2 Literature Discovery and Citation Exploration

Connected Papers (connectedpapers.com) is a web-based tool that builds a visual graph of papers related to a seed paper, using co-citation and bibliographic coupling similarity. It is designed for literature discovery (finding related work), not for analyzing an individual’s citation profile. It shows how papers are connected to each other, not how people are connected to the researchers they cite.

ResearchRabbit (researchrabbit.ai) is a free tool that builds interactive visualizations of citation networks and coauthorship connections from a seed collection of papers. It excels at discovering related work and tracking research trends. Like Connected Papers, it is a discovery tool rather than a profile analysis tool. It does not decompose a researcher’s incoming citations by network proximity or produce structural scores.

Litmaps (litmaps.com) provides interactive citation maps showing how a set of papers are related through citation links, with timeline visualization and monitoring for new relevant publications. It is oriented toward systematic review and literature monitoring rather than individual citation profile analysis.

### 7.2.3 Citation Context and Intent

scite.ai (scite.ai; [67]) is the tool most conceptually adjacent to Citation-Constellation in its ambition to go beyond raw citation counts. Scite classifies citations by intent, specifically whether a citation provides supporting, contrasting, or mentioning evidence, using deep learning on full-text citation contexts. This is a genuinely valuable dimension of citation analysis that addresses the question how is this work being cited? Citation-Constellation addresses a different but complementary question: who is citing this work, and what is their network relationship to the author? Scite tells you whether a citation supports or contradicts a finding; Citation-Constellation tells you whether a citation comes from a co-author, a departmental colleague, or an independent researcher. The two analyses are orthogonal and could, in principle, be combined. A citation from an independent researcher that provides contrasting evidence carries a very different epistemic signal than a supporting citation from a direct co-author. Scite requires institutional subscription for full access; Citation-Constellation is free and open.

### 7.2.4 Proprietary Institutional Analytics

Scopus Author Analyzer (scopus.com) provides author-level metrics including h-index, citation counts, document counts, and co-author lists. It can display self-citation statistics and field-weighted citation impact. However, it does not classify citations by co-authorship distance, institutional affiliation, or venue governance. It treats all non-self citations as equivalent. Access requires a Scopus institutional subscription.

InCites (incites.clarivate.com) is a Clarivate research evaluation platform built on Web of Science data that provides institution-level and author-level citation analytics, including percentile rankings, category-normalized citation impact, and collaboration metrics. InCites can identify international and institutional collaboration rates, but it does not decompose an individual researcher’s incoming citations by the network proximity between citing and cited authors. It operates at the aggregate level (collaboration rates across a portfolio) rather than the per-citation level (classifying each individual citation). Access requires an institutional subscription.

SciVal (scival.com) provides research performance benchmarking and analytics built on Scopus data, including collaboration metrics, topic prominence, and institutional comparison. Like InCites, it offers aggregate collaboration indicators but does not perform per-citation network proximity classification.

### 7.2.5 Open Bibliometric Data Platforms

OpenAlex (openalex.org; [22]) is the open data platform that Citation-Constellation builds upon. OpenAlex provides the raw data (260M+ works, 100M+ authors, 2.8B+ citation links) but does not perform citation network decomposition. OpenAlex can report self-citation counts and provides the building blocks (author IDs, institutional affiliations, citation links) from which Citation-Constellation constructs its multi-layer classification. A researcher using OpenAlex directly would need to write custom code to replicate what Citation-Constellation automates.

Semantic Scholar (semanticscholar.org) from the Allen Institute for AI provides a free academic search engine with author pages, citation graphs, and AI-powered paper recommendations. Its TLDR feature summarizes papers, and its citation context feature shows snippets of how papers are cited. Semantic Scholar does not perform network proximity analysis on a researcher’s citation profile.

Google Scholar (scholar.google.com) provides the most widely used free author profile with citation counts, h-index, and i10-index. It does not distinguish between self-citations and external citations, does not classify citations by network proximity, and provides no audit trail or transparency into how metrics are computed.

Per-Citation Decomposition

Network Scoring

Free & Open

Audit Trail

Tool Primary Function

VOSviewer Field-level network visualization No No Yes (free) No CiteSpace Research front detection & trends No No Yes (free) No Bibliometrix Comprehensive science mapping (R) No No Yes (open-source) No Connected Papers Literature discovery from seed paper No No Freemium No ResearchRabbit Citation/co-authorship exploration No No Yes (free) No Litmaps Citation timeline & monitoring No No Freemium No Scite.ai Citation intent classification Partially (intent, not network) No Subscription No Scopus Author metrics & self-citation Self-citation only No Subscription No InCites Institutional research evaluation No (aggregate only) No Subscription No SciVal Research performance benchmarking No (aggregate only) No Subscription No OpenAlex Open bibliometric data platform No (raw data only) No Yes (open) No Semantic Scholar AI-powered academic search No No Yes (free) No Google Scholar Author profiles & citation counts No No Yes (free) No Citation-Constellation Per-citation network decomposition Yes (multi-layer) Yes (BARON + HEROCON) Yes (free, open-source) Yes (full JSON)

Table 5: Comparison of bibliometric tools.

### 7.3 Bridging the Gap

The conceptual literature and the tool landscape summary (Table 5), taken together, reveal a specific and persistent gap. On one side, decades of research, from Crane’s invisible colleges [10] through Wallace et al.’s network-distance citation analysis [4] to Ioannidis’s generalized self-citation taxonomy [3], have established that citation patterns are shaped by social network proximity, that different network relationships mediate citation in structurally distinct ways, and that treating all citations as equivalent discards information that matters for understanding scholarly influence. This is settled science. The insight is not in dispute.

On the other side, the practical tools available to researchers in 2026 do not act on this insight at the individual level. VOSviewer, CiteSpace, and Bibliometrix visualize network structure beautifully, but at the field level, not the individual profile level. Scopus, InCites, and SciVal provide author-level metrics, but collapse all non-self citations into a single undifferentiated count. Scite.ai classifies individual citations, but by rhetorical intent (supporting, contrasting, mentioning), not by social network proximity. OpenAlex provides the raw data from which a network decomposition could be built, but building it requires custom engineering that few individual researchers can undertake. Google Scholar reports numbers without any decomposition at all.

Consequently, a researcher in 2026 who wants to understand the network composition of their own citation profile possesses no tool to answer that question. Such a researcher might want to know what fraction of their citations come from co-authors, from institutional colleagues, from editorial connections, or from genuinely independent researchers, yet no existing instrument provides this decomposition.

The knowledge exists in the literature. The data exists in OpenAlex. The computation is not prohibitively complex. However, the instrument does not exist.

Citation-Constellation is that instrument. It takes the conceptual framework established by Wallace et al. [4], Ioannidis [3], and others, operationalizes it through a multi-layer detection architecture with ORCID-validated identity resolution and temporal affiliation matching, packages it as both a command-line tool and a no-code web application accessible to any researcher with a browser, and documents every classification decision in a contestable audit trail. It does not invent the insight. Rather, it builds the tool that the insight has been waiting for. Furthermore, through the seamless integration of large language models and AI agents, it augments this robust architecture, bridging the gap between rigorous network analysis and universally accessible exploration.

I turn now to the implications, appropriate use cases, and structural tensions that Citation-Constellation and its BARON and HEROCON scores might create.

## 8 Discussion

### 8.1 Framing: Structure, Not Quality

BARON and HEROCON measure citation network structure, where in the social graph citations originate, not research quality, impact, or integrity. This distinction is the central design principle. A low BARON score might indicate a productive lab leader whose group naturally builds on their foundational contributions [14], a small-field researcher in a 50-person community where nearly everyone is a co-author’s co-author [12], or an insular practice that warrants self-examination. A high BARON score might indicate a cross-disciplinary thinker [68], an early-career researcher who has not yet built a collaborative network, or a lone genius working in isolation. The tool cannot distinguish these cases.

This reframing is not modesty. It is epistemic honesty about what the numbers can and cannot say. A BARON score of 40% reports that 60% of a researcher’s citations come from within their detected network. Whether that reflects healthy collaboration, strategic citation behavior [56], or simply the natural dynamics of a small field [10] requires qualitative judgment that no metric can provide.

### 8.2 Alignment with Responsible Research Assessment

DORA [5] calls for moving beyond single-number metrics. The Leiden Manifesto [2] requires that quantitative evaluation support qualitative judgment. De Rijcke et al. [39] documented how indicator use distorts research behavior, directly relevant to any new bibliometric tool, including this one.

I resolve the tension between introducing new quantitative metrics and the responsible assessment movement by positioning BARON and HEROCON as supporting evidence for narrative evaluation, not standalone metrics. The key distinction is between metrics designed to rank (h-index, impact factor) and metrics designed to describe (BARON,

HEROCON). A ranking metric invites competition; a descriptive metric invites reflection. The Leiden Manifesto’s first principle is satisfied when a metric provides structural context enriching human judgment rather than replacing it.

The audit trail makes this alignment concrete. A committee evaluating a researcher’s portfolio could examine the audit file to understand why a BARON score takes a particular value, whether from intensive collaboration, a small field, or editorial roles. The number alone is silent; the audit trail speaks. This approach resonates with Rafols et al.’s [69] argument that responsible indicators should make complexity visible rather than hiding it behind a single number.

### 8.3 The Goodhart Vulnerability

If BARON/HEROCON were adopted for evaluation, researchers would optimize for them, a direct manifestation of Goodhart’s Law [70, 61]. The strategies are predictable: soliciting citations from strangers, avoiding citation of relevant co-author work, publishing in unfamiliar venues. Edwards and Roy [58] documented similar perverse incentives. Smaldino and McElreath [59] modeled the evolutionary dynamics.

A researcher could inflate BARON by (a) publishing under multiple name variants to split their co-author graph [43], (b) rotating institutional affiliations, (c) establishing reciprocal citation arrangements outside their detected network [46], or (d) strategically managing ORCID records. Similar strategies have been documented for h-index manipulation [56, 60].

My mitigation: prominent disclaimers in every output, data quality reporting that makes scores visibly approximate, and positioning for self-reflection and policy research. I acknowledge these guardrails are imperfect; the history of bibliometric gaming suggests that sufficiently motivated actors will find ways to optimize any published metric [61].

### 8.4 The Case for HEROCON as Experimental

I do not have empirical evidence for the specific HEROCON weight values. As discussed in Section 6.1.1, these weights encode a formal hypothesis about the relative strength of different network pathways. The ordering is consistent with findings that co-authorship represents a stronger social tie than mere institutional proximity [13, 14], and that transitive network connections carry meaningful but attenuated social influence [71, 4]. However, the cardinal distances between weights are not grounded in data.

Preliminary informal testing suggests that HEROCON scores are relatively stable under small weight changes for researchers with diverse citation profiles. However, scores can shift substantially for researchers whose citations are concentrated in a single category. This echoes a general challenge in composite indicators [72, 73, 74].

BARON, by contrast, is binary and requires no weight calibration. It is the methodologically robust contribution. HEROCON is a promising extension whose value depends on future empirical work, but even in its current form, the gap’s existence (if not its precise magnitude) is robust to weight perturbation.

##### 8.5 Use Cases and Appropriate DeploymentI identify three appropriate use cases, in order of decreasing confidence:

- 1. Science policy research. Analyzing citation network structure at the field level is the safest use case. Aggregate patterns are more robust than individual scores [2], and field-level analyses can reveal disciplinary norms [4] informing policy on evaluation practices and collaboration incentives. Comparing BARON distributions across career stages, institution types, or geographic regions could provide evidence for structural inequalities [57, 17].
- 2. Self-reflection. A researcher examining their own citation profile. The audit trail makes this actionable: inspect which co-authors cite most, whether institutional peers contribute substantially, and how external reach evolves over time. This aligns with calls for researcher self-awareness about citation practices [53, 3].
- 3. Contextualizing evaluation. Providing structural context alongside other evaluation evidence, consistent with DORA [5] and the Leiden Manifesto [2]. The structural context helps evaluators ask better questions; it does not answer them. I explicitly discourage use in hiring, promotion, or funding decisions as a standalone criterion.


## 9 Limitations

Coverage bias. OpenAlex is English-heavy and recent-heavy [75, 23]. Researchers in non-English-language traditions or with older publication records may have systematically lower coverage.

Temporal resolution limits. Affiliation data is derived from publication-time institutional records, not employment records. A researcher changing institutions mid-year may have citations misclassified [76, 77, 78].

The small-field problem. In a 50-person community, nearly everyone may be a co-author’s co-author at depth 2 [12]. BARON would classify most citations as in-group, reflecting field size rather than citation practice. I plan to address this through field normalization (see Section 10.4).

ORCID selection bias. Researchers with complete ORCID records [19] tend to be affiliated with well-resourced institutions [79]. Consequently, my ORCID-based validation provides better protection for the researchers who perhaps need it least.

Author disambiguation remains imperfect. Despite ORCID cross-validation, researchers without ORCID records cannot benefit.

HEROCON weights are not empirically calibrated. Diverse profiles are robust to perturbation; concentrated profiles are sensitive (see Section 6.1.1). Until calibration is completed, HEROCON should be interpreted as indicative rather than definitive.

UNKNOWN creates a conditioned sample. If UNKNOWN citations are systematically different from classifiable ones, from developing countries with poor metadata [80, 75], older publications, or certain disciplines, then computed scores reflect a biased subset. I plan to address this through sensitivity analysis (see Section 10.1).

Department-level matching is noisy. ROR lacks department-level identifiers for most institutions [27].

Venue governance database coverage. Phase 4’s incremental database means first-time analyses in underserved fields have limited coverage. Coverage improves with use, following a pattern common in incrementally constructed knowledge bases where initial sparsity gives way to density as more queries contribute data [81, 82].

LLM extraction accuracy. Phase 4 relies on a locally deployed language model for structured extraction from heterogeneous HTML pages. Recent work has demonstrated that LLMs can perform structured information extraction from web pages with competitive accuracy, including zero-shot extraction without task-specific training [83, 84], but errors remain inevitable for non-standard page structures, non-English content, or dynamically rendered editorial boards.

The tool detects correlation, not causation. A citation classified as DIRECT_COAUTHOR may represent a genuinely motivated citation, a co-author who cites the work because it is the best available reference, not because of social proximity. The classification identifies structural potential for network-mediated citation, not actuality. This distinction between structural position and actual influence is well-established in social network analysis [85, 86].

The lone genius problem. The framework implicitly assumes that collaboration is the norm, an assumption that holds for most contemporary science [87] but not universally. A truly independent researcher who works alone would have a very high BARON score for reasons opposite to those intended. The tool cannot distinguish this from massive external reach. This reinforces that it is a structural, not a quality, metric.

No empirical validation against ground truth. I have not yet demonstrated that scores correspond to independently verifiable properties of citation behavior. Validation would require showing that scores differ between collaborative and independent researchers, that ORCID validation changes scores for common names, or that structural classifications align with self-reported citation motivations. The extensive literature on citing behavior [86, 88] demonstrates that researchers cite for diverse scientific and non-scientific reasons, suggesting that structural classifications will capture meaningful but incomplete signal about citation motivation.

## 10 Future Work (Figure 15)

![image 19](Where Do Your Citations Come From Citation-Constellation A Free Open-Source No-C_images/imageFile19.png)

- Figure 15: Development roadmap. Phase 4 introduces venue governance detection via a three-tool ecosystem (Pulsar, Astrolabe, Constellation). Phase 5 adds field normalization and comparative analytics. Phase 6 focuses on empirical validation and multi-source data fusion.


### 10.1 Sensitivity Analysis (Priority)

I plan to systematically examine how scores respond to perturbation along four axes: (a) HEROCON weight variation (±0.1, ±0.2) to map the sensitivity surface; (b) UNKNOWN imputation strategy (all-EXTERNAL, all-in-group, proportional allocation); (c) co-author graph depth (1 to 3); and (d) temporal decay rate (half-lives of 3.5, 7, and 14 years). For each axis, I will report score distributions across researchers from diverse fields and career stages.

### 10.2 Empirical Weight Calibration

I envision three approaches: survey-based citation motivation studies mapping self-reported motivations onto structural classifications; field-specific weight optimization using known collaborative versus independent profiles; and information-theoretic approaches maximizing discriminative power of the HEROCON–BARON gap. Calibrated weights would be published as field-specific weight files alongside the tool.

### 10.3 Cross-Validation with Citation Motivation Studies

Cross-referencing structural classifications against ground-truth data on citation motivation. I note that citation motivation is notoriously difficult to study; the goal is to establish whether the structural signal is informative, not whether it is deterministic.

### 10.4 Field-Normalized Percentile Scoring (Phase 5)

BARON 70% in theoretical physics means something different than 70% in biomedical research. Phase 5 will compute percentile ranks against peer cohorts, enabling statements like "BARON 72% (65th percentile in computational biology)."

### 10.5 Confidence Intervals

Bootstrap confidence intervals reflecting sample size and metadata quality. A well-cited researcher with BARON 72% ± 4% presents a very different picture from an early-career researcher with BARON 72% ± 27%.

### 10.6 Temporal Career Trajectory Analysis

Windowed analysis (rolling 5-year BARON) to answer: Did external reach grow after changing institutions? Did BARON decline after establishing a large lab?

### 10.7 Multi-Source Data Fusion

Cross-referencing OpenAlex with Semantic Scholar, CrossRef, and DBLP [75] to improve coverage and assess score sensitivity to data source choice.

### 10.8 Collaborative and Community Extensions

Discipline-specific weight calibrations from domain experts, integration with institutional CRIS systems, support for non-Latin name scripts, and a shared venue governance database growing through distributed contribution.

## 11 Conclusion

In this paper, I have introduced BARON and HEROCON, two complementary bibliometric scores that decompose a researcher’s citation profile into a structured map of self-citation, co-authorship, institutional proximity, venue governance, and genuine external reach. Where conventional metrics collapse all citations into a single number, these scores reveal where in the social graph citations actually originate.

The contributions are both conceptual and architectural. Conceptually, the dual-score framework offers a new diagnostic lens. BARON’s strict binary classification anchors the boundary of a citation profile by counting only fully external citations. HEROCON’s graduated weighting maps the full constellation, assigning partial credit based on relationship proximity. The gap between the two serves as a readable diagnostic of inner-circle dependence, a quantity that, to my knowledge, no existing bibliometric tool reports.

Architecturally, I contribute an open-source, multi-layer detection system that combines self-citation analysis, coauthorship graph traversal with temporal decay, temporal affiliation matching via the Research Organization Registry, and AI-driven venue governance extraction into a single pipeline. The venue governance phase demonstrates a reusable pattern for AI-agent-driven bibliometric infrastructure. A locally deployed large language model performs structured extraction from heterogeneous web pages, an entity resolution layer matches extracted names against open bibliometric databases, and a persistent database captures the results, all running on commodity academic computing resources. This pattern is applicable well beyond venue governance and offers a template for automated extraction of any structured scholarly metadata that exists on the web but is not yet systematically captured.

Several engineering choices address persistent practical challenges that have historically prevented theoretical insights about network-mediated citation from becoming usable tools. ORCID-based identity validation mitigates author disambiguation error. The UNKNOWN classification honestly reports citations with insufficient metadata rather than silently inflating scores. Comprehensive audit transparency documents every classification decision with a humanreadable rationale. And accessibility through both a command-line interface and a freely available no-code web application on SciLifeLab Serve ensures that citation profile analysis is not gated by technical skill, institutional subscription, or cost.

I am deliberate about what these scores are not. They are not quality indicators. They are not integrity detectors. They are not suitable for hiring, promotion, or funding decisions. They describe where in the social graph citations originate, nothing more, nothing less.

BARON is the methodologically robust contribution: binary, requiring no weight calibration, and directly interpretable. HEROCON is an experimental extension whose graduated weights encode testable hypotheses about the relative strength of different network pathways in mediating citation behavior. I have been transparent throughout this paper about what is established and what remains unvalidated.

If there is a single contribution I would ask readers to remember, it is the audit trail. Every classification decision is documented. Every uncertainty is flagged. Every assumption is exposed to scrutiny. In a field where metrics are too often treated as authoritative pronouncements, I offer a tool that shows its work and invites others to check it.

The tool is open-source and available. I welcome empirical evaluations, cross-field analyses, and community contributions toward grounding these structural diagnostics in evidence.

#### pulsar → astrolabe → constellation

the signal the instrument the map

###### Component Purpose Link

Citation-Constellation BARON & HEROCON scoring No-Code Tool | Code Citation-Pulsar-Helm LLM inference on Kubernetes Code Citation-Astrolabe Venue governance database Code

The Citation-Cosmograph ecosystem on GitHub.

## Acknowledgements

This work would not exist without the infrastructure and generosity of others.

I am profoundly grateful to SciLifeLab Data Centre and the SciLifeLab Serve platform for providing the computational home where Citation-Constellation lives and breathes. Serve’s commitment to hosting open research tools, freely, without barriers, for anyone, embodies exactly the democratic ethos this project aspires to. That a researcher anywhere in the world can navigate to a URL and decompose their citation profile without installing software, creating an account, or paying a fee is not my achievement alone; it is Serve’s architecture that makes that sentence true.

I owe a particular and unusual debt to Claude (Anthropic). Citation-Constellation is, in the most literal sense, a project born in the quiet night hours after my daughter falls asleep, a pastime pursued after bedtime stories and lullabies. The idea of decomposing citation profiles by network proximity had lived in my head for some time, but the distance between an idea and an implementation is vast, and the hours between a child’s sleep and one’s own are few. Claude bridged that distance.

Finally, I thank my daughter, whose nightly surrender to sleep is the starting gun for everything I build in the dark. The constellations in this paper are named for heroes and boundary guardians, but the brightest star in my sky is

considerably smaller. I hope that one day she will read this paper, understand very little, care even less, and still say, with the generous conviction that only a daughter can muster, "This is really cool! Abbu."

## A Letter to the Reader

If you have read this far, you have already seen what this tool does and how to use it. You may wonder why it exists, or why I built it alone, in the hours between my daughter’s bedtime and my own.

It is now two years since my PhD. This paper represents my last formal scholarly work, not because I am leaving science, but because I want to leave something for science that is not entangled with the incentive structures I have spent these pages critiquing. I built Citation-Constellation as a gift. It is not a stepping stone to tenure, not a citation magnet, and not a product. It is infrastructure that I needed and could not find, so I built it for us.

The idea came from a specific frustration: watching brilliant colleagues at under-resourced institutions struggle to demonstrate their impact to committees who only saw raw citation counts. Watching early-career researchers in small fields penalized for low h-indices that reflected their community size, not their influence. Watching myself wonder, genuinely, whether my own citations came from intellectual reach or from the natural amplification of my immediate network. The tools to answer that question existed in theory, locked behind paywalls and technical barriers. I wanted to put them in a web browser, for free, with no registration required, because curiosity about your own scholarly footprint should not require an institutional subscription.

I am a new father, and I found that the only hours available for side projects are those quiet moments after lullabies. My daughter provided the structure: her bedtime ritual became the starting gun for every coding session. This tool carries the DNA of those nights. Imperfect, earnest, built under constraints, but offered with generosity.

I hope you use it to understand yourself better, not to rank yourself against others. I hope you use it to advocate for yourself in evaluation contexts, or to check your own biases in citation practices, or simply to satisfy a curiosity about the invisible architecture of your intellectual community. I hope you find the gap between BARON and HEROCON not as a judgment but as a map, showing where you stand in relation to the communities that sustain and cite you.

If this tool helps one researcher at a teaching-intensive college demonstrate their external reach to a promotion committee; if it helps one graduate student realize their citations are more diverse than they feared; if it helps one field recognize that their "low" citation counts reflect close collaboration rather than low impact, then those nights were worth it.

This is my gift to the scholarly community that sustained me. Use it kindly.

Mahbub Ul Alam Stockholm, Sweden

28 March, 2026

## References

- [1] Ludo Waltman. A review of the literature on citation impact indicators. Journal of Informetrics, 10(2):365–391,

2016. doi:10.1016/j.joi.2016.02.007.

- [2] Diana Hicks, Paul Wouters, Ludo Waltman, Sarah de Rijcke, and Ismael Rafols. Bibliometrics: The Leiden Manifesto for research metrics. Nature, 520(7548):429–431, 2015. doi:10.1038/520429a.
- [3] John P. A. Ioannidis. A generalized view of self-citation: Direct, co-author, collaborative, and coercive induced selfcitation. Journal of Psychosomatic Research, 78(1):7–11, 2015. doi:10.1016/j.jpsychores.2014.11.008.
- [4] Matthew L. Wallace, Vincent Larivière, and Yves Gingras. A small world of citations? The influence of collaboration networks on citation practices. PLoS ONE, 7(3):e33339, 2012. doi:10.1371/journal.pone. 0033339.
- [5] DORA. San francisco declaration on research assessment. Disease Models & Mechanisms, 6:2–3, 2013. doi:10.1242/dmm.012955.
- [6] Jorge E. Hirsch. An index to quantify an individual’s scientific research output. Proceedings of the National Academy of Sciences, 102(46):16569–16572, 2005. doi:10.1073/pnas.0507655102.
- [7] Per O. Seglen. Why the impact factor of journals should not be used for evaluating research. BMJ, 314(7079):497,


#### 1997. doi:10.1136/bmj.314.7079.497.

- [8] Lutz Bornmann and Hans-Dieter Daniel. Does the h-index for ranking of scientists really work? Scientometrics, 65(3):391–392, 2005. doi:10.1007/s11192-005-0281-4.
- [9] Rodrigo Costas and María Bordons. The h-index: Advantages, limitations and its relation with other bibliometric indicators at the micro level. Journal of Informetrics, 1(3):193–203, 2007. doi:10.1016/j.joi.2007.02.001.
- [10] Diana Crane. Invisible Colleges: Diffusion of Knowledge in Scientific Communities. University of Chicago Press, Chicago, 1972. URL: https://archive.org/details/invisiblecollege0000cran.
- [11] Alesia Zuccala. Modeling the invisible college. Journal of the American Society for Information Science and Technology, 57(2):152–168, 2006. doi:10.1002/asi.20256.
- [12] Mark E. J. Newman. The structure of scientific collaboration networks. Proceedings of the National Academy of Sciences, 98(2):404–409, 2001. doi:10.1073/pnas.98.2.404.
- [13] Mark E. J. Newman. Coauthorship networks and patterns of scientific collaboration. Proceedings of the National Academy of Sciences, 101(suppl_1):5200–5205, 2004. doi:10.1073/pnas.0307545100.
- [14] Wolfgang Glänzel and András Schubert. Analysing scientific networks through co-authorship. In Handbook of Quantitative Science and Technology Research, pages 257–276. Springer, 2004. doi:10.1007/ 1-4020-2755-9_12.
- [15] James Moody. The structure of a social science collaboration network: Disciplinary cohesion from 1963 to 1999. American Sociological Review, 69(2):213–238, 2004. doi:10.1177/000312240406900204.
- [16] Caroline S. Wagner and Loet Leydesdorff. Network structure, self-organization, and the growth of international collaboration in science. Research Policy, 34(10):1608–1618, 2005. doi:10.1016/j.respol.2005.08.002.
- [17] Vincent Larivière and Yves Gingras. The impact factor’s Matthew Effect: A natural experiment in bibliometrics. Journal of the American Society for Information Science and Technology, 61(2):424–427, 2010. doi:10.1002/ asi.21232.
- [18] Raj Kumar Pan, Kimmo Kaski, and Santo Fortunato. World citation and collaboration networks: uncovering the role of geography in science. Scientific Reports, 2:902, 2012. doi:10.1038/srep00902.
- [19] Laurel L. Haak, Martin Fenner, Laura Paglione, Ed Pentz, and Howard Ratner. ORCID: a system to uniquely identify researchers. Learned Publishing, 25(4):259–264, 2012. doi:10.1087/20120404.
- [20] Lorna Wildgaard, Jesper W. Schneider, and Birger Larsen. A review of the characteristics of 108 author-level bibliometric indicators. Scientometrics, 101(1):125–158, 2014. doi:10.1007/s11192-014-1423-3.
- [21] Darrel C. Ince, Leslie Hatton, and John Graham-Cumming. The case for open computer programs. Nature, 482(7386):485–488, 2012. doi:10.1038/nature10836.
- [22] Jason Priem, Heather Piwowar, and Richard Orr. OpenAlex: A fully-open index of scholarly works, authors, venues, institutions, and concepts. arXiv preprint arXiv:2205.01833, 2022. doi:10.48550/arXiv.2205.01833.
- [23] Alberto Martín-Martín, Mike Thelwall, Enrique Orduna-Malea, and Emilio Delgado López-Cózar. Google Scholar, Microsoft Academic, Scopus, Dimensions, Web of Science, and OpenCitations’ COCI: a multidisciplinary comparison of coverage via citations. Scientometrics, 126(1):871–906, 2021. doi:10.1007/s11192-020-03690-4.
- [24] Martijn Visser, Nees Jan van Eck, and Ludo Waltman. Large-scale comparison of bibliographic data sources: Scopus, Web of Science, Dimensions, Crossref, and Microsoft Academic. Quantitative Science Studies, 2(1):20– 41, 2021. doi:10.1162/qss_a_00112.
- [25] Jonathan P. Tennant. Web of science and scopus are not global databases of knowledge. European Science Editing, 46:e51987, 2020. doi:10.3897/ese.2020.e51987.
- [26] Márton Demeter. Academic Knowledge Production and the Global South: Questioning Inequality and Underrepresentation. Springer, 2020. doi:10.1007/978-3-030-52701-3.
- [27] Rachael Lammey. Solutions for identification problems: a look at the Research Organization Registry. Science Editing, 7(1):65–69, 2020. doi:10.6087/kcse.192.
- [28] UNESCO. UNESCO Recommendation on Open Science. United Nations Educational, Scientific and Cultural Organization, Paris, 2021. doi:10.54677/MNMH8546.
- [29] Silvio Peroni and David Shotton. OpenCitations, an infrastructure organization for open scholarship. Quantitative Science Studies, 1(1):428–444, 2020. doi:10.1162/qss_a_00023.
- [30] Ludo Waltman and Nees Jan van Eck. Openness of research information – democratising the use of scientometrics. Lecture at the Swiss Year of Scientometrics (SYoS), ETH Zurich, 2024. doi:10.5281/zenodo.11652015.


- [31] Bianca Kramer, Cameron Neylon, and Ludo Waltman. Barcelona declaration on open research information. https://barcelona-declaration.org/, 2024. URL: https://barcelona-declaration.org/.
- [32] Santo Fortunato, Carl T. Bergstrom, Katy Börner, James A. Evans, Dirk Helbing, Staša Milojevi´c, Alexander M. Petersen, Filippo Radicchi, Roberta Sinatra, Brian Uzzi, Alessandro Vespignani, Ludo Waltman, Dashun Wang, and Albert-László Barabási. Science of science. Science, 359(6379):eaao0185, 2018. doi:10.1126/science. aao0185.
- [33] Chun-Kai Huang, Cameron Neylon, Chloe Brookes-Kenworthy, Richard Hosking, Lucy Montgomery, Katie Wilson, and Alkim Ozaygen. Comparison of bibliographic data sources: Implications for the robustness of university rankings. Quantitative Science Studies, 1(2):445–478, 2020. doi:10.1162/qss_a_00031.
- [34] John P. A. Ioannidis, Jeroen Baas, Richard Klavans, and Kevin W. Boyack. A standardized citation metrics author database annotated for scientific field. PLoS Biology, 17(8):e3000384, 2019. doi:10.1371/journal.pbio. 3000384.
- [35] Alexander M. Petersen, Massimo Riccaboni, H. Eugene Stanley, and Fabio Pammolli. Persistence and uncertainty in the academic career. Proceedings of the National Academy of Sciences, 109(14):5213–5218, 2012. doi: 10.1073/pnas.1121429109.
- [36] Katy Börner, Jeegar T. Maru, and Robert L. Goldstone. The simultaneous evolution of author and paper networks. Proceedings of the National Academy of Sciences, 101(suppl_1):5266–5273, 2004. doi:10.1073/ pnas.0307625100.
- [37] Yian Yin and Dashun Wang. The time dimension of science: Connecting the past to the future. Journal of Informetrics, 11(2):608–621, 2017. doi:10.1016/j.joi.2017.04.002.
- [38] James Wilsdon, Liz Allen, Eleonora Belfiore, Philip Campbell, Stephen Curry, Steven Hill, Richard Jones, Roger Kain, Simon Kerridge, Mike Thelwall, Jane Tinkler, Ian Viney, Paul Wouters, Jude Hill, and Ben Johnson. The metric tide: Report of the independent review of the role of metrics in research assessment and management. Technical report, HEFCE, London, 2015. doi:10.13140/RG.2.1.4929.1363.
- [39] Sarah de Rijcke, Paul F. Wouters, Alex D. Rushforth, Thomas P. Franssen, and Björn Hammarfelt. Evaluation practices and effects of indicator use—a literature review. Research Evaluation, 25(2):161–169, 2016. doi: 10.1093/reseval/rvv038.
- [40] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. LLaMA: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971, 2023. doi:10.48550/arXiv.2302.13971.
- [41] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, et al. Qwen technical report. arXiv preprint arXiv:2309.16609, 2023. doi:10.48550/arXiv.2309.16609.
- [42] Georgi Gerganov. llama.cpp: Port of Facebook’s LLaMA model in C/C++. https://github.com/ggml-org/ llama.cpp, 2023. URL: https://github.com/ggml-org/llama.cpp.
- [43] Anderson A. Ferreira, Marcos André Gonçalves, and Alberto H. F. Laender. A brief survey of automatic methods for author name disambiguation. ACM SIGMOD Record, 41(2):15–26, 2012. doi:10.1145/2350036.2350040.
- [44] Elba Mauleón, Laura Hillán, Luz Moreno, Isabel Gómez, and María Bordons. Assessing gender balance among journal authors and editorial board members. Scientometrics, 95(1):87–114, 2013. doi:10.1007/ s11192-012-0824-4.
- [45] Eleanor R. Palser, Maia Lazerwitz, and Aikaterini Fotopoulou. Gender and geographical disparity in editorial boards of journals in psychology and neuroscience. Nature Neuroscience, 25(3):272–279, 2022. doi:10.1038/ s41593-022-01012-w.
- [46] Alberto Baccini, Giuseppe De Nicolao, and Eugenio Petrovich. Citation gaming induced by bibliometric evaluation: A country-level comparative analysis. PLoS ONE, 14(9):e0221212, 2019. doi:10.1371/journal. pone.0221212.
- [47] Belén Álvarez-Bornstein, Fernanda Morillo, and María Bordons. Funding acknowledgments in the Web of Science: completeness and accuracy of collected data. Scientometrics, 112(3):1793–1812, 2017. doi:10.1007/ s11192-017-2453-4.
- [48] Ginny Hendricks, Dominika Tkaczyk, Jennifer Lin, and Patricia Feeney. Crossref: The sustainable source of community-owned scholarly metadata. Quantitative Science Studies, 1(1):414–427, 2020. doi:10.1162/qss_ a_00022.
- [49] Ludo Waltman and Nees Jan van Eck. The inconsistency of the h-index. Journal of the American Society for Information Science and Technology, 63(2):406–415, 2012. doi:10.1002/asi.21678.


- [50] Leo Egghe. Theory and practise of the g-index. Scientometrics, 69(1):131–152, 2006. doi:10.1007/ s11192-006-0144-7.
- [51] Ludo Waltman, Nees Jan van Eck, Thed N. van Leeuwen, Martijn S. Visser, and Anthony F. J. van Raan. Towards a new crown indicator: Some theoretical considerations. Journal of Informetrics, 5(1):37–47, 2011. doi:10.1016/j.joi.2010.08.001.
- [52] Loet Leydesdorff and Lutz Bornmann. How fractional counting of citations affects the impact factor: Normalization in terms of differences in citation potentials among fields of science. Journal of the American Society for Information Science and Technology, 62(2):217–229, 2011. doi:10.1002/asi.21450.
- [53] Dag W. Aksnes. A macro study of self-citation. Scientometrics, 56(2):235–246, 2003. doi:10.1023/A: 1021919228368.
- [54] Ameni Kacem, Justin W. Flatt, and Philipp Mayr. Tracking self-citations in academic publishing. Scientometrics, 123(2):1157–1165, 2020. doi:10.1007/s11192-020-03413-9.
- [55] James H. Fowler and Dag W. Aksnes. Does self-citation pay? Scientometrics, 72(3):427–437, 2007. doi: 10.1007/s11192-007-1777-2.
- [56] Marco Seeber, Mattia Cattaneo, Michele Meoli, and Paolo Malighetti. Self-citations as strategic response to the use of metrics for career decisions. Research Policy, 48(2):478–491, 2019. doi:10.1016/j.respol.2017.12.004.
- [57] Bas Hofstra, Vivek V. Kulkarni, Sebastian Munoz-Najar Galvez, Bryan He, Dan Jurafsky, and Daniel A. McFarland. The diversity–innovation paradox in science. Proceedings of the National Academy of Sciences, 117(17):9284– 9291, 2020. doi:10.1073/pnas.1915378117.
- [58] Marc A. Edwards and Siddhartha Roy. Academic research in the 21st century: Maintaining scientific integrity in a climate of perverse incentives and hypercompetition. Environmental Engineering Science, 34(1):51–61, 2017. doi:10.1089/ees.2016.0223.
- [59] Paul E. Smaldino and Richard McElreath. The natural selection of bad science. Royal Society Open Science, 3(9):160384, 2016. doi:10.1098/rsos.160384.
- [60] Lokman I. Meho. Gaming the metrics: bibliometric anomalies in global university rankings and the research integrity risk index (RI2). Scientometrics, 130:6683–6726, 2025. doi:10.1007/s11192-025-05480-2.
- [61] Michael Fire and Carlos Guestrin. Over-optimization of academic publishing metrics: observing Goodhart’s Law in action. GigaScience, 8(6):giz053, 2019. doi:10.1093/gigascience/giz053.
- [62] Christian Schulz, Amin Mazloumian, Alexander M. Petersen, Orion Penner, and Dirk Helbing. Exploiting citation networks for large-scale author name disambiguation. EPJ Data Science, 3(1):11, 2014. doi:10.1140/epjds/ s13688-014-0011-3.
- [63] Björn Brembs. Prestigious science journals struggle to reach even average reliability. Frontiers in Human Neuroscience, 12:37, 2018. doi:10.3389/fnhum.2018.00037.
- [64] Nees Jan van Eck and Ludo Waltman. Software survey: VOSviewer, a computer program for bibliometric mapping. Scientometrics, 84(2):523–538, 2010. doi:10.1007/s11192-009-0146-3.
- [65] Chaomei Chen. CiteSpace II: Detecting and visualizing emerging trends and transient patterns in scientific literature. Journal of the American Society for Information Science and Technology, 57(3):359–377, 2006. doi:10.1002/asi.20317.
- [66] Massimo Aria and Corrado Cuccurullo. bibliometrix: An R-tool for comprehensive science mapping analysis. Journal of Informetrics, 11(4):959–975, 2017. doi:10.1016/j.joi.2017.08.007.
- [67] Josh M. Nicholson, Milo Mordaunt, Patrice Lopez, Ashish Uppala, Domenic Rosati, Nuno P. Rodrigues, Peter Grabber, Daniel Dunne, Kareem Moustafa, Anna Kerber, et al. scite: A smart citation index that displays the context of citations and classifies their intent using deep learning. Quantitative Science Studies, 2(3):882–898,

2021. doi:10.1162/qss_a_00146.

- [68] Ismael Rafols and Martin Meyer. Diversity and network coherence as indicators of interdisciplinarity: case studies in bionanoscience. Scientometrics, 82(2):263–287, 2010. doi:10.1007/s11192-009-0041-y.
- [69] Ismael Rafols, Loet Leydesdorff, Alice O’Hare, Paul Nightingale, and Andy Stirling. How journal rankings can suppress interdisciplinary research: A comparison between innovation studies and business & management. Research Policy, 41(7):1262–1282, 2012. doi:10.1016/j.respol.2012.03.015.
- [70] C. A. E. Goodhart. Problems of Monetary Management: The UK Experience, pages 91–121. Macmillan Education UK, London, 1984. doi:10.1007/978-1-349-17295-5_4.


- [71] Mark S. Granovetter. The strength of weak ties. American Journal of Sociology, 78(6):1360–1380, 1973. doi:10.1086/225469.
- [72] L. Cherchye, W. Moesen, N. Rogge, T. Van Puyenbroeck, M. Saisana, A. Saltelli, R. Liska, and S. Tarantola. Creating composite indicators with DEA and robustness analysis: The case of the technology achievement index. SSRN Electronic Journal, 2006. doi:10.2139/ssrn.888461.
- [73] Salvatore Greco, Alessio Ishizaka, Menelaos Tasiou, and Gianpiero Torrisi. On the methodological framework of composite indices: A review of the issues of weighting, aggregation, and robustness. Social Indicators Research, 141:61–94, 2018. doi:10.1007/s11205-017-1832-9.
- [74] OECD and Joint Research Centre–European Commission. Handbook on Constructing Composite Indicators: Methodology and User Guide. OECD Publishing, Paris, 2008. doi:10.1787/9789264043466-en.
- [75] Mengxue Zheng, Lili Miao, Yi Bu, and Vincent Larivière. Understanding discrepancies in the coverage of OpenAlex: The case of China. Journal of the Association for Information Science and Technology, 76(11):1591– 1601, 2025. doi:10.1002/asi.70013.
- [76] Paul Donner, Christine Rimmert, and Nees Jan van Eck. Comparing institutional-level bibliometric research performance indicator values based on different affiliation disambiguation systems. Quantitative Science Studies, 1(1):150–170, 2020. doi:10.1162/qss_a_00013.
- [77] Valeria Aman. Does the Scopus author ID suffice to track scientific international mobility? A case study based on Leibniz laureates. Scientometrics, 117(2):705–720, 2018. doi:10.1007/s11192-018-2895-3.
- [78] Nicolás Robinson-Garcia, Cassidy R. Sugimoto, Dakota Murray, Alfredo Yegros-Yegros, Vincent Larivière, and Rodrigo Costas. The many faces of mobility: Using bibliometric data to measure the movement of scientists. Journal of Informetrics, 13(1):50–63, 2019. doi:10.1016/j.joi.2018.11.002.
- [79] Simon J. Porter. Measuring research information citizenship across ORCID practice. Frontiers in Research Metrics and Analytics, 7, 2022. doi:10.3389/frma.2022.779097.
- [80] Ismael Rafols, Tommaso Ciarli, and Diego Chavarro. Under-reporting research relevant to local needs in the global south. database biases in the representation of knowledge on rice. In Proceedings of the 15th International Society of Scientometrics and Informetrics Conference (ISSI 2015), Istanbul, Turkey, 2015. doi:10.31235/osf. io/3kf9d.
- [81] Jaeho Shin, Sen Wu, Feiran Wang, Christopher De Sa, Ce Zhang, and Christopher Ré. Incremental knowledge base construction using DeepDive. In Proceedings of the VLDB Endowment, volume 8, pages 1310–1321, 2015. doi:10.14778/2809974.2809991.
- [82] Marvin Hofer, Daniel Obraczka, Alieh Saeedi, Hanna Köpcke, and Erhard Rahm. Construction of knowledge graphs: State and challenges. arXiv preprint arXiv:2302.11509, 2023. doi:10.48550/arXiv.2302.11509.
- [83] Arvind Arasu and Hector Garcia-Molina. Extracting structured data from web pages. In Proceedings of the 2003 ACM SIGMOD International Conference on Management of Data, 2003. doi:10.1145/872757.872799.
- [84] Alexander Brinkmann, Nick Baumann, and Christian Bizer. Using LLMs for the extraction and normalization of product attribute values. In Advances in Databases and Information Systems (ADBIS), 2024. doi:10.1007/ 978-3-031-70626-4_15.
- [85] Stephen P. Borgatti. Centrality and network flow. Social Networks, 27(1):55–71, 2005. doi:10.1016/j.socnet. 2004.11.008.
- [86] Lutz Bornmann and Hans-Dieter Daniel. What do citation counts measure? A review of studies on citing behavior. Journal of Documentation, 64(1):45–80, 2008. doi:10.1108/00220410810844150.
- [87] Stefan Wuchty, Benjamin F. Jones, and Brian Uzzi. The increasing dominance of teams in production of knowledge. Science, 316(5827):1036–1039, 2007. doi:10.1126/science.1136099.
- [88] Iman Tahamtan and Lutz Bornmann. What do citation counts measure? An updated review of studies on citations in scientific documents published between 2006 and 2018. Scientometrics, 121(3):1635–1684, 2019. doi:10.1007/s11192-019-03243-4.


