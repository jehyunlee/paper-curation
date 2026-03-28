# arXiv:2503.10970v1[cs.AI]14 Mar 2025

## TxAgent: An AI Agent for Therapeutic Reasoning Across a Universe of Tools

Shanghua Gao1, Richard Zhu1, Zhenglun Kong1, Ayush Noori1, Xiaorui Su1, Curtis Ginder1,2, Theodoros Tsiligkaridis3, and Marinka Zitnik1,4,5,6,‡

1Department of Biomedical Informatics, Harvard Medical School, Boston, MA 2Cardiovascular Division, Department of Medicine, Brigham and Women’s Hospital, Harvard Medical School, Boston, MA 3MIT Lincoln Laboratory, Lexington, MA 4Kempner Institute for the Study of Natural and Artificial Intelligence, Harvard University, Cambridge, MA 5Broad Institute of MIT and Harvard, Cambridge, MA 6Harvard Data Science Initiative, Cambridge, MA ‡Corresponding author. Email: marinka@hms.harvard.edu

TXAGENT project is at https://zitniklab.hms.harvard.edu/TxAgent TXAGENT code and demos are at https://github.com/mims-harvard/TxAgent TOOLUNIVERSE is at https://github.com/mims-harvard/ToolUniverse

Precision therapeutics require multimodal adaptive models that generate personalized treatment recommendations. We introduce TXAGENT, an AI agent that leverages multi-step reasoning and real-time biomedical knowledge retrieval across a toolbox of 211 tools to analyze drug interactions, contraindications, and patient-specific treatment strategies. TXAGENT evaluates how drugs interact at molecular, pharmacokinetic, and clinical levels, identifies contraindications based on patient comorbidities and concurrent medications, and tailors treatment strategies to individual patient characteristics, including age, genetic factors, and disease progression. TXAGENT retrieves and synthesizes evidence from multiple biomedical sources, assesses interactions between drugs and patient conditions, and refines treatment recommendations through iterative reasoning. It selects tools based on task objectives and executes structured function calls to solve therapeutic tasks that require clinical reasoning and cross-source validation. The TOOLUNIVERSE consolidates 211 tools from trusted sources, including all US FDA-approved drugs since 1939 and validated clinical insights from Open Targets. TXAGENT outperforms leading LLMs, tool-use models, and reasoning agents across five new benchmarks: DrugPC, BrandPC, GenericPC, TreatmentPC, and DescriptionPC, covering 3,168 drug reasoning tasks and 456 personalized treatment scenarios. It achieves 92.1% accuracy in open-ended drug reasoning tasks, surpassing GPT-4o by up to 25.8% and outperforming DeepSeek-R1 (671B) in structured multi-step reasoning. TXAGENT generalizes across drug name variants and descriptions, maintaining a variance of <0.01 between brand, generic, and description-based drug references, exceeding existing tool-use LLMs by over 55%. By integrating multi-step inference, real-time knowledge grounding, and toolassisted decision-making, TXAGENT ensures that treatment recommendations align with established clinical guidelines and real-world evidence, reducing the risk of adverse events and improving therapeutic decision-making.

## Main

Precision therapy personalizes treatments based on individual patient conditions to maximize efficacy and minimize risks. Prescribing the appropriate drug requires evaluating multiple factors, including patient-specific characteristics, comorbidities, drug interactions, contraindications, current clinical guidelines, drug mechanisms of action, and the underlying biology of the disease [1]. Large language models (LLMs) can process therapeutic tasks by large-scale pretraining [2–6] followed by fine-tuning on medical data [7–9]. While LLMs generate fluent, contextually relevant responses, they lack real-time access to updated biomedical knowledge, frequently hallucinate, and cannot reliably reason over multiple clinical variables. Retraining these models with new medical insights is computationally expensive and impractical due to catastrophic forgetting. Furthermore, LLMs absorb large volumes of open-net data, which may contain unverified or deliberately misleading medical information [10]. Tool-augmented LLMs [11–13] incorporate external knowledge retrieval mechanisms, such as retrieval-augmented generation (RAG) [14], to mitigate these issues. These models retrieve drug and disease information from external sources but cannot execute multi-step reasoning required for treatment selection. Precision therapy could benefit from iterative reasoning, where models could retrieve information from verified sources, evaluate interactions, and dynamically refine treatment plans.

We introduce TXAGENT, an AI agent [15–19] that delivers evidence-grounded treatment recommendations by combining multi-step reasoning with real-time biomedical tool integration. TXAGENT generates natural language responses alongside a transparent reasoning trace, detailing each step of its decision-making process. It executes goal-driven tool selection, calling external databases and specialized machine learning (ML) models to ensure accuracy. To support complex medical queries, TXAGENT leverages TOOLUNIVERSE, a biomedical toolbox consolidating 211 expert-curated tools, spanning drug mechanisms, interactions, clinical guidelines, and disease annotations. These tools integrate trusted sources, including openFDA [20], Open Targets [21], and the Human Phenotype Ontology [22]. TXAGENT further employs TOOLRAG model, an ML-based retrieval system that dynamically selects the most relevant tools from TOOLUNIVERSE based on query context.

TXAGENT consists of: (1) TOOLUNIVERSE, a diverse collection of 211 biomedical tools, (2) a specialized LLM fine-tuned for multi-step reasoning and tool execution, and (3) TOOLRAG model, an adaptive tool retrieval model. To construct tools compatible with TXAGENT, we introduce TOOLGEN, a multi-agent tool construction system that generates tools from API docu-

mentation. TXAGENT is fine-tuned using TXAGENT-INSTRUCT, a dataset of 378,027 instructiontuning samples that is derived from 85,340 multi-step reasoning traces and encompasses 177,626 reasoning steps and 281,695 function calls. The dataset is generated using QUESTIONGEN and TRACEGEN, multi-agent systems that construct diverse therapeutic queries and generate stepwise reasoning traces that cover treatment and drug information in FDA labels since 1939.

We introduce five new benchmarks (DrugPC, BrandPC, GenericPC, DescriptionPC, TreatmentPC, Table 1). These benchmarks comprehensively assess drug selection, treatment personalization, and reasoning robustness across structured and unstructured queries. TXAGENT outperforms larger LLMs and existing tool-use models across all five benchmarks, achieving state-of-theart performance in open-ended drug reasoning and patient-specific therapeutic decision-making. On the DrugPC benchmark, which evaluates 11 common drug reasoning tasks, TXAGENT attains 92.1% accuracy in the open-ended setting, where the model generates answers without predefined choices. This performance surpasses GPT-4o [23], the strongest closed-weight reference model, by 25.8% (GPT-4o: 66.3%) and outperforms Llama-3.1-70B-Instruct [2], a model nearly 9× larger, by 39.3% (Llama-3.1-70B-Instruct: 52.8%). TXAGENT, based on the fine-tuned 8-billion parameter Llama-3.1-8B-Instruct model [2], delivers superior accuracy while maintaining computational efficiency. Compared to tool-use LLMs with function-calling capabilities, such as ToolACE and WattTool [12,13], TXAGENT significantly outperforms both models in open-ended drug reasoning tasks. Unlike existing tool-augmented LLMs, which struggle with multi-step tool selection and iterative reasoning, TXAGENT dynamically retrieves and synthesizes knowledge from 211 biomedical tools, achieving more accurate and context-aware therapeutic decisions.

Beyond drug reasoning, TXAGENT generalizes across drug name variants and descriptions, overcoming a key limitation of LLM-based methods [24,25]. Many models exhibit high variance when drugs are referenced by brand names, generic names, or detailed descriptions [24]. In contrast, TXAGENT achieves an exceptionally low accuracy variance of <0.01 across these variations, whereas GPT-4o exhibits a variance of 9.96, indicating a much higher sensitivity to representation shifts. On DescriptionPC, a benchmark that evaluates drug reasoning when drug names are replaced with descriptive narratives, TXAGENT attains 56.5% accuracy, outperforming GPT-4o by 8.3% and indicating TXAGENT’s robustness to infer drug identities from contextual clues. TXAGENT also excels in personalized treatment recommendations, where it evaluates patient-specific drug selection. On TreatmentPC, which assesses 456 real-world treatment scenarios, TXAGENT outperforms GPT-4o by 13.6% and Llama-3.1-70B-Instruct by 25.4% in the open-ended setting,

establishing its superiority in personalized medicine. Compared to DeepSeek-R1 [26], a 671billion parameter model optimized for multi-step reasoning, TXAGENT achieves 7.5% higher accuracy in open-ended queries, demonstrating that specialized reasoning and tool-use capabilities outweigh model size.

We conduct ablation studies to evaluate TXAGENT’s toolbox size, tool dependency, and reasoning process. Increasing the number of tools in TOOLUNIVERSE improves performance, demonstrating that access to external biomedical tools improves therapeutic reasoning. We compare realworld tool usage to an LLM acting as a tool substitute and find that tool-assisted decision-making consistently outperforms LLM-only reasoning, highlighting the need for grounding AI agents in continually updated and verified therapeutic knowledge. We also examine the impact of explicit reasoning steps before function calls and show that structured reasoning improves performance more than multi-round function calls alone. Finally, we analyze the effect of multi-step training traces and find that increasing the number of reasoning steps in fine-tuning and inference significantly improves TXAGENT’s ability to handle complex drug reasoning and treatment selection.

## Results

#### TXAGENT: Multi-step therapeutic reasoning with a universe of tools

TXAGENT uses multi-step, white-box reasoning and tool-use for solving precision treatment problems (Figure 1a). Using a wide array of tools that connect to verified knowledge bases, such as FDA-approved drug labels and the Open Targets [20, 21], as well as machine learning tools for special purposes such as tool retrieval (Figure 1b), TXAGENT performs detailed reasoning on drugs, diseases, and patient populations. This ability to leverage a vast array of biomedical tools ensures TXAGENT is not limited by the internal knowledge of LLMs, enabling it to generate accurate and reliable answers with transparent reasoning traces. It can handle a variety of patient scenarios, from specific patient populations and complex medical histories to polypharmacy and individual-specific genetic variants. TXAGENT uses TOOLUNIVERSE, which is a generalizable toolbox with 211 tools that support real-time retrieval of knowledge from verified data sources, including openFDA [20], Open Targets [21], and the Human Phenotype Ontology from the Monarch Initiative [22]. These tools address diverse aspects of drugs and diseases, such as drug indications and usage (Figure 1c).

TXAGENT is an LLM trained to use tools. This is achieved by building three training datasets (a tooling dataset, a comprehensive therapeutic question dataset, and a reasoning trace

dataset), which we create using three auxiliary agent systems (Figure 2a). Given these datasets, we instruction-tune an LLM [2] to achieve multiple capabilities, including multi-step reasoning and tool call argument generation. For each step in the multi-step reasoning process, TXAGENT receives either a therapeutic question or tool feedback from the previous round. Based on this input, TXAGENT generates a language-based thought process and invokes calls to tools. During the reasoning process, to identify and utilize relevant tools, TXAGENT invokes the TOOLRAG model, which selects suitable candidates from TOOLUNIVERSE based on descriptions provided by TXAGENT. This iterative process continues until TXAGENT arrives at a final answer and invokes the FINISH tool to conclude the reasoning process. The output of TXAGENT includes both the final answer and a multi-step reasoning trace. Each step of the reasoning trace includes a thought process, function calls to utilize tools, and feedback from those tools. We show the detailed inference process of TXAGENT in Online Methods Section 1.2 and Algorithm 1.

#### Capabilities of TXAGENT

TXAGENT generates reasoning traces, constructs function call arguments, performs multi-step logical reasoning, and searches for, selects, and invokes tools to solve a therapeutic reasoning task. These capabilities are developed through instruction tuning of the LLM (Online Methods Section 1.2). By applying these capabilities, TXAGENT retrieves verified biomedical knowledge through tool calls, selects tools based on specific objectives, solves problems through multi-step reasoning, and integrates continuously updated knowledge bases.

Knowledge grounding using tool calls. Treatment decisions require reliable answers with transparent justifications. LLMs lack inherent mechanisms to verify their predictions, requiring users to assess trustworthiness manually. TXAGENT addresses this by retrieving verified information from trusted sources through function calls. Instead of generating responses directly, TXAGENT queries tools to obtain accurate data and formulates answers based on verified outputs. In Figure 1f, TXAGENT determines the dosage of Kisunla (donanemab-azbt), an FDA-approved drug from 2024, which is beyond the training data of its base LLMs. TXAGENT recognizes the knowledge gap, calls get dosage, and retrieves dosage details from FDA records. It then synthesizes the retrieved information into a response. This approach ensures factual accuracy and transparency, allowing users to verify responses through reasoning traces.

Goal-oriented tool selection. TXAGENT uses TOOLRAG model to search for, identify, and apply the most relevant tools. Figure 1g shows TXAGENT retrieving adverse reactions for Alyftrek

(vanzacaftor, tezacaftor, deutivacaftor). It recognizes the need for external data, generates function call arguments, and queries TOOLUNIVERSE. From the returned tools, TXAGENT selects get adverse reactions to extract relevant information from FDA drug labels. This process enables TXAGENT to dynamically integrate new tools rather than relying on static, pre-trained knowledge. By first generating a plan and then selecting appropriate tools, TXAGENT supports adaptive decision-making.

Multi-step therapeutic reasoning. TXAGENT applies multi-step reasoning to address complex problems that require integrating multiple sources of information or adapting to incomplete data. Single-step approaches fail when problems demand information from multiple perspectives or when function calls return insufficient results. By iteratively generating reasoning steps and function calls, TXAGENT refines its analysis until it reaches a well-supported answer. In Figure 1h, TXAGENT identifies protein targets for breast cancer, a task no single TOOLUNIVERSE tool can complete. Therefore, TXAGENT first retrieves the disease’s EFO ID using get disease id desc, then queries TOOLUNIVERSE for tools that map diseases to protein targets. From the returned options, TXAGENT selects get associated targets and ranks the retrieved proteins by score. This iterative process ensures robust reasoning in cases where direct retrieval is insufficient.

Real-time retrieval from continually updated knowledge sources. LLMs retain only the knowledge available at the time of training and cannot update dynamically. Retraining models to incorporate new biomedical information is computationally expensive and impractical. Retrievalaugmented generation [27] mitigates this by querying a precomputed vector database, but maintaining high-quality embeddings for frequent updates is resource-intensive. TXAGENT addresses this limitation by executing function calls to directly query real-time data sources, such as Open Targets and FDA databases. This approach enables TXAGENT to retrieve current drug approvals, clinical guidelines, and treatment indications without requiring model retraining. Unlike static vector databases, which require periodic reprocessing, TXAGENT continuously integrates new information from multiple verified sources. Figure 1i illustrates this capability. Bizengri (zenocutuzumabzbco) was approved by the FDA in December 2024, after the knowledge cutoff of TXAGENT’s base model, Llama3.1-8B (December 2023). Instead of relying on outdated internal knowledge, TXAGENT calls the get indications tool to query the openFDA API, retrieving the latest drug label information. This allows TXAGENT to correctly identify Bizengri’s approved indications for non-small cell lung cancer and pancreatic adenocarcinoma. By integrating continuously updated sources, TXAGENT ensures access to the latest biomedical knowledge, eliminating reliance on

static training data and mitigating knowledge obsolescence.

#### TOOLUNIVERSE: A universe of tools and machine learning models

TOOLUNIVERSE is a suite of 211 biomedical tools that integrate with TXAGENT. It covers a wide range of categories (Figure 1c), including adverse events, risks, and safety; addiction and abuse; drug usage in specific populations; drug administration and handling; pharmacology; drug mechanisms and composition; ID and labeling tools; general clinical annotations; clinical laboratory information; patient and caregiver resources; pairwise disease, phenotype, target, and drug associations; biological annotation tools; publication information; search tools; and target characterization. Tools in TOOLUNIVERSE are built on APIs from trusted sources, including openFDA [20], Open Targets [21], and the Monarch Initiative [22]. Extended Data Figure 3 provides a detailed breakdown of TOOLUNIVERSE tools.

TOOLGEN agents generate a dataset of tool specifications used to create TOOLUNIVERSE. The TOOLGEN system constructs tools in TOOLUNIVERSE using a multi-agent approach that converts API documentation into structured tool specifications (Extended Data Figure 2a). API documentation varies widely in format and content, making direct integration with TXAGENT challenging. TOOLGEN standardizes this process by organizing API functions into well-defined tools with clear, concise descriptions that TXAGENT can interpret. The system operates in four stages:

- 1. Capability summarization: The SUMMARIZER agent extracts and condenses API documentation to identify the API’s core functionalities.
- 2. Tool generation: The TOOL GENERATOR agent translates these capabilities into structured tool specifications. Each tool specification includes a description for TXAGENT’s function calls and a mapping rule that converts function calls into API requests. The tool description defines the tool’s name, purpose, input arguments, data types, and mandatory parameters (examples in Figure 1b and Extended Data Figure 1).
- 3. Tool validation: The TOOL CHECKER agent generates test cases with predefined queries and function calls to verify the tool’s functionality.
- 4. Human verification: Experts manually review and refine tools to ensure correctness, meaningful applications, and robustness to unexpected inputs.


The SUMMARIZER, TOOL GENERATOR, and TOOL CHECKER agents operate by prompting the LLM with specialized instructions. Online Methods Section 2.2 provides additional details about

the TOOLGEN system.

#### TXAGENT-INSTRUCT dataset of therapeutic tasks and reasoning traces

We construct TXAGENT-INSTRUCT, a multi-step reasoning and function call training dataset (Figure 2d). TXAGENT-INSTRUCT consists of three datasets: a tooling dataset, a therapeutic question dataset, and a reasoning trace dataset, generated by three agent systems (Extended Data Figure 2). The tooling dataset contains augmented versions of 211 tools from TOOLUNIVERSE. Each tool description is rephrased to introduce variability, ensuring that TXAGENT learns tool usage rather than memorizing specific descriptions. The therapeutic question dataset includes 85,340 questions and functional instructions generated by the QUESTIONGEN agent system to train TXAGENT’s reasoning capabilities. The reasoning trace dataset comprises 85,340 detailed reasoning traces that contain 177,626 reasoning steps and 281,695 function calls, all generated by the TRACEGEN agent system. Processing these three datasets (as detailed in Online Methods Section 4.1) results in TXAGENT-INSTRUCT, which includes 378,027 instruction-tuning samples. The agent systems generate training data by sampling drugs and disease information from verified biomedical sources. Drug data is obtained from FDA drug labeling documents [20], while disease information is sourced from PrimeKG [28]. Drug-disease, phenotype, and target associations are compiled from Open Targets [21].

QUESTIONGEN agents generate a dataset of therapeutic questions. QUESTIONGEN constructs therapeutic questions with treatment, disease, and drug-related information. Training TXAGENT requires a large dataset of questions that address various forms of therapeutic reasoning, including patient populations, drug side effects, and drug interactions. Manually generating these questions is infeasible. Instead, QUESTIONGEN, a multi-agent system, generates meaningful questions from verified knowledge bases (Online Methods Section 3.2, Extended Data Figure 2b). QUESTIONGEN operates in three stages. First, the INFORMATION EXTRACTOR agent identifies and extracts key information from biomedical documents and data sources. Next, the QUESTION GENERATOR agent constructs questions using the extracted information and generates corresponding answers with detailed explanations that clarify how the answer addresses the question. Finally, QUESTIONGEN evaluates each question based on knowledge grounding, solvability, and reasonableness. Only validated questions proceed to the TRACEGEN system for reasoning trace generation.

TRACEGEN agents generate a dataset of therapeutic reasoning traces. To generate valid reasoning traces that integrate feedback from real-world tools, we design TRACEGEN, a multi-agent

system that constructs complex, step-wise reasoning traces (Extended Data Figure 2c). TRACEGEN produces training data for each question, including a reasoning trace and the final answer. Generating reasoning traces presents several challenges: (1) Complexity of questions: Many questions require multi-step reasoning and the analysis of multiple factors, making it difficult to generate a single direct answer. TRACEGEN must generate reasoning traces that effectively handle this complexity. (2) Integration of external tools: Effective reasoning requires incorporating real-world tools rather than relying solely on the internal knowledge of LLMs. TRACEGEN must integrate tool outputs into reasoning traces while ensuring consistency across sources. (3) Handling unpredictable tool outputs: External tools often produce unexpected results. TRACEGEN must manage failure cases, filter noisy outputs, and ensure that reasoning progresses toward a valid solution despite deviations in tool responses. TRACEGEN addresses these challenges using a multi-agent system consisting of the HELPER agent, the TOOL PROVIDER module, the SOLVER agents, and a reasoning trace evaluation step (Extended Data Figure 2c).

