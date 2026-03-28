This article is licensed under aCreative Commons Attribution-NonCommercial 3.0 Unported Licence.

Open Access Article. Published on 04 November 2025. Downloaded on 1/30/2026 9:41:41 PM.

![image 1](Reeves-McLaren and Moth-Lund Christensen_2026_Data integrity in materials science in the era of AI balancing accelerated discovery with responsib_images/imageFile1.png)

Journal of

# Materials Chemistry A

#### View Article Online

## PERSPECTIVE

View Journal | View Issue

Cite this: J. Mater. Chem. A, 2026, 14, 276

## Data integrity in materials science in the era of AI: balancing accelerated discovery with responsible science and innovation

Nik Reeves-McLaren *a and Sarah Moth-Lund Christensen b

Received 8th July 2025 Accepted 31st October 2025

DOI: 10.1039/d5ta05512a rsc.li/materials-a

Artiﬁcial intelligence promises to revolutionise materials discovery through accelerated prediction and optimisation, yet this transformation brings critical data integrity challenges that threaten the scientiﬁc record. Recent studies demonstrate that experts cannot reliably distinguish AI-generated microscopy images from authentic experimental data, while widespread errors plague 20–30% of materials characterisation analyses. Generative AI tools can now produce code for data manipulation at pace, creating plausible-looking results that violate fundamental physical principles yet evade traditional peer review. These risks are compounded by inherent biases in training datasets that systematically over represent equilibrium-phase oxide systems, and by the “black box” opacity of AI models that challenges scientiﬁc accountability and epistemic agency. We propose a multifaceted framework for enhanced research integrity encompassing materials-speciﬁc ethical governance, professional standards for AI disclosure and data validation, and modular integrity checklists with technique-speciﬁc validation protocols. Critical enablers include mandatory deposition of structured raw instrument ﬁles, AI-powered fraud detection systems, and cultivation of critical AI literacy through interdisciplinary education. Without immediate action to address these challenges, the materials science community risks perpetuating errors and biases that will fundamentally undermine AI's transformative potential.

These challenges appear at a time when articial intelligence (AI) is set to reshape materials science, promising rapid discovery of advanced materials by predicting material properties, optimising compositions, and exploring vast chemical design spaces. Emergent examples include the development of alloys with superior mechanical properties,2 the generation of numerous MOF candidates, and advances in battery material discovery.3–5 Developments such as Google DeepMind's GNOME (graph networks for materials exploration) have demonstrated the potential for large-scale materials discovery, identifying 2.2 million stable crystal structures and representing an order-ofmagnitude expansion in known stable materials.6 The reliability of such AI models, however, depends entirely on the integrity of their training data.7

### 1 Introduction

Consider the scene: an early-career researcher, comparing their experimental data to a published standard, instructs a generative articial intelligence to ‘improve’ their results to better match the reference dataset. The AI complies, subtly altering the data points. The researcher subsequently asks their supervisor whether this action is an acceptable method of data processing – or maybe they don't. This situation illustrates a serious emerging threat to the integrity of the scientic record, one that extends far beyond issues of academic writing and into the manipulation of primary experimental data itself.

The severity of this threat was recently demonstrated in nanomaterials research, where a survey of 250 scientists found that experts could not reliably distinguish AI-generated microscopy images from authentic experimental data.1 These AI-generated images were created in under one hour using publicly available tools, requiring no specialised technical knowledge. The traditional peer review process, reliant on visual inspection by experts, is no longer suﬃcient to detect sophisticated image fraud.

High-quality, relevant, and representative data is essential for accurate and eﬀective generalisation. The principle “garbage in, garbage out” is key: if training data are limited or awed, AI models will be inaccurate.8 Intense debate followed a 2023 publication on an automated lab for rapid synthesis and characterisation of ‘new’ inorganic materials, with critiques of the work focussed around issues of metadata and what constitutes a novel discovery, the quality of automated analyses, and the ability to model the complexities of real materials, such as disorder.9,10

aSchool of Chemical, Materials and Biological Engineering, University of Sheﬃeld, Mappin Street, Sheﬃeld, S1 3JD, UK. E-mail: nik.reeves-mclaren@sheﬃeld.ac.uk bCentre for Machine Intelligence, University of Sheﬃeld, Mappin Street, Sheﬃeld S1 3JD, UK

Despite the clear promise of AI, widespread errors and inconsistencies in data, along with fraudulently manipulated or

This article is licensed under aCreative Commons Attribution-NonCommercial 3.0 Unported Licence.

Open Access Article. Published on 04 November 2025. Downloaded on 1/30/2026 9:41:41 PM.

![image 2](Reeves-McLaren and Moth-Lund Christensen_2026_Data integrity in materials science in the era of AI balancing accelerated discovery with responsib_images/imageFile2.png)