- • The HELPER agent provides the SOLVER with step-by-step hints, guiding the reasoning process based on previous steps. It has access to correct answers and explanations, ensuring alignment with expected outcomes.
- • The TOOL PROVIDER module identifies relevant tools based on the question and recommendations from TOOLRAG model, which iteratively improves tool selection accuracy by learning from previously generated data.
- • The SOLVER agent integrates information from the TOOL PROVIDER, HELPER, and existing reasoning traces to iteratively generate reasoning steps and function calls until reaching a final answer.
- • The evaluation step verifies the correctness of the answer, function calls, and reasoning process while detecting hallucinations, arbitrary outputs, and repetitive reasoning patterns.


Details of TRACEGEN are provided in Online Methods Section 3.3.

#### TXAGENT outperforms larger LLMs in multi-step reasoning

We construct the DrugPC (Drug Prescribing Card) benchmark to evaluate TXAGENT’s performance in drug reasoning. DrugPC includes 3,168 questions spanning 11 tasks: drug overview, ingredients, warnings and safety, dependence and abuse, dosage and administration, use in specific populations, pharmacology, clinical information, nonclinical toxicology, patient-focused information, and storage and supply. To mitigate data leakage from pretraining, we focus on drugs

approved by the FDA in 2024, reducing the likelihood that LLMs have encountered them. We exclude drugs approved after 2023 from the training set and use drugs approved in 2024 for evaluation. We perform instruction tuning on LLMs, such as the Llama-3.1-8B-Instruct model with 8 billion parameters, using TXAGENT-INSTRUCT to develop TXAGENT’s reasoning and tool-use capabilities. Training details are provided in Online Methods Section 4.3. We evaluate models in two settings: multiple-choice, where the model selects the correct answer from given options, and open-ended, where the model generates responses without predefined choices. By default, QUESTIONGEN generates questions with 4-5 options, verified by human experts. To create open-ended versions, we remove answer choices from the input. After generating a response, the model selects the correct option from the original choices based on its generated text. Table 3 provides examples of both formats. Further details on benchmark datasets and evaluation are in Online Methods Section 5.

TXAGENT is built on the Llama-3.1-8B-Instruct model, which has 8 billion parameters and is fine-tuned for multi-step reasoning and function call execution. We compare TXAGENT to larger models, including Llama3.1-70B-Instruct (70 billion parameters) and GPT-4o (Figure 1d). Despite its smaller size, TXAGENT consistently outperforms Llama3.1-70B-Instruct in both multiplechoice and open-ended tasks. In the multiple-choice setting, TXAGENT achieves 93.8% accuracy, surpassing Llama3.1-70B-Instruct’s 75.1%. In the open-ended setting, TXAGENT maintains

- 92.1% accuracy, while Llama3.1-70B-Instruct drops to 52.8%. Among baseline models, GPT-4o performs best, achieving 76.4% in multiple-choice and 66.3% in open-ended tasks. However, TXAGENT outperforms GPT-4o by 17.4% in multiple-choice and 25.8% in open-ended settings. By leveraging multi-step reasoning and executing function calls to TOOLUNIVERSE for verified information, TXAGENT surpasses larger models in accuracy and reliability. The open-ended setting is more challenging than the multiple-choice format, as models cannot rely on answer choices. GPT-4o and Llama3.1-70B-Instruct show accuracy drops of 10.1% and 22.3%, respectively, when switching to open-ended tasks. In contrast, TXAGENT exhibits only a 1.7% decline, highlighting its robustness in open-ended reasoning.


We evaluate performance across all 11 tasks in the DrugPC benchmark (Figure 2b,c). Although GPT-4o is the strongest baseline overall, it does not consistently outperform other models. For example, Llama3.1-70B-Instruct achieves higher accuracy than GPT-4o on the Warning and Safety task. In contrast, TXAGENT surpasses all baselines in all tasks, demonstrating its effectiveness in multitask drug reasoning. TXAGENT provides reasoning traces supported by verified

function call results, allowing users to assess the reliability of the response. In contrast, LLMgenerated outputs require manual verification, limiting trust without external validation.

#### TXAGENT outperforms tool-use LLMs in multi-step reasoning

We compare TXAGENT with tool-use LLMs that support function calling [11–13] (Figure 1e). Existing models focus on generating accurate function calls based on input questions and tool descriptions but lack the ability to handle complex problems requiring multi-step function calls, reasoning, and diverse tool integration. By incorporating multi-step reasoning and function call capabilities, TXAGENT provides key advantages over existing tool-use LLMs: (1) Expanded tool support: TXAGENT employs goal-oriented tool selection, enabling access to a large number of tools in TOOLUNIVERSE. In contrast, existing methods rely on including all tool descriptions in the context window, limiting the number of tools they can handle. Some tool-use LLMs [29] cannot support large-scale toolboxes like TOOLUNIVERSE. (2) Improved problem-solving: TXAGENT performs multi-round function calls to address complex problems. When a single function call does not provide sufficient information, TXAGENT reevaluates and selects alternative tools to refine its solution.

We compare TXAGENT against state-of-the-art tool-use LLMs, including ToolACE-8B [13] and WattTool-8B [12], both fine-tuned on the same Llama-3.1-8B-Instruct model as TXAGENT. To ensure a fair comparison, we provide all models with full access to TOOLUNIVERSE and enable multi-step reasoning. Since existing tool-use LLMs do not natively support multi-step reasoning but allow multi-round interactions, we simulate multi-step reasoning by feeding tool results back

- as user messages, allowing the LLM to continue function calls until reaching a final answer. Additionally, because most tool-use LLMs struggle with switching between function calls and answer generation, we introduce a special GIVEANSWER tool. This tool requires the model to invoke it with the final answer once problem-solving is complete, ensuring a structured response process.


TXAGENT achieves significantly higher accuracy than existing tool-use LLMs. In the multiple-

choice setting, TXAGENT outperforms ToolACE by 62.5% and WattTool by 59.1%. In the openended setting, TXAGENT surpasses ToolACE by 59.4% and WattTool by 55.0%. This performance gap arises from key limitations in existing tool-use LLMs: (1) Limited tool selection: These models struggle to handle many tools in a single context window and often fail to select the correct tool from hundreds available in TOOLUNIVERSE. (2) Single-round function calls: They fill in function arguments based only on the input question, without making additional calls to retrieve missing

information. (3) Ineffective multi-step reasoning: Lacking adaptive reasoning, they often repeat initial function calls instead of refining their approach based on previous results, leading to failures when reaching the maximum reasoning round limit.

We quantify these failures by tracking invalid answers—cases where the model cannot produce a valid response. WattTool-8B fails on 58.9% of multiple-choice and 56.6% of open-ended questions. ToolACE-8B fails on 63.1% and 60.7% of multiple-choice and open-ended questions, respectively. In contrast, TXAGENT employs multi-step reasoning, iterative function calls, and goal-oriented tool selection, allowing it to fully use TOOLUNIVERSE in therapeutic reasoning.

#### TXAGENT generalizes across drug name variants and descriptions

We evaluate TXAGENT’s ability to generalize across different drug representations. LLM-based models are sensitive to variations in how drugs are referenced [24], such as brand versus generic names. To test generalization, we construct three modified versions of the DrugPC benchmark: BrandPC, GenericPC, and DescriptionPC. BrandPC and GenericPC systematically replace drug names in DrugPC with their brand or generic equivalents. Questions that do not reference drug names remain unchanged, while those requiring conversion between brand and generic names are modified accordingly. Both datasets maintain the same number of samples as DrugPC. Sample questions are shown in Figure 3a.

DescriptionPC replaces drug names with detailed descriptions to assess generalization without explicit drug names, including indications, mechanisms of action, contraindications, and interactions. We removed DrugPC questions that became unanswerable after this transformation, resulting in 626 questions. Since multiple drugs may share similar descriptions, DescriptionPC introduces a two-step evaluation: (1) drug identification and (2) answer correctness (Figure 3b). In the first step, the model identifies the drug based on its description. The ground truth includes all drugs that could match the given description. In the second step, the model selects the correct answer to a multiple-choice question using its predicted drug name. If drug identification is incorrect, the answer is automatically marked incorrect, ensuring that predictions rely on accurate drug recognition.

TXAGENT achieves 93.6% accuracy on BrandPC and 93.7% on GenericPC, outperforming both pure LLMs and tool-use LLMs on both benchmarks (Figure 3a). Among pure LLMs, Llama3.1-70B-Instruct performs best on BrandPC (73.0%), while GPT-4o leads on GenericPC (77.3%). TXAGENT surpasses these top reference models by 20.6% and 16.4%, respectively.

Among tool-use LLMs, WattTool-8B achieves the highest accuracy, with 40.2% on BrandPC and 31.5% on GenericPC. TXAGENT outperforms these baselines by 53.4% and 62.2%, respectively. TXAGENT also exhibits lower performance variance across the original, BrandPC, and GenericPC datasets, with a variance of 0.00667. In contrast, GPT-4o has a variance of 9.96, Llama3.1-70BInstruct 2.42, WattTool-8B 13.07, and ToolACE-8B 1.05. These results demonstrate TXAGENT’s superior robustness and generalization across different drug name representations.

On the DescriptionPC benchmark (Figure 3b), when evaluating only answer correctness (without considering whether the model identifies the correct drug) TXAGENT achieves 90.4%, surpassing GPT-4o (85.9%) and Llama3.1-70B-Instruct (85.3%). However, models may be able to “guess” the answer to certain questions in DescriptionPC without first identifying the class of drugs being referenced, which limits model trustworthiness. Specifically, when requiring both correct drug identification and answer selection, accuracy drops significantly for Llama3.1-70BInstruct to 20.1%, indicating unreliable drug grounding. In contrast, TXAGENT maintains the highest performance at 56.5%, outperforming GPT-4o by 8.3%. For drug name identification alone, TXAGENT achieves the highest accuracy at 60.1%, compared to GPT-4o’s 55.8% and Llama3.170B-Instruct’s 23.6%. These results highlight TXAGENT’s stronger ability to reason over drugs and base decisions on correct information.

#### TXAGENT for precision treatment recommendation

We evaluate TXAGENT’s ability to provide personalized treatment recommendations using the TreatmentPC benchmark, which consists of 456 questions focused on specialized treatment scenarios. While multiple drugs may treat a single disease, patient-specific factors (such as pregnancy or comorbidities) require tailored drug selection and dosage adjustments. TreatmentPC assesses these cases by formulating questions that account for varying drug application conditions. We select drugs approved by the FDA in 2024, identify their indicated diseases, and analyze treatment options by comparing drug attributes. For example, among all available treatments, only one drug may be suitable for pregnant patients. This analysis is based on FDA documentation, including indications, usage in specific populations, safety warnings, precautions, and contraindications.

Using these drug-specific properties, we generate multiple-choice questions with 4-5 options, ensuring only one correct choice based on the patient’s condition. Questions also include scenarios where drug interactions must be considered, requiring the model to account for contraindications. We evaluate models in both multiple-choice and open-ended settings. In the multiple-choice for-

mat, the model selects the most appropriate drug from the given options. In the open-ended format, the model generates a treatment recommendation and later selects the correct answer from its own response. TreatmentPC measures TXAGENT’s ability to analyze patient conditions and recommend appropriate treatments. Further details on the benchmark dataset and evaluation methodology are in Online Methods Section 5.

TXAGENT outperforms LLMs and tool-use LLMs in TreatmentPC. TXAGENT achieves significantly higher accuracy than its fine-tuning base model, Llama-3.1-8B-Instruct (Figure 4a). In the multiple-choice setting, TXAGENT reaches 86.8% accuracy, surpassing Llama-3.1-8BInstruct’s 56.1%. In the open-ended setting, TXAGENT attains 75.0%, outperforming Llama-3.18B-Instruct’s 33.11%. Compared to larger LLMs, TXAGENT maintains superior performance. In the multiple-choice setting, it outperforms GPT-4o by 12.7% and Llama-3.1-70B-Instruct by 16.4%. The gap widens in the open-ended setting, where TXAGENT exceeds GPT-4o by 13.6% and Llama-3.1-70B-Instruct by 25.4%. Even in the open-ended setting, TXAGENT (75.0%) surpasses GPT-4o’s multiple-choice accuracy (74.1%), despite the latter benefiting from predefined answer choices.

TXAGENT also outperforms tool-use LLMs (Figure 4b). ToolACE-8B and WattTool-8B, fine-tuned on the same Llama-3.1-8B-Instruct model and given full access to TOOLUNIVERSE, perform significantly worse. In the multiple-choice setting, WattTool-8B achieves only 18.2%, while TXAGENT reaches 86.8%. In the open-ended setting, ToolACE-8B scores 13.4%, compared to TXAGENT’s 75.0%. As observed in DrugPC, TXAGENT’s advantage stems from its multi-step reasoning capabilities. It integrates information from multiple sources, executes iterative function calls, refines queries when initial tool calls return empty results, and dynamically adjusts its approach. These strengths enable TXAGENT to solve complex treatment recommendation tasks more effectively than existing tool-use LLMs.

TXAGENT outperforms reasoning LLMs, including DeepSeek-R1. Recent reasoning LLMs, such as DeepSeek-R1 [26] and GPT-o1 [30], are designed for long chain-of-thought reasoning and test-time scaling. Since TreatmentPC requires multi-step reasoning over patient conditions and drug effects, we compare TXAGENT with DeepSeek-R1 models (Figure 4c). To enable multistep reasoning in DeepSeek-R1, we explicitly prompt it to generate reasoning steps using special tokens <think> and <\think>. Despite DeepSeek-R1’s full model having 671 billion parameters, TXAGENT outperforms it by 10.3% in the multiple-choice setting (86.8% vs. 76.5%) and by 7.5% in the open-ended setting. Extended Data Figure 5 shows the comparison between Deepseek-R1

and TxAgent. Deepseek-R1 relies on internal knowledge for reasoning, risking hallucinations and misjudgments. In contrast, TxAgent bases its reasoning on trusted sources, such as FDA drug labels, minimizing the risk of hallucinations and ensuring more reliable conclusions.

TXAGENT also surpasses distilled variants, including DeepSeek-R1-Llama-8B/70B, which are trained on Llama-3.1-8B and Llama-3.1-70B. Against DeepSeek-R1-Llama-8B, which shares the same base model as TXAGENT, TXAGENT achieves accuracy gains of 36.1% in multiplechoice and 34.9% in open-ended tasks. Unlike reasoning LLMs that rely solely on internal knowledge, TXAGENT integrates multi-step reasoning with verified external information from TOOLUNIVERSE, making it more effective for specialized treatment recommendation tasks.

#### Examples of TXAGENT reasoning traces for specialized treatments

We present detailed TXAGENT reasoning traces for four personalized treatment questions, evaluating its ability to incorporate drug mechanisms, drug-drug interactions, comorbidities, and clinical guidelines for specific patient groups, including elderly and pediatric patients.

- (1) Treatment selection based on drug mechanism and pediatric use. Figure 4d presents a case of a pediatric male patient with Duchenne muscular dystrophy (DMD) seeking treatment. The patient does not want steroid-based therapies due to side effects, including weight gain and mood changes [31], and is ineligible for exon-skipping antisense oligonucleotides, which are effective only for specific genetic mutations [32]. TXAGENT must identify an appropriate non-steroidal, non-exon-skipping treatment. TXAGENT first calls TOOLRAG model to find tools that identify drugs based on indications. It selects get drug names by indication and retrieves ten DMD drugs. Analyzing the results, TXAGENT determines that Duvyzat is the only drug meeting the patient’s criteria. To assess pediatric suitability, TXAGENT calls get drug name by pediatric use, but this tool does not return relevant information. TXAGENT then queries TOOLRAG model again for tools related to pediatric guidelines and selects get pediatric use by drug name, which confirms that Duvyzat is safe for children over six years old. Based on this reasoning, TXAGENT confidently recommends Duvyzat for this patient. This case study highlights TXAGENT’s ability to distinguish drugs by mechanism despite similar indications and to integrate mechanistic considerations with personalized factors such as pediatric safety.

- (2) Treatment selection considering drug-drug interactions. Figure 4e examines a treatment decision that involves drug-drug interactions. The patient is currently taking Prozac (fluoxetine hydrochloride) for Major Depressive Disorder and is considering adding Xolremdi (mavorixafor)


for WHIM syndrome. TXAGENT assesses whether these medications can be taken together. TXAGENT first queries TOOLRAG model for tools related to drug indications and contraindications. It simultaneously calls get indications and get contraindications for Xolremdi. The retrieved data confirm that Xolremdi is indicated for WHIM syndrome but is contraindicated with drugs dependent on CYP2D6 for clearance. Xolremdi inhibits CYP2D6, reducing its enzyme activity and prolonging the presence of drugs metabolized by CYP2D6 in the body.

To determine whether this contraindication applies to Prozac, TXAGENT calls get drug interactions, which reveals that Prozac is both a substrate and an inhibitor of CYP2D6. This presents two potential drug-drug interactions: (1) Direct contraindication: Prozac is metabolized by CYP2D6, and since Xolremdi inhibits this enzyme, Prozac exposure would increase, potentially leading to adverse effects. (2) Compounded inhibition: Both Prozac and Xolremdi reduce CYP2D6 activity. Their combined effect could further affect the metabolism of CYP2D6, increasing exposure to other drugs metabolized with CYP2D6. Based on these interactions, TXAGENT concludes that taking Prozac and Xolremdi together is not suitable for the patient. This case highlights TXAGENT’s ability to analyze drug-drug interactions through multi-step reasoning and detailed biological insights retrieved from TOOLUNIVERSE.

- (3) Treatment selection considering geriatric use. Figure 4f examines TXAGENT’s ability to consider geriatric-specific treatment adjustments. A 70-year-old patient with schizophrenia seeks the maximum recommended dosage for Cobenfy (xanomeline and trospium chloride), a recently approved drug. Since the dosage can be adjusted based on patient response, TXAGENT must determine the appropriate upper limit and provide justification. TXAGENT first calls TOOLRAG model to retrieve relevant dosage- and age-related tools from TOOLUNIVERSE. It then selects and executes get dosage and storage info and get geriatric use info. The dosage tool confirms that the maximum recommended dose for elderly patients is 100 mg/20 mg twice daily, lower than the 125 mg/30 mg twice daily recommended for younger patients. The geriatric use tool explains that this adjustment is due to an increased risk of urinary retention in elderly patients. TXAGENT synthesizes these findings and provides a final answer with supporting evidence. This case study highlights TXAGENT’s ability to conduct parallel reasoning threads—both identifying and explaining the maximum dosage—by executing multiple tool calls simultaneously. It also demonstrates how TXAGENT integrates verified external information to deliver patient-specific, evidence-based treatment recommendations.

- (4) Treatment selection considering comorbidities. Figure 4g demonstrates TXAGENT’s ability


to incorporate comorbidities into treatment recommendations. The patient has two cardiac conditions: second-degree AV block, which disrupts electrical signaling in the heart, and hypertension. TXAGENT is tasked with identifying an appropriate hypertension treatment while considering the AV block. TXAGENT first retrieves indication-related tools using TOOLRAG model. It calls get drug names by indication to identify ten potential hypertension treatments. Next, it filters these candidates based on contraindications for AV block. Using get drug name by contraindication with the argument “AV block,” TXAGENT searches FDA-approved drug labels for contraindications. The results show that two of the retrieved hypertension drugs are contraindicated for patients with second-degree AV block. TXAGENT then summarizes the mechanisms of the noncontraindicated drugs and provides them as the final answer. This case study highlights TXAGENT’s ability to integrate comorbidity considerations into treatment recommendations and efficiently search and filter drug candidates using FDA drug labels.

#### Impact of tools in TOOLUNIVERSE on TXAGENT’s performance

We evaluate two factors: the reliability of tools compared to language model-based alternatives and the effect of expanding TOOLUNIVERSE on agent’s performance.