fabricated data threaten research validity in materials characterisation. Generative AI (GenAI) is readily capable of, for example, producing code to manipulate data, and then cover one's tracks, without asking any challenging ethical questions of researchers increasingly under ‘publish or perish’ pressures. Manipulating data to report a new room temperature superconductor would be discredited within hours of publication, but smaller iterative materials developments are more likely to sneak past peer review.

There is an urgent need for research on, and new approaches to, data integrity. Given the broad uptake of generative AI in materials science, and across all disciplines in engineering and the physical sciences, small errors, biases in foundational training data, and outright unethical conduct risk widespread research misdirection.

### 2 Outlining the data integrity challenges

The challenges of AI-driven or assisted research can be classied into several areas, each impacting the validity and trustworthiness of scientic ndings.

2.1. Widespread errors and underused verication methods

Studies show that a large proportion, from 20% to 30%, of data analyses across various common materials characterisation techniques, contain basic inaccuracies.7 A recent study used an AI tool to examine over 3000 papers in Organic Letters and found only 40% of chemical research papers had error-free mass measurements.11 The study also found cases where miscalculated values seemed validated by experimental measurements, casting doubts on researcher understanding, as well as raising concerns about potential data fabrication.

There are widespread issues with the underutilisation of well-established physical consistency checks in materials science data analyses, compounded by many instances of poor understanding of statistical measures employed to judge the perceived quality of work. Rietveld renement is a powerful tool for extracting structural information from powder diﬀraction data, but misinterpretations of statistical measures are common; one example is the eﬀective ‘goodness of t’ of the diﬀraction pattern calculated from the rened structure to the experimental data, the reduced chi-squared (c2). A critical misunderstanding is evident when reports on a renement quote a c2 value less than 1.0, statistically problematic as it implies a t that is “better than ideal”. This can indicate either that the standard uncertainties associated with the observed data are overestimated, or that too many parameters have been introduced, leading to overtting of the model to noise rather than true physical phenomena. The result is publication of structural parameters that are statistically unreliable or physically meaningless.12,13 Furthermore, many publications fail to report or justify crucial details of the renement model itself, such as the mathematical function used to model the peak proles and background, the constraints applied to parameters, or the handling of atomic displacement parameters (ADPs).

This frequently leads to the publication of physically nonsensical results, such as negative ADPs, and structural models that are statistically unsound and ultimately irreproducible.14

A further example: despite proven utility for ensuring consistency in dielectric functions and accurate optical and electronic property measurements, methods such as F-sum rules and Kramers–Kronig (K–K) relations are reportedly oen overlooked in research on optical materials.7 K–K relations are mathematical constraints linking the real and imaginary components of optical constants, derived from fundamental causality requirements. Violation of these relations – or of Fsum rules, which constrain integrated absorption based on electron density – indicates either measurement errors, incomplete spectral data, or data manipulation. The failure to apply such validation methods leaves optical property claims vulnerable to fabrication, particularly as GenAI tools could generate supercially plausible spectra that nevertheless violate basic physical constraints.

These types of widespread shortcomings highlight potentially severe issues around the reliability of reported materials and their properties, creating a substantial barrier to the development of high-performance advanced materials. Without improvement in data integrity, handling and reporting, we risk these shortcomings becoming xtures of AI training and validation data sets – in turn undermining the promise of AI in materials science and leaving us instead with unreliable models, and misdirected research.

2.2. Deliberate data manipulation and synthetic data risks

Research misconduct can be dened to include data fabrication, falsication, or plagiarism committed intentionally, knowingly, or recklessly, representing a signicant departure from accepted research practices.15,16 The recent reporting of around 800 papers published in crystallography and exoticchemistry journals originating from “paper mills” highlights one example of such systemic fraud.7,17 Other reports show 3.8% of published papers in biomedical research contain inappropriate image duplication.18

The arrival of GenAI brings new and complex ethical and scientic problems, at a time when research integrity in materials science is already under pressure. Highly realistic synthetic GenAI data and images can easily be misrepresented as experimental. Real data can be altered to better support scientic hypotheses. This capability poses serious risks to research integrity. Traditional methods for detecting fraud, such as identifying non-random digits, are now obsolete due to GenAI's sophistication, leading to an “arms race” between AI tools for detection and new methods designed to avoid them.15

The growth in use of text produced using GenAI tools such as ChatGPT, Gemini, Claude etc. means that many journals now require authors to declare where these have been used. But what about manipulation or fabrication of raw data? There is much less awareness around this risk. One GenAI tool these authors tested was able to yield reuseable Python code for data manipulation (to remove secondary phase peaks in diﬀraction data and ll the resulting void with randomly generated believable

This article is licensed under aCreative Commons Attribution-NonCommercial 3.0 Unported Licence.

Open Access Article. Published on 04 November 2025. Downloaded on 1/30/2026 9:41:41 PM.

![image 3](Reeves-McLaren and Moth-Lund Christensen_2026_Data integrity in materials science in the era of AI balancing accelerated discovery with responsib_images/imageFile3.png)

background, or to manipulate long-term battery testing data to remove noise and glitched cycles) in comfortably less than an hour. This is a challenge for the here and now.

Recent work in nanomaterials characterisation provides sobering empirical evidence of these capabilities. Researchers generated convincing fake atomic force microscopy (AFM), scanning transmission electron microscopy (STEM), and transmission electron microscopy (TEM) images in less than one hour using commercially available generative AI tools.1 When presented to 250 scientists in a blind survey, experts correctly identied real versus AI-generated images only 40–51% of the time for most image pairs – performance indistinguishable from random guessing. For four out of six image pairs tested, statistical analysis (chi-squared test, p > 0.05) showed no signicant diﬀerence in scientists' ability to identify authentic versus fake images.

Energy materials research oﬀers another good example of how research elds are facing vulnerabilities to AI-assisted data manipulation, in this case due to the complex, multi-parameter nature of electrochemical measurements. Photovoltaic current– voltage characteristics are readily susceptible to algorithmic enhancement, where ll factors could be articially improved from experimentally observed values of 0.83 to theoretically optimal values approaching 0.89 through subtle modication of series resistance contributions.19 Such manipulations remain within plausible ranges for peer review assessment whilst signicantly inating reported power conversion eﬃciencies. Electrocatalyst performance data present similar vulnerabilities through fabrication of Tafel slope values. Experimental studies demonstrate that Pt/C catalysts exhibit Tafel slopes varying from 30 mV dec−1 in 0.5 M H2SO4 to 120 mV dec−1 under fuel cell conditions, with additional dependence upon catalyst loading (63 to 211 mV dec−1 across diﬀerent overpotential ranges for identical materials).20 It is perceivable that GenAI tools could readily generate synthetic data presenting articially consistent Tafel slopes of 30 mV dec−1 across varied conditions, thereby suggesting superior kinetic performance. Electrochemical impedance spectroscopy measurements in battery and fuel cell research are similarly vulnerable, where complex multi-semicircle Nyquist plots can be algorithmically simplied to eliminate inconvenient high-frequency resistances or lowfrequency inductive features associated with side reactions or interface instabilities.21

If a research group was to fraudulently manipulate data and present the discovery of a room-temperature superconductor based on these types of subtle data hacks, they would likely be found out on the same day. For the more iterative work on less transformative materials that makes up much of the publication record – we propose this is currently much more likely to slip through the net unnoticed.

The Retraction Watch database currently runs to almost 60

000 records, but none yet specically focus on the use of AI for the purposes discussed here. One tangentially related case claimed to track the productivity of “a thousand material scientists” at a large R&D company, reporting a “44% increase in materials discovery” and an “81% productivity increase for top-decile scientists” due to the introduction of a “machine

learning material generation tool”. The data included were found to be “suspiciously clean and neat: nearly every sub measure of success gave a clear and statistically signicant result”. Following an internal, condential review, the sole author's institution concluded that the paper “should be withdrawn from public discourse” and requested the paper's withdrawal.22

- 2.3. Inherent biases and quality shortcomings in AI training datasets

Materials characterisation data can oen be noisy, incomplete and inconsistent, which directly impacts the performance of machine learning models. For example, a comprehensive review of over 1300 research papers focusing on X-ray photoelectron spectroscopy (XPS) analyses revealed wide-ranging issues with the quality and reliability of published data, directly exemplifying these challenges. Over 40% of publications contained errors that could have signicantly aﬀected the conclusions drawn; 35% neglected to provide details on the spectrometer used, and 85% did not specify the analytical soware used.23

It may seem unintuitive to think of bias in the context of materials science data, but our scientic track record – the AI's training data – fundamentally overrepresent stable, inorganic, equilibrium-phase systems, particularly oxide based materials, especially relative to amorphous, disordered or highly entropic materials.24 AI models trained on such data struggle to generalise or extrapolate to new, unexplored chemistries or processing conditions, oen leading to “hallucinations” or unreliable predictions for novel materials. Generative AI models can accidently learn and then amplify any biases and shortcomings present in their training data.25

For instance, if AI models are predominantly trained on data from materials developed and characterised under specic, well-established (e.g., equilibrium) conditions or for certain applications, they may inadvertently learn to prioritise or ‘hallucinate’ properties that conform to these existing paradigms. This could lead to a biased prediction landscape, where novel materials with unusual or non-equilibrium properties, or those relevant to emerging applications, are systematically overlooked or inaccurately predicted. Such a bias could perpetuate existing research trajectories, eﬀectively ‘stereotyping’ what constitutes a ‘good’ or ‘feasible’ material based on historical data, rather than enabling truly disruptive discoveries.