TOOLUNIVERSE tools provide more accurate information than LLMs. TOOLUNIVERSE improves TXAGENT’s reasoning accuracy by integrating verified knowledge sources through specialized tools. We compare its effectiveness against an LLM-only approach, where the model mimics tool functionality by receiving structured prompts that describe each tool’s capabilities and arguments (Figure 3c, Online Methods Section 6.1). GPT-4o and Llama 3.1-Instruct-8B serve as the backend LLMs in this analysis, with all other settings unchanged. Replacing real tools in TOOLUNIVERSE with LLM-based tools significantly reduces accuracy. On DrugPC, using Llama3.18B-Instruct as tools lowers accuracy from 93.8% to 68.7% (-25.1%), while using GPT-4o results in 72.7% (-21.1%). Although GPT-4o performs better, both models remain inferior to TOOLUNIVERSE, demonstrating the limitations of LLM-only approaches in retrieving precise biomedical information. We observe a similar pattern on TreatmentPC. GPT-4o and Llama3.1-8B-Instruct achieve 67.11% and 74.78% accuracy, respectively, compared to 86.84% with real tools in TOOLUNIVERSE. While advanced LLMs improve factual consistency, they still underperform compared to real-world tools. TOOLUNIVERSE ensures verifiable results, allowing users to validate TXAGENT’s reasoning trace and final outputs.

###### Scaling TOOLUNIVERSE improves performance. We evaluate the effectiveness and scalability

of TOOLUNIVERSE by measuring how performance changes as more tools are added. We construct four subsets containing 10%, 20%, 50%, and 75% of TOOLUNIVERSE, ensuring each larger subset includes all tools from the smaller ones. This approach allows us to assess the incremental impact of adding tools while maintaining continuity across evaluations. Using TXAGENT equipped with each subset and the full TOOLUNIVERSE, we measure accuracy on the DrugPC and TreatmentPC benchmarks (Figure 3d). Accuracy on DrugPC increases from 78.4% with 10% of the tools to

- 93.8% with the full selection. A similar trend is observed on TreatmentPC, where accuracy rises from 71.7% to 86.8%. These results demonstrate that expanding TOOLUNIVERSE consistently improves TXAGENT’s ability to handle complex, specialized treatment tasks. The critical role of reasoning in TXAGENT


This section evaluates the role of reasoning in TXAGENT through three experiments. First, we assess the impact of thought generation by removing this process. Second, we examine how the number of reasoning steps in training data affects performance by limiting the maximum reasoning traces. Finally, we evaluate the influence of reasoning during inference by imposing a step limit, forcing TXAGENT to generate a final answer after a predefined number of steps.

Explicit thought generation drives reasoning in TXAGENT. We evaluate the impact of thought generation by comparing TXAGENT with and without this process on the DrugPC and TreatmentPC benchmarks, using accuracy as the metric (Figure 3e). Unlike existing tool-use LLMs that generate only function calls, TXAGENT produces both reasoning thoughts and function calls

- at each step. To assess the importance of thought generation, we modify TXAGENT to generate only function calls without intermediate reasoning. At the final step, it directly outputs the answer instead of reasoning through function calls. We implement this by removing the thought process from the TXAGENT-INSTRUCT dataset (Online Methods Section 6.2). Eliminating thought generation reduces accuracy on DrugPC from 93.8% to 71.5% (-22.3%) and on TreatmentPC from 86.4% to 64.9% (-21.5%). This decline demonstrates the critical role of explicit reasoning in TXAGENT and its advantage over tool-use LLMs that rely solely on function calls. Long multi-step training traces improve performance on complex tasks. We evaluate how the number of reasoning steps in TXAGENT’s training data affects its performance on the DrugPC and TreatmentPC benchmarks, using accuracy as the metric (Figure 3f). TXAGENT acquires multi-step reasoning through fine-tuning on the TXAGENT-INSTRUCT dataset. To assess the impact of reasoning depth, we filter training data to retain samples with at most 1, 3, or 5 reasoning steps, or all


available steps (Online Methods Section 4.1). During inference, TXAGENT remains unrestricted in the number of reasoning steps it can take. Reducing reasoning steps in training significantly decreases performance. A model trained with only 1 reasoning step sees accuracy drop from 86.8% to 66.9% on TreatmentPC and from 93.8% to 71.6% on DrugPC. The decline is more pronounced on TreatmentPC, indicating that complex treatment decisions require stronger multi-step reasoning. These results demonstrate that deeper reasoning traces during training improve TXAGENT ’s ability to handle complex therapeutic tasks.

Longer inference traces improve performance. We assess the impact of reasoning depth during inference by imposing a step limit on TXAGENT, using the TreatmentPC benchmark and accuracy as the evaluation metric (Figure 3g). TXAGENT is trained on the full TXAGENT-INSTRUCT dataset but is restricted to a maximum number of reasoning steps at inference. As described in Algorithm 1, instead of allowing TXAGENT to autonomously determine when to generate the special token [FinalAnswer], we enforce this token when TXAGENT reaches the step limit, instructing it to produce the final answer based on the accumulated reasoning trace. For reasoning traces shorter than the limit, the inference process remains unchanged. Accuracy improves as the reasoning step limit increases. When restricted to a single step—equivalent to conventional LLMs that generate direct answers—TXAGENT achieves 73.5% accuracy, 13.3% lower than its unrestricted multi-step reasoning configuration. Performance continues to improve with additional steps, showing notable gains up to five steps, after which improvements plateau. The diminishing returns beyond five steps suggest that most essential reasoning occurs within this range, though maintaining full reasoning capacity remains optimal.

As a reference, we present the average number of reasoning steps and tool calls for TXAGENT in Extended Data Figure 4. The TreatmentPC benchmark requires more reasoning steps than the DrugPC benchmarks, suggesting that precise treatment recommendations require more reasoning steps before reaching a conclusion. Similarly, the TreatmentPC benchmark involves a greater number of tool calls compared to DrugPC. When comparing multiple-choice and openended settings, DrugPC shows no significant difference in reasoning steps or tool calls. However, in the open-ended setting, TreatmentPC requires a significantly larger number of reasoning steps and tool calls compared to the multiple-choice setting.

## Discussion

TXAGENT is an AI agent that applies multi-step reasoning and tool usage to solve therapeutic problems, including drug prescriptions and disease treatment recommendations, while considering patient-specific factors. Unlike conventional models that produce probability scores without explanations, TXAGENT generates a reasoning trail along with its answer, making its decision-making process transparent and interpretable. TXAGENT integrates external tools from TOOLUNIVERSE to retrieve real-time biomedical knowledge, overcoming the limitations of LLMs that rely solely on static training data. This enables TXAGENT to recommend newly approved drugs, assess indications, and provide evidence-based prescriptions. By grounding the responses in verified sources, TXAGENT allows users to trace each decision step in a transparent manner.

Treatment decisions must account for patient-specific factors, including age, comorbidities, pregnancy status, disease severity, and immune function. Existing models predict disease-drug links but fail to consider these variations. TXAGENT addresses this limitation through dynamic, multi-step reasoning. It identifies the disease based on phenotypes, retrieves potential treatments by considering associated phenotypes and biological targets, and evaluates drug suitability based on patient characteristics. Rather than following a fixed sequence, TXAGENT adapts its reasoning through iterative function calls to biomedical tools, ensuring decisions are grounded in verified sources such as FDA drug labels. For example, TXAGENT determines that Xolremdi, a treatment for WHIM syndrome, should not be used with Prozac, a CYP2D6 inhibitor, because it alters Xolremdi’s metabolism. By integrating patient-specific constraints into its reasoning process, TXAGENT ensures clinically relevant and personalized treatment recommendations.

TXAGENT’s limitations highlight areas for future research. It relies on tool calls for external information, but gaps in TOOLUNIVERSE restrict access to specific data types, limiting its ability to address a broader range of questions. Uncertainty quantification in TXAGENT’s internal knowledge remains a challenge. The current approach grounds reasoning through external tools, improving verifiability. However, integrating internal knowledge with tool feedback could enhance flexibility for exploratory tasks. TXAGENT processes only natural language inputs and does not yet support other modalities such as pathology images, EHR data, or web-based lab results. Expanding multi-modal support would enable TXAGENT to handle more complex cases and specialized clinical analyses.

TXAGENT is an AI agent for therapeutic reasoning that leverages a universe of tools to generate transparent reasoning traces grounded in multi-source medical evidence and continuously

updated medical knowledge. It integrates verified information from FDA drug labels, Open Targets, and other trusted sources to produce evidence-based therapeutic recommendations. Future advances in integrating clinical modalities and extended memory for patient histories could allow TXAGENT to analyze multi-modal clinical data [33]. TXAGENT establishes a new framework for precision therapeutics by advancing personalized therapy selection and supporting regulatorycompliant clinical decision-making.

Data and code availability. The project page is available at https://zitniklab.hms.harvard.edu/Tx Agent. The code and demo of TXAGENT are available at https://github.com/mims-harvard/TxAge nt. The code of TOOLUNIVERSE is available at https://github.com/mims-harvard/ToolUniverse. The pre-trained models are available at https://huggingface.co/collections/mims-harvard/txagent -67c8e54a9d03a429bb0c622c.

Acknowledgements. We gratefully acknowledge the support of NIH R01-HD108794, NSF CAREER 2339524, US DoD FA8702-15-D-0001, Harvard Data Science Initiative, Amazon Faculty Research, Google Research Scholar Program, AstraZeneca Research, Roche Alliance with Distinguished Scientists, Sanofi iDEA-iTECH, Pfizer Research, Gates Foundation (INV-079038), Chan Zuckerberg Initiative, John and Virginia Kaneb Fellowship at Harvard Medical School, Biswas Computational Biology Initiative in partnership with the Milken Institute, Harvard Medical School Dean’s Innovation Fund for the Use of Artificial Intelligence, and Kempner Institute for the Study of Natural and Artificial Intelligence at Harvard University. Any opinions, findings, conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the funders. We thank Owen Queen and Thomas Hartvigsen for their helpful discussion and feedback on our project.

DISTRIBUTION STATEMENT A. Approved for public release. Distribution is unlimited. This material is based upon work supported by the Under Secretary of Defense for Research and Engineering under Air Force Contract No. FA8702-15-D-0001. Any opinions, findings, conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the Under Secretary of Defense for Research and Engineering.

Competing interests. The authors declare no competing interests.

![image 1](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile1.png)

![image 2](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile2.png)

![image 3](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile3.png)

a

Tool use through function calls

Patient information

![image 4](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile4.png)

Answer Reasons

Reasoning Tx

![image 5](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile5.png)

211 tools

![image 6](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile6.png)

![image 7](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile7.png)

Disease understanding

![image 8](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile8.png)

Reasoning trace

![image 9](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile9.png)

TxAgent

ToolRAG ToolUniverse

Finish tool

Mechanism of drug action

![image 10](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile10.png)

![image 11](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile11.png)

Therapeutic reasoning

![image 12](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile12.png)

Prompt

Feedback

{name: get_associated_targets_by_disease_efoID description: Find targets associated with a specific disease or phenotype based on EFO ID. input: EFO ID} {name: get_contraindications_by_drug_name description: Retrieve contraindications information based on the drug name. input: Drug name} {name: get_associated_diseases_by_HPO_ID description: Retrieve diseases associated with a list of phenotypes by the phenotype HPO IDs. input: HPO ID}

###### b

![image 13](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile13.png)

52 tools

![image 14](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile14.png)

![image 15](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile15.png)

156 tools

![image 16](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile16.png)

![image 17](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile17.png)

3 tools

Machine learning models

{name: Tool_RAG description: Retrieve related tools from the toolbox based on the provided description. input: Description}

![image 18](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile18.png)

1 tool

###### d

###### c eOpen-ended

Drug handling, administration

Multi-choice questions

Open-ended reasoning

Drug, target, phenotype, disease information

Multi-choice questions

Drug labels and drug identification

reasoning

Pregnancy Pediatric use

No tools Uses tools

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


![image 19](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile19.png)

![image 20](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile20.png)

![image 21](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile21.png)

| |tric use| | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


![image 22](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile22.png)

Geria

Use in specific populations

Adverse reactions, risks, and safety

![image 23](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile23.png)

![image 24](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile24.png)

g h i

###### f

Continually updated knowledge bases

Knowledge grounding using tools

Goal-oriented tool selection

Problem solving with multi-step reasoning

What is the indication for the newly approved Bizengri?

What adverse reactions should be considered when taking Alyftrek?

Identify protein targets for breast cancer.

What is the recommended dosage of Kisunla?

![image 25](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile25.png)

Tx

Tx

Tx

Tx

I need a tool that identifies adverse reactions.

I will use get_disease_id_desc to find the EFO ID for breast cancer.

I need to get dosage information about Kisunla.

I need to retrieve info about Bizengri.

get_disease_id_desc: “breast cancer”

get_dosage: “Kisunla” ToolRAG: “tools for adverse reactions”

ToolRAG: “info on newly approved drugs, incl. indications”

“…ID: EFO_0000305. Name: breast carcinoma. Description:…”

“The recommended dosage of Kisunla is 700 mg administered as an intravenous infusion over approximately…”

“get_adverse_reactions, get_when_using_info, …”

– OpenTargets The efoID is EFO_0000305. Now, I need to find associated targets.

Relevant TxToolbox tools

– TxToolbox

ToolRAG: “ID associated proteins” I will use get_indications

– FDA drug labels

I will use get_adverse_reactions get_adverse_reactions: “Alyftrek”

get_indications: “Bizengri”

Relevant TxToolbox tools I will use get_associated_targets.

Initial dosing is 700 mg administered over ~30 minutes every 4 weeks for the first 3 doses. After first 3 doses, 1400 mg every 4 weeks. Also, monitor for amyloid-related imaging abnormalities (ARIA).

“Bizengri is a bispecific antibody...”

get_associated_targets: “EFO_0000305” “…ID: ENSG00000139618. Symbol: BRCA2. Score: 0.923…”

Tx

Tx

– FDA drug labels Indications are nonsmall cell lung cancer and pancreatic adenocarcinoma in adults.

“In 5% of patients…”

– FDA drug labels

……

– OpenTargets

Most common adverse reactions include cough, nasopharyngitis, increased AST, and rash.

Some of the top targets are:

- 1. BRCA2: Involved in DNA repair
- 2. BRCA1: Involved in DNA repair
- 3. PIK3CA: PIK3 catalytic subunit


Tx

...

|Function call results|
|---|


|Answer|
|---|


Question Thought Function call

###### Figure 1

- Figure 1: a) TXAGENT processes specialized therapy-related questions, generating detailed step-by-step reasoning and conducting parallel function calls across a vast array of biomedical tools and specialized tools. It delivers solutions supported by clear, rational, and verified reasoning traces. b) Examples of tools in TOOLUNIVERSE and the machine learning tool. TOOLUNIVERSE consolidates 211 tools linked to trusted sources, including all US FDA-approved drugs since 1939 and validated clinical insights from Open Targets and Monarch Initiative. The machine learning tool, e.g., TOOLRAG model, is based on a machine learning model instead of APIs. c) TOOLUNIVERSE includes 211 biomedical tools that address various aspects of drugs and diseases. It covers the following categories: adverse events, risks, safety; addiction and abuse; drug usage in patient populations; drug administration and handling; pharmacology; drug use, mechanism, composition; ID and labeling tools; general clinical annotations; clinical laboratory info; general info for patients and relatives; disease, phenotype, target, drug links; biological annotation tools; publications; search; target characterization. d) TXAGENT demonstrates superior performance compared to LLMs with a larger number of parameters, such as GPT-4o, excelling in both open-ended and multiplechoice questions. e) TXAGENT demonstrates superior performance compared to tool-use LLMs that also have full access to TOOLUNIVERSE, excelling in both open-ended and multiple-choice questions. f-i) Capabilities of TXAGENT: knowledge grounding using tool calls, goal-oriented tool selection, problem solving with multi-step reasoning, and leverage constantly updated knowledge base. f) Knowledge grounding using tool calls, where TXAGENT utilizes tools to obtain verified knowledge and provides outputs based on it.


- g) Goal-oriented tool selection, where TXAGENT proactively requests tools from TOOLUNIVERSE using the TOOLRAG model model and selects and applies the most suitable tool from the available candidates.
- h) Problem solving with multi-step reasoning, where TXAGENT manages complex tasks or unexpected responses from tools through multiple iterations of thought and function calls. i) Leveraging constantly updated knowledge bases, where TXAGENT accesses continuously updated databases via tools to handle problems that go beyond the TXAGENT’s intrinsic knowledge.


###### a

TraceGen Reasoning trace generation

QuestionGen Question generation

ToolGen Tool generation

![image 26](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile26.png)

![image 27](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile27.png)

![image 28](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile28.png)

211 Tools 85,340 Questions 85,340 Reasoning traces

###### Tool specification

###### Question Reasoning trace

Question: Which pain medication should be avoided in a 60-year-old female with rheumatoid arthritis and a recent myocardial infarction? Options:

Tool description

Thought: Find tools to identify drugs based on conditions. Tool call: … Tool results: … Thought: Identify pain management drugs for rheumatoid arthritis. Tool call: … Tool results: … Thought: Retrieve cardiovascular risk warnings for each drug. Tool call: … Tool results: … Thought: Determine which drug to avoid for a recent MI patient. Answer: Avoid Etodolac due to increased risk of reinfarction and cardiovascular death.

Name: get_drug_active_ingredient Description: Fetch active ingredients in a specific drug product. Arguments: drug_name

- A) Ondansetron Hydrochloride;
- B) Etodolac ER;
- C) Quetiapine Fumarate Correct Answer: B) Etodolac ER Explanation: Etodolac ER carries a boxed warning for increased cardiovascular thrombotic risk, making it unsuitable for a patient with a recent myocardial infarction.


Mapping between a tool in TxAgent and an external API

Tool API fields drug_name

brand_name generic_name

return active_ingredient

TxAgent-Instruct dataset

![image 29](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile29.png)

Reasoning steps: 177,626 Tool calls: 281,695

![image 30](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile30.png)

Instruction tuning Tx

![image 31](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile31.png)

TxAgent

- b DrugPC (multi-choice questions)

Product overview

IngredientsWarnings and safety

Drug dep. and abuse

Dosage and admin.

Usein specific pop. PharmacologyClinical infoNonclinical toxicology

Patientfocused info

Storage and supply

No tools

Uses tools

Uses tools

Uses tools

| | |
|---|---|
| | |
| | |
| | |
| | |


No tools

Uses tools

| | |
|---|---|
| | |
| | |
| | |
| | |


Product overview

IngredientsWarnings and safety

Drug dep. and abuse

Dosage and admin.

Usein specific pop. PharmacologyClinical infoNonclinical toxicology

Patientfocused info

Storage and supply

- c DrugPC (open-ended reasoning)


| | |
|---|---|
| | |
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |
| | |


###### Figure 2

- Figure 2: a) TXAGENT-INSTRUCT dataset is a diverse synthetic multi-step reasoning and massive function call training dataset anchored in biomedical knowledge. To generate TXAGENT-INSTRUCT, we construct three datasets—a tooling dataset, a comprehensive therapeutic question dataset, and a reasoning trace dataset—using the auxiliary agent systems. The tooling dataset consists of augmented versions of 211 tools from TOOLUNIVERSE. The comprehensive therapeutic question dataset includes 85,340 therapeutic questions and functional instructions designed to train TXAGENT’s abilities. These are generated by the QUESTIONGEN agent system. The reasoning trace dataset comprises 85,340 detailed reasoning traces for answering therapeutic questions. These traces collectively encompass 177,626 reasoning steps and 281,695 function calls, all generated by the TRACEGEN agent system. By processing the data from these three datasets, we construct TXAGENT-INSTRUCT, which comprises 378,027 instruction-tuning data samples. b) TXAGENT outperforms larger open-source LLMs and GPT-4 across 11 tasks from the DrugPC dataset, excelling in both open-ended and multiple-choice questions. These tasks cover various drug-related topics, including drug overview, ingredients, warnings and safety, dependence and abuse, dosage and administration, use in specific populations, pharmacology, clinical information, nonclinical toxicology, patient-focused information, and storage and supply. c) Across the 11 tasks of the DrugPC dataset, TXAGENT demonstrates superior performance compared to existing tool-use LLMs.