- 2.4. Challenges of transparency, explainability, and human oversight in AI systems


A signicant hurdle to data integrity in AI-driven materials science is the “black box” problem of AI models, wherein the ‘reasoning’ or the way the systems gets to a specic output is an opaque process for users and programmers alike. As such an AI model may suggest adding a tiny amount of a given element to an alloy will signicantly improve its tensile strength, but one might struggle to get an accurate and directly related explanation on why it predicts these properties. This issue pertains

This article is licensed under aCreative Commons Attribution-NonCommercial 3.0 Unported Licence.

Open Access Article. Published on 04 November 2025. Downloaded on 1/30/2026 9:41:41 PM.

![image 4](Reeves-McLaren and Moth-Lund Christensen_2026_Data integrity in materials science in the era of AI balancing accelerated discovery with responsib_images/imageFile4.png)

especially to AI models, such as deep learning neural networks, where complexity results in opaque decision-making.25 A lack of transparency and explainability severely complicates and hinders understanding of AI outputs, accountability, identication of causes of errors and biases, as well as potentially limiting trust in model predictions.

To reduce these risks and ensure responsible AI deployment, meaningful human control and oversight are essential. This involves actively monitoring AI behaviour and developing plans to prevent harmful eﬀects on users, with human validation being crucial for high-risk decisions.25 Ethical guidelines for trustworthy AI, such as those from the European Commission, outline diﬀerent levels of human involvement and oversight of AI system activity, including consideration of societal and ethical impacts, and ultimate decision-making.26

The impact of AI on human “epistemic agency” – the control individuals have over their beliefs, the questions they ask, and the reasons they entertain – is also a critical concern. There is an ongoing discussion about whether AI-based science poses a social epistemological problem, particularly concerning trust in opaque models and the responsibility of scientists for outputs based on AI models.27 Some argue that full transparency is not always needed for trust if systems follow established academic and institutional norms, but this applies to human and institutional actors, not to AI models which cannot be held to norms in the same way. Therefore, how can materials scientists ensure research integrity and fully take responsibility for AI tools, when they cannot foresee, fully understand nor verify how these tools gets to a given specic output? For example, if an AI model identies a novel battery electrolyte composition but cannot explain why certain additives improve ionic conductivity, researchers cannot properly assess safety risks or optimise the formulation further. Similarly, if an AI predicts a ceramic will exhibit ferroelectric properties but provides no mechanistic insight, experimental validation becomes trial-and-error rather than hypothesisdriven science. This requires an evolving understanding of scientic responsibility and epistemic agency in the AI era. The traditional idea of scientic responsibility assumes a human agent's full understanding and control over their research tools.27 AI's opacity directly challenges this, raising basic questions about who is accountable when an AI system makes a awed decision or generates inaccurate data, and curtailing the scientist's ability to articulate the reasons and evidence supporting AI-generated hypotheses. This implies a profound shi in the epistemology of science, and a new understanding of human agency in research integrity and accountability.25–27

### 3. Developing frameworks for enhanced research integrity in AIdriven materials science

Dealing with data integrity issues in AI-driven materials science will require a multi-faceted approach, combining governance, professional standards, and human vigilance.

- 3.1. Ethical foundations and materials-specic governance

With rapid developments in AI, the corresponding AI regulatory and governance landscape is trying to play catchup under the headings of primarily “ethical AI”, “responsible AI”, and “trustworthy AI”. Despite the language ux, core principles are emerging that mirror the technical limitations and concerns for particularly GenAI: transparency, explainability, accountability, fairness, privacy and safety. Key initiatives, such as the National Institute of Standards and Technology's (NIST) research on trustworthy AI characteristics and UNESCO's global standard on the Ethics of Articial Intelligence, highlight these shared priority principles for AI development.

Despite the concerted eﬀorts in AI governance, the practical challenges for materials science-oriented adoption of these principles and governance frameworks is and will not be straightforward. Even these broad principles need to be translated into specic guidelines and governance mechanisms relevant to the specic challenges of materials science data. Further, the current generalised list of ethical AI principles can and should not be expected to be exhaustive. One must expect that considerable work will be needed to identify potential ethical challenges posed by the use and development of AI specically in and for materials science research. This includes ethical challenges requiring both technical and non-technical address, for example potentially relating to sustainability, dual use, and how AI might change perceptions and assumptions about materials science research practises.

Frameworks for assessing “AI-ready” data are appearing to deal with some of these problems. The SciHorizon framework, for instance, suggests four main aspects: quality, FAIRness (ndable, accessible, interoperable, reusable), explainability, and compliance.8 Key parts of the ‘quality’ component include completeness, accuracy, consistency (both internal coherence within a dataset and external alignment to related datasets), and timeliness (prompt publication and continuous updating). ‘Compliance’ stresses the importance of data provenance (clear documentation of data sources, authorship, and licensing), ethics & safety (adherence to scientic ethical standards), and trustworthiness (compliance with national regulations and sustainability of data services). This shis the focus from sheer data volume to the quality, relevance, and representativeness of the data, but implicit in this is a fundamental re-evaluation of how scientic data is collected, curated, and prepared – with both good practice and AI in mind.

- 3.2. Professional standards and best practices for materials data and AI


Professional bodies and scientic publishers increasingly set specic standards and best practices for ethical AI use in scientic research and its dissemination through journal articles. For the materials science community, Nature Portfolio journals, including Nature Materials, have established clear guidelines for authors and peer reviewers regarding AI tools.28 Their policies establish that accountability for work cannot be eﬀectively applied to AI tools, precluding large language models such as ChatGPT from author attribution on publications. A

This article is licensed under aCreative Commons Attribution-NonCommercial 3.0 Unported Licence.

Open Access Article. Published on 04 November 2025. Downloaded on 1/30/2026 9:41:41 PM.

![image 5](Reeves-McLaren and Moth-Lund Christensen_2026_Data integrity in materials science in the era of AI balancing accelerated discovery with responsib_images/imageFile5.png)

nuanced distinction is made for AI-assisted improvements to human-generated texts for readability, style, grammar, spelling, and tone, which does not require declaration. However, in all cases, human accountability for the nal text remain paramount.

The Nature Portfolio also largely prohibits the use of generative AI for images due to unresolved legal copyright and research integrity issues. This stance, while understandable from a legal and ethical perspective, may be an implicit hurdle for AI-driven materials discovery workows reliant on generative models to propose novel material structures or microstructures, where visual representation is key.

Recent calls from the microscopy community emphasise the need to reframe expectations around image quality, recognising that not every nanomaterial or assembly is perfect, and that pristine images may signal manipulation rather than excellence.1 Excessive demands for polished images create pressure on researchers that can inadvertently incentivise AI usage. Reviewers should not request “better looking” images unless visual improvements would change the authors' scientic conclusions. The purpose of images is to support conclusions and enable fair judgment, not to serve as polished content for dissemination. Editors must actively dismiss such reviewer comments when they are scientically unjustied, recognising that this pressure contributes to the integrity crisis.

Standardised validation protocols are also becoming more prominent. There is a recognised need for new norms, standards, and best practices for conducting research with AI. Data provenance is vital for AI authentication, transparency, and traceability. The detailed requirements for documentation, including researcher responsibilities, workow, input, output, metadata, origin/access point, and data management, go beyond a traditional citation. This implies that for AI-driven materials science, true reproducibility and trustworthiness depend not just on the nal model or results, but on a carefully documented “data trail” from raw source to nal output, especially given AI's potential to hallucinate and/or generate synthetic data.

3.3. Using AI as a tool for materials data quality control

Paradoxically, while AI brings new integrity challenges, it also oﬀers powerful ways to detect misconduct, including data manipulation, image fraud, and fabricated results. AI systems can analyse datasets for statistical inconsistencies and patterns suggesting fabrication or manipulation, using machine learning models to compare experimental results with established scientic principles and assess adherence to expected distributions or statistical norms. Natural language processing tools can check for consistency between text descriptions, gures, and tables, agging any diﬀerences for authors and editors alike.

The potential for automated quality assurance and better peer review processes specically within materials science is signicant. Some publishers and research institutions already use AI tools to scan submitted manuscripts for image integrity problems before peer review. Christmann's study showed the

power of AI-powered data analysis in uncovering previously unknown systematic errors in chemical publications highlights AI's capability for automated quality control in chemical and materials data.11 The future must bring better collaboration between AI and human reviewers to improve fraud detection. This will likely involve AI handling issues of scale and initial pattern detection, with human experts then providing critical judgement, contextual understanding, and deal with nuanced cases AI might miss.

The Science family of journals has adopted Proog, an AIpowered image-analysis tool, to screen for manipulation.29 However, ethical implementation requires that AI-agged suspicions be reviewed by humans, with outcomes communicated to authors who must have opportunity to respond, in accordance with Committee on Publication Ethics (COPE) guidelines. Such tools should be deployed both during submission and retrospectively to audit previous publications, with the sophistication of anti-fraud measures potentially serving as an indicator of journal quality.

3.4. Cultivating a culture of data responsibility and critical AI literacy in materials science