- a
- b

Q: What condition is imetelstat used to treat? A: myelodysplastic syndrome

GenericPC

Q: What condition is Rytelo used to treat? A: myelodysplastic syndrome

BrandPC

Choose between brand and generic drug name versions

DrugPC

Tools in ToolUniverse

| | |
|---|---|
| | |
| | |
| | |
| | |


No tools

Uses tools

| | |
|---|---|
| | |
| | |
| | |
| | |


- c d


![image 32](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile32.png)

![image 33](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile33.png)

No tools

Uses tools

![image 34](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile34.png)

Uses tools

DescriptionPC

Q: What impact does this oligonucleotide telomerase inhibitor have on fertility in females of reproductive potential according to animal studies? This drug is indicated for adult patients with low- to intermediate-1 risk myelodysplastic syndromes (MDS) with transfusion-dependent anemia. It works by inhibiting telomerase activity, reducing telomere length, and inducing apoptotic cell death. Notable adverse reactions include thrombocytopenia and neutropenia.

![image 35](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile35.png)

A: Drug: Rytelo (imetelstat) A: May impair fertility, but effect is reversible.

ToolUniverse versus LLM-as-a-tool

| | |
|---|---|
| | |
| | |
| | |
| | |


|Percentage of tools in ToolUniverse|
|---|


Percent se

ToolUniverse

e f g

| | |
|---|---|
| | |
| | |


| | |
|---|---|
| | |
| | |


| | |
|---|---|
| | |
| | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |


###### Figure 3

- Figure 3: a) TXAGENT surpasses both native and tool-use LLMs on the DrugPC benchmark, as well as its Brand and Generic variants, where drug names are replaced with their brand and generic counterparts. Additionally, TXAGENT demonstrates minimal variance when handling drug names with different representations. b) TXAGENT surpasses LLM in a two-step evaluation on the DescriptionPC benchmark, where drug names are replaced with their descriptions, including indications, mechanisms of action, contraindications, and interactions. In this evaluation, the first step involves identifying the correct drug name based on its description, followed by answering the question using the correctly identified drug name. c) Comparison of real-world tools from TOOLUNIVERSE versus relying on an LLM’s internal knowledge as a substitute for external tools on DrugPC and TreatmentPC benchmarks. When paired with TXAGENT, TOOLUNIVERSE tools provide more accurate information than using LLMs ike GPT-4o as tools. d) The impact of increasing the number of tools in TOOLUNIVERSE on the DrugPC and TreatmentPC benchmarks. As more tools are incorporated into TOOLUNIVERSE, the results consistently demonstrate steady and significant performance improvements. e) Explicit thought generation is fundamental to reasoning in TXAGENT. We evaluate TXAGENT with and without thought generation on the DrugPC and TreatmentPC benchmarks. The absence of thought generation results in a significant performance decline, underscoring its essential role in TXAGENT ’s reasoning process. f) Long multi-step traces in training data enhance TXAGENT ’s ability to handle complex tasks. We examine how the number of reasoning steps in TXAGENT ’s training data affects its performance on the DrugPC and TreatmentPC benchmarks. As the number of reasoning steps decreases, performance gradually declines, suggesting that more complex tasks demand a stronger multi-step reasoning capability from TXAGENT. g) Longer inference traces enhance model performance. To assess the impact of reasoning during inference, we impose a step limit on TXAGENT and evaluate its performance on the TreatmentPC benchmark. Results show a clear upward trend in accuracy as the number of reasoning steps increases, highlighting the importance of extended reasoning in TXAGENT ’s inference process.


a TreatmentPC Multi-choice questions

###### b

c TreatmentPC

TreatmentPC

d Multi-choice questions

Open-ended reasoning

|Multi-cho question|ice s|Open-ended reasoning|
|---|---|---|
| |![image 36](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile36.png)|![image 37](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile37.png)|


Open-ended reasoning

![image 38](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile38.png)

![image 39](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile39.png)

![image 40](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile40.png)

![image 41](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile41.png)

No tools Uses tools

| | |
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |


![image 42](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile42.png)

Drug mechanisms & pediatric use Geriatric use

###### d

###### e f

g Comorbidities

Drug-drug interactions

My patient has a second degree AV block and hypertension. Identify suitable drug treatments for their hypertension.

I have a pediatric patient with Duchenne muscular dystrophy. The patient cannot take steroid treatments for DMD due to the side effects. The patient’s genetic mutation profile also makes existing exon-skipping medications impractical. Please identify any non-steroidal, non-exonskipping treatments indicated for DMD, as well as the corresponding pediatric use guidelines. Make sure the identified drug has the correct indication and is not a steroid or exonskipping treatment.

A 30-year-old patient is taking Prozac to treat their depression. They also carry WHIM syndrome and require a treatment for that condition as well. Is Xolremdi suitable for this patient, considering contraindications?

My 70-year-old patient just started Cobenfy. What is his maximum recommended dosage for the drug and why?

###### Tx

###### Tx

I need to find tools that can provide drug dosage info based on age and specific conditions.

I need to gather information on drugs indicated for hypertension and are safe to use in patients with AV block.

###### Tx

I will start by retrieving tools to gather info on Xolremdi’s indications and contraindications.

ToolRAG: “Tool for drug dosage info based on age…”

ToolRAG: “Tool that retrieves a list of drugs for a specific medical condition…”

Relevant tools from TxToolbox

ToolRAG: “Tool for indications” ToolRAG: “Tool for contraindications”

I will retrieve relevant info using get_dosage_and_storage_info and get_geriatric_use_info

###### Tx

Relevant tools from TxToolbox I will use get_drug_names_by_indication get_drug_name_by_indication: “hypertension”

I need to gather info on drugs indicated for DMD and their usage guidelines.

Relevant tools from TxToolbox I will use the tools get_indications and get_contraindications. get_indications: “Xolremdi” get_contraindications: “Xolremdi”

get_dosage_and_storage_info: “Cobenfy” get_geriatric_use_info: “Cobenfy”

ToolRAG: “Tool that retrieves drug names based on indication”

“Enalapril maleate, vermapil hydrochloride, diltiazem hydrochloride,…”

Dosage: “…For geriatric patients, recommended starting dosage of COBENFY is 50 mg/20 mg orally twice daily. Consider a slower titration. The maximum recommended dosage is 100 mg/20 mg twice daily...”

Relevant tools from TxToolbox I need to use get_drug_names_by_indication. get_drug_names_by_indication: “Duchenne muscular dystrophy”

Indication: “…patients 12+ with WHIM syndrome…”

– FDA drug labels I have obtained a list of hypertension drugs. Next, we evaluate their use with AV block.

![image 43](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile43.png)

Contraindication: “…drugs highly dependent on CYP2D6 for clearance…”

“Indicated drugs include Duvyzat, Viltepso, Emflaza,…”

– FDA drug labels

Geriatric use: “There were insufficient numbers of elderly patients in clinical studies. Because Cobenfy can increase the risk of urinary retention in geriatric patients, including older males with bladder outlet obstruction due to benign prostatic hyperplasia (BPH), a slower titration and lower maximum dosage is recommended in geriatric patients.”

get_drug_name_by_contraindication: “AV block”

– FDA drug labels

Xolremdi is indicated for WHIM, contraindicated for drugs using CYP2D6-based clearance. I need to confirm if Prozac is dependent on CYP2D6 for clearance.

Vermapil hydrochloride: “Contraindicated in second-or-thirddegree AV block”

I have identified Duvyzat as a nonsteroidal, non-exon-skipping drug. Next, I must verify pediatric usage. get_drug_name_by_pediatric_use: “Duvyzat pediatric use guidelines” No useful info retrieved by tool call

Diltiazem hydrochloride: “Contraindicated in patients with cardiogenic shock, second or third degree AV block…”

get_drug_interactions: “Prozac”

“Prozac is a potent inhibitor of CYP2D6 pathway…Prozac is metabolized by CYP2D6…”

Since the tool call was not useful, I will explore alternative methods.

….

– FDA drug labels The maximum recommended dosage for Cobenfy in geriatric patients is 100 mg/20 mg orally twice daily. This dosage is lower…due to the increased risk of urinary retention.

– FDA drug labels

ToolRAG: “Tool for pediatric use…”

– FDA drug labels Prozac is a potent inhibitor of CYP2D6, which means that Xolremdi cannot be used safely with Prozac.

These two drugs are contraindicated for this patient, so I will suggest the others on the list

Relevant tools from TxToolbox

I can use get_pediatric_use_by_drug_name

The following drugs are indicated for hypertension without a contraindication for AV block:

get_pediatric_use_by_drug_name: “Duvyzat”

The maximum recommended dosage for Cobenfy for a 70-year-old patient is 100 mg/20 mg orally twice daily. This dosage is lower compared to younger adults due to the increased risk of urinary retention in geriatric patients, including older males with bladder outlet obstruction due to benign prostatic hyperplasia (BPH). A slower titration is also recommended for geriatric patients.

No, Xolremdi is not suitable for the patient. It is indicated for WHIM but contraindicated with drugs highly dependent on CYP2D6 for clearance. Prozac is metabolized by CYP2D6 and a potent inhibitor of this enzyme pathway. Therefore, there is potential for serious drug interactions.

“Safety and effectiveness in children age 6+ have been established....”

- 1. Enalapril maleate: ACE inhibitor commonly used to treat hypertension and generally safe for patients with AV block.
- 2. Amlodipine Besylate: Calcium channel blocker that is effective for hypertension and not contraindicated for AV block.
- 3. Valsartan: An angiotensin II receptor blocker…


– FDA drug labels

I have confirmed Duvyzat’s DMD indication and pediatric safety.

Duvyzat is a suitable non-steroidal, non-exon-skipping DMD treatment for patients age 6 years and older.

|Function call results|
|---|


|Answer|
|---|


Question Thought Function call

###### Figure 4

- Figure 4: a) Performance comparison between TXAGENT and large-scale LLMs on the TreatmentPC benchmark. Despite being based on an 8-billion-parameter model, TXAGENT outperforms larger LLMs such as GPT-4o and Llama 3.1-70B-Instruct in both open-ended and multiple-choice settings. Notably, in the open-ended setting, TXAGENT achieves a higher accuracy (75%) than GPT-4o does in the multiplechoice setting (74.1%), even though the latter benefits from predefined answer options that simplify the task. b) Performance comparison between TXAGENT and tool-use LLMs on the TreatmentPC benchmark. Although ToolACE-8B and WattTool-8B, like TXAGENT, are fine-tuned on Llama-3.1-8B-Instruct and have full access to the TOOLUNIVERSE, TXAGENT still achieves a significantly higher performance. c) Performance comparison between TXAGENT and reasoning LLMs (e.g., DeepSeek-R1) on the TreatmentPC benchmark. TXAGENT achieves superior performance compared to the full DeepSeek-R1 model and its two distilled versions based on Llama-3.1-8B and Llama-3.3-70B. d) TXAGENT identifies Duvyzat as the optimal treatment for a pediatric patient with Duchenne muscular dystrophy by evaluating drug mechanisms and pediatric use guidelines. e) TXAGENT evaluates the potential drug-drug interactions between Prozac and Xolremdi, highlighting the risks of combined use due to their effects on the CYP2D6 enzyme. f) TXAGENT provides personalized, evidence-based treatment advice for elderly patients, adjusting the maximum dosage of Cobenfy based on age-specific considerations and the associated risks. g) TXAGENT personalizes treatment recommendations by considering comorbidities, ensuring hypertension drugs are not contraindicated for a patient’s second-degree AV block.


##### a

###### Tool description Tool description

b

###### name:

get_active_ingredient_by_drug_name description:

###### name:

get_associated_phenotypes_by_disease_efoId

Fetch active ingredients in a specific drug product. arguments:

description: Find HPO phenotypes associated with the specified disease efoId.

drug_name: type: string description: The name of the drug. required: true

arguments: efoId:

type: string, description: The efoId of a disease or

limit: type: integer description: The number of records to return. required: false

phenotype. required: true

c d

Mapping between a tool in TxAgent and external APIs in OpenFDA

Mapping between a tool in TxAgent and external APIs in Open Targets

search_fields:

query diseaseAnnotation($efoId: String!) { disease(efoId: $efoId) {

drug_name: [ openfda.brand_name, openfda.generic_name

id name phenotypes { rows { phenotypeHPO {

]

return_fields: [ dosage_and_administration, how_supplied

id name description namespace} phenotypeEFO {

id name}} }}}

]

Extended Data Figure 1: Examples of tool specifications in TOOLUNIVERSE. Each specification includes a tool description, which serves as a reference for TXAGENT’s function calls, and a mapping rule that translates function calls into API requests. The tool description outlines the tool’s name, purpose, and the arguments it accepts, including details such as each argument’s name, purpose, data type, and whether it is mandatory. a) Tool description for the tool from OpenFDA. b) Tool description for the tool from Open Targets. c) Mapping between Tools in TxAgent and external APIs from from OpenFDA. d) Mapping between Tools in TxAgent and external APIs from from Open Targets.

- a
- b

Documentation

![image 44](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile44.png)

Discard

Question evaluation

![image 45](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile45.png)

Keep QG

![image 46](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile46.png)

New question

IE Documents

QuestionGen generate therapeutic questions

Information extractor Question generator

![image 47](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile47.png)

- c TraceGen agents generate therapeutic reasoning traces


ToolGen agents generate tools in ToolUniverse

![image 48](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile48.png)

![image 49](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile49.png)

![image 50](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile50.png)

###### S TG TC

Summarizer Tool generator Tool checker Human verifier

ToolUniverse

![image 51](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile51.png)

Explanation

Step-wise hint H

![image 52](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile52.png)

Question Helper Reasoning Keep

![image 53](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile53.png)

###### S

![image 54](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile54.png)

trace evaluation Reasoning trace

Discard

Solver

![image 55](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile55.png)

![image 56](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile56.png)

ToolRAG

![image 57](Gao et al._2025_TxAgent An AI Agent for Therapeutic Reasoning Across a Universe of Tools_images/imageFile57.png)

ToolUniverse Tool initialization

- Extended Data Figure 2: The multi-agent systems, (i.e., TOOLGEN, QUESTIONGEN, and TRACEGEN) that construct the TXAGENT-INSTRUCT training dataset for instruction tuning LLM to achieve the capabilities of TXAGENT. a) TOOLGEN: A tool generation multi-agent system that transforms APIs into 211 agent-compatible tools, aggregating them into the TOOLUNIVERSE. b) QUESTIONGEN: A question generation multi-agent system designed to extract critical information from documents (e.g., FDA drug documentation) and generate relevant questions. c) TRACEGEN: A reasoning trace generation multi-agent system, where a HELPER agent and a TOOL PROVIDER module assist the SOLVER agent in generating step-bystep reasoning and function calls to solve a problem.


efoId

g et_ ass oc ate

blId

g et_ ass

g et_si milar_ e ntities _ by _targ et_ e ns e m blID

efoId

g et_si

blId

blID

g et_ ass

efoId

g et_si

g

blID

g et_

efoId

et_joint_ ass

g et_si

blID

m

m

g et_

blID

m

m

dru

_

e

_

e

e

e

g et_

fects

_

e

m

e

milar_ e

e

- g

_c

- h


m

dru g

ns

- g

_c

- h


milar_ e

_info

- g

et_ p

- h ar


_

e

as

as

ociate

ns

m

ociate

a

- g _ p
- h ar


dru g _ n a

e

g

e

e

e

as

milar_ e

n

et_

ns

et_targ et_ h o m olo g u es_ by_ e nse m blID

as

m

e

ary

get_target_interactions_by_ensemblID

e

e

e

dru g _ n a

_

ns

e

e

dis

dis

g

e

_interactio

et_

a

dru

_targ

e

dru

g

e

use

_

et_similar_ e

dis

m

m

warning

et_

n

get_dosage_for

dru

dis

e

- d _

dru gs _ by

_targ et_

- e


nic

- d _ p h
- e n


- d

_targ ets _ by _ dru

- g _c
- h


- e m blId


ociate

ntities _ by _

_

_

_

a

_targ

me

_

m

get_dosage_and_storage_infor

ntities _ by _ dis e as e _

_

_

g

by

m

by

_

n

by

_targ

m

_

by

by

_

_

me

by_safety_su

get_drug_na

e

by

ntities _ by

m

dru

_

by

p

_

aco g e

by

warning_by_drug_na

by

g

ac o g e

_

g

get_drug_na

es

_

get_drug_names_by_overdosage_info

_

m e _

by_sto

_

es _ by

_terato

_

dru

gs

get_overdosage_info_by_drug_na

_

- d _ dis
- e as


ntities

profile

es

by

p

_

_

by_

get_asse

me

ntities

mes_by_residue_

by

ntities

oty

oty p

ets

fects

dru

ns _ by

as

get_calibration_instructions_by_drug_na me

_

me_by_other_safety_info

by_

_

by _ p h

n

get_other_safety_info_by_drug_na

- n
- o


ntities

_

es

ntities_

e

_targ

- n
- o


get_drug_na

me

- d

_

dis

- e


_ dru

h

es _

_info

_

_

dru

mes_by_dosage_for

mics_info _ by_

ms_and_strengths_by_drug_na me

p

e

_

by

ary_

as

_ dru

d

e

e

get_drug_na

mes_by_nonteratogenic_efects

e

_

e

afety

milar_

get_nonteratogenic_efects_by_drug_na

mics _ d

es

mbly_instalation_info_by_drug_na me

ociate

es _

m

milar_

_

milar_

- d

_

dis

- e


_

_

by _

- g _c
- h e m blId


ar m

me

get_dosage_and_storage_information_by_drug_na me

nic

g

as

d

es_

es

e

dru g _ n a

a

use

me_by_dosage_info

m

by_targ et_ e nse m blID

_interactio ns

ociate

milar_

- g _c
- h e m blId


- d

_

dis

- e


n

by _ H P O

ociate

get_nonclinical_toxicology_info_by_drug_na

get_storage_and_handling_info_by_drug_na me

mes_by_nonclinical_toxicology_info

m

dis e

et_s

e

m

_

ac o g e

m

g

et_si

g

_

a

get_drug_na

me

et_safety_su

ass

mes_by_asse

ociate

et_si

et_terato

et_si

ata

a

p

dru

n

ns e

efoId

as e _

ociate

n

get_lab_test_interference_info_by_drug_na

et_sto

_

et_targ

get_accessories_info_by_drug_na me

mes_by_lab_test_interference

ass

me_by_calibration_instructions

et_si

ass

_

get_drug_na

g

get_residue_

et_

mation_by_drug_na me

et_

m e

g

g

m bID

dru

get_drug_names_by_accessories

- n
- o mics


dru g _ n a

get_environmental_warning_by_drug_name

_ID _list

g

g

ms_and_strengths_info

dru

ass

et_

ass

efoId

et_

g

g

retrieve_device_use_by_drug_name retrieve_drug_name_by_device_use

get_drug_name_by_environmental_warning

et_

g

g

me_by_storage_and_handling_info

et_

et_

et_

g

g

g

g

get_drug_na

mbly_instalation_info

get_drug_names_by_carcinogenic_mutagenic_fertility_impairment_info

g

g

g

g

g

Dis e as

m e

ns

get_disposal_info_by_drug_name

get_carcinogenic_mutagenic_fertility_impairment_info_by_drug_name

profile

Drug-disease associations

fects

ociatio

get_drug_names_by_disposal_info

get_drug_names_by_contraindications

Drug-drug associations

Drug-target associations

Stop use info

get_drug_na

Safety summary

Pharmacogenomics

get_do_not_use_info_by_drug_name

get_drug_names_by_instructions_for_use

afety

T

e-dis e as

warning

arget-target associations

get_instructions_for_use_by_drug_name

get_contraindications_by_drug_name

e

get_drug_na

Overdosage info

ass

s

get_drug_na

nic

et

get_route_info_by_drug_name

get_drug_names_by_general_precautions

Other safety info

Targ

Dosing

e

get_drug_names_by_route

efects

get_general_precautions_by_drug_name

e

p

e/p h e n