Ultimately, researchers are responsible for checking the accuracy of data, AI-generated output and ensuring that data provenance is carefully maintained. It is not enough to just use AI tools; researchers must become responsible guardians who understand AI's abilities, limits, as well as its ethical and scientic implications, actively checking its outputs and ensuring proper disclosure. This necessitates at least two additions or changes to the norms of material science research. First, it requires higher level of general data and AI literacy among researchers. Second, as the state of AI and available AI research tools is far from static, it also requires researchers to continuously reect upon (1) the potential ethical concerns in their adoption of these tools, and (2) whether their trust, understanding and control of given AI tools and their outputs is adequate for genuine knowledge creation.

Fostering a reective research culture by bringing AI ethics and sound data analysis skills into scientic education and training is an essential and proactive step. For instance, Freie Universit¨at Berlin's Department of Biology, Chemistry, and Pharmacy plans to bring AI tools into its curriculum to help students develop strong data analysis skills and critical thinking, preparing them for their future research careers.30 Similarly, Cornell Engineering has started a graduate-level course, “AI for materials”, designed to give the next generation of researchers and engineers the knowledge to drive discovery where AI and materials science meet, highlighting both applications and the challenges involved. The challenges posed by AI can also be seen as an opportune moment to foster new interdisciplinary relations, and to benet from the strengths of disciplines, who specialise in ethics or metascience matters. As an example, “Embedded EthiCS” at Harvard is a collaboration between computer scientists and philosophers fuelling both teaching and research on ethical concerns in AI development and adoption.

This article is licensed under aCreative Commons Attribution-NonCommercial 3.0 Unported Licence.

Open Access Article. Published on 04 November 2025. Downloaded on 1/30/2026 9:41:41 PM.

![image 6](Reeves-McLaren and Moth-Lund Christensen_2026_Data integrity in materials science in the era of AI balancing accelerated discovery with responsib_images/imageFile6.png)

Encouraging a culture of critical reection and healthy scepticism towards AI outputs is essential. It is vital to develop a culture within materials science that sees AI models as tools requiring responsible use while instilling strong data analysis skills and critical thinking skills in researchers – at all levels, ensuring we are all equipped with the necessary knowledge and ethical grounding to navigate the complexities of AI-driven science responsibly.

To supplement individual diligence, the community should also consider adopting established structural approaches from other scientic disciplines designed to improve the reliability of research ndings. Adversarial collaborations, for instance, unite researchers with conicting viewpoints to jointly design and conduct a critical experiment, increasing the impartiality of the outcome. The Registered Reports publication format, where methods and analysis protocols are peer-reviewed before

experiments are conducted, mitigates publication bias and questionable research practices. Finally, a ‘Red Team’ approach, where researchers actively solicit rigorous, structured criticism of a project from designated colleagues prior to submission, can identify weaknesses in argumentation and data interpretation that might otherwise be missed. The adoption of such practices would represent a systemic commitment to research integrity.

3.5. Practical implementation: data integrity checklists and validation frameworks

To move from identifying these challenges towards actionable solutions, we rst propose a modular checklist for authors, reviewers, and journal editors, inspired by best practices in clinical research such as the INSPECT-SR criteria for systematic

Table 1 Modular data integrity checklist for materials science publications. The core data integrity module is required for all submissions, while technique-speciﬁc modules should be applied as relevant to the methods used. This framework provides concrete validation steps for authors, editors, and reviewers while accommodating the diverse methodological landscape of materials research. Additional modules can be developed for other characterisation techniques as community priorities emerge

![image 7](Reeves-McLaren and Moth-Lund Christensen_2026_Data integrity in materials science in the era of AI balancing accelerated discovery with responsib_images/imageFile7.png)

This article is licensed under aCreative Commons Attribution-NonCommercial 3.0 Unported Licence.

Open Access Article. Published on 04 November 2025. Downloaded on 1/30/2026 9:41:41 PM.

![image 8](Reeves-McLaren and Moth-Lund Christensen_2026_Data integrity in materials science in the era of AI balancing accelerated discovery with responsib_images/imageFile8.png)

reviews.31 This approach provides a structured framework for data validation specic to common materials science techniques. The core module, Table 1, outlines general principles of data integrity and AI usage declaration applicable to all manuscripts. We have also suggested initial technique-specic modules for X-ray diﬀraction with Rietveld renement and for electrochemical battery testing, two areas where data quality is frequently suboptimal. This modular design is extensible, and we invite community contributions to develop and validate further modules.

A critical enabler for this checklist is a policy mandating the deposition of raw experimental data. The distinction between raw and processed data is vital for integrity. It is insuﬃcient to provide only processed data, such as a text le of a diﬀraction pattern (.xy); journals must require the structured, machinereadable raw data les generated by the instrument itself (e.g., .raw, .xrdml). Raw instrument les contain a rich set of metadata – including calibration parameters, detector settings, and collection times – that are essential for reproducing the analysis and verifying the data's origin. This embedded metadata makes the convincing fabrication of a raw data le substantially more diﬃcult than creating a simple text le of processed numbers. To make verication of these les practical rather than overwhelming, recent proposals from the nanomaterials community suggest adopting standardised data storage structures.1 The minimal arrangement of instrument les (MAIF) framework proposes that each manuscript has its own folder, with each gure having a subfolder containing primary instrument les specic to that gure, and non-gure data stored in a separate ‘additional data’ folder.1 This structured approach – as opposed to idiosyncratic, researcher-specic ling systems – enables eﬃcient checking of key instrument les for legitimacy without overwhelming reviewers or investigators. We recommend that journals require structured raw data les (following MAIF or similar principles) as a publication criterion, published as compressed directories in supplementary information or repositories such as Zenodo, Open Science Framework, or Figshare. This requirement should over time become mandatory rather than merely encouraged.

While the checklist approach we propose addresses the integrity of individual studies, a distinct but related challenge is the quality control of the large, aggregated datasets upon which foundational AI models are built. In elds such as clinical science, where meta-analyses of randomised controlled trials face similar issues with awed or fraudulent data, researchers have developed formal tools to identify problematic studies before their inclusion in a wider analysis.31 A parallel approach is required in materials science to ensure that AI models are not trained on compromised data.

Accordingly, we propose the development of a complementary data-vetting framework specically for the curation of AI training sets. Such a framework would consist of a series of checks to be applied to any dataset being considered for inclusion in a larger corpus, including: (i) verication of the publication status of the source data, checking for retractions, corrections, or expressions of concern; (ii) screening against public post-publication review platforms for credible criticisms;

and (iii) programmatic checks for statistical anomalies or physically implausible results within the data itself, such as eﬃciencies exceeding 100% or unrealistic electrochemical parameters.

These proposed actions are not one-and-done xes, and as shown earlier connects with larger reections upon how AI interacts with our notion of trustworthy research and knowledge generation, therefore instead requiring continuous involvement and engagement from both the materials science research community and beyond. However, we hope with these initial suggestions to open up for a focused discussion on responsible AI adoption in Materials Sciences, and encourage a wider dialogue on how we can ensure trustworthy and responsible research practices in the AI age.

### Conﬂicts of interest

There are no conicts to declare.

### Data availability

No original data are included in this perspective.

### References

- 1 N. Davydiuk, et al., The rising danger of AI-generated images in nanomaterials science and what we can do about it, Nat. Nanotechnol., 2025, 20, 1174–1177, DOI: 10.1038/s41565025-02009-9.
- 2 F. Wang, et al., Experimentally validated inverse design of FeNiCrCoCu MPEAs and unlocking key insights with explainable AI, npj Comput. Mater., 2025, 11, 124, DOI: 10.1038/s41524-025-01600-x.
- 3 A. Beadle, How Is AI Accelerating the Discovery of New Materials?, https://www.technologynetworks.com/appliedsciences/articles/how-is-ai-accelerating-the-discovery-ofnew-materials-394927, 2025.
- 4 H. Park, et al., A generative articial intelligence framework based on a molecular diﬀusion model for the design of metal-organic frameworks for carbon capture, Commun. Chem., 2024, 7, 21, DOI: 10.1038/s42004-023-01090-2.
- 5 A. D. Sendek, et al., Machine Learning-Assisted Discovery of Solid Li-Ion Conducting Materials, Chem. Mater., 2019, 31, 342–352, DOI: 10.1021/acs.chemmater.8b03272.
- 6 A. Merchant, et al., Scaling deep learning for materials discovery, Nature, 2023, 624, 80–85, DOI: 10.1038/s41586023-06735-9.
- 7 S. H. Aboutalebi, Ensuring Data Integrity in AI-Driven Materials Science: Why F-Sum Rules and Kramers-Kronig Relations Matter, Nanoscale Adv. Mater., 2025, 2, 10–15, DOI: 10.22034/nsam.2025.01.02.
- 8 C. Qin, et al., SciHorizon: Benchmarking AI-for-Science Readiness from Scientic Data to Large Language Models, arXiv, 2025, preprint arXiv:2503.13503, DOI: 10.48550/ arXiv.2503.13503.


This article is licensed under aCreative Commons Attribution-NonCommercial 3.0 Unported Licence.

Open Access Article. Published on 04 November 2025. Downloaded on 1/30/2026 9:41:41 PM.