g

oty

Nonclinicaltoxicology

get_precautions_by_drug_name

Residue

get_safe_handling_warnings_by_drug_name

Terato

Setup instructions

n

Labtestinterference

get_drug_name_by_precautions

Storage Accessories

get_drug_names_by_safe_handling_warning

e

Nonteratogenic

h

oty p e

warning

get_drug_id_description_by_name

get_drug_name_by_adverse_reaction

e/p

Associated

get_drug_names_by_alarm

get_drug_description_by_chemblId

as

mutagenic,fertility,impairmentinfo

ass

Disposal

e

get_alarms_by_drug_name

get_brand_name_generic_name

et-dis

Environmental

ociatio ns

Generalinstructions

get_known_drugs_by_drug_chemblId

get_adverse_reactions_by_drug_name

Contraindications

devices

Routeofadministration

get_drug_synonyms_by_chemblId

get_drug_adverse_events_by_chemblId

Targ

get_warnings_by_drug_name

get_drug_trade_names_by_chemblId

Safe handling

Precautions

Dis e

get_disease_description_by_efoId

get_warnings_and_cautions_by_drug_name

get_disease_id_description_by_name

get_user_safety_warning_by_drug_names

as e, p h e n

Carcinogenic,

Adverse events and alarms

Drugname/descriptionandIDmap

get_disease_synonyms_by_efoId

get_drug_names_by_food_safety_warnings

Drug ad

get_drug_name_by_set_id

get_drug_names_by_user_safety_warning

oty p

get_document_id_by_drug_name

get_drug_names_by_warnings_and_cautions

events,risks,safety

ministration and

Diseasename/descriptionandIDmap

get_drug_name_by_set_id

get_drug_withdrawn_blackbox_status_by_chemblId

e, targ et, dru

get_drug_warnings_by_chemblId

get_drug_name_by_document_id

get_drug_names_by_risk

get_drug_name_by_application_number_NUI_identifier_SPL_document_ID_SPL_set_ID

DruglabeldocumentandsetIDs

arningsandrisks

get_drug_names_by_boxed_warning

get_active_ingredient_application_number_manufacturer_name_NDC_number_administration_route_by_drug_name

handling

W

glinks

get_drug_name_by_warnings

Adverse

ID and labeling tools Drug patient populations

get_drug_names_by_application_number_manufacturer_name_NDC_number

App num., manufacturer name, other IDs

get_risk_info_by_drug_name

get_drug_name_by_application_number_NUI_identifier_SPL_document_ID_SPL_set_ID

get_HPO_ID_by_phenotype get_phenotype_by_HPO_ID

get_boxed_warning_info_by_drug_name

Phenotype name and ID map

search_category_counts_by_query_string

Search

Search tools

Targetcharacterization

Target name/description and ID map

multi_entity_search_by_query_string

get_target_id_description_by_name

T

arget therapeutic potential

Clinicallaboratoryinfo

andrelatives

get_target_constraint_info_by_ensemblID

get_target_synonyms_by_ensemblID

n

get_labor_and_delivery_info_by_drug_name get_drug_name_by_labor_and_delivery_info

get_target_enabling_packages_by_ensemblID

Publications

ositio

G e n

Addiction and abuse

Pregnancy

Biolo

get_target_tractability_by_ensemblID

Pharmacology

Microbiology

get_chemical_probes_by_target_ensemblID

get_drug_name_by_pregnancy_or_breastfeeding_info

- o

m

- p


eral

patients

get_drug_names_by_pregnancy_effects_info

get_drug_name_by_microbiology

Referencedocuments

gic al a n n

Labtests

get_pregnancy_or_breastfeeding_info_by_drug_name

c

get_microbiology_info_by_drug_name

clinical a n n

m,

Nursing mother Pediatric use

get_pregnancy_effects_info_by_drug_name

Generalinfofor

nis

Clinical studies

get_lab_tests_by_drug_name

get_drug_names_by_teratogenic_efects

get_drug_names_by_lab_tests

a

get_teratogenic_efects_by_drug_name

h

Publications

get_drug_name_by_pregnancy_or_breastfeeding_info

ec

get_drug_name_by_reference

otatio n to ols

get_reference_info_by_drug_name

Pharmacokinetics

Generalpatientpop.info

get_info_for_nursing_mothers_by_drug_name

m

patients

otatio ns

get_drug_names_by_clinical_studies

Pharmacodynamics

get_pregnancy_or_breastfeeding_info_by_drug_name

e,

get_clinical_studies_info_by_drug_name

Clinicalpharmacology

get_drug_names_by_info_for_nursing_mothers

us

Animalpharmacology

get_publications_by_disease_efoId

g

get_child_safety_info_by_drug_name

andinfofor

Dru

get_publications_by_drug_chemblId

Geriatric use

Consult doctor/pharmacist

get_publications_by_target_ensemblID

get_drug_names_by_child_safety_info

Controlled substance

Drug

S plin d exin g d ata ele m e nts a n d u

get_pharmacokinetics_by_drug_name

D e ar

get_drug_names_by_pediatric_use

get_drug_names_by_pharmacokinetics

get_pediatric_use_info_by_drug_name

Disease biological annotation

dependence

Drug abuse

get_pharmacodynamics_by_drug_name

h e

T

get_drug_names_by_population_use

get_population_use_info_by_drug_name

wners/caregivers

get_drug_name_by_pharmacodynamics

alth c are

arget biological annotation

display

get_drug_names_by_clinical_pharmacology

get_geriatric_use_info_by_drug_name

get_clinical_pharmacology_by_drug_name

get_drug_names_by_animal_pharmacology_info

Label

get_medication_guide_info_by_drug_name

get_drug_name_from_patient_package_insert

get_animal_pharmacology_info_by_drug_name

get_drug_names_by_geriatric_use

Ingredients

Mechanism of action

Drug

provid erle ter

get_drug_name_by_principal_display_panel

get_drug_name_by_dependence_info

efectivetime

Health claims

Questions

get_drug_names_by_medication_guide

get_dependence_info_by_drug_name

get_principal_display_panel_by_drug_name

drug

get_abuse_types_and_related_adverse_reactions_and_controled_substance_status_by_drug_name

Approval

get_info_for_patients_by_drug_name

me

Indication

Dru

Gene ontology

get_drug_na

m_drug_na

using

get_drug_names_by_abuse_info

o

nclassifie d

me

get_drug_na

a n

g p are

contact

Infofor

medication_info

get_abuse_types_and_related_adverse_reactions_and_controled_substance_status_by_drug_na me

medication_info_by_drug_na

- d rec
- e nt


status

me_by_abuse_types_and_related_adverse_reactions_and_controled_substance_status

while

get_controled_substance_

me_by_info_on_conditions_for_doctor_consultation

get_abuse_info_by_drug_na me

get_drug_names_by_info_on_consulting_doctor_pharmacist_for_drug_interactions

get_drug_na

nt c hild

get_contact_for_questions_info_by_drug_na me

me

get_patient_package_insert_fro

Avoid

mes_by_controled_substance_D E

me

get_info_on_consulting_doctor_pharmacist_for_drug_interactions_by_drug_na

sectio n

wners_or_caregivers

get_info_on_conditions_for_doctor_consultation_by_drug_na

me_by_abuse_types_and_related_adverse_reactions_and_controled_substance_status

c h a n g

get_drug_approval_status_by_che mblId

me

m olec ules

get_when_using_info

wners_or_caregivers_by_drug_na

mes_by_patient_

me

g et_ dru g _ n a m es_

ministration_route_by_drug_na

get_drug_na

es

g

e

et_spl_in d

m

get_efective_time_by_drug_na me

g et_

- es_ by_

- d
- e


ar_ h e

alth

_care _

provid er_le

ter_info

g

- et_spl_
- u


a

get_drug_na

g et_

- D
- E


e

g et_

n

nt

get_health_claims_by_drug_na me

blId

dru g _ n a

m

_

A_schedule_info_by_drug_na me

die

g

blId

- d
- e


a

g et_ dis e as e _

blID

g

mation_for_o

retrieve_patient_

dru

p are

n

- m

_

of_

actio

- n

g

et_

biolo

gic

al_

m

- o


g

m

ar_ h e

e

et_targ

g et_

g et_ dis e as e _ a nc

gre

_

et_rec e

exin g _ d

retrieve_drug_na

mber_ad

nclassifie d

m

e

m

g

m

by_

blId

g

- g

_c

- h


- m

bID

g

et_targ et_ g e

- n
- o


mes_by_efective_time

m

dru

a

e

nt_c

e

_in

et_ g e

A_schedule

alth _c

C_nu

e

h

n

e

dis e

m

e

when_using_info

by_spl_in d

_

ns

_c

_

ns

_

g

m

D

m

g et_

active

a

nt_info

N

mes_by_health_claim

g

hild _ m

et_ g e

e

me_

dru

by

mes_by_infor

et_targ

ata _

n

e

by

n

- d

els

_

by

_

- e


a

dru

e

nt_c h a n g

are _

get_drug_na

m

as e

manufacturer_na

_

atio

_

n

h

_

- n e _
- o


_

by

_

g

a

_

nt_info

_c

_sectio n _

ele m e

dis e as e

n

mation_for_o

_

- d esc
- e n d a


by

provid er_le

nis

dru

n

g

by_in

_

_th

actio

- n e _
- o


by

olec

die

dic

by

_

dru

ns

exin g _ d

_

mber_

a

g

ntolo gy

et_class

- es_

by_

active

_in

gre

die

nt

g

- et_


- m bID

g

et_targ et_ g e

- n e _
- o


ns

_

_

- m

c _

oc at o

- n _


era p e

gre

o

_

h

get_drug_na

dru

_in

nts_ by_ dru g _ n a m e

- es_

by_in

gre

die

nt

g

- et_in


ules _ by

n

by

get_active_ingredient_application_nu

_

of_

ns

ec

die

at

atio

estors _ p

_

es _ by

ntolo

actio

o

by

m

e

_in

_

oc

m

by

m

atio

_loc atio

_

_

m

by_ dru g _ n a m e

ata _

get_infor

gre

ntolo gy _ by _ e ns e m

m

ter_info _ by

a

nts

_

dic

by

ms

_

nts _c

utic _ are

_

active

n

a

ar_

_info

_

a

e

of_

_ter

gy _

by

_

n

get_

_ dru

_in

dic

n

es

us

die

ele m e

_

_in

_

nis

es _

g

_

_

dru g _ n a

ns

_

dru

u

g

_

g

m

are nts _ by _

e

by _ e

es

_in

d

hildre n _

dru

ms _

a

gre

et_

m

- g _c
- h e m


e

dru

activ

e

atio

e

- g

_

m

ec

- h


by _ e

ns _

a

et_

_

nts

bc

os

m

nis

prov

by _ e

dru g _ n a

g

n

as _

g

a

et_

u

dru

_

by _ g

ns e m

urp

g

dic

a

et_in

n

et_s

by _

g

- g

et_

m

ec

- h


p

ns e

_

by _

m e

dru

g

bl_ID

ns e

et_

a

g

by _

p

et_in

dru

m e

et_

dru

et_

efoId

et_targ

oID

g

blID

efoId

m blID

et_

efoId

g

efoId

et_

g

et_

g

blID

g

g

g

g

g

- Extended Data Figure 3: Categories of biomedical tools in TOOLUNIVERSE. TOOLUNIVERSE contains 211 biomedical tools and includes the following categories: adverse events, risks, safety; addiction and abuse; drug usage in patient populations; drug administration and handling; pharmacology; drug use, mechanism, composition; id and labeling tools; general clinical annotations; clinical laboratory info; general info for patients and relatives; disease, phenotype, target, drug links; biological annotation tools; publications; search; target characterization.


### a b

| | |
|---|---|
| | |
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |
| | |


- Extended Data Figure 4: a) The average number of reasoning steps for multiple-choice questions and open-ended reasoning in the DrugPC and TreatmentPC benchmarks. The TreatmentPC requires more reasoning steps compared to the DrugPC benchmarks, indicating that precision treatment recommendations require more reasoning steps before reaching a conclusion. b) The average number of tool calls for multiple-choice questions and open-ended reasoning in the DrugPC and TreatmentPC benchmarks. Similarly, the TreatmentPC benchmark requires a greater number of tool calls compared to the DrugPC.


Question: A 12-year-old boy with alopecia areata is being considered for treatment. He has a history of heterozygous familial hypercholesterolemia (HeFH) and is currently on a lipid-lowering diet. Which medication should be avoided due to potential side effects in pediatric patients?

A: Triamcinolone Acetonide (Correct) B: ZOCOR C: Both medications are safe D: Neither medication is safe

Deepseek R1 answer: 1. Triamcinolone Acetonide: This corticosteroid is commonly used intralesionally or topically for alopecia areata. Local administration minimizes systemic absorption, making it safe in pediatric patients with minimal side effects (e.g., local skin atrophy). There is no contraindication for its use in this context (DeepSeek hallucinates incorrect information, leading to misjudgment.)…… Both medications are safe for use in this patient. Answer: C (Both medications are safe).

TxAgent answer: A: Triamcinolone Acetonide. The analysis of the safety profiles indicates that Triamcinolone Acetonide poses significant risks for pediatric patients, including HPA axis suppression, Cushing's syndrome, and intracranial hypertension. These risks make it unsuitable for use in children, especially considering the potential impact on growth and development. (Trust source from FDA doc retrieved by tool use.) In contrast, ZOCOR has been established as safe and effective for pediatric patients aged 10 years and older with HeFH, without significant effects on growth or sexual maturation. Therefore, Triamcinolone Acetonide should be avoided in this case.

- Extended Data Figure 5: Comparison between TXAGENT and Deepseek-R1. Deepseek-R1 relies on its internal knowledge for reasoning, which can sometimes lead to hallucinated information and misjudgments. In contrast, TxAgent bases its reasoning on trusted sources, such as FDA drug labels, minimizing the risk of hallucinations and ensuring more reliable conclusions.


Benchmark Size Description DrugPC 3,168 FDA newly approved drugs in 2024

Drug Overview 242 package label principal display panel; description Drug Ingredients 83 product data elements Drug Warnings and Safety 515 boxed warning; warnings and cautions; contraindications;

adverse reactions; drug interactions Drug Dependence and Abuse 53 drug abuse and dependence; abuse; controlled substance;

overdosage Dosage and Administration 507 indications and usage; dosage and administration; dosage

forms and strengths; instructions for use Drug use in Specific Populations 333 use in specific populations; pregnancy; pediatric use; geri-

atric use; nursing mothers Pharmacology 565 clinical pharmacology; mechanism of action; pharmacody-

namics; pharmacokinetics Clinical Information 146 clinical studies Nonclinical Toxicology 172 nonclinical toxicology; carcinogenesis and mutagenesis

and impairment of fertility; animal pharmacology and or toxicology

Patient-Focused Information 349 information for patients; patient medication guide; patient

package insert; patient medication information

Storage and Supply Information 203 how supplied; storage and handling BrandPC 3,168 Drugs represented with drug brand name GenericPC 3,168 Drugs represented with drug generic name DescriptionPC 626 Drugs represented with descriptions instead of names TreatmentPC 456 Questions regarding specialized treatment recommenda-

tions considering patient populations

Table 1: Benchmark datasets. These datasets are derived from newly approved FDA drugs in 2024 to minimize the risk of information leakage from LLMs. A human evaluation process is conducted to carefully review and refine the questions and answers, ensuring the exclusion of non-biomedical questions.

###### Variable Description

Q A precision therapy question. A The final answer, including the rationale and the solution. G The ground truth answer G. X The explanation of why G answers Q. F The TXAGENT’s backend LLM.

FTX F prompted by the system prompt of being an TXAGENT.

FS F prompted by the system prompt of a summarization prompt. Ri The verified reasoning trace {R1,R2,...,Ri} until the ith step.

i Index representing the step in the reasoning trace. Ti The thought at the ith step of the reasoning trace. Pi The collection of tools available at step i. Pˆ0 Tools obtained from the reference information during training data generation process.

PˆiRAG Tools obtained from the TOOLUNIVERSE at the ith step during training data generation process. Ci The set of function calls {Ci,1,Ci,2,...,Ci,k} at step i. Ei Response of the function calls in the ith step. Ri The ith step in the reasoning trace, Ri = [Ti,Ci,Ei].

Ci,k The kth function call at the ith step in the reasoning trace.

B The tool set containing various tools {B1,B2,...,Bj}. Bj The jth tool from the tool set.

I Real-world biomedical information, including FDA documents, disease and drug data.

Table 2: Additional notation.

Multi-choice setting Open-ended setting

Question A 60-year-old female patient with a history of myocardial infarction and hypertension is being evaluated for medication adjustments. She is currently on a beta-blocker and has no known renal or hepatic impairments. Which medication would be most appropriate to add to her regimen to further reduce her cardiovascular risk?

A 60-year-old female patient with a history of myocardial infarction and hypertension is being evaluated for medication adjustments. She is currently on a beta-blocker and has no known renal or hepatic impairments. Which medication would be most appropriate to add to her regimen to further reduce her cardiovascular risk?

Options A: Sitagliptin B: Altace C: Katerzia D: Aspirin

Answer B Ramipril (Altace) is the most appropriate medication to add to the patient’s regimen to further reduce her cardiovascular risk. Ramipril is an ACE inhibitor that is indicated for reducing the risk of myocardial infarction, stroke, and death from cardiovascular causes in patients 55 years or older who are at high risk of developing a major cardiovascular event. This aligns with the patient’s profile, as she is 60 years old with a history of myocardial infarction and hypertension. Additionally, Ramipril is indicated for use in stable patients with signs of congestive heart failure post-myocardial infarction, making it a suitable choice for this patient. Therefore, adding Ramipril to her current regimen of a betablocker would provide comprehensive cardiovascular protection.

Table 3: The examples of questions, options, and answers in open-ended and multi-choice settings.

## Online Methods

- 1 TXAGENT


#### 1.1 Overview

We introduce TXAGENT, an agentic AI model for precision therapy, leveraging an extensive array of biomedical tools and multi-step, white-box drug reasoning grounded with verified real-world knowledge. TXAGENT interprets user questions written in natural language and generates answers accompanied by detailed rationales and reasoning traces (Figure 1b). These traces include multiple thought processes, function calls, and grounded information drawn from tools, enabling users to clearly understand and verify the basis of its conclusions. To address complex queries, TXAGENT performs a series of actions such as analyzing user inputs and current contexts, identifying relevant tools, executing function calls on selected tools, synthesizing answers, and coordinating among tools to compile a comprehensive and accurate response. This functionality is powered by unified multi-step reasoning, where each step involves iterative thinking and tool utilization. TXAGENT is supported by a TOOLUNIVERSE and specialized tools, such as machine learning model-based tools. The TOOLUNIVERSE includes 211 biomedical tools for accessing high-quality knowledge, such as FDA drug information. Specialized tools are created for specific usages, such as the TOOLRAG model, which is an embedding model that facilitates efficient tool retrieval, and the FINISH tool, which signals the conclusion of multi-step reasoning. The multi-step reasoning with function call abilities is achieved through fine-tuning open-source large language models (LLMs) such as Llama-3.1. By utilizing open-source models, our method supports local deployment for private applications, safeguarding patient information and ensuring privacy.

To achieve TXAGENT, the collection of TOOLUNIVERSE and the fine-tuning of LLMs for multi-step reasoning and function calls are essential. We introduce three key multi-agent systems: the TOOLGEN system for tool construction, the QUESTIONGEN system for training question generation, and the TRACEGEN system for reasoning trace generation. These multi-agent systems leverage AI agents powered by LLMs through prompting. Drawing on real-world biomedical information and APIs from verified sources—including FDA documents [20], the OpenTarget database [21], and the PrimeKG graph [28]—they enable the generation, verification, and filtering of data. Using these systems, we construct the TXAGENT-INSTRUCT dataset to fine-tune LLMs and achieve TXAGENT.

Preliminaries. During the inference process, given a therapy question Q, TXAGENT generates a verified reasoning trace Ri = {R1,R2,R3,...,Ri} and the final answer A, which includes the rationale for the answer, such as treatment recommendations. The i-th step in the reasoning trace Ri consists of a thought Ti, a set of function calls Ci = {Ci1,Ci2,...Cik}, and responses from the function calls Ei = {Ei1,Ei2,...Eik}, i.e., Ri = {Ti,Ci,Ei}. The TOOLUNIVERSE B = {B1,B2,...,Bj} contains a wide array of biomedical tools from TOOLUNIVERSE. Pi is the collection of tools available at step i, which contains the default specialized tools and tools retrieved by the TOOLRAG model in previous steps. To aid understanding, Table 2 provides the complete definitions and explanations of all notations used in this work.

#### 1.2 Skills of TXAGENT

TXAGENT is an LLM-based agentic model designed to address complex drug reasoning problems through its versatile capabilities. These capabilities are enabled by TXAGENT’s multi-step reasoning processes and its ability to perform function calls, which leverage the combined effects of its diverse skill set. This section introduces the core skills of TXAGENT, which are obtained by the instruction finetuning of an LLM as introduced in Section 4. Then, we detail the advanced capabilities TXAGENT can achieve by integrating these skills and describe the inference process of TXAGENT.

Contextual thought generation. TXAGENT is capable of generating thoughtful, context-aware, step-by-step reasoning based on prior interactions and user inputs. Given a user query Q and a sequence of previous reasoning traces Ri−1, TXAGENT produces a new thought Ti at step i, expressed in natural language. This thought generation process can be represented as:

Ti = FTX(Q,Ri−1,Pi), (1)

where FTX is the TXAGENT’s backend LLM prompted by the system prompt of being an TXAGENT, which operates in an autoregressive manner [34], and Pi is a set of available tools at this step. The query Q along with the reasoning traces Ri−1 is provided as input to FTX to generate Ti, which incorporates reasoning about the analysis of prior steps and determines the next actions. Function call arguments generation. TXAGENT executes tools by generating function call arguments based on the tool descriptions provided in the prompts. Each tool description consists of the tool’s name, its purpose, and the arguments it accepts. For each argument, the description specifies its name, purpose, data type, and whether it is mandatory (Extended Data Figure 1). Fol-

lowing the generated thought Ti of reasoning step Ri, given a set of tool descriptions Pi available to TXAGENT, TXAGENT produces the corresponding function call arguments for tool calls:

###### Ci = FTX(Q,Ri−1,Ti,Pi), (2)

where Ci = {Ci1,Ci2,...,Cik} is a list that contains multiple function calls as TXAGENT supports parallel tool execution by generating multiple function calls across various tools. The k-th function

call at step i, Cik, is represented as a code snip in JSON format:

Cik = name,Aki , (3) where name is the name of the tool selected from the set of available tools Pi, Aki = {a1,a2,...,an} represents the arguments required by tool Cik, where each aj corresponds to a specific argumentvalue pair corresponding to the description of the selected tool. The generated function call arguments Ci are sent to the TOOLUNIVERSE codebase for execution. The results from these function calls Ei = {Ei1,Ei2,...Eik}, where Eik is the result of k-th function call, are then sent back to TXAGENT as part of the current step of the reasoning trace Ri = {Ti,Ci,Ei}. The reasoning trace Ri is then updated as: Ri = Ri−1 ∪ Ri. Tools used by TXAGENT involve a variety of types, such as biomedical tools in TOOLUNIVERSE that gather outputs from multiple verified sources, and the machine learning-based tools (TOOLRAG model) that use a machine learning model to achieve certain functions. Moreover, we will explore tool use of TXAGENT in a broader range, such as the formation of a multi-agent system where tools represent specialized agents with unique capabilities, or even the creation of a new instance of TXAGENT. To add new capabilities to TXAGENT, simply introduce new tools to the framework, and TXAGENT will automatically incorporate and utilize them when needed.

Logical multi-step reasoning and decision-making. TXAGENT achieves logical multi-step reasoning by iteratively generating thoughts and formulating tool arguments. At each step, TXAGENT evaluates whether the reasoning trace up to that point—particularly the outputs from prior function calls—provides sufficient information to answer the user’s query by generating thought Ti. Based on this assessment, it decides on the next action, which could involve generating new function calls Ci to use tools for accessing new information or generating the final answer A, depending on if the special token [FinalAnswer] is generated or not:

Ci = FTX(Q,Ri−1,Ti,Pi), [FinalAnswer] ∈/ Ti; A,CF = FTX(Q,Ri−1,Ti,Pi), [FinalAnswer] ∈ Ti,

(4)

where CF is a final function call to the special FINISH tool, signifying the end of the reasoning process. Despite its simplicity, this iterative thought and function call generation process has potential to incorporate complex and dynamic agentic workflows.

Proactive tool search, selection and utilization. TOOLUNIVERSE includes 211 tools spanning various aspects of the biomedical field. However, due to the limited context window of the LLM (i.e., the number of text tokens it can handle in a prompt), it is impractical to include all tool descriptions within the prompt. To address this, TXAGENT employs a proactive tool search strategy by utilizing the TOOLRAG model. When no suitable tool is available for the next action, TXAGENT dynamically invokes the TOOLRAG model by function call to search for tools matching the desired requirement. Rather than relying on tools memorized during training, TXAGENT selects and uses tools based on its current requirements and descriptions of tools, ensuring flexibility and scalability. The TOOLRAG model is an embedding model designed to retrieve tools based on specific requirements. During inference, the TOOLRAG model processes all tool descriptions in TOOLUNIVERSE to generate their semantic embeddings. For each new function call to TOOLRAG model, the model encodes the requirement argument obtained from the function call arguments into an embedding and retrieves the top-k tools whose embeddings have the highest similarity to the requirement’s embedding. The newly retrieved tools are put into the tool set Pi. Due to the expansive scope of TOOLUNIVERSE, imperfection of TOOLRAG model, and the open-ended reasoning approach of TXAGENT, not all tools retrieved by TOOLRAG model are immediately applicable to TXAGENT’s next action. Drawing from the prior reasoning trace and the descriptions of the retrieved tools, TXAGENT identifies the most suitable options from Pi, formulates new thoughts, and generates parallel function calls to effectively utilize the selected tools.

Concise summarization. Tool outputs can often be lengthy, especially in complex cases. This poses a challenge due to the limited context window of the LLM, as lengthy outputs restrict the maximum number of reasoning steps that can be performed. To overcome this limitation, TXAGENT introduces a mechanism to transform lengthy tool outputs into concise, accurate, and meaningful summaries. Given a reasoning step Ri = {Ti,Ci,Ei}, TXAGENT generates a summarized version of tool response Ei as follows:

###### Eˆi = FS (Ti,Ci,Ei), (5)

where FS is the backend LLM of TXAGENT prompted with a summarization prompt. This summary retains the essential information relevant to the thought Ti, ensuring that the critical details

are preserved. By compressing lengthy outputs into a compact form, TXAGENT enables a larger number of reasoning steps while avoiding context window overflow.

Structured question responses. While TXAGENT generates open-ended answers along with a reasoning trace, it can also be used for evaluating multiple-choice questions. Given a question and the open-ended answer, TXAGENT can map the answer to the correct option from the provided choices.

Algorithm 1: TXAGENT multi-step inference process. Input: Question Q, TOOLUNIVERSE B, Initial available tools P0 Output: Reasoning trace R, final answer A Initialize R ← {}, tools P ← P0, step i ← 0 ; while Reasoning is incomplete do

i ← i + 1; Generate thought: Ti = FTX(Q,Ri−1,Pi) ; if [FinalAnswer] in Ti then

Generate final answer: A,CF = FTX(Q,Ri−1,Ti,Pi); Execute FINISH tool to end the multi-step reasoning; Return Ri,A;

###### else

Generate function calls: Ci = FTX(Q,Ri−1,Ti,Pi); if call to TOOLRAG in Ci then

Execute TOOLRAG and update Pi; else

Execute tools from Ci to get tool response Ei; Update reasoning trace: Ri ← Ri−1 ∪ {Ti,Ci,Ei};

#### 1.3 Capabilities of TXAGENT

In Algorithm 1, we present the inference process of TXAGENT, leveraging the skills described above. We highlight the capabilities of TXAGENT made possible through its diverse skill sets.

Knowledge grounding using tool calls. The treatment problem demands reliable answers accompanied by transparent explanations to justify decisions. However, a significant concern arises from the inability of machine learning models, such as LLMs, to provide dependable explana-

tions for their predictions. This forces users to invest additional effort in determining whether the model’s predictions can be trusted. With the function calling skill, TXAGENT provides answers to user queries grounded in verified information by leveraging tools connected to trusted sources. Instead of generating responses directly like traditional LLMs, TXAGENT utilizes tools to retrieve accurate information. The answers are then crafted based on the verified outputs of these tools. For instance, it can query the dosage instructions for a medication from official FDA documents. This knowledge-grounding approach allows users to validate the factual correctness of answers by reviewing the reasoning trace, ensuring transparency and reliability.

Goal-oriented tool selection. Through the proactive tool search, selection and utilization skills, TXAGENT leverages TOOLRAG model to search for tools, identify suitable options, and effectively utilize the most appropriate tools from the candidates provided by TOOLRAG model. This approach enables TXAGENT to access a vast array of tools and seamlessly adapt to new ones. Instead of relying solely on tools memorized during training, the goal-oriented tool selection process allows TXAGENT to reason more freely by first generating a plan of action and then identifying the tools necessary to execute it. Furthermore, TXAGENT can expand its capabilities by integrating additional tools into the TOOLUNIVERSE without requiring retraining. When faced with new scenarios where existing tools are insufficient, TXAGENT can address these cases by incorporating relevant tools into the TOOLUNIVERSE, showcasing its flexibility and adaptability in handling novel challenges.

Multi-step therapeutic reasoning. When tackling complex therapeutic problems that cannot be solved in a single step, TXAGENT employs multi-step therapeutic reasoning to iteratively generate new thoughts and function calls based on the prior reasoning trace. There are two key scenarios where multi-step reasoning is essential. First, solving complex problems often requires gathering information from multiple perspectives before arriving at a well-founded answer. Second, in realworld applications, interactions with the environment can be unpredictable—such as function calls failing to retrieve necessary information—making it common for a single attempt to fall short. By leveraging multi-step reasoning, TXAGENT can effectively address both cases by systematically collecting information, generating new ideas, and making additional function calls to explore alternative solutions. This iterative process continues until the goal is successfully achieved.

Real-time retrieval from continually updated knowledge sources. Once a model finishes training, its internal knowledge remains static and is no longer updated. Given the high cost and tech-

nical challenges associated with continuously training large models, such as LLMs, it is difficult to incorporate new knowledge directly into these models. Retrieval-augmented generation [27], a special form of tool-use model, retrieves relevant text by matching query embeddings with a precomputed vector database. However, maintaining a high-quality vector database is computationally intensive, making frequent updates difficult. TXAGENT takes a different approach by using function calls to directly access multiple constantly updated data sources, such as the OpenTargets and FDA databases. By leveraging these dynamic knowledge bases, TXAGENT can answer questions about newly approved drugs, even when the training data lacks relevant information. Additionally, it integrates complementary information from multiple sources, eliminating the need to construct and maintain a vector database.

## 2 TOOLUNIVERSE

The TOOLUNIVERSE consists of 211 biomedical tools that provide real-time, up-to-date information on diseases, drugs, targets, and other essential biomedical data. Constructing such a vast number of tools manually would be impractical; therefore, we developed TOOLGEN, a tool construction multi-agent system that automates the creation of tool descriptions and the critical mappings between tools and APIs. This section first presents an overview of TXAGENT, followed by an introduction to TOOLGEN system.

#### 2.1 Overview of TOOLUNIVERSE

TOOLUNIVERSE has 211 biomedical tools, covering the following categories: adverse events, risks, safety; addiction and abuse; drug patient populations; drug administration and handling; pharmacology; drug use, mechanism, composition; ID and labeling tools; general clinical annotations; clinical laboratory info; general info for patients and relatives; disease, phenotype, target, drug links; biological annotation tools; publications; search; target characterization. Tools in TOOLUNIVERSE are built upon APIs from multiple sources, including OpenFDA, OpenTargets, and the Monarch Initiative. The complete distribution of tools across these categories is presented in Extended Data Figure 3. Each tool includes a tool description that will be provided to TXAGENT as the reference for function call, along with backend code that translates function calls into API requests to these external sources. Tool description consists of the tool’s name, its purpose, and the arguments it accepts. For each argument, the description specifies its name, purpose, data type, and whether it is mandatory (Examples in Extended Data Figure 1).

#### 2.2 TOOLGEN: a multi-agent system for constructing tools

TOOLGEN is a tool construction multi-agent system for constructing tools that are suitable for TXAGENT, based on API documentation. API documentation often varies significantly in format and content, presenting challenges for direct integration into TXAGENT. For instance, OpenTargets utilizes a GraphQL schema to describe its API; OpenFDA employs Elasticsearch as its API backend and includes documentation to explain available fields; The Monarch Initiative provides RESTful APIs. This diversity in API representation complicates the process of converting them into tools for TXAGENT. TOOLGEN system addresses this by organizing the API functions into a set of tools, each with a specific purpose and a clear description that is easily understandable to TXAGENT. TOOLGEN system comprises three agents: the SUMMARIZER, TOOL GENERATOR, and TOOL CHECKER (Extended Data Figure 2a). Since their abilities are simple, these agents are implemented by providing specialized instructive prompts to GPT-4o. After completing the tool construction, a human evaluation process is conducted to assess the generated tools.

API summarization. The SUMMARIZER agent serves as the initial step in the system. It extracts API documentation from a given source to summarize the API’s capabilities. The result is a list of potential functions that could be enabled using the APIs, such as “identify the active ingredients for a drug” and “find disease-related phenotypes”.

Tool construction. For each capability in the list, the TOOL GENERATOR agent refers to the API documentation to create detailed tool specifications. These specifications include the tool’s name, description, arguments, and specialized mapping data to translate arguments into API requests. Each argument includes the name, description, data type, and an indication of whether it is required. Mappings for OpenTargets and Monarch Initiative correspond to the query string defined in the GraphQL and RESTful schema, with variables in APIs connected to arguments in the tool. Mapping for OpenFDA employs the search and return fields of Elasticsearch, where search fields are tied to arguments in the tool, and return fields are selected to align with the tool’s description (Extended Data Figure 1).

Tool check. The TOOL CHECKER agent evaluates the validity of generated tools by constructing and testing questions and function calls. In this process, we first verify the mapping, ensuring its correctness by checking the validity of the provided mappings. Next, we randomly sample data points linked to either the input or output of the APIs, such as drug names, disease names, target names, and their corresponding IDs, to test the APIs. If useful information can be retrieved through

API requests, the retrieved data and the tool specifications are sent to the TOOL CHECKER agent. The agent then generates test questions and function call arguments for the tool. If the generated function call arguments produce valid outputs, the tool is deemed functional and valid. However, if any of the steps in this process fail, the tool is marked invalid and subsequently removed.

Human verification. After the tool construction process, human experts manually verify and refine the tools. This evaluation includes determining whether the tool has meaningful applications, verifying that it functions as described, and ensuring its stability when handling unexpected inputs. Once this process is complete, the validated tools are included in the TOOLUNIVERSE.

#### 2.3 Tool Graph

The tool graph is a directed graph that connects tools in TOOLUNIVERSE. It is used to facilitate the construction of training data. In the tool graph, each node represents a tool, and a directed link is established when the output of one tool serves as the input for another. The presence of a link is determined by providing descriptions of the two tools to an LLM, which then decides if a directed link should exist between them. Sampling a tool chain from a tool graph enables the construction of complex questions that require multiple rounds of tool calls. Further uses of the tool graph are described in Section 3. The tool graph is used solely for constructing the training dataset, not for the inference process in TXAGENT, due to the challenges in constructing an exceptionally precise tool graph. Unrestricted by the tool graph, TXAGENT can seamlessly integrate newly added tools during the inference process.

## 3 Constructing TXAGENT-INSTRUCT dataset

We perform instruction tuning on open-source LLMs using a collected TXAGENT-INSTRUCT dataset to achieve the capabilities of TXAGENT. This section describes the construction process of TXAGENT-INSTRUCT. To achieve comprehensive coverage of specialized treatment and drug information, we employ QUESTIONGEN, a question construction multi-agent system that produces diverse questions. Recognizing the challenges in generating valid reasoning traces that effectively integrate feedback from real-world tools, we design TRACEGEN, a multi-agent system that leverages a helper agent to assist in generating complex, step-wise reasoning traces.

- 3.1 TXAGENT-INSTRUCT Data Sources The source information of TXAGENT-INSTRUCT is collected from the following sources.


OpenFDA is a health informatics database maintained by the FDA, offering public access to FDA data on approved drugs, devices, and foods [20]. This work utilizes the drug labeling data provided by the platform, which covers more than 67,000 drugs currently on the market [35]. OpenFDA includes a search API for retrieving information based on specific query fields. In this study, we use the drug API of OpenFDA to obtain FDA documentation on various drugs. Each drug entry contains numerous fields, such as indications, boxed warnings, and supply information (Table 1).

Open Targets is a platform that integrates data from 23 public resources, including Orphanet, Gene2Phenotype, and ChEMBL [21], to facilitate target identification and prioritization. As of September 2024, Open Targets includes 63,121 targets, 28,327 diseases, 18,041 drugs, 17,853,184 evidence entries, and 8,155,988 target-disease associations [36]. In this study, we utilize the association data from Open Targets to extract drug-disease relationships, drug status, drug-target interactions, and disease-target associations.

Human Phenotype Ontology from the Monarch Initiative (HPO) is a database that provides an ontology of medically relevant phenotypes and disease-phenotype annotations [22]. It includes over 18,000 terms and more than 156,000 annotations linked to hereditary diseases. We leverage HPO to establish connections between diseases and phenotypes.

PrimeKG is a comprehensive medicine-focused knowledge graph designed to offer a holistic view on diseases [28]. It incorporates data from 20 high-quality biomedical resources, capturing details about 17,080 diseases and their 4,050,249 relationships across ten key biological scales. In this work, PrimeKG provides the disease list and disease-related information for generating diseaserelated questions.

#### 3.2 QUESTIONGEN Multi-agent System for Question Construction

While training TXAGENT requires a large number of diverse questions that cover different aspects regarding treatment, disease, and drugs, and considers specialized cases such as patient populations, drug side effects, and drug interactions, manually writing these questions would be too costly. To effectively collect questions, QUESTIONGEN system is proposed as a question construction multi-agent system that generates meaningful questions from verified knowledge bases such as FDA documents. QUESTIONGEN system begins with the information extraction, which identifies and extracts key information relevant to the desired questions from documents and data sources. Using the extracted information, the question construction step creates questions, corre-

sponding answers, and detailed explanations that clarify how the answer addresses the question. At last, the question evaluation step verifies questions in multiple aspects.

Question types. We generate questions through three distinct approaches: drug-centered, diseasecentered, and tool-chain-centered question construction. Drug-centered questions focus on common therapeutic aspects of drugs, including their use in specific patient populations, indications, dosage, safety warnings, and potential risks. Disease-centered questions address specialized treatment scenarios. These questions incorporate detailed patient profiles, such as phenotypes, medical histories, current medications, and characteristics of the patient population. Tool-chain-centered questions are generated by randomly sampling a sequence of tools from the TOOLUNIVERSE tool graph, followed by creating questions based on the selected tool chain, which increases the diversity of questions.

Information extraction. This step identifies and extracts key information relevant to the desired questions from documents and data sources. Different information extraction strategies are designed to meet the requirements of various question types.

For drug-centered questions, we randomly sample drugs from the FDA database and retrieve their corresponding FDA documents as raw data sources. From each drug’s FDA document, one field is randomly selected and extracted as the reference data for question construction. To enable question construction beyond just related to drug names, descriptive information about the drug—such as its mechanism of action, indications, and contraindications—is also extracted. This allows for the creation of questions that focus on the drug’s characteristics without explicitly mentioning its name.

For disease-centered questions, we begin by randomly sampling a disease and gathering its description, associated phenotypes, targets, and all potential drugs. For each drug in the list, we retrieve its FDA document and extract information on indications, patient populations, contraindications, warnings, and drug interactions. The extracted data is then categorized by field and passed to the INFORMATION EXTRACTOR agent, which compares the drugs across these fields and highlights their differences. The generated comparison serves as the reference for question construction, enabling the creation of challenging, specialized questions that account for subtle differences among drugs.