![image 9](Reeves-McLaren and Moth-Lund Christensen_2026_Data integrity in materials science in the era of AI balancing accelerated discovery with responsib_images/imageFile9.png)

- 9 J. Leeman, et al., Challenges in High-Throughput Inorganic Materials Prediction and Autonomous Synthesis, Phys. Rev. X, 2024, 3, 011002, DOI: 10.1103/PRXEnergy.3.011002.
- 10 N. J. Szymanski, et al., An autonomous laboratory for the accelerated synthesis of novel materials, Nature, 2023, 624, 86–91, DOI: 10.1038/s41586-023-06734-w.
- 11 M. Christmann, What I Learned from Analyzing Accurate Mass Data of 3000 Supporting Information Files, Org. Lett., 2025, 27, 4–7, DOI: 10.1021/acs.orglett.4c03458.
- 12 A. L. Spek, What makes a crystal structure report valid?, Inorg. Chim. Acta, 2018, 470, 232–237, DOI: 10.1016/ j.ica.2017.04.036.
- 13 B. H. Toby, R factors in Rietveld analysis: How good is good enough?, Powder Diﬀr., 2006, 21, 67–70, DOI: 10.1154/ 1.2179804.
- 14 L. B. McCusker, R. B. Von Dreele, D. E. Cox, D. Louer and P. Scardi, Rietveld renement guidelines, J. Appl. Crystallogr., 1999, 32, 36–50, DOI: 10.1107/ S0021889898009856.
- 15 D. B. Resnik, M. Hosseini, J. J. H. Kim, G. Epiphaniou and C. Maple, GenAI synthetic data create ethical challenges for scientists. Here's how to address them, Proc. Natl. Acad. Sci. U. S. A., 2025, 122, e2409182122, DOI: 10.1073/ pnas.2409182122.
- 16 J. Gu, et al., AI-enabled image fraud in scientic publications, Patterns, 2022, 3, 100511, DOI: 10.1016/ j.patter.2022.100511.
- 17 J. A. Byrne, et al., A call for research to address the threat of paper mills, PLoS Biol., 2024, 22, e3002931, DOI: 10.1371/ journal.pbio.3002931.
- 18 E. M. Bik, A. Casadevall and C. Fang Ferric, The Prevalence of Inappropriate Image Duplication in Biomedical Research Publications, mBio, 2016, 7(3), e00809.
- 19 M. A. Green, Solar cell ll factors: General graph and empirical expressions, Solid-State Electron., 1981, 24, 788– 789, DOI: 10.1016/0038-1101(81)90062-9.


- 20 T. Shinagawa, A. T. Garcia-Esparza and K. Takanabe, Insight on Tafel slopes from a microkinetic analysis of aqueous electrocatalysis for energy conversion, Sci. Rep., 2015, 5, 13801, DOI: 10.1038/srep13801.
- 21 A. C. Lazanas and M. I. Prodromidis, Electrochemical Impedance Spectroscopy–A Tutorial, ACS Meas. Sci. Au, 2023, 3, 162–193, DOI: 10.1021/acsmeasuresciau.2c00070.
- 22 MIT Economics, Assuring an accurate research record, https:// economics.mit.edu/news/assuring-accurate-researchrecord, 2025.
- 23 G. H. Major, et al., Assessment of the frequency and nature of erroneous x-ray photoelectron spectroscopy analyses in the scientic literature, J. Vac. Sci. Technol., A, 2020, 38, 061204, DOI: 10.1116/6.0000685.
- 24 M.-H. Van, P. Verma, C. Zhao and X. Wu, A Survey of AI for Materials Science: Foundation Models, LLM Agents, Datasets, and Tools, arXiv, 2025, preprint arXiv:2506.20743, DOI: 10.48550/arXiv.2506.20743.
- 25 UK Government, Government Digital Service, 2025.
- 26 European Commission, Directorate-General for Research and Innovation, Brussels, 2025.
- 27 U. Peters, Science Based on Articial Intelligence Need not Pose a Social Epistemological Problem, Social Epistemology Review and Reply Collective, 2024, 13, 58–66.
- 28 Springer Nature, Articial Intelligence (AI), https:// www.nature.com/nmat/editorial-policies/ai, 2025.
- 29 H. H. Thorp, Genuine images in 2024, Science, 2024, 383, 7, DOI: 10.1126/science.adn7530.
- 30 Freie Universit¨at Berlin’s Department of Biology, Chemistry, Pharmacy, Freie Universitat¨ Berlin's Department of Biology, Chemistry, Pharmacy, 2025.
- 31 J. Wilkinson, et al., Protocol for the development of a tool (INSPECT-SR) to identify problematic randomised controlled trials in systematic reviews of health interventions, BMJ Open, 2024, 14, e084164, DOI: 10.1136/ bmjopen-2024-084164.