For tool-chain-centered questions, we first sample a tool-chain from the tool graph starting from common tools such as identify drug ID or disease ID based on names. Then, we obtain

information that can be retrieved by tools and the tool descriptions as the reference for question construction.

Question construction. In this step, the QUESTION GENERATOR leverages reference information extracted during the information extraction process to produce the question Q, corresponding answer G, and explanations justifying why the answers are correct X. For multiple-choice questions, it also generates answer options. The inclusion of explanations plays a crucial role, as they ensure the meaningfulness of the generated questions and offer solution hints for the HELPER agent during reasoning trace generation.

The QUESTION GENERATOR operates by prompting GPT-4o with instructions for generating questions. It utilizes multiple prompt variations, each designed for specific question types. During the question-construction process, general guidelines for question creation, reference information, and specific requirements for particular question types are provided as contextual input to the QUESTION GENERATOR to produce the questions.

Question evaluation. The generated question undergoes evaluation based on three key aspects: knowledge-based grounding, answerability, and reasonableness. For each aspect, GPT-4o is prompted to perform the evaluation. For knowledge-based grounding, to ensure the question is generated from the reference information and not from hallucinations by the language model, both the question and reference information are provided to GPT-4o. GPT-4o is tasked with verifying whether the information in the question is directly derived from the reference information. For the answerability check, GPT-4o is prompted to assess whether the question can be adequately answered using the provided reference information. For the reasonableness check, the explanation in the generated question is sent to GPT-4o, which evaluates whether the reasoning behind the explanation is logical and makes sense. If any of the checks fail, the question is discarded. Otherwise, it is retained and sent to TRACEGEN for reasoning trace construction.

#### 3.3 Reasoning Trace Generation

TRACEGEN is designed to generate training data consisting of a reasoning trace R and the final answer A based on the question Q. However, generating R faces several challenges: 1) Complexity of questions: Many questions require multi-step reasoning and analysis of multiple aspects, making it difficult to generate a single straightforward answer. The challenge is to create a reasoning trace that can handle these complexities effectively. 2) Incorporating external tools: To improve reasoning with the help of a massive number of tools, it’s important to incorporate real-world tools

into R. The challenge here is integrating the outputs of these tools, rather than relying solely on the internal knowledge of LLMs. 3) Handling uncontrollable tool outputs: The results from external tools are often unpredictable. A key challenge is how to manage failure cases and continue progressing toward a solution, even when tool outputs deviate from expectations.

TRACEGEN is a multi-agent system designed to address various challenges through its key components: the HELPER agent, the TOOL PROVIDER module, and the SOLVER agent. The HELPER agent assists the SOLVER by offering step-by-step solution hints. It has access to the answers and explanations for questions and provides guidance for the next steps in the reasoning process based on the prior steps generated by the SOLVER agent. The TOOL PROVIDER presents a selection of potential tools for the SOLVER agent to choose from. These tools are identified based on reference information from the current question and a TOOLRAG model, which is iteratively trained on previously collected data to improve its recommendations. Armed with tools from the TOOL PROVIDER module, hints from the HELPER agent, the current question, and previously generated reasoning traces, the SOLVER agent iteratively solves the problem. It does so by generating subsequent reasoning steps and function calls until arriving at the final answer.

Providing solution hint with HELPER. The HELPER agent plays a crucial role in assisting the SOLVER by providing solution hints, which is achieved by prompting GPT-4o with instructions. At each reasoning step i, the HELPER has access to the problem question Q, the ground truth answer G, and its explanation X. Additionally, it takes as input the current reasoning trace Ri = {R1,R2,...,Ri}, which represents all steps generated by the SOLVER up to step i. Using this information, the HELPER generates a solution hint, denoted as Hi+1, which guides the SOLVER toward the next step in the reasoning process. When the SOLVER provides an answer A, the HELPER checks whether A matches the ground truth answer G. If A = G, the reasoning process is deemed complete. If A ̸= G, the HELPER prompts the SOLVER to reflect on its reasoning and continue the reasoning process. In such cases, the HELPER generates a hint Hi+1 to guide the SOLVER back into the reasoning process and help refine the answer. HELPER is defined as:

###### Hi+1 = HELPER([Q,G,X],Ri,A), (6)

where A is empty if it is not provided to the HELPER. By iteratively providing hints Hi+1, the HELPER ensures that the SOLVER progresses logically, generating the reasoning trace until the solution A is fully constructed and consistent with the ground truth answer G and explanation X.

Providing tools with the TOOL PROVIDER. The TOOL PROVIDER module supports the SOLVER

by supplying relevant tools during the reasoning process. It operates in two stages. First, the module analyzes the reference information attached to the problem question Q and identifies an initial set of tools Pˆ0 from the tool set B. These initial tools are provided to the SOLVER at the start of the reasoning process. Second, if the SOLVER determines that no suitable tools are available for a specific reasoning step, it invokes the TOOLRAG model within the TOOL PROVIDER module. This model retrieves additional tool suggestions, denoted as PˆiRAG, based on the tool descriptions provided by the SOLVER. By combining these two stages, the TOOL PROVIDER module ensures that the SOLVER has access to the most relevant tools throughout the reasoning process, either by leveraging the initial set of tools Pˆ0 or dynamically adapting to the problem’s demands with tools PˆiRAG from the TOOLRAG model.

Step-wise reasoning trace generation with SOLVER. The SOLVER serves as the central component for iteratively generating the reasoning trace R and deriving the final answer A, which is achieved by prompting GPT-4o. We provide the algorithm in Algorithm 2. At each step i, the SOLVER integrates the question Q, tools from the TOOL PROVIDER, solution hints Hi provided by the HELPER, and its prior reasoning Ri−1. Using this information, it formulates intermediate thoughts Ti and function calls Ci, driving the reasoning process toward a complete and accurate solution. To simulate the inference process, the SOLVER avoids directly utilizing tools available in the initial set Pˆ0. Instead, it generates virtual TOOLRAG calls, which simulate accessing these tools. Each virtual call specifies the tool’s name and its rewritten description from Pˆ0. These virtual calls are later replaced by actual calls to TOOLRAG. When the SOLVER identifies that no suitable tools are available for the current reasoning step, it invokes the TOOLRAG model within the TOOL PROVIDER to dynamically suggest additional tools. These new tools, denoted as PˆiRAG, are retrieved based on descriptions provided by the SOLVER. Hints Hi+1 from the HELPER guide the SOLVER through the reasoning trajectory by suggesting logical next steps. This iterative mechanism allows the reasoning trace to evolve through external tool usage, dynamic adjustments based on feedback, and updates to the reasoning trace. The process continues until the END tool suggests a candidate answer A. If validated by the HELPER, the reasoning trace R and the final answer A are returned. If the answer is deemed incorrect, the SOLVER removes the corresponding reasoning step and continues refining R.

Algorithm 2: Step-wise reasoning trace generation with SOLVER Input: Question Q, TOOLUNIVERSE B, ground truth G, explanation X Output: Reasoning trace R, final answer A Initialize R ← {}, tools P ← {}, step i ← 0 ; Obtain initial hints H0 from HELPER; Obtain initial tools Pˆ0 from TOOL PROVIDER; while Reasoning is incomplete do

i ← i + 1; if Suitable tools exist in P then

Generate thought Ti and call Ci based on Q, Hi, and Ri−1; if Suitable tools exist in Pˆ0 then

Generate thought Ti and virtual calls Ci; foreach Virtual call in Ci do

Replace virtual TOOLRAG call with real arguments; if No suitable tools in P then

Generate thought Ti and request additional tools PˆiRAG by calling TOOLRAG with desired tool’s descriptions;

Execute tool calls from Ci and update reasoning trace: R ← R ∪ {Ri}; Obtain the next hint Hi+1 from HELPER; if END tool provides candidate answer A then

if HELPER confirms correctness then

###### Return R,A; else

Remove the Ri from R; Return R,A;

Reasoning trace evaluation. We consider the quality of the reasoning trace to be essential for the performance of TXAGENT. Evaluating the reasoning trace ensures both its reliability and correctness. This evaluation focuses on two main aspects: correctness and behavior. For correctness, we examine the correctness of the answer, reasoning trace, and function calls. For answer correctness, in the case of multiple-choice questions, we compare the predicted option with the correct one. For open-ended reasoning questions, GPT-4 is prompted as a judge to determine if the prediction aligns with the correct answer. For the reasoning trace, we use GPT-4 as a judge, with the question and

the ground truth answer serving as references to assess the quality of the reasoning process. For function calls, we verify that the correct tool is used, and we check the correctness of the argument names, argument value types, and the inclusion of any required arguments. Even if the generated reasoning trace passes the correctness check, undesired behaviors may still occur, leading to incorrect reasoning during inference. In the behavior check, we examine issues such as hallucinations, arbitrary results, and repeated reasoning. For hallucinations, we look for hallucinated placeholders in object names and IDs, such as drug names, disease names, and target IDs in function calls. Since IDs for drugs or diseases are not general knowledge, we eliminate reasoning traces where IDs appear without being shown earlier in the context. The goal of TXAGENT is to generate verified reasoning traces, meaning the answers should be based on feedback from function calls. However, arbitrary results can arise when answers are derived from the model’s unverified internal knowledge rather than tool feedback. We remove reasoning traces that are based on general knowledge instead of the feedback from the tools. In more complex cases, SOLVER may generate reasoning traces that include repeated thoughts or function calls. For repeated thoughts, we assess the similarity between them, and for repeated function calls, we identify steps with identical function calls using the same arguments. We remove reasoning traces that involve repeated thoughts and function calls. If the reasoning trace passes all checks, it is retained. However, if it fails due to errors in correctness or undesired behaviors, it is discarded. This evaluation ensures that only high-quality reasoning traces are considered in training data.

#### 3.4 Iterative Training for TOOLRAG model

TOOLRAG model is used in both TXAGENT inference process and the training data collection phase. It utilizes gte-Qwen2-1.5B-instruct [37] as the base model, which is fine-tuned on pairs of requirements and tool descriptions using the multiple negatives ranking loss. In the TOOL PROVIDER module, we use the TOOLRAG model to identify tools beyond the initial list retrieved from the reference information of the question. While the TOOLRAG model requires training data from reasoning traces, we propose an iterative training process for TOOLRAG model, where it is trained on the generated reasoning traces, which in turn helps improve the generation of future reasoning traces. In the first stage, since the TOOLRAG model is not yet available, we rely solely on the initial set of tools Pˆ0 that are obtained from the reference information of the question, to generate the reasoning trace. From this trace, we extract pairs of tool requirements and tool descriptions, which are then used to train the TOOLRAG model. In the second stage, after the

initial training of TOOLRAG model, we use it to select tools instead of relying exclusively on Pˆ0. This approach allows the reasoning trace to better reflect real-world use cases, as tools are now retrieved directly by the TOOLRAG model. Using the data collected from this stage, we continue to gather new pairs for further training of the TOOLRAG model. This process is repeated iteratively, continually refining both the TOOLRAG model and the quality of reasoning trace generation.

## 4 Training TXAGENT model

To enable the multi-step reasoning and function call capabilities of TXAGENT, we fine-tune LLMs using the TXAGENT-INSTRUCT dataset designed to encompass the diverse behaviors required by TXAGENT. This section introduces the training dataset TXAGENT-INSTRUCT and the training strategies.

#### 4.1 TXAGENT Training Dataset: TXAGENT-INSTRUCT dataset

We use three agent systems to generate three training datasets, including a tooling dataset, a therapeutic question dataset, and a reasoning trace dataset. The question dataset comprises 85,340 therapeutic questions, while the reasoning trace dataset includes 177,626 reasoning steps and 281,695 function calls. Then, we begin by integrating the question with a reasoning trace and incorporating augmented tools. Next, we break down the complete reasoning trace into step-wise training data. This process results in the creation of the TXAGENT-INSTRUCT dataset that contains 378,027 instruction tuning data samples. The TXAGENT-INSTRUCT dataset is generated by randomly sampling from drugs in the FDA drug label database and disease phenotypes from the PrimeKG database. To prevent any leakage of evaluation data through the training data, we remove all drugs approved after 2023.

Constructing step-wise training data. During supervised fine-tuning, in order to enable TXAGENT to have step-wise reasoning and function call abilities, we apply step-wise supervision on the thoughts and function calls at each reasoning step. Given a question Q, a reasoning trace R = {R1,R2,R3,...,RM} consisting of M reasoning steps, and the final answer A, where each reasoning step Ri is represented as a tuple Ri = {Ti,Ci,Ei} — with Ti and Ci being the thought and function calls at the i-th step, and Ei results of function calls — we decompose the reasoning trace into M step-wise samples for supervision. Each of these step-wise samples consists of an input and an output for the fine-tuned LLM.

For each i ∈ {1,2,...,M − 1}, the input to the model consists of the system prompt S,

question Q, a set of available tools at step i denoted as Pi, and the reasoning trace up to the previous step, denoted as R1:i−1, which represents the reasoning steps from R1 to Ri−1. The output of the model is the components [Ti,Ci], which correspond to the thought and function calls at step i. At the final step M, the input consists of the system prompt S, question Q and the reasoning trace up to the M − 1-th step, i.e., R1:M−1 = {R1,R2,...,RM−1}, as well as the tools available up to that step, PM. The output consists of the thought TM, the final function call to the FINISH tool CM, and the final answer A. Thus, for each i ∈ {1,2,...,M}, the i-th step-wise sample is:

Input: [S,Q,R1:i−1,Pi], Output: [Ti,Ci] for i ∈ {1,2,...,M − 1}, Input: [S,Q,R1:M−1,PM], Output: [TM,CM,A] for i = M.

(7)

While each step in the reasoning trace may involve multiple function calls, we introduce an argument, ID, which is a randomly generated string, to uniquely identify each function call. This ID is added to both the function call arguments Ci,k, and the corresponding results returned by the function Ei,k. The ID is added to the input reasoning trace R1:M−1 and is removed in model output as it’s random unpredictable string.

This step-wise decomposition allows for effective supervision of the reasoning process, with each sample providing contextual information about the model’s reasoning at every intermediate step. At the final step, both the reasoning components and the final answer are output together, marking the completion of the reasoning process.

#### 4.2 Training data augmentation

We design several training data augmentation strategies to ensure that TXAGENT is trained to perform function calls based on contextual information and can generalize to new tools.

Augmenting tools. To prevent over-fitting to the tools in TOOLUNIVERSE, we apply augmentation to the tool descriptions by randomly rephrasing all fields of a tool. For each tool in TOOLUNIVERSE, we prompt the LLM to rewrite the original description and generate 20 distinct versions of the tool’s name, function description, argument names, and argument descriptions. For each training sample in TXAGENT-INSTRUCT, we randomly select from these rewritten fields to create a new, augmented tool description. Then, we replace the tool name and argument names in the function call arguments to generate the augmented training sample. This strategy enables TXAGENT to learn how to call functions based on the tool names and arguments, rather than memorizing the specific functions encountered during training. As a result, the model can generalize to new and

unseen tools during inference, enabling flexible scaling of TOOLUNIVERSE.

Extending the available tool set. The available tool set P (index note of i-th step is omitted here for simplicity) in each sample of TXAGENT-INSTRUCT consists of tools used in the reasoning traces. However, during inference, the tools retrieved by the imperfect TOOLRAG model may include additional candidates, making it challenging for TXAGENT to select the most suitable tools from the returned set. To address this, we enhance the tool set P by including all tools retrieved by TOOLRAG model, not just those explicitly used in the reasoning traces. Additionally, we randomly sample several tools from TOOLUNIVERSE and add them to P. This approach ensures that TXAGENT learns to effectively select the correct tool from a broader set of candidate tools.

Shuffling the tool list. To mitigate any potential bias introduced by the position of tools in the tool list P, we shuffle the tools in P. This ensures that the order in which tools appear does not influence the ability of TXAGENT to select the correct tool. By randomizing the positions of the tools, we encourage TXAGENT to focus on the context and descriptions of the tools, rather than their position in the list. This strategy helps the model learn to make tool selections based on the contextual information rather than relying on the order of the tools in the tool set.

Replacing long results to results summary. To ensure the training data fits within the context window while preserving the overall reasoning trace, we shorten samples that exceed the maximum context limit by replacing the full tool results with summarized versions. This process begins with the earliest step in the reasoning trace and continues until the total length of the sample is within the context limit.

#### 4.3 Training design

Model. We use pre-trained LLMs, such as Llama3.1-8B-Instruct, as the base models for finetuning on the TXAGENT-INSTRUCT. The Llama3 series is built on the Transformer architecture [38], which leverages self-attention mechanisms to process input sequences in parallel. This enables efficient learning of contextual relationships between tokens. Our model initialization begins with loading the pre-trained weights from the instruction-tuned version of the Llama3 series, specifically fine-tuned on question-and-answer data. To further adapt the model to our specific task, we apply Low-Rank Adaptation (LoRA) fine-tuning [39]. LoRA enhances the fine-tuning process by introducing low-rank updates to the pre-trained weights, reducing computational costs and the number of parameters trained. This allows us to efficiently fine-tune the model while

preserving the knowledge from the pre-trained LLM. Training process. During the training process, the input of one training sample [S,Q,R1:i−1,P1:i−1]

and the corresponding output [Ti,Ci] are formatted according to the instruction-following format of the LLM (e.g., the chat template of Llama). The formatted text is then processed by the LLM tokenizer to generate a sequence of tokens x = {x1,x2,...,xN}, where N is the total number of tokens. These tokens are embedded and passed through the model for autoregressive prediction. The model predicts the next token xt based on all previously generated tokens {x1,x2,...,xt−1}, producing a conditional probability distribution p(xt | x1,x2,...,xt−1). The training objective is to minimize the autoregressive loss, but only for the tokens corresponding to the output sequence x ⊆ xout. The loss is defined as:

###### log p(xt | x1,x2,...,xt−1), (8)

###### L = −

t∈Idxout

where Idxout represents the indices of tokens in x corresponding to the output sequence xout. By focusing on the output tokens, this loss ensures that the model learns to generate thought and function calls instead of over-fitting to the results from tools.

#### 4.4 Training implementation

Training resources. We use the Nvidia H100 GPU cluster provided by the Kempner Institute for the Study of Natural and Artificial Intelligence at Harvard University to train TXAGENT. For training the TXAGENT-8B model, we utilize 4 GPUs, totaling 320GB of GPU memory. Training TXAGENT-8B requires 9.93 GPU days.

Training infrastructure. The training infrastructure of TXAGENT is modified based on several key libraries, including TRL [40], Alignment Handbook [41], Transformers [42], Deepspeed [43], and PyTorch [44]. The fully sharded data parallel (FSDP) technique is employed as the multiGPU distributed training method. In this setup, the model’s parameters are split across multiple GPUs to reduce memory usage, enabling the training of TXAGENT with large backend LLMs and long context windows. This approach efficiently distributes both computation and model weights, allowing for better scalability while minimizing communication overhead. For multi-node training, we leverage the PyTorch implementation of FSDP. For single-node training, the Deepspeed implementation of FSDP is utilized, which is also referred to as Deepspeed Stage 3.

## 5 Benchmarking TXAGENT

#### 5.1 Benchmarks

We constructed five evaluation benchmarks, including DrugPC, BrandPC, GenericPC, DescriptionPC, and TreatmentPC. Given that LLMs have been pretrained on vast amounts of publicly available internet data, there is a risk of potential data leakage, meaning that LLMs may have previously encountered similar questions. To mitigate this risk in our evaluation datasets, we focused on creating new datasets centered around drugs approved by the FDA in 2024, reducing the likelihood that the LLMs have been exposed to this specific information. Statistics of all benchmarks are shown in Table 1.

DrugPC: A comprehensive benchmark covering 11 common therapeutic tasks. We created the DrugPC dataset, which includes 3,168 questions covering 11 common tasks related to therapy. These sub-tasks include drug overview, drug ingredients, drug warnings and safety, drug dependence and abuse, dosage and administration, use in specific populations, pharmacology, clinical information, nonclinical toxicology, patient-focused information, and storage and supply (as detailed in Table 1). To facilitate evaluation, the dataset is formatted as multiple-choice questions, with each question followed by several options (most having 4 options, with some having 2 or

- 5). The dataset construction process follows these steps: 1) We classify the sections within FDA documents and map them to 11 tasks. The specific fields for each task are outlined in Table 1.


2) For question construction, we use the text from relevant sections of FDA documents as context. Using the question construction multi-agent system QUESTIONGEN, we create questions, multiple-choice options, and corresponding answers that can be answered using the provided context. The evaluation process checks whether the questions are answerable based on the context provided and ensures that the answers are accurate according to the given information. 3) After construction, a human evaluation process is conducted to carefully review and refine the questions and answers, ensuring that non-biomedical content, such as information about drug manufacturers, is excluded.

BrandPC/GenericPC: Datasets representing drug name in brand and generic forms. LLMbased methods have been shown to be sensitive to variations, such as representing drugs by either their brand or generic names. To assess the robustness of TXAGENT, we transform the DrugPC dataset into two versions: BrandPC and GenericPC. In these versions, drug names are systematically replaced with their respective brand or generic names. Problems that do not involve drug

names in the questions or options remain unchanged, while those requiring conversion between brand and generic names are also kept as is.

DescriptionPC: A benchmark representing drugs with detailed descriptions. The drug name plays a crucial role in enabling LLM-based methods to effectively answer questions. However, to evaluate the models’ generalization capabilities in the absence of explicit drug names, we introduce the DescriptionPC benchmark. In this benchmark, drug names are replaced with detailed descriptions that include information such as indications, mechanisms of action, contraindications, and drug interactions. To ensure the validity of the dataset, we manually remove questions in the DrugPC benchmark that cannot be answered after replacing the drug name with its description. This process results in 626 questions, forming the DescriptionPC benchmark. While a model might infer an answer without explicitly identifying the drug name from its description, ensuring that the prediction is based on the correct drug rather than exploiting patterns is critical. To address this, the DescriptionPC benchmark incorporates a two-step evaluation process: drug identification and answer correctness evaluation. Drug identification: The model must identify the drug name based on the provided description. Since multiple drugs can share similar descriptions, we construct the ground truth for this step by first collecting drug descriptions corresponding to their original names. We then identify similar drugs that can be described in the same way and include them in the ground truth. Answer correctness evaluation: Using the drug names predicted in the first step, the model is tasked with selecting the correct answer from multiple-choice questions. During the two-step evaluation process, if the drug identification in the first step is incorrect, the second step is automatically marked as incorrect, regardless of the answer’s correctness in that step. This approach ensures that the evaluation rigorously tests the model’s reasoning based on the intended drug descriptions.

TreatmentPC: A specialized treatment benchmark for precision therapy in targeted conditions. While multiple indications can be applied to a single disease, patients with specific conditions, such as pregnancy or comorbidities, require specialized treatment approaches, such as customized drug selection and dosage adjustments. The TreatmentPC benchmark is designed to address such specialized treatment scenarios by generating questions based on the varying application conditions of drugs. This is achieved using the question construction system QUESTIONGEN. We first select drugs approved by the FDA in 2024, identifying their indicated diseases. For each disease, we compile all associated treatments and analyze the unique attributes of each drug. This

analysis is conducted by examining FDA documents, including information on indications, usage in specific populations, safety warnings, precautions, and contraindications. Next, we generate multi-choice questions that specifically account for differences among drugs. The answer options represent treatments for the disease, but only one is suitable based on the patient’s specific condition. For instance, we include scenarios where a patient is taking other medications that are contraindicated for certain treatments. The TreatmentPC benchmark requires the model to do a thorough analysis of the patient’s condition before determining an appropriate solution.

#### 5.2 Evaluation strategy

To assess performance on the aforementioned benchmarks, we employ two evaluation strategies: multiple-choice evaluation and open-ended evaluation. Examples of both multiple-choice and open-ended questions can be found in Table 3.

Multi-choice evaluation. In this approach, the question is accompanied by multiple options, and the model must select the correct answer from these options. Accuracy across the dataset is reported as the evaluation metric.

Open-ended evaluation. The model is presented with only the question, without any options, and is required to generate an open-ended answer. Evaluating such answers is inherently challenging. To address this, we introduce an additional step: the generated open-ended answer is provided as context, and the model is tasked with selecting the correct answer from multiple options based on this context. This allows for the evaluation of open-ended questions by producing quantitative results.

Performance metrics. For both multi-choice evaluation and open-ended evaluation, we report the accuracy on the benchmark dataset as the performance metrics.

## 6 Settings for analysis of TXAGENT

#### 6.1 TOOLUNIVERSE vs. LLM-as-tools

In the experiments comparing TOOLUNIVERSE with LLM-as-tools, we prompt the LLM with the following instruction to make it function as tools:

LLM-as-a-tool

You are a function that answers the questions based on your given description and given input. Do not answer questions that you don’t have knowledge about.

Here is your definition: {tool description}. Here is the input to the function:{function call arguments}. The tool response:

In this instruction, the function call arguments generated by TXAGENT serve as the input, while the tool description obtained from the TOOLUNIVERSE is used as a reference. The LLM is then prompted to simulate the tool’s outputs.

#### 6.2 Limit TXAGENT to function calls only, no thoughts

To verify the role of reasoning thoughts in TXAGENT, we build a modified version of TXAGENT that does not generate reasoning thoughts (Algorithm 3). This modified version of TXAGENT follows a multi-step inference process where, at each step, instead of explicitly reasoning through generating intermediate thoughts, the model directly produces function calls. The process starts with the initialization of the reasoning trace R ← {}, the set of available tools P ← P0, and a step counter i ← 0. In each iteration, the model generates function calls or the final answer:

Ui = FTX(Q,Ri−1,Pi). (9)

If Ui contains textual content, it is assigned as the final answer A, and the FINISH tool is executed to terminate the reasoning process, returning Ri and A. Otherwise, Ui is the function calls arguments Ci, which are executed. If Ci includes a call to TOOLRAG, the available tools Pi are updated accordingly. The reasoning trace is iteratively updated as:

###### Ri ← Ri−1 ∪ {Ci,Ei}. (10)

Algorithm 3: TXAGENT multi-step inference process without thoughts. Input: Question Q, TOOLUNIVERSE B, Initial available tools P0 Output: Reasoning trace R, final answer A Initialize R ← {}, tools P ← P0, step i ← 0 ; while Reasoning is incomplete do

i ← i + 1; Generate function calls or final answer: Ui = FTX(Q,Ri−1,Ti,Pi) if Ui contains text then

Split the text as the final answer: A; Execute FINISH tool to end the multi-step reasoning; Return Ri,A;

###### else

Ci = Ui; if call to TOOLRAG in Ci then

Execute TOOLRAG and update Pi; else

Execute tools from Ci;

Update reasoning trace: Ri ← Ri−1 ∪ {Ci,Ei}; Return R,A;

## 7 Prompt sketches

This section shows the prompts used to build agents in the data generation multi-agent systems. For simplicity, we provide prompt sketches that contain an outline of the full prompt that summarizes key points and omits unnecessary details.

#### 7.1 System prompt for TXAGENT

TxAgent

You are a helpful assistant that will solve problems through detailed, step-by-step reasoning and actions based on your reasoning. Typically, your actions will use the provided functions. You have access to the following functions. {functions}

#### 7.2 Prompts for TOOLGEN

Summarizer

{API schema}

Using the provided {database name} API Schema, generate all possible specific functional commands in words with no code. Output them in a list.

Tool Generator (for openFDA tools)

You are a helpful assistant for generating functions based on the field descriptions and API schema of openFDA: {API schema, field descriptions, and example functions} Guidelines:

- • Generate two functions: one function retrieves the drug name based on the field information, and the other function retrieves information for that field based on drug names.
- • Align the function with the expected fields and descriptions.
- • Each function must be unique and different from existing examples.
- • Fields should contain search fields and return fields:


- – search fields is a dict, where the keys are the function input parameters and the values are the fields to be searched.

- – return fields is a list of field names from which information must be returned.


The capabilities of the functions should be related to the given capabilities: {capabilities}

Tool Generator (for OpenTarget tools)

You are a helpful assistant for generating functions based on the OpenTarget API schema:

{API schema and example functions} Guidelines for the generated function:

- • The function should align with the schema’s functional and structural requirements.
- • The function’s name, description, input parameters, and schema should be unique and different from the existing example functions.
- • The function capabilities should be related to the given capabilities: {capabilities}


Tool Checker

You are a helpful assistant who generates test queries based on a given function. You are provided the following:

- • Function: {generated tool}
- • Related keywords and information for questions and queries:{additional information}


Based on the provided function, you must generate {number} different questions in natural language that require using the function.

Guidelines:

- • The questions should be specific and diverse; avoid general questions
- • Function calls must include “name” and “arguments” arguments
- • Question examples: {examples}


#### 7.3 Prompt for QUESTIONGEN

Information Extractor (for disease-centered personalized treatment questions)

You are provided the following information:

- • Disease Information: These phenotypes or symptoms in the following disease-related information will be used to construct a patient profile. {disease desc info}
- • Paired Drug Information: Here is a side-by-side comparison of multiple drug options that help in designing design patient conditions. Consider the side effects, drug interactions, contraindications, and other aspects of these drugs in deciding which patientspecific factors would require someone to take one drug instead of the other options. For example, one drug may be a better option than the others given specific adverse drugdrug interactions, warnings, age restrictions, patient population restrictions, pregnancy considerations, and contraindications. Include such factors in the constructed patient profile to make one drug the definitive correct answer. {drug information}


Generate a comparison analysis of the selected drugs based on the provided information. Show the differences between the drugs and provide evidence for the differences.

Question Generator (for disease-centered personalized treatment questions)

You are an assistant specializing in creating advanced biomedical multiple-choice questions focused on drug treatments given various patient-specific information like diseases, phenotypes, and genetic variation.

Guidelines:

- • Frame questions around patient case scenarios, where a patient is diagnosed with a disease or exhibits specific phenotypes, and the goal is to identify the most suitable treatment. You may also provide protein targets or genes. If additional info is given in the Personalized Information section below, incorporate this info into the profile being constructed.
- • Construct questions and answer choices that compare multiple similar drug treatments and select the most suitable one given the patient’s particular conditions. Incorrect answer choices could be drugs indicated for the disease but unsuitable for this particular patient due to factors like age, comorbidities, or dosage considerations. The correct answer should be the most appropriate drug for the patient’s specific profile.
- • Selected Tools: Generate questions related to these functions. {selected tools}
- • Disease Information: Use phenotypes or symptoms in the following disease-related information to construct the patient profile. {disease desc information}
- • Personalized Information: When constructing the patient profile, use the following analysis of the side-by-side drug comparison. Consider the side effects, drug interactions, contraindications, and other aspects of these drugs in deciding which patientspecific factors would require someone to take one drug instead of the other options. For example, one drug may be a better option than the others given specific adverse drugdrug interactions, warnings, age restrictions, patient population restrictions, pregnancy considerations, and contraindications. Include such factors in the constructed patient profile to make one drug the definitive correct answer. Drug information: { drug information } Drug comparison analysis: {side by side drug comparison from Information Extractor agent} Generate a question, answer, and explanation according to this format: {format outline}


Question Generator (for tool-chain-centered questions)

You are a helpful assistant for generating expert-level biomedical questions. Based on the given functions, generate a single independent question that focuses on the given drug. The question should be specific, diverse, and framed in multiple ways, requiring the use of as many functions as possible. Do not write a long question; break up the question into multiple sentences if needed. Do not include details that a scientist, physician, or patient would not know (e.g., ontology IDs like MONDO, EFO, CHEMBL, Ensembl/ENS).

Use only the following information:

- 1. Functions that can retrieve information related to the drug: {tool descriptions in the sampled tool chain}
- 2. Related information from functions: {information obtained from tools}
- 3. Related information from PrimeKG interactions: {drug or disease related information from the PrimeKG knowledge graph}


Generate a question, answer, and explanation according to this format: {format outline}

Question Generator (for drug-centered questions)

You are a helpful assistant to generate meaningful and challenging multi-choice questions for expert biomedical researchers. Formulate biomedical questions and generate answers using only the drug name and field information provided below:

- • Drug generic name: {generic name}
- • Drug brand name: {brand name}
- • Specific field of information for the drug (e.g., contraindications): {field information}

Other guidelines:

- • Generate multiple, different questions to utilize all of the provided information. Make sure the questions do not overlap in content.
- • Formulate questions that can be answered without needing additional information beyond the field information provided.
- • Ask questions in different ways. Don’t always start with “What” and “Which”.


Generate a question, answer, and explanation according to this format: {format outline}

#### 7.4 Prompts for TRACEGEN

Helper

Please act as a helper to provide solution hints for the next step in solving the question. Give some suggestions about what to do next, but never give the final answer or information that directly leads to the final answer. Only provide hints for one reasoning step.

Also, make sure the user’s final answer contains the correct answer. If not, let the user do self-reflection and continue reasoning until the correct answer is found.

- • Question:{question}
- • Correct final answer:{answer}
- • Explanation of correct answer:{explanation}
- • Previous reasoning steps:{reasoning trace}


Solver

You must fully understand and solve a question through reasoning and function calls.

Guidelines:

- • For each step, you must generate a reasoning thought and correct function call. If needed, call multiple functions.
- • If you think you have answered the question, thoroughly reflect on your reasoning to verify you have in fact answered the question. If not, continue reasoning. If so, call the ‘Finish’ function and provide your final answer, which should be 1) comprehensive,

2) explain how you arrived at the answer, and 3) why the answer addresses the question.

- • If the result from the last function call is empty or not useful, you must continue reasoning and call ToolRAG (or simulate a virtual ToolRAG call) to retrieve more tools.

- – If the tool you need is in the Function List below, you must retrieve them using a virtual ToolRAG call that simulates obtaining the tool through ToolRAG.
- – If the tool you need is not in the Function List below, you need to call ToolRAG.
- – {Description of ToolRAG and virtual ToolRAG tools}


- • Do not answer the question based on general knowledge. You must answer the question based on the information returned by the tools.
- • If all previous solution attempts have failed, do not repeat the same thoughts and function calls. Instead, come up with new solution approaches.


Function List: {available tools description of the initial set of tools Pˆ0}

For each reasoning step, respond in this JSON format: {reasoning step format}

For the final step, respond in this JSON format, providing the final answer and a detailed

explanation: {final reasoning step format} Previous reasoning steps: {previous multi-step reasoning trace} Hint for next step: {solution hint from Helper agent}

## References

- 1. Huang, K. et al. A foundation model for clinician-centered drug repurposing. Nature Medicine 30, 3601–3613 (2024).
- 2. Dubey, A. et al. The llama 3 herd of models. arXiv preprint arXiv:2407.21783 (2024).
- 3. Radford, A., Narasimhan, K., Salimans, T., Sutskever, I. et al. Improving language understanding by generative pre-training (2018).
- 4. Jiang, A. Q. et al. Mistral 7b. arXiv preprint arXiv:2310.06825 (2023).
- 5. Touvron, H. et al. Llama: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971 (2023).
- 6. Bai, J. et al. Qwen technical report. arXiv preprint arXiv:2309.16609 (2023).
- 7. Singhal, K. et al. Large language models encode clinical knowledge. Nature 620, 172–180

(2023).

- 8. Singhal, K. et al. Toward expert-level medical question answering with large language models. Nature Medicine 1–8 (2025).
- 9. Chen, Z. et al. Meditron-70b: Scaling medical pretraining for large language models. arXiv preprint arXiv:2311.16079 (2023).
- 10. Alber, D. A. et al. Medical large language models are vulnerable to data-poisoning attacks. Nature Medicine 1–9 (2025).
- 11. Yan, F. et al. Berkeley function calling leaderboard. https://gorilla.cs.berkeley.edu/blogs/8 b erkeley function calling leaderboard.html (2024).

- 12. Dadao, I. watt-tool-8b: A fine-tuned language model for tool usage and multi-turn dialogue. https://huggingface.co/watt-ai/watt-tool-8B (2025).
- 13. Liu, W. et al. Toolace: Winning the points of llm function calling. arXiv preprint arXiv:2409.00920 (2024).
- 14. Gao, Y. et al. Retrieval-augmented generation for large language models: A survey. arXiv preprint arXiv:2312.10997 (2023).
- 15. Gao, S. et al. Empowering biomedical discovery with ai agents. Cell 187, 6125–6151 (2024).
- 16. Boiko, D. A., MacKnight, R., Kline, B. & Gomes, G. Autonomous chemical research with large language models. Nature 624, 570–578 (2023).
- 17. Yao, S. et al. React: Synergizing reasoning and acting in language models. In International Conference on Learning Representations (ICLR) (2023).
- 18. Bran, A. M. et al. Chemcrow: Augmenting large-language models with chemistry tools. arXiv preprint arXiv:2304.05376 (2023).
- 19. Swanson, K., Wu, W., Bulaong, N. L., Pak, J. E. & Zou, J. The virtual lab: Ai agents design new sars-cov-2 nanobodies with experimental validation. bioRxiv 2024–11 (2024).


- 20. Kass-Hout, T. A. et al. Openfda: an innovative platform providing access to a wealth of fda’s publicly available data. Journal of the American Medical Informatics Association 23, 596–600

(2016).

- 21. Ochoa, D. et al. The next-generation open targets platform: reimagined, redesigned, rebuilt. Nucleic acids research 51, D1353–D1359 (2023).
- 22. Castellanos, F. et al. The human phenotype ontology in 2024: phenotypes around the world. Nucleic Acids Research 52 (2024).
- 23. OpenAI. Gpt-4o (2024).
- 24. Gallifant, J. et al. Language models are surprisingly fragile to drug names in biomedical benchmarks. arXiv preprint arXiv:2406.12066 (2024).
- 25. Chen, C. et al. Clinicalbench: Can llms beat traditional ml models in clinical prediction? arXiv preprint arXiv:2411.06469 (2024).
- 26. Guo, D. et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint arXiv:2501.12948 (2025).
- 27. Lewis, P. et al. Retrieval-augmented generation for knowledge-intensive nlp tasks. Advances in Neural Information Processing Systems 33, 9459–9474 (2020).
- 28. Chandak, P., Huang, K. & Zitnik, M. Building a knowledge graph to enable precision medicine. Nature Scientific Data (2023).
- 29. Ji, C. C.-J. et al. Gorilla openfunctions v2 (2024).
- 30. OpenAI. Introducing openai o1-preview (2024).
- 31. Gloss, D., Moxley, R. T. I., Ashwal, S. & Oskoui, M. Practice guideline update summary: Corticosteroid treatment of duchenne muscular dystrophy. Neurology 86, 465–472 (2016).
- 32. Matsuo, M. Antisense oligonucleotide-mediated exon-skipping therapies: precision medicine spreading from duchenne muscular dystrophy. JMA journal 4, 232–240 (2021).
- 33. Su, X. et al. Multimodal medical code tokenizer. arXiv:2502.04397 (2025).
- 34. Brown, T. et al. Language models are few-shot learners. Advances in neural information processing systems 33, 1877–1901 (2020).
- 35. U.S. Food and Drug Administration. openfda (2024).
- 36. Targets, O. 24.09 platform release now live. https://community.opentargets.org/t/24-09-platf orm-release-now-live/1556?ref=blog.opentargets.org (2024).
- 37. Li, Z. et al. Towards general text embeddings with multi-stage contrastive learning. arXiv preprint arXiv:2308.03281 (2023).
- 38. Vaswani, A. Attention is all you need. Advances in Neural Information Processing Systems

(2017).

- 39. Hu, E. J. et al. Lora: Low-rank adaptation of large language models. arXiv preprint arXiv:2106.09685 (2021).


- 40. von Werra, L. et al. Trl: Transformer reinforcement learning. https://github.com/huggingface /trl (2020).
- 41. Tunstall, L. et al. The Alignment Handbook.
- 42. Wolf, T. et al. Transformers: State-of-the-art natural language processing. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations, 38–45 (Association for Computational Linguistics, Online, 2020).
- 43. Rasley, J., Rajbhandari, S., Ruwase, O. & He, Y. Deepspeed: System optimizations enable training deep learning models with over 100 billion parameters. In Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, 3505– 3506 (2020).
- 44. Paszke, A. et al. Automatic differentiation in pytorch. In NIPS-W (2017).


