1234567890():,;

1234567890():,;

npj | computational materials Article

Published in partnership with the Shanghai Institute of Ceramics of the Chinese Academy of Sciences

https://doi.org/10.1038/s41524-025-01564-y

# Fine-tuning large language models for domain adaptation: exploration of training strategies, scaling, model merging and synergistic capabilities

![image 1](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile1.png)

Check for updates

A list of authors and their afﬁliations appears at the end of the paper

The advancement of Large Language Models (LLMs) for domain applications in ﬁelds such as materials science and engineering depends on the development of ﬁne-tuning strategies that adapt models for specialized, technical capabilities. In this work, we explore the effects of Continued Pretraining (CPT), Supervised Fine-Tuning (SFT), and various preference-based optimization approaches, including Direct Preference Optimization (DPO) and Odds Ratio Preference Optimization (ORPO), on ﬁne-tuned LLM performance. Our analysis shows how these strategies inﬂuence model outcomes and reveals that the merging of multiple ﬁne-tuned models can lead to the emergence of capabilities that surpass theindividual contributions of the parent models. We ﬁnd that model merging is not merely a process of aggregation, but a transformative method that can drive substantial advancements in model capabilities characterized by highly nonlinear interactions between model parameters, resulting in new functionalities that neither parent model could achieve alone, leading to improved performance in domain-speciﬁc assessments. We study critical factors that inﬂuence the success of model merging, such as the diversity between parent models and the ﬁne-tuning techniques employed. The insights underscore the potential of strategic model merging to unlock novel capabilities in LLMs, offering an effective tool for advancing AI systems to meet complex challenges. Experiments with different model architectures are presented, including the Llama 3.1 8B and Mistral 7B family of models, where similar behaviors are observed. Exploring whether the results hold also for much smaller models, we use a tiny LLM with 1.7 billion parameters and show that very small LLMs do not necessarily feature emergent capabilities under model merging, suggesting that model scaling may be a key component. In open-ended yet consistent chat conversations between a human and AI models, our assessment reveals detailed insights into how different model variants perform, and shows that the smallest model achieves a high intelligence score across key criteria includingreasoning depth,creativity,clarity, andquantitativeprecision.Otherexperimentsincludethe development of image generation prompts that seek to reason over disparate biological material design concepts, to create new microstructures, architectural concepts, and urban design based on biological materials-inspired construction principles. We conclude with a series of questions about scaling and emergence that could be addressed in future research.

e-mail: mbuehler@mit.edu

The development of Large Language Models (LLMs)1–6 has enhanced our abilities for natural language processing (NLP) in scientiﬁc and engineering applications, due to signiﬁcant advancementsacross diverse domains, from general-purpose applications to specialized ﬁelds such as materials science and engineering7–14. These models, including prominent open-source architectures like Llama and Mistral, have demonstrated strong capabilities in understanding and generating human-like text. However, their application in technical ﬁelds requires ﬁne-tuning strategies that adapt these modelstospeciﬁcdomainchallengesandtechnicalrequirements,whichare often poorly understood. In the ﬁeld of biomateriomics, for instance, researchers aim to develop systematic explorations of knowledge across scales, domains, and application areas, including biological material design inspiration7,15–19.Theseandotherchallengescanbeaddressedsynergistically using multimodal reasoning engines that have, at their core, capabilities derived from LLMs. One rationale is that LLMs have shown strong capabilities to integrate diverse concepts and provide an integrative modeling strategy for diverse contexts seen in biological materials engineering7,20.

Fine-tuningLLMsfordomain-speciﬁcapplicationsinvolvesmorethan simplyretrainingonspecializeddata;itrequirestheexplorationofstrategies toendowthemodelwithnewknowledgewhileretainingcapabilitieslearned in earlier training stages, to yield optimal model performance. This is particularly challenging since most of the time it is not feasible to train models from scratch due to cost, or because the original datasets are not available. This is a particular concern in open-source models like Llama or Mistral, where certain details about the training process have been released, but the full datasets during pre-training, ﬁne-tuning, and alignment phases are unknown4,6.

An often-effective strategy that has been used in earlier work is lowrank adaptation (LoRA)21, where a set of small trainable low-rank tensors is added to linear layers of a larger model to adapt it towards new capabilities14,21,22. While this can be an effective method, there are limits to how mucha model can be improved and how much new knowledge can be incorporated. Other research suggested that continued pre-training (CPT) on domain-speciﬁc corpora can help better introduce new knowledge within the target domain23, enhancing itsrelevance and accuracy. However, this typically requires a host of additional strategies to make a model useful fordownstreamapplications,suchasinstructionfollowing,chatinteraction, agentic use, tool calling, and others. Supervised ﬁne-tuning (SFT) is a method used to reﬁne these models by directly teaching them to perform well on speciﬁc tasks through curated datasets. However, the potential for further enhancing model performance and unlocking new capabilities through advanced optimization techniques remains a critical area of exploration. In this context, preference-based optimization strategies, such as Direct Preference Optimization (DPO)24 and Odds Ratio Preference Optimization (ORPO)25, have emerged as promising approaches. Unlike traditional Reinforcement Learning (RL) methods26, which often require explicit reward functions and complex environment models, DPO and

ORPOfocusonoptimizingmodelsbased ondirect feedbackorpreferences. These methods offer a ﬂexible and efﬁcient means of reﬁning model behavior, particularly when the goal is to align the model’s outputs with humanexpectationsordomain-speciﬁccriteria,suchasbeingabletoreason over or logically deduce answers in a particular domain, such as materials science.

Another area of recent interest is the practice of model merging27–29, where multiple, differently trained models are combined to create a new model with potentially superior capabilities. Earlier experiments have shown that this process is not simply additive; as we will show, it leads to highlynonlinearinteractionsbetweentheparametersofthemergedmodels, resulting in the emergence of new functionalities that neither parent model possessed individually. Such emergent behavior suggests that model merging could be a powerful tool for advancing LLM capabilities, enabling the development of models that are not only more accurate but also more adaptable to complex, real-world challenges.

As thisbrief review shows,there are a myriad of possible strategies, but relativelylittledataisavailableintermsofsystematicexplorations.LLMsare highlycomplexmodels,andtrainingisexpensiveandtime-consuming,and often developers focus on a particular approach that yielded acceptable results. Here we take a different approach and speciﬁcally investigate the effects of various ﬁne-tuning and optimization strategies on LLM performance,withaparticularfocusonasystematic,consistentsetofexperiments assummarizedinTable1.Figure1showsanoverviewofthetrainingcorpus and information processing, covering both the general process of utilizing different types of data (raw, processed/distilled, conversational, etc.) and a visualization of the transformation fromindividual pieces of information to a structured network of interconnected insights.

Theplanofthepaperisasfollows.Weﬁrstpresentabriefintroduction into key concepts, then present results along with a discussion, followed by conclusions. We present detailed methods and references to codes and model weights, and discuss our dataset creation, development, and training mechanisms.

Results

We follow the process depicted in Fig. 2 in developing models and conducting assessments. Figure 2A shows a conventional linear training pipeline where a base model undergoes Continued Pre-Training (CPT), followed by Supervised Fine-Tuning (SFT), and then optimized using methods like Direct Preference Optimization (DPO) or Odds Ratio PreferenceOptimization(ORPO)toproduceatrainedmodel.Figure2Bshows an alternative pipeline where, after CPT, SFT, and optimization (e.g., DPO, ORPO), the model is further enhanced by merging it with another ﬁnetuned model (e.g., a general-purpose model). We note that model merging canbedonewithmodelsextractedfromvarioustrainingstages,suchasafter CPT, SFT or at the ﬁnal stage. The implementation process is structured sequentially, with each step building upon the previous one to enhance the

- Table 1 | Summary of model development approaches explored with datasets used, and a brief description of capabilities


Approach Deﬁnition Example Dataset type

CPT (Continued PreTraining)

Continuing the training of a language model on a speciﬁc domain or additional data after initial pretraining (no template/instruction format use).

Enhancing model knowledge in specialized ﬁelds like materiomics, bioinformatics, or broader ﬁelds like materials science.

Raw text from papers plus text with reasoning, summarization, distillation

SFT (Supervised FineTuning)

Fine-tuning a pre-trained model using labeled data with supervised learning techniques.

Adapting models to speciﬁc tasks such as QA, reasoning,scientiﬁcmethod,ordialogsystems.

Question-answer or instructionanswer pairs, conversations

DPO (Direct Preference Optimization)

Optimizing a model by directly learning from preferences, often involving human feedback or ranking.

Aligning models with human preferences for content generation, physics-awareness, reasoning, or human considerations.

Positive/negative examples

ORPO (Odds Ratio Preference Optimization)

A reference model-free monolithic odds ratio preference optimization algorithm that eliminates theneedforaseparatepreferencealignmentphase.

Reﬁning models without a baseline reference, using direct odds ratio for preference tasks.

Positive/negative examples

Model Merging Combining multiple models or checkpoints into a single model, e.g., using techniques like spherical linear interpolation (SLERP).

Creating hybrid models that incorporate strengths from different pre-trained models.

No training data used

![image 2](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile2.png)

| | |
|---|---|
| | |


- Fig. 1 | Overview of the approach used in this study, including the scientiﬁc training corpus and information processing. A Thetrainingcorpus comprises raw text from various sources such as papers, documents, and websites. This text undergoes extraction of keyinsights, reasoning, and logical deduction, leadingtothe generation of question-answer or instruction-response pairs. B Visualization of the transformation from individual pieces of information (here shown as scattered


nodes of varying sizes) to a structured network of interconnected insights, illustrating the consolidation of knowledge through the training process. This overall schematic illustratesthegoals ofthisresearch, tobuildmodels forcomplex problems that integrate distinct features, modalities, and concepts. The image above “Actionable outcomes” was generated using lamm-mit/leaf-ﬂux.

model’s capabilities in stages. As summarized in Table 1, CPT exposes the model to domain-relevant data, while SFT delivers task-speciﬁc instruction using labeled datasets in formats such as question-answer or instructionresponse. Preference optimization methods (e.g., DPO or ORPO) align the modelwithhumanorbaselinepreferencesestablishedinpriorsteps.Finally, modelmergingintegratesthestrengthsofdifferenttrainingpaths,leadingto improved generalization and, in many cases, the emergence of new capabilitiesabsentfromindividualmodels.Thisstructuredprogressionensures a balance between task-speciﬁc accuracy and user preference alignment by addressing knowledge acquisition and preference tuning at distinct stages.

Forthepurposeoftheanalysis,wegointothedetailsofmodelmerging strategies. In this work, we focus on Spherical Linear Interpolation (SLERP, details see “Materials and methods” section), as we found it to be the most effective method. SLERP is a mathematical technique originally introduced in the ﬁeld of computer graphics for smoothly interpolating between rotations represented by quaternions30. SLERP has found widespread application in various domains that require smooth transitions between orientationsorstates,includingrobotics,physicssimulations,aswellasrealtime graphics. For instance, in robotics, SLERP is used for the practical parameterization of rotations, allowing for seamless motion planning and control31. In physics simulations and computer graphics, SLERP is crucial for visualizing and animating rotations in a way that preserves the continuity and smoothness of motion32,33. By maintaining the geometric relationships between interpolated states, SLERP ensures that transitions are both smooth and physically meaningful, making it a useful tool in scenarios

where precise and continuous interpolation is required. Figure 3 shows the basic concepts of SLERP (versus linear interpolation, LERP), visually. A key aspectofthisstrategyisthatthesmooth,nonlinearpathhelpstopreservethe underlying structure of the model parameters. The sphere in this context represents the inherent structure of the model’s parameter space, and by maintaining the geometric relationship between the parameters, SLERP ensures that the interpolation respects this original structure and does not puncture it (as linear combination of points would), leading to a more meaningful and coherent blending of capabilities rather than random, unstructured changes. Because the merged points are both congruent with the model geometry (that is, they lie on the sphere used here for demonstration) and because they realize new points previously not accessed, emergent features and capabilities could potentially be unlocked. The smoothness and spherical symmetry assumed in SLERP help preserve angular relationships between parameters, avoiding high-loss regions typically encountered in linear interpolation. This capability is especially beneﬁcial for materials science applications, where parameter space discontinuities and asymmetries are common. SLERP enables better generalization and the development of emergent capabilities, making it a powerful tool in this domain.

In the following, we present a series of results from assessment experiments conducted with different model families and training/merging strategies (details on training, models, datasets, and assessment benchmarks, see “Materials and methods” section). Figure 4 depicts a series of performance evaluations of Llama-3.1 Model variants across

| |
|---|


- Fig. 2 | Model training, merging and assessment stages. A A conventional training pipeline where a base model undergoes Continued Pre-Training (CPT), followed by Supervised Fine-Tuning (SFT), and then optimized using methods like Direct Preference Optimization (DPO) or Odds Ratio Preference Optimization (ORPO) to produce a trained model. Assessment of the model can be performed at each of the


stages, such as using the SFT results for benchmarking. B An alternative pipeline where, after CPT, SFT, and optimization (e.g., DPO, ORPO), the model is further enhanced by merging it with another ﬁne-tuned model (e.g., a general-purpose model). Merging can be done with models extracted from various training stages, such as after CPT, SFT or at the ﬁnal stage.

benchmarks. We use two basic models as the foundation for our training. First, meta-llama/Meta-Llama-3.1-8B, the base model of the Llama family that has not been ﬁne-tuned and aligned. Second, the metallama/Meta-Llama-3.1-8B-Instruct model that has been ﬁnetuned and aligned to conduct question-answer interactions, along with a hostofothercapabilities6.ExceptfortheLoRAcase14,allofourexperiments include CPT (see Table 1 for an overview of the training stages and acronyms used) as the ﬁrst step, with the aim to endow the base model with domain knowledge from our materials science corpus of papers and distilled, extracted and processed datasourcedfrom scientiﬁc studies. We then implement a range of variations, such as CPT only, CPT-SFT, CPT-SFTORPO and CPT-SFT-DPO. At each stage, we also implement model merging with the meta-llama/Meta-Llama-3.1-8B-Instruct model. Overall, the results reveal that the models that have undergone SLERP merging (especially those combined with DPO and ORPO strategies) generally show the highest accuracy across benchmarks. The best strategy without model merging is found to be the Instruct-CPT-SFT-DPO strategy.

We now conduct the same series of experiments using Mistralv0.3 model variants4 across benchmarks. As in the previous set of results, we use the same dataset across all cases, and we present both non-merged cases and merges with the mistralai/Mistral-7B-Instructv0.3 model. Figure 5 depicts an overview of the performance evaluations across benchmarks for this case. As before, the results show that these modelsthathavealsoundergoneSLERPmerginggenerallyshowthehighest accuracy across benchmarks. The best strategy without model merging is found to be the Base-CPT-SFT strategy, albeit the performance of the Instruct-CPT-SFT strategy is very similar.

The CPT stage involves ﬁve epochs. To explore the effect of the number of epochs in this phase, we computed the performance of the directCPT-SLERP mergesfortheMistralmodels from differenttraining epochs. It is noted that the original merges assessed (and SFT, DPO/ ORPO training stages) in Fig. 5 were conducted based on CPT results

from epoch 5. Figure 6 depicts a comparison of averaged scores across different epochs for both the Base and Instruct models, using the SLERP method. Figure 6A shows an overview of the results, in a similar format as the earlier performance assessments, depicting performance across all models and variants of CPT epochs used. Figure 6B shows the performance of the Instruct model as a function of the number of CPT training epochs, and Fig. 6C illustrates the performance of the Base model. We can see that the Instruct model demonstrates a consistent improvement in performance with each epoch, peaking at the best score by epoch 5, indicating that it beneﬁts signiﬁcantly from continued training. In contrast, the Base model shows a more ﬂuctuating performance, with its highest score at epoch 1, followed by slight declines and only a minor recovery at epoch 5. This suggests that while the Base model starts strong, it does not consistently improve with additional training, potentially indicating a saturation point. Both models, however, consistently outperform the baseline score set by the original mistralai/ Mistral-7B-Instruct-v0.3 model, underscoring the effectiveness of the SLERP method, and consistent with the earlier results. The more substantial improvement of the Instruct model over the baseline highlights its robustness in instruction-tuned tasks, making it the preferable choice for such applications, particularly when extended ﬁnetuning is feasible.

Detailed analysis of key factors in model merging

As the results in Figs. 4 and 5 clearly reveal, SLERP appears to signiﬁcantly improve model performance due to its ability to respect the geometric properties of the parameter space. However, this analysis did not yet reveal whetherwehaveasigniﬁcantsynergisticeffect.Toexaminethis,weplotthe results differently, comparing the actual measured performance with an expected performance that is computed by simply averaging the scores of thetwoparentmodels.Toproperlydeﬁneallkeyvariables,theperformance of amergedmodelisdeﬁnedasPmerged;P

1;P2 (measuredperthe benchmark), while the expected, averaged score E(P1, P2) is calculated as the linear

![image 3](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile3.png)

- Fig.3| Comparison of SLERP (Spherical Linear Interpolation) andLERP(Linear Interpolation) between two points on a unit sphere, illustrating their application in merging Large Language Model (LLM) parameters. SLERP interpolates


represented by the unit sphere, potentially unlocking novel interactions between features that lead to enhanced performance and the development of emergent capabilities. The sphere in this context represents the inherent structure of the model’s parameter space, and by maintaining the geometric relationship between the parameters, SLERP ensures that the interpolation respects this original structure and does not puncture it (as the LERP points would), leading to meaningful and coherent blending of capabilities rather than random, unstructured changes. A key point is that because the merged points are both congruent with the model geometry (that is, they lie on the sphere used here for demonstration) and because they realize new points previously not accessed, emergent features and capabilities could potentially be unlocked.

between points p1 and p2 along a spherical path on the surface of the sphere, calculated as SLERP(t), where t is the interpolation parameter (equations see main text). In contrast, LERP interpolates linearly between the same two points, following a straight line through the sphere. Intermediate points at 30% and 70% along both paths are highlighted, showing the difference in how SLERP and LERP handle interpolation. In the context of LLMs, SLERP is particularly effective for merging model parameters from different pre-trained models, facilitating the emergence of new abilities that neither parent model possessed alone. The smooth, nonlinear path of SLERP helps to preserve the underlying structure of the model parameters,

average of the performances of the two parent models:

P1 þ P2 2

EðP1; P2Þ ¼

:

Usingthesemetrics,Fig.7showsadetailedexplorationofperformance of SLERP variants for different cases, plotting the actual observed performance over an estimated, expected score based on a simple average of the score of both parent models (linear combination).

Notably, the strong deviation from the diagonal reveals nonlinear, synergistic effects, where the actual observed model performance is much greater than a simple averaging of the capabilities of the parent models alone. Results are shown for both the Llama-3.1-8B and Mistral7B-v0.3 model series, respectively, for a variety of training strategies and datasets used in the process. We ﬁnd that the results are similar for both models. An important distinction that can be seen in the analysis is that for the Llama models, the best-performing model (lamm-mit/Llama3.18b-Instruct-CPT-ORPO-SLERP) is based off the Llama Instruct model, whereas for the Mistral model (lamm-mit/mistral-7BBase-v0.3-CPT-SFT-SLERP) it is based off the Mistral Base model.

To better understand the mechanics behind the observed effects, we brieﬂy discuss the mathematical underpinnings of SLERP merging. Unlike

linearinterpolation,whichassumesaﬂatEuclideanspace,SLERPexploresa richerparameterspacebyinterpolatingalongacurvedpathonaunitsphere (we refer also to Fig. 3). This approach allows SLERP to uncover regions in theparameterspacethatmightrepresentcombinationsofparametersmore effectivethanthosefoundineithermodelalone.SLERPfurtherbalancesthe specialized knowledge learned by each model, combining their strengths without simply averaging them. By avoiding high-loss regions that linear interpolation might pass through, SLERP ensures a smoother transition, potentially leading to better generalization in the merged model. The nonlinear nature of SLERP’s path also considers the complex interactions between parameters, which can reveal beneﬁcial interactions that a simple linear combination would miss. Furthermore, SLERP may act as a form of regularization, preventing overﬁtting to the idiosyncrasies of a single model’s training data, thus enhancing generalization. Finally, SLERP helps mitigate the effects of catastrophic forgetting, preserving knowledge from both models when one has been ﬁne-tunedor trained afterthe other. These factors combine to makeSLERP apowerful toolformodelmerging, leading to a merged model that often performs better than either of the original models on their own.

Hence, we believe that the observed effectiveness of SLERP in merging models can be attributed to its ability to enhance nonlinear interactions between parameters by exploring the spherical geometry of

![image 4](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile4.png)

![image 5](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile5.png)

![image 6](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile6.png)

![image 7](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile7.png)

![image 8](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile8.png)

![image 9](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile9.png)

![image 10](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile10.png)

![image 11](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile11.png)

![image 12](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile12.png)

![image 13](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile13.png)

![image 14](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile14.png)

![image 15](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile15.png)

![image 16](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile16.png)

![image 17](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile17.png)

![image 18](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile18.png)

the parameter space. Given two sets of model parameters θ1 and θ2, each parameter can be seen as a vector in a high-dimensional space. The interpolation performed by SLERP respects the curvature of this space, allowing for combinations of parameters that are not simply linear but involve deeper, nonlinear synergies (see Fig. 3). Consider the parameters θ1 and θ2 as consisting of individual components θ1,i and θ2,i in a given

layer of the neural network. SLERP combines these parameters as follows:

θi;merged ¼k θ1k1 t k θ2kt

sinðð1 tÞωÞ sinðωÞ

sinðtωÞ sinðωÞ

^θ1;i þ

^θ2;i

- Fig. 4 | Performance evaluation P of Llama-3.1 model variants across benchmarks. A Accuracy results for various variants on different benchmarks: Spider Silk, Bio-inspired/Biological Materials, and Overall Accuracy. The models were evaluated after undergoing different training and optimization strategies (Continued Pre-Training (CPT), Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO)/Odds Ratio Preference Optimization (ORPO), and model merging). B Relative improvement of model variants over the meta-llama/ Meta-Llama-3.1-8B-Instruct baseline model. This highlights how each training strategy contributes to the model’s performance gains or losses across the variousbenchmarks, providinginsightintotheeffectivenessofdifferent approaches. It is notable that models that underwent CPT, SFT, and to some extent preference


optimization (e.g., DPO, ORPO) show a deterioration in performance, as indicated by negative relative improvement values. However, after applying the Spherical Linear Interpolation (SLERP) merging technique, these same models exhibit signiﬁcant performance gains, surpassing the baseline model. This highlights the effectiveness of model merging in combining the strengths of different specialized models, resulting in a robust ﬁnal model with superior overall performance. Overall, the results show that the models that have undergone SLERP merging (especially those combined with DPO and ORPO strategies) generally show the highest accuracy across benchmarks. Merging in this case is always done with meta-llama/ Meta-Llama-3.1-8B-Instruct. All models have been trained with the same datasets in all stages, as shown in Table 6.

This combination allows for interactions between θ1,i and θ2,i that are nonlinearinnature.Forexample,ifθ1,iandθ2,irepresentweightsconnected to different features in the network, their spherical combination could activate a new feature ϕi that is not present in either model individually:

ϕi ¼ f θi;merged xi

wherexiistheinputfeatureandf(⋅)istheactivationfunction.Thenonlinear combinationof parameters may lead to new behaviorsorcapabilities, as the interpolated parameters could synergistically enhance or suppress features in ways that the individual models cannot.

SLERP avoids destructive interference by maintaining the angular relationships between the parameter vectors, which can prevent the loss of specialized features learned by either model. The spherical symmetry imposed by SLERP introduces a regularization effect, smoothing the transition between the models and enabling the merged model to generalize better. This process often results in the emergence of new capabilities or improvementsinperformancethatneitheroftheoriginalmodelspossessed.

The ability of SLERP to uncover these new capabilities can also be understood through the lens of overparameterization and the principles of ensemble methods. Overparameterized neural networks are known to generalize well, even when trained to zero error, due to their increased capacity to capture complex patterns34. SLERP leverages this capacity by combining parameters in a nonlinear fashion, effectively utilizing the highdimensional space in which these parametersreside.As a result, the merged model can exhibit emergent properties that are not apparent in either of the original models. SLERP’s mechanism resembles ensemble methods, where combining diverse models leads to better generalization35. In this case, the diversity comes from the different training histories and learned features of the two models. The spherical interpolation pathway created by SLERP acts as a continuum of model ensembles,where at each pointalong the path, the combined parameters may activate new and beneﬁcial feature interactions. SLERPnotonlypreservesthestrengthsoftheindividualmodelsbutalsohas the potential to generate entirely new capabilities through its sophisticated interpolation method. This makes it a useful tool for our goal to merge models that complement each other or to create a more versatile and generalizable model from existing pre-trained models.

We examine the variations and potential trends in the strategies explored using clustering analysis. Figure 8 provides a comprehensive clustering analysis of SLERP strategies applied to both the Llama-3.18b and Mistral-7B-v0.3 models, and the resulting impact on their performance.Weexploretheuseoftwomethods.First,K-Meansclustering, a partition-based method that groups data into a predeﬁned number of clusters by minimizing the distance between data points and the cluster centroids, providing insight into the natural groupings of models based on their expected and actual performance. Second, we use hierarchical clustering, an agglomerative method that creates a tree-like structure, a dendrogram, to show the nested relationships between models at various levels of similarity, revealing the hierarchical organization and potential subgroupings within the data.

Figure 8 A illustrates the K-Means clustering of the Llama-3.1-8b models using standardized expected and actual scores, with Gaussian KDE (Kernel Density Estimation) applied to visualize the centroids. The analysis reveals distinct groupings that correspond to different SLERP strategies, indicating that speciﬁc merging techniques produce closely related performance outcomes.Figure8BpresentsasimilarK-MeansclusteringfortheMistral7B-v0.3models.Heretoo,distinctclustersemerge,showingthattheSLERP strategiessigniﬁcantlyinﬂuencethemodels’performanceproﬁles.Notably,the clustering patterns observed in the Mistral models are more pronounced compared to the Llama models, suggesting that the Mistral architecture might be more sensitive to these optimization and merging strategies.

Across both the Llama and Mistral models, the K-Means analysis clearly delineates two performance-based clusters. Models that incorporate multiple ﬁne-tuning strategies, especially ORPO, consistently form clusters with higher actual scores, outperforming models that rely on simpler strategies. This suggests that the complexity and thoroughness of the ﬁnetuning process play a crucial role in achieving better model performance,as indicatedbytheclusteringresults.Nextweexplorehierarchicalclusteringas a way to better break down these distinctions.

To do this, we use a dendrogram analysis. A dendrogram is a tree-like diagram that displays the arrangement of clusters generated through hierarchicalclustering.Thisvisualizationhelpselucidatetherelationshipsamong the models, with closely related models (in terms of performance) clustering together. The dendrogram reveals that models employing similar training strategies are grouped into distinct subclusters, highlighting the effectiveness oftheseapproachesinshapingmodelperformance.Figure8Cintroducesthe hierarchical clustering dendrogram for the Llama-3.1-8b models, and Fig. 8D for the Mistral-7b models. The dendrogram demonstrates how different models cluster together, indicating similar performance outcomes. When comparing the dendrograms of the Llama and Mistral models, it becomes evident that while both models are positively inﬂuenced by SLERP strategies, the Mistral models show more deﬁned clustering patterns. This suggestsastrongerimpactofthevariousstrategiesontheMistralarchitecture.

Figure 9 shows the effect of using a larger CPT dataset using the extended dataset of 8000 papers, but with more varied format including more defected text, when training the Llama series. As can be seen, performance decreases, underscoring the effect of higher quality, clean data for positive training outcomes. As mentioned earlier, the extended dataset was constructed using a mix of PDF2Text and Nougat OCR36; we found these methods to yieldmore variable text quality. While, forinstance,Nougat can successfully render equations in Markup format, it also leads to a relatively frequentoccurrenceofunknownsymbols,pagebreaks,repeatedcharacters, and other defects. These methods did not cause issues when the data was further processed into question-answer pairs or summaries, rational explanations, and so on, but there is an apparent negative effect on CPT as the data is provided in raw format.

Likewise, a similar test case with the extended dataset was conducted with the Mistral series of models. The variant trained on the original integrated dataset achieved the best overall benchmark of 0.81, whereas the variant trained on the extended dataset achieved 0.80. These results suggest that future experiments could be conducted to assess the effect of this particular dataset variation on that model architecture’s performance. We

![image 19](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile19.png)

![image 20](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile20.png)

![image 21](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile21.png)

![image 22](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile22.png)

![image 23](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile23.png)

![image 24](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile24.png)

![image 25](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile25.png)

![image 26](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile26.png)

![image 27](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile27.png)

![image 28](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile28.png)

![image 29](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile29.png)

![image 30](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile30.png)

![image 31](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile31.png)

![image 32](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile32.png)

leave this to future work; noting that the overall effects of model merging and the use of Base vs. Instruct models as basis are stable, with differences, however, in which exact strategy yields the best results: For the Llama and Mistralmodels,itwasInstruct-CPT-SFT-ORPO-SLERPandInstruct-CPTORPO-SLERP. These observations are further complicated by the effect of prompting, which can skew results one way or the other. An overarching

theme, however, is that consistently, SLERP merging yields super performance. For a straightforward and computationally effective way to implementaﬁne-tuningstrategy,theprocedureInstruct-CPT-SLERPisprobably the best overall choice. While it does not yield the best performance for all scenarios, it generally yields strong performance. The differences show that nuanced benchmarking and prompt engineering can be critical.

- Fig. 5 | Performance evaluation P of Mistral-7B-v0.3 model variants. A Accuracy results for various Mistral-7B-v0.3 model variants on the Spider Silk, Bio-inspired/Biological Materials,and Overall Accuracy benchmarks. Initial models trained with Continued Pre-Training (CPT) and Supervised Fine-Tuning (SFT) show moderate performance. Models further optimized using Odds Ratio Preference Optimization (ORPO) or Direct Preference Optimization (DPO) exhibit signiﬁcant improvements in accuracy across all benchmarks. Model merging results in further signiﬁcant improvements. The relative improvements are even more pronounced thanthose seen intheLlama-3.1 models (here exceeding 20%versus around 12%), indicating the particular effectiveness of these techniques for the Mistral series. B Relative improvement of model variants over the baseline

mistralai/Mistral-7B-Instruct-v0.3 model. The Base model subjected to CPT alone initially shows a decrease in relative performance. However, after SFT, ORPO and especially after applying Spherical Linear Interpolation (SLERP) merging, especially with ORPO or DPO optimization, these models demonstrate substantial positive relative improvement, surpassing the baseline by a greater margin than the improvements seen in the Llama-3.1 models. This highlights the powerful impact of these combined strategies in enhancing the overall performanceof theMistral models. Itis notablethat adirect merge of the Base-CPTSFT model results in signiﬁcant performance, close to the Instruct-CPT-SFT strategy. Merging is always done with mistralai/Mistral-7B-Instructv0.3. The same training set is used for all experiments, as deﬁned in Table 6.

![image 33](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile33.png)

![image 34](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile34.png)

![image 35](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile35.png)

![image 36](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile36.png)

![image 37](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile37.png)

![image 38](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile38.png)

![image 39](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile39.png)

- Fig. 6 | Comparison of averaged scores across different epochs for both the Base and Instruct models ﬁne-tuned with the Spherical Linear Interpolation (SLERP) method. The baseline score for the mistralai/Mistral-7B-Instructv0.3 model is indicated by the red dashed line in both subplots. A shows an overview of the results, in similar format as the earlier performance assessments


(Figs. 4 and 5), showing performance across all models and variants of Continued Pre-Training (CPT) epochs used. B shows the performance of the Instruct model over ﬁve training epochs, while C subplot illustrates the performance of the Base model over ﬁve epochs.

![image 40](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile40.png)

![image 41](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile41.png)

![image 42](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile42.png)

![image 43](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile43.png)

![image 44](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile44.png)

![image 45](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile45.png)

![image 46](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile46.png)

![image 47](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile47.png)

![image 48](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile48.png)

![image 49](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile49.png)

![image 50](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile50.png)

![image 51](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile51.png)

![image 52](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile52.png)

![image 53](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile53.png)

![image 54](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile54.png)

![image 55](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile55.png)

![image 56](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile56.png)

![image 57](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile57.png)

![image 58](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile58.png)

![image 59](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile59.png)

![image 60](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile60.png)

![image 61](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile61.png)

- Fig. 7 | Exploration of performance of Spherical Linear Interpolation (SLERP) variants for different cases, plotting the actual observed performance of the


much smaller SmolLM family of models, where the deviation of the observed score from the expected score is not as signiﬁcant, and even below the best performance of one of the pre-merged models (see Fig. 13 for a detailed analysis). Results for the Llama and Mistral models are similar across all experiments and show a clear nonlinear effect of model merging. As marked with a red circle, ∘, the CPT-BaseSLERP strategy tends to yield some of the highest deviation from the expected score and is, at the same time, a relatively straightforward training strategy.

mergedmodelPmerged;P

1;P2 overalinear,expectedaveragescoreE(P1,P2)basedon a simple average of the score of both parent models (linear combination). The deviation from the diagonal shows clear nonlinear, synergistic effects, where the actual observed model performance is much greater than a simple averaging of the capabilities of the parent models alone. Results are shown for both the Llama-3.1

- (A)andMistral-7B-v0.3 (B)model series, respectively. Cshowsresults forthe


Mechanistic analysis to elucidate key steps with highest impact on performance

As a next step in the analysis, we focus on correlation heatmaps to illustrate the relationships between various model attributes and the performance of merged models. As shown in Fig. 10, the performance of a merged model is denoted as Pmerged, while the performance of the two parent models is denotedasP1andP2.Performanceimprovementisdeﬁnedasthedifference between the performance of the merged model and the maximum

performance of the two parent models:

PerformanceImprovement ¼ Pmerged maxðP1;P2Þ

Diversity between parent models is measured as the absolute difference between their individual performances:

Diversity ¼ jP1 P2j

![image 62](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile62.png)

- Fig. 8 | Clustering analysis of Spherical Linear Interpolation (SLERP) strategies and hierarchical clustering dendrograms for model performance. A K-Means clustering of Llama-3.1-8b models using standardized expected and actual scores, with Gaussian KDE (Kernel Density Estimation) applied to visualize the centroids. The clustering reveals distinct groupings based on the performance outcomes of various SLERP strategies. B K-Means clustering of Mistral-7Bv0.3 models using the same approach as in (A). Similar to the Llama models, distinct clusters emerge, highlighting the different performance proﬁles of the


models post-SLERP merging. A Hierarchical clustering dendrogram for the Llama-3.1-8b models based on the clustering analysis. B Hierarchical clustering dendrogram for the Mistral-7B-v0.3 models. The dendrograms in (C and D), respectively, reveal how different models cluster together, indicating that these strategies yield similar performance outcomes. The comparison between the Llama-3.1-8b (C) and Mistral-7B-v0.3 dendrograms (D) shows that whilebothmodelsrespondwelltoSLERPstrategies,theMistralmodelsexhibitmore distinct clustering patterns.

To elucidate overall trends that can be gleanedfrom the results, Fig. 10 depicts correlation heatmaps for the ﬁne-tuned Llama and Mistral models. The data reveals distinct relationships between various metrics. In Llama models, a strong negative correlation between diversity and SFT suggests that higher diversity reduces reliance on supervised ﬁne-tuning, whereas performance improvement shows moderate positive correlations with both merged performance and SFT, indicating that these factors contribute to improved outcomes. In contrast, Mistral models exhibit a more robust positive correlation between performance improvement and merged

performance, especially in instruction-tuned models, where the Base model typesigniﬁcantlyenhancesmergedperformance.ORPO,whilecontributing to performance improvements in both models, has a more pronounced impactinMistralmodels.Overall,theﬁndingssuggestthatdiversitytendsto reduce SFT dependency, particularly in Llama models, while instructiontuned Base models in Mistral beneﬁt more from merging strategies, emphasizing the importance of model selection and optimization methods.

In model merging, there are several parameter choices, including the relative density of the parameters that are preserved across the

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


- Fig. 9 | Effect of using a larger Continued Pre-Training (CPT) dataset using the extended dataset, along with the lamm-mit/magpie-ultra-v0.1 dataset, including a more varied quality with a higher content including more defected text. As can be seen, performance decreases, underscoring the effect of

higher quality, clean data for positive training outcomes. Future experiments could be done to discern these effects more clearly, especially focusing on the effect of various training data compositions.

![image 63](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile63.png)

![image 64](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile64.png)

![image 65](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile65.png)

![image 66](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile66.png)

- Fig.10|Visualizationofcorrelationheatmapstoassesstherelationshipsbetween various model attributes and the performance of merged models, where the performance of the merged model is the primary outcome of interest. The attributes considered include the diversity between parent models, the performance improvement relative to the parent models, Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO)/Odds Ratio Preference Optimization (ORPO), and whether the model is based on the Base or Instruct architecture. The correlation coefﬁcients range from −1 to 1, with positive values indicating a direct relationship between the attribute and the merged model performance, and negative values indicatinganinverserelationship.ALlamaModels:SFTshowsthestrongestpositive correlation with merged performance, suggesting that models incorporating SFT tend to achieve better results after merging. Conversely, diversity between parent models has a strong negative correlation with merged performance, implying that greater differences between parent models are associated with lower merged


performance. ORPO and the Instruct architecture exhibit moderate positive correlations with merged performance, indicating that these factors also contribute positively, though less signiﬁcantly than SFT. B Mistral Models: In the Mistral models, performance improvement shows a robust positive correlation with merged performance, particularly in instruction-tuned models, which also show a strong positive correlation between the base model type and merged performance. Diversity, however, exhibits a negative correlation with merged performance, similar to the Llama models, though the effect is less pronounced. ORPO demonstrates a moderate positive correlation with performance improvement, suggesting that this optimizationmethodcontributestoenhancedperformance inMistral models, albeit not as strongly as SFT in Llama models. The ﬁndings suggest that instruction-tuned base models and merging strategies play a crucial role in optimizing Mistral model performance, while diversity and SFT inﬂuence these outcomes differently in Llama models.

layers of the LLMs being merged. This is exempliﬁed in Fig. 3 for the two points merged at 30% vs. 70% along their SLERP paths. In Fig. 11 we conduct a systematic analysis on variants of the original SLERP merge used in the earlier examples, with a range of alternative options, for the best-performing strategy in the case of the Llama3.1 Model variants (CPT-SFT-ORPO-SLERP). As depicted visually, we vary the self-attention ﬁlter values distinctly from the multilayer

perceptron (MLP) values (Fig. 11A). Different weighting schemes are employed, starting from the reference case that was chosen based on earlier work29. Resulting performance measures are summarized in Fig. 11B, showing that Variants G and F show the best performance (where G is a simple linear progression across the depth of the LLM) (detailed performance assessments for other variants are shown in Fig. 11).

![image 67](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile67.png)

![image 68](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile68.png)

![image 69](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile69.png)

![image 70](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile70.png)

![image 71](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile71.png)

![image 72](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile72.png)

![image 73](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile73.png)

![image 74](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile74.png)

![image 75](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile75.png)

![image 76](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile76.png)

![image 77](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile77.png)

- Fig. 11 | Model merging incorporates varying the relative density of how parameters are combined across the layers of the large language models (LLMs) involved (see in Fig. 3 for the two points merged at 30% vs. 70%). The analysis shown here focuses on variants of the original Spherical Linear Interpolation (SLERP) merge used in the earlier examples, for the best-performing strategy in the caseoftheLlama-3.1Modelvariants(CPT-SFT-ORPO,thenmerge).Asdepicted


visually, we vary the self-attention ﬁlter values distinctly from the multilayer perceptron (MLP) values (A). Different weighting schemes are employed, starting from the reference case that was chosen based on earlier work29. Resulting performance measures are summarized in (B), showing that Variants G and F show the best performance (where G is a simple linear progression).

Contrasting assessments with very small LLMs

While the models studied earlier were modest in size, around 7–8 billion parameters, recent research has resulted in even smaller, yet useful, models that can be particularly useful for edge computing applications, or deployment on devices such as mobile phones or robotic systems. We now examinewhethersuchmodelsalsoshowthemarkedeffectsobservedearlier due to model merging. We conduct this analysis using the SmolLM model series, speciﬁcally the 1.7 billion parameter model. This choice is partially motivated by the complete open access of the model, training strategy, and training data. As in the earlier analyses, we start with the base model and successively apply CPT, SFT and DPO (we found that for this small model, DPO worked better than ORPO). Though never reaching the level of

absolute performance of ﬁne-tuned 7B or 8B models, in almost all ﬁnetuning cases with SmolLM, we ﬁnd the most signiﬁcant performance increases relative to its original model with the CPT-SFT-DPO version of SmolLM being the top performing variant.

As depicted in Fig. 12 while we observe a signiﬁcant emergence of new capabilities when applying SLERP to large-scale language models in the 7B and 8B parameter ranges, these emergent behaviors were absent in smaller models, such as those with 1.7B parameters. This may suggest a threshold effectwhereSLERP’spotentialtounlocknovelabilitiesiscontingentonmodel size. Smaller models might lack the same level of complexity as larger 7B–8B models that have notably richer high-dimensional parameter spaces and capabilities, especially for reasoning and knowledge recall. These ﬁndings

![image 78](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile78.png)

![image 79](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile79.png)

![image 80](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile80.png)

![image 81](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile81.png)

![image 82](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile82.png)

![image 83](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile83.png)

![image 84](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile84.png)

![image 85](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile85.png)

![image 86](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile86.png)

![image 87](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile87.png)

![image 88](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile88.png)

![image 89](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile89.png)

![image 90](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile90.png)

underscore the importance of model scale in the manifestation of emergent properties and provide critical insights into the interplay between interpolation techniques and model complexity. Our results contribute to the broader understandingofscalinglawsinneuralnetworks,highlightingtheconditions under which advanced capabilities may be realized. A summary of the observed performance over the expected, averaged performance of the base model is shown in Fig. 7C.

Further quantiﬁcation of the effects of model merging across all model architectures

To better understand whether or not and to what degree model merging improves performance over either one of the two models used for merging, we present the analysis shown in Fig. 13. The plot shows performance deviation of SLERP merged models compared to the best original model used as source.

combined with DPO yields a slight reduction in performance over the CPT-SFTDPOcase,instarkcontrasttotheearlier results forLlamaandMistral.Theemergent behaviors triggered by SLERP in larger models are not observed here, indicating a potential threshold effect. This suggests that SLERP's ability to unlock novel capabilities may depend on the scale of the model, with smaller models like the 1.7B parameter SmolLM failing to exhibit these emergent properties. These ﬁndings underscore the critical role of model scale in realizing advanced capabilities, contributing to the broader understanding of scaling laws in neural networks. Note, in (B), the top bar is zero since this model is used as the reference to compute model improvement. It is kept in the visualization for consistency with the earlier plots (where some variants yielded performance degradation, that is, negative values).

- Fig. 12 | Comparative performance analysis of SmolLM-1.7B models across benchmarks. A Accuracy results for various SmolLM-1.7B model variants on the Spider Silk, Bio-inspired/Biological Materials, and Overall Accuracy benchmarks. The HuggingFaceTB/SmolLM-1.7B-Instruct model serves as the baseline,albeittrainingisdonesolelyontheBasemodel(HuggingFaceTB/SmolLM1.7B). While applying Continued Pre-Training (CPT) and Supervised FineTuning (SFT) strategies improves performance, the addition of Direct Preference Optimization (DPO) yields further accuracy gains. However, unlike in the much larger Llama or Mistral models, here, Spherical Linear Interpolation (SLERP) merging does not yield the best performance overall. This is more clearly shown in


- (B), where we plot the relative improvement over the baseline model (HuggingFaceTB/SmolLM-1.7B-Instruct) across the benchmarks. Notably SLERP


The results reveal that the deviation in performance between models merged using SLERP and their best-performing original counterparts, whereby the deviation is calculated as the difference between the best original model’s performance and the SLERP model’s performance. Hence, negative deviations, where SLERP underperforms relative to the best original model, are marked in red. Positive deviations, indicating better performanceoftheSLERPmodel,areshowninshadesofblue,withdarkerblue representing greater improvements.

Interactive examples for open-ended cross-material reasoning and material design tasks

In our next experiment, we conduct interactive conversations with a set of the models, using consistent system prompts and identical user input. We aim to test multi-turn capabilities of the models, assess responsiveness to system prompts and instructions, and the capability to produce structured output(JSON).Wewillfurtherassessthequalityofsynthesisofeachmodel, along a set of criteria that include depth of reasoning, creativity, clarity, and whether or not quantitative predictions are featured. Each of the conversations unfolds as follows:

As shown in Fig. 14, the model lamm-mit/Llama3.1-8b-Instruct-CPTSFT-DPO provides a well-organized and detailed discussion, drawing clear parallels between the structure and function of collagen and leaves. The proposed material design is robust, incorporating key components like a collagen-based matrix, vascular-like channels, and mesophyll-like cells. The response is notable for its comprehensive breakdown of each component’s role, leading to a thorough and scientiﬁcally grounded design. The JSON summaryisprecise,reﬂectingthestructureoftheproposeddesigneffectively.

- Figure 15 shows results for the lamm-mit/Llama3.1-8bInstruct-CPT-SFT-ORPO-SLERP-Var_G model. This model delivers a more concise but also insightful analysis of collagen and leaves. The material design focuses on integrating collagen ﬁbrils with cellulose microﬁbrils and chloroplast-inspired nanoparticles. This resembles an inventive approach to enhancing the material’s properties. This model excels in identifying the potential applications of the designed material, showcasingabroadervisionforitsuse.TheJSONrepresentationisclearand well-structured, effectively summarizing the design features.
- Figure 16 captures results of the lamm-mit/mistral-7B-v0.3Base-CPT-SFT-DPO model. The responses are found to be comprehen-


Figures 14–18 present the results of conversations of a human user with a selection of ﬁve models (best-performingmodels, and DPO trained models).

All ﬁve models demonstrate a strong ability to connect seemingly unrelated concepts, such as collagen and leaves, and to propose innovative materials designs. The output features rich Markup formatting (note, the raw source is shown here). The models show a consistent understanding of the biological and materials science concepts involved, suggesting that their ﬁne-tuning on domain-speciﬁc content has been effective. The differences in the responses mainly pertain to the depthof explanation, the creativity of the proposed designs, and the clarity of the output in both natural language and structured formats like JSON.

sive, with a strong focus on the mechanical properties of collagen and leaves. The proposed material design is detailed, incorporating collagen ﬁbrils, cellulose nanoﬁbers, silk ﬁbroin, and a nanocellulose-based matrix. This model particularlystandsoutforitsemphasisontheintegrationofthesecomponents to enhance the material’s toughness and durability. The JSON summary is thorough,capturingthecomplexityofthedesignanditspotentialapplications.

Next, Fig. 17 shows results for the lamm-mit/mistral-7Bv0.3-Base-CPT-SFT-SLERP model. This result illustrates a more straightforwardandlessdetailedanalysiscomparedtothe others.Whilethe connection between collagen and leaves is adequately explained, the material design is simpler, focusing on collagen ﬁbers, cellulose nanoﬁbers, chlorophyll, and pectin. This response is notable for its clarity and

![image 91](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile91.png)

- Fig. 13 | Performance deviation of Spherical Linear Interpolation (SLERP) merged models compared to the best original model. The plot illustrates the deviation in performance between models merged using SLERP and their bestperforming originalcounterparts(eitherwithoutSLERPorwith instructiontuning). The deviation is calculated as the difference between the best original model’s


performance and the SLERP model’s performance. Negative deviations, where SLERP underperforms relative to the best original model, are highlighted in red. Positive deviations,indicating better performance of the SLERP model, are shown in shades of blue, with darker blue representing greater improvements. Models are ordered from most signiﬁcant improvement to most signiﬁcant underperformance.

simplicity, making it accessible but perhaps lacking the depth seen in other models. The JSON summary is basic but effective in conveying the key elements of the design.

Finally,Fig.18showcasestheresultsofthesmallestmodelinthisstudy, lamm-mit/SmolLM-Base-1.7B-CPT-SFT-DPO. The model offers an inventive, creative, and highly detailed response, integrating a broad range of components such as collagen ﬁbrils, nanocrystalline cellulose, and an alginate adhesive, resulting in a material creatively referred to as “LeafyCoraline (LC) Composite”. This model excels in proposing a novel composite material with self-healing and shape-memory properties, reﬂecting a relatively high level of creativity and technical understanding. The JSON summary is comprehensive, capturing the innovative aspects of the design and its potential applications effectively. In spite of its size, this model provides excellent responses.

A summary of key observations is shown in Table 2.We can see that each model demonstrates strengths in different areas, from detailed explanations and innovative designs to clear and concise JSON summaries. The variations in depth, creativity, and technical detail among the models highlight the diversity of approaches and the potential for each to be suited to different types of tasks or applications. Overall, these models provide a strong foundation for further exploration and development in the ﬁeld of bio-inspired materials design. A detailed

breakdown of the analysis, generated using GPT-4o by analyzing the raw text of the conversations, is shown in Table 3, showing the results of an analysis conducted by sharing the raw text with GPT-4o and prompting the model to identify criteria and assess the different versions. We emphasize that GPT-4o is used as a supporting evaluator, not the deﬁnitive authority. LLM-based evaluation minimizes subjectivity and ensures reproducibility across tasks and models compared with human assessment. The potential of LLMs as evaluators has been explored in refs. 37,38 and evaluated in refs. 39–41, and GPT-4o is supported by studies beyond OpenAI’s GPT-report42.

Agentic use in image generation: applications in cross-domain knowledge integration for materials and urban design

Weshowseveralexamplestohighlightthecapabilitiesandpotentialofﬁnetuned LLMs, showcasing a particular application in materials design. The overallgoalistoexplorehowtheLLMsdevelopedherecanbeusedtoreason over complex materials principles and use the insights developed through multi-steppromptingtocreateapromptforimagegeneration.Wenotethat our ﬁne-tuned SmolLM based model performs extremely well for this task and yields quite creative prompts that integrate various ideas and concepts (underscoringitspotentialasacreativeagent),andthevisualrepresentation of conceptual designs guided by the prompts are generated via a custom

- Fig. 14 | Conversation generated by the model. lamm-mit/Llama3.1-8b-Instruct-CPT-SFT-DPO.


version of a FLUX.1 [dev] model43 ﬁne-tuned using a image dataset of leaf microstructures.ThepromptgenerationdemonstratestheLLM’scapability to conceptualize new materials-inspired design principles, which have the potential to be synthesized into physical structures. Speciﬁcally, the innovative designs are guided by the decomposed principles generated through prompt generation,whicharedirectlyrelevantto materialsscience.Besides, LLM-generated prompts, new design possibilities can be explored that may not have beenintuitive through traditional design processes. This approach bridges the gap between conceptual design and practical material development, and shows how AI can assist in design informatics by accelerating concept exploration and identifying viable design features.

While slight variations of prompting are used to yield different examples (each result presented here includes a detailed presentation of all features), the general goal is to think about design principles that we can extract from combining different biological materials. For instance, we ask the model to think about ways to combine design elements from spider silk and collagen to make a strong, lightweight but tough material, and to also incorporate design cues from leaf microstructures. The approach can be used to focus directly on material microstructures but can also be used to yield cross-domain results, such as architectural ideas or city design. We have provided several design examples that span a range of applications, from structural to urban design, to illustrate the versatility and potential of

bio-inspired design principles. The examples showcase how models trained on biomimetic materials can conceptualize structural motifs commonly observed in hierarchical composites and biomaterial-inspired structures. Furthermore, by presenting visual representations of bio-inspired designs, we demonstrate the capability of the LLM to bridge conceptual design with potential real-world synthesis in the ﬁeld of materials science.

In our ﬁrst example, we prompt the lamm-mit/SmolLM-Base1.7B-CPT-SFT-DPO model as follows (Fig. 19 shows the entire conversation):

which is designed to resemble ﬂoating leaves and create a dynamic urban landscape.Thedesignshowsresiliencetoclimatechange,offering ﬂexibility in adapting to changes in water levels.

Asillustratedintheseexamples,bio-inspireddesignsinarchitecturego beyond mere esthetics by incorporating natural elements into urban facilities, often enhancing functionality. Speciﬁcally, as shown in Fig. 20, these designshavethepotentialtoimprovesustainabilityandenergyefﬁciencyby optimizing material usage and structural topology compared to conventionaldesigns.Forinstance,thedesignsinrowthreereﬂectdesignsimplicity

A collection of images produced in this way is shown in Fig. 20. The resulting images resemble a visionary architectural concept where biomorphic structures seamlessly blend with nature, creating a futuristic and sustainable environment. The designs are inspired by natural forms such as honeycombs, coral, and cellular structures, characterized by ﬂuid, curving lines and intricate lattice-like frameworks that evoke the organic world. These structures are integrated with greenery, emphasizing harmony with the environment and suggesting the use of innovative, eco-friendly materials. The open, ﬂowing spaces with large archways and natural light emphasize a connection with the outdoors, creating a sense of tranquility and well-being. As can be seen in some of the images, human ﬁgures within these spaces highlight the livability and community-centric design, suggesting a vision where technology and nature coexist harmoniously. The images present a forward-looking approach to architecture, where sustainability, esthetics, and advanced techniques converge to create a new paradigm for living and public spaces. A close inspection of the resulting designs further suggests a clear emergence of the leaf microstructure patterns, a result of the prompt and the ﬁne-tuned ability of the generative model to incorporate this particular design idea.

These design ideas have the potential to be implemented, with speciﬁc functionality emphasized. Real-life examples of bio-inspired architectural designs include “The Hive”, a building on the NUT campus designed by Heatherwick Studio. Its honeycomb structure mirrors the cellular organization of hives, providing a modiﬁed modular hexagonal form that improves structural efﬁciency, particularly by optimizing airﬂow and ventilationsystems.Anothercompellingexampleis“LittleIsland”inNewYork,

and potential material saving, incorporating non-uniform cellular structures tailored for different space usages. The structural design also satisﬁes the load path analysis, with larger column sizes at lower ﬂoors compared to the top ones, which also shows the load-bearing capacity enhancement. Moreover, energy efﬁciency can be improved by optimizing heating and cooling systems, as seen in designs that mimic leaf veins, such as the ﬁrst design in row one. The second design in row ﬁve demonstrates a bioinspiredroofdesign,withbeamthicknessinspiredbyleafveinstomaximize lighting and energy efﬁciency. Additionally, these designs enhance the user experience by integrating natural elements into urban facilities, such as bridges and pathways within the designs. However, to actualize these designs in real-life applications, further research is needed, which includes studying wind effects and façade analysis considering the integration of extended plants and ensuring the loading and structural integrity, as well as selecting materials that are compatible with greenery.

Furthermore, bio-inspired structures featuring cellular patterns have the potential to be furtherenhanced withtopology optimization for various purposes, such as optimizing material usage while maintaining structural integrity and architectural features. We note that these bio-inspired designs reveal innovative design approaches for environmental integration and sustainability improvements, offering a promising start for exploring the vast design space, although more research is needed to fully validate the application in the real world.

In our second example, we prompt the lamm-mit/mistral-7Bv0.3-Base-CPT-SFT-DPO model as follows (Fig. 21 shows the entire conversation):

A collection of images produced in this way is shown in Fig. 22. The images showcase close-up views of a novel form of a biological material, highlighting their intricate vein patterns and microstructures. The leaves exhibita varietyofgeometricveinarrangements,rangingfrompolygonalto radialpatterns,allsharplycontrastedagainstthegreenleafsurfacesbybright yellow to gold veins. The diversity in leaf shapes and vein structures offers a variety of structural options, including a prominent feature of spider-weblike motifs. Several of the leaf patterns in the image resemble spider webs or

urban systems, for instance, how to interconnect individual structures, ensuring seamless integration with other facilities and alignment with an overall urban planning strategy.

The integration of nature into architecture has roots in movements such as organic architecture, as advocated by Frank Lloyd Wright45, where the harmony between human habitation and the natural world is paramount. The designs proposed here, however, push this concept further by embedding extensive greenery directly into the

spider-web-like structures. The veins in these particular leaves form radial patterns that converge toward a central point, much like the structure of a 2D orb spider web. This similarity is especially pronounced in some of the leaves where the vein network is more symmetrical and evenly spaced, creating a web-like appearance. These spider-web-like patterns, some of which resemble projections of various 3D webs such as cobwebs and sheet webs, add an interesting visual for studies related to natural design and biomimicry. A close inspection of the resulting images shows that textures and depth are captured in ﬁne detail. We ﬁnd that the soft yet focused lighting accentuates these patterns.

Figure23showsafewadditionalsampleimagesspeciﬁcallyprompting the model to develop urban design ideas based on a set of biological materials, including spider silk, collagen, and leaves, developed by lammmit/SmolLM-Base-1.7B-CPT-SFT-DPO. The images presented illustrate a conceptual approach to urban design that synthesizes advanced architectural techniques with principles of ecological integration and sustainability. The structures exhibit biomimetic design, characterized by their spiraling, organic forms that mimic natural patterns, possibly inﬂuenced by leaf microstructures. This design approach aligns with the principles of biophilic architecture44, which aims to reconnect urban environments with the natural world by incorporating natural elements into the built environment.

Several similar architectural designs have been realized, validating the potential for these generated concepts. Examples include Azabudai Hills, a district in Tokyo featuring curving planted rooftops; CapitaSpring, a skyscraperinSingaporewithorthogonalstripsofplantsembeddedinitsfaçade; and the Vertical Forest, designed by Stefano Boeri Architetti, which integrates residential buildings with diverse greenery. However, there remains signiﬁcant potential to explore and expand these ideas within extended

architectural framework, creating vertical gardens and green terraces that are integral to the building’s structure rather than ancillary elements. Moreover, the buildings are interconnected through elevated walkways, which not only facilitate human movement but also promote ecological connectivity, potentially serving as corridors for urban wildlife and contributing to biodiversity. This interconnectedness suggests a systems-thinking approach to urban design, where the built environment is considered part of a larger ecological network rather than an isolated entity.

The design concepts represented in these images could perhaps be seen as a potential paradigm shift in urban planning, where we move beyond sustainability to focus on regenerative design. This approach aims to create urban environments that not only minimize ecological impact but actively restore and enhance the natural environment. Such a model could potentially represent a signiﬁcant advancement in urban ecology, proposing a future where cities operate as living systems, integrated with and supportive of their surrounding ecosystems. More work would be necessary to explore this, but this example illustrates a use case where the methods developed here can guide creative research and technology developments.

Discussion

This study addressed fundamental questions in the ﬁne-tuning of large language models (LLMs) for domain-speciﬁc knowledge, exploring how different optimization strategies and datasets inﬂuence model performance, and assessed effects of model size and capabilities. Our investigation focused on a host of techniques applied consistently across models/architectures and parameter numbers. These included Continued Pre-Training (CPT), Supervised Fine-Tuning (SFT), Direct

- Fig. 15 | Conversation generated by the model. lamm-mit/Llama3.1-8b-Instruct-CPTSFT-ORPO-SLERP-Var_G.


Preference Optimization (DPO), and Odds Ratio Preference Optimization (ORPO). The goal was to determine how these methods impact the specialization of LLMs, particularly in the context of engineering or science domains.

A key ﬁnding of our research is that model scale plays a crucial role in the efﬁcacy of ﬁne-tuning strategies. Larger models, such as those with 7B

and 8B parameters, not only exhibited substantial improvements in domain-speciﬁc tasks but also showed the emergence of novel capabilitiesan outcome not observed in smaller models like the 1.7B parameter SmolLM model. This observation, as shown in a comparative plot (Fig. 13) suggests a threshold effect, where the beneﬁts of advanced optimization techniques, including model merging through SLERP (Spherical Linear

- Fig. 16 | Conversation generated by the model. lamm-mit/mistral-7B-v0.3-Base-CPT-SFT-DPO.


Interpolation), become signiﬁcantly more pronounced as model size increases. There are notable differences between the Llama and Mistral family of models that deserve further investigation. However, such investigations are hamperedbythe lackof detailed insights into the datasets used for training (during pre-training and ﬁne-tuning) as well as a lack of details

on speciﬁc training approaches. A summary of the key insights, including the most effective approach, is shown in Table 4.

The comparison between the Llama-3.1-8b and Mistral-7Bv0.3modelshighlightedhowSLERP,whencombinedwithSFT,DPOand ORPO, can effectively unlock synergistic properties, leading to reﬁned

- Fig. 17 | Conversation generated by the model. lamm-mit/mistral-7B-v0.3-Base-CPT-SFT-SLERP.


performanceoutcomesthatclusterdistinctlyinouranalysis.However,these improvements were not mirrored in the smaller SmolLM-1.7B models, which showed a deterioration of performance under model merging, underscoring the importance of scale in realizing the full potential of ﬁnetuning techniques. Figure 24 shows an overview of the signiﬁcant performance gains achieved through ﬁne-tuning across different model families, emphasizing how larger models like Llama and Mistral beneﬁt more substantially from these advanced techniques in terms of the overall scale of performance reached.

As shown in Fig. 24A, ﬁne-tuning consistently enhances model performance, with Llama leading in absolute performance scores. However, Fig. 24B reveals an interesting trend: Despite SmolLM’s lower baseline whichislikelyduetotheinherentlimitationsofitssmallerparameterscount and reduced access to high-dimensional parameter spaces compared to larger models, its relative improvement from ﬁne-tuning is the most pronounced, illustrating how smaller models, while not reaching the peak performance of their larger counterparts, can still gain substantially from targeted optimization strategies. This differential improvement pattern underscores the critical role of model size in both the efﬁcacy and scope of ﬁne-tuning processes. Consequently, while the larger Llama and Mistral models are better equipped to leverage the full spectrum of ﬁne-tuning techniques like DPO and ORPO combined with SLERP, SmolLM demonstrates that even smaller-scale models can achieve meaningful performance boosts, albeit with limitations imposed by their smaller capacity.

Figure 25 shows performance over the number of pre-training tokens (note, 1 trillion for SmolLM, 8 trillion for Mistral, and 15 trillion were used

for Llama-3.1). While this is an approximate analysis as each model/ architecture has unique features, training strategies, and datasets associated with it, but an overall trend can be observed that more pre-training tends to yield better performance, but also diminishes relative improvements that can be achieved. This agrees with the general consensus that for transformer-based models,there seem to be diminishingreturns as training data and model size are increased, implying that as performance gets better, exponentially larger and better datasets and larger models must be used.

Theresultsreportedherecontributetotheongoingdiscourseonthe optimal strategies for ﬁne-tuning LLMs, particularly in specialized domainswherepreciseandsophisticated understanding is required.The results suggest that while CPT and SFT are foundational, the application of advanced optimization methods like DPO and ORPO, especially whencoupledwithmodelmergingtechniqueslikeSLERP,arecriticalfor achieving high-performance outcomes in larger models. The data shows that there is room to optimize performance for each model, and some basic understanding needs to be developed of how different base models perform and how they can best be improved. Overall, the use of CPT, SFT, and ORPO/DPO followed by model merging can be seen as a viable approach for strong domain performance. The use of CPT and the other steps tends to yield much better results than simpler approaches such as LoRA, albeit, at a much higher computational cost. For smaller models, model merging may not be advisable, albeit we would recommend experimentation for model architectures to explore this particular feature and also identify the threshold of model size in which emergent capabilities prominently appear.

- Fig. 18 | Conversation generated by the model. lamm-mit/SmolLM-Base-1.7B-CPT-SFT-DPO.


There are numerous other parameters and angles to be explored. First, the effect of prompting. We kept the prompting consistent across all experiments. However, each model or model family will likely respond differently to prompts, and it is possible that additional performance gains can be achieved via prompt engineering. We deliberately did not address

thisissuehereaswewantedtofocusonanoverall,consistentcomparison.In somepreliminaryassessments,wedidnoticethatfortheMistralmodels,the CPT-SFT-DPO series resulted in rather low benchmark performance, where a closer inspection suggested thatthis maybedue to limited ability to follow directions, and lengthy answers. Our benchmarks are consistent in

- Table 2 | Summary of model performance, strengths, weaknesses, and design strategies based on conversations related to collagen and leaves


Model Key strengths Weaknesses Observations

The model excels in providing a thorough and detailed analysis. The robust material design effectively integrates various components, showcasing strong scientiﬁc reasoning. However, the complexity of the design may limit its practicality in certain applications. The JSON summary is precise, but the depth of detail could be overwhelming in less technical contexts.

May be overly complex for some applications; focuses heavily on structural components, potentially missing opportunities for simpler solutions

lamm-mit/Llama3.1-8bInstruct-CPT-SFT-DPO

Detailed and comprehensive design; strong scientiﬁc grounding

This model offers a concise yet insightful analysis. Its focus on innovation is evident in the integration of chloroplast-inspired nanoparticles for energy harvesting, which is unique among the models. However, the lack of depth in the explanation of mechanical properties could be a drawback in more technical discussions. The JSON representation is clear and well-structured, reﬂecting the model’s focus on innovative applications.

Concise and inventive; broader application vision

Lacks depth in certain areas; the brevity may sacriﬁce some detail in the explanation of the material properties

lamm-mit/Llama3.1-8bInstruct-CPT-SFTORPO-SLERP-Var_G

The model provides a detailed and comprehensive approach, particularly in its focus on the mechanical properties of the proposed material. The integration of multiple materials, such as cellulose nanoﬁbers and silk ﬁbroin, is handled well, though the emphasis on mechanical properties may limit the exploration of other innovative aspects. The JSON summary effectively capturesthedesign’scomplexity,thoughitmaybeseen as overly technical for broader audiences.

Potentially too focused on mechanical properties, which might limit creativity in design

Comprehensive integration of components; strong mechanical focus

lamm-mit/mistral-7Bv0.3-Base-CPTSFT-DPO

lamm-mit/mistral-7Bv0.3-Base-CPTSFT-SLERP

Simple and straightforward; clear and accessible design

Lacks depth and innovation; may be seen as too simplistic compared to other models

This model provides a straightforward and accessible design, focusing on essential components like collagen ﬁbers and cellulose nanoﬁbers. While the simplicity makesitaccessible,italsolimitsthedepthandcreativity of the design. The JSON summary is basic but clear, making it suitable for less technical audiences but potentially insufﬁcient for more advanced applications.

lamm-mit/SmolLMBase-1.7B-CPTSFT-DPO

Highly creative and detailed; innovative features like selfhealing

Complexity might make it challenging to implement; could be seen as too speculative for practical use

The model stands out for its creativity and innovation, particularly in its inclusion of self-healing and shapememory features. These advanced characteristics make it suitable for high-end applications, though the complexity of the design may pose challenges in practical implementation. The JSON summary is comprehensive, effectively conveying the unique aspects of the design, but the speculative nature of some features may limit its immediate applicability.

Evaluation conducted using GPT-4o.

thattheytestnotonlydomainknowledgebutalsohowcloselymodelsfollow directives to answer in a certain way (single word, as done here). Further experiments with the Mistral CPT-SFT-DPO series could entail using a more diverse dataset during DPO, including additional instructionfollowing foci. These and other variations are left to future work.

Wepresentedvariousmaterials-speciﬁcapplicationsofthemodelsthat go beyond question-answer benchmarking, focusing on general reasoning capabilities to integrate complex, disparate biological materials concepts, step-by-step analysis, structured outputs, and others. Results of consistently prompted conversations with various models were shown in Figs. 14–18. These conversations of a human user with models provided important insightsintothedifferentstrengthsandweaknessesofthemodelsinrealistic use-cases.

Building on this, focusing on another real-world use case of our models, we prompted the LLMs to develop image generation prompts, showing a powerful use case of the LLMs in conjunction with a pipeline of models interacting via agentic modalities (see, e.g., Figs. 20, 22, and 23 ranging from futuristic architecture, bio-inspired material microstructures, to urban/cityscape design). The design examples underscore the transformative potential of bio-inspired design principles, demonstrating how modelstrainedonbiomimeticmaterialscaninformtheconceptualizationof structural motifs characteristic of hierarchical composites and biomaterialinspiredsystems.TheseinsightspavethewayforintegratingadvancedLLM

capabilities into materials science, bridging innovative design with practical synthesis. In addition, these studies could be further expanded by incorporating a feedback loop, where in a multi-agent framework, images generated can be analyzedby vision-LLMs (e.g., Cephalo46) and the insights fed back into the LLMs for improved reasoning and adjustments.

Future research could further go deeper into the mechanisms behind the observed emergent behaviors, exploring how they can be harnessed across different architectures and domains, perhaps using tools from statistical mechanics or thermodynamics that may offer a fundamental perspective of how multi-particle systems behave and how these behaviors can be modeled. Other work to focus on interpretable insights could help also, following recent work47. Additionally, understanding the limitations and potential of smaller models remains an important area of inquiry, particularly as we seek to ﬁne-tune LLMs for speciﬁc tasks without the extensive computational resources required for larger models. Other avenues include scale-up of the experiments to 70B or 405B models in the Llama series. Giventhelessonslearnedfromthepresentpaper,agoodstrategycouldbeto do CPT on the Instruct model and then merge with the original Instruct model using SLERP. On the other side, more research could be done with thesmallLLMs.OurresultbasedonSmolLMisinterestingastheyprovidea model with reasonable performance on a tiny scale; this model could, for instance, become an effective tool when combined with in-context learning such as retrieval-augmented generation (RAG)48.

We assign scores from 1 to 10 for each criterion, including (1) Depth of reasoning: how well the model explains concepts and connects ideas, (2) Creativity: the uniqueness and innovation in the material design. (3) Clarity: how clearly the model communicates its ideas. (4)

ModelDepth of reasoningCreativityClarityQuantitative predictionsTotal score (Max 40)Average score (Max 10)Normalized intelligence score

Table 3 | Summary of model performance with individual criterion scores, total intelligence score, average score, and normalized intelligence score

lamm-mit/SmolLM-Base-1.7B-CPT-SFT-DPO101099389.510.0

lamm-mit/Llama3.1-8b-Instruct-CPT-SFT-DPO9897338.258.7

lamm-mit/mistral-7B-v0.3-Base-CPT-SFT-DPO8787307.57.9

lamm-mit/mistral-7B-v0.3-Base-CPT-SFT-SLERP6675246.06.3

SLERP-Var_G 8986317.758.2

Quantitative predictions: whether the model includes numerical or quantitative aspects in its response. Evaluation conducted using.GPT-4o

lamm-mit/Llama3.1-8b-Instruct-CPT-SFT-ORPO-

This study sheds light on the nuanced role of model scale and ﬁnetuning strategies in the development of domain-speciﬁc LLMs. By advancing our understanding of these dynamics, we move closer to unlocking the full capabilities of AI in specialized ﬁelds. The high degree of complexity across parameters and variables leaves this to be a challenging ﬁeld of study that offers many opportunities for future research. More work could also be done in improving the datasets. We ﬁnd that using a larger dataset is not necessarily beneﬁcial for downstream performance. We also found similar results for the Mistral model, where we did not see a signiﬁcant decrease but an almost identical performance. Combined with other recent studies, this indicates that data quality is a major issue that can be addressed by further distillation, processing and perhaps ﬁltering data components for relevance. The use of DPO or ORPO is particularly intriguing as it offers avenues for improving scientiﬁc accuracy and aligning the model with particular styles of responses (e.g., reasoning in a systematic way, step-by-step). Dataset curation could target several of these aspects and more experiments could shed light on the effects of these on performance. In the same vein, theincorporationof visualcues(e.g., ﬁgures,plots, microstructures,etc.) as done in recent work46 can be another source for data.

Materials and methods

We provide details about the materials and methods used to conduct this study.

Dataset curation and processing

The datasetused fortrainingincludes scientiﬁc papers from broad domains of biological materials, mechanics/mechanical properties, and spider silk. Earlier work focused on around 1000 papers in training; here, the dataset consists of the original training set and an additional set of ~4300 papers in the realm of spider silk. All of the training was done with this integrated dataset unless mentioned otherwise. A few experiments were done where training also included an extended dataset of ~3800 more papers on biological materials, see details below.

The dataset used for training includes scientiﬁc papers from broad domains of biological materials, mechanics/mechanical properties, and spidersilk.Earlierworkfocusedonaround1000papersintraining;here,the dataset consists of the original training set and an additional set of ~4300 papers in the realm of spider silk. All of the training was done with this integrated dataset unless mentioned otherwise. A few experiments were done where training also included an extended dataset of ~3800 more papers on biological materials, see details in the following sections.

Additionally, the quantity and quality of the dataset are crucial factors in the model training process. The curation and processing procedures outlined below ensure that the datasets are domain-speciﬁc, high-quality, and relevant. Speciﬁcally, for CPT, data quality is especially critical. As showninFig.9,usinganextendeddatasetwithvariedformatsanddefective text led to a decline in model performance. To overcome these challenges andensuretheaccuracy,consistency,andefﬁciencyofspecializedLLMs,we implemented several key strategies: (1) Datasets were cleaned, structured, and formatted before training. (2) Model performance was rigorously evaluated using a tailored benchmark for the spider silk and bio-inspired materials domains, covering diverse question types and knowledge areas to ensure comprehensive validation. (3) A systematic training pipeline (as detailed in the “Results” section) was followed to maintain consistency at each stage. (4) Model merging was applied to integrate strengths from various training paths, enabling generalization and the emergence of new capabilities.

Firstly, we introduce a new dataset, the spider silk materials dataset, tailoredtostudiesonspidersilk.Astheﬁrststep,wecuratedasetofPDFﬁles using the method outlined in Fig. 26. The process involved four key steps:

- 1. Collecting 4520 papers from Web of Science,
- 2. Performing digital object identiﬁer (DOI) lookups for missing entries using the habanero.Crossref Python client,
- 3. Screening for duplicates and irrelevant entries, and


- Fig. 19 | Conversation generated by the model. lamm-mit/SmolLM-Base-1.7B-CPT-SFT-DPO, aimed to develop an image generation prompt. The interactions include several stages, such as ideation and principle identiﬁcation, the creation of the image generation prompt, and the solicitation of a short version of the prompt.


4. Downloading 4323 papers through publisher application programming interfaces (APIs), manual downloads, and library requests. A total of 4323 spider silk-related papers were downloaded in PDF format and used for training. 4520 papers were initially collected from the Web of Science search engine on April 17, 2024, using the keywords “spider silk”. The search was limited to English-language articles published between 1900-01-01 and 2024-04-17. For the collected papers that were missing Digital Object Identiﬁers (DOIs), we used the habanero.Crossref Python client to interact with the CrossRef API, conducting DOI lookups based on the article titles, publication years, authors, and journals, where available. After initial collection, the paper entries were screened before downloading. Ultimately, 4323 papers were successfully downloaded in PDF format, resulting in a 95.6% yield. The remaining papers were not downloaded due to duplication, irrelevant content, or unavailability. Among the 4323 papers, 1603 were downloaded using the APIs of three publishers (420 from Wiley, 450 from Springer Nature, and 733 from Elsevier), 2638 were manually downloaded, and 82 out of 98 interlibrary requests were provided by MIT Illiad. All collected paper details are summarized in

the corresponding supplementary information (‘SI_source_articles_1.csv’) for easier identiﬁcation.

Another developed dataset is the biological materials dataset. The original dataset developed from 1034 biological materials papers was described in earlier work14. Thcon on original biological materials dataset is summarized in the Supplementary Information ‘SI_source_articles_2.csv’. A secondary much larger dataset was also created, which we refer to as the ‘extended dataset’. This extended dataset consists of 3826 biological materials-related papers, captured from a larger scope of search terms including “biological materials mechanical structure” - a broader scope than the previous search terms “biological materials mechanical hierarchical structure”. From the results, only a portion of the entries were retrieved from API-supported publishers including 2159 articles from Elsevier, 749 articles from Wiley, and 998 articles from Springer Nature, rendering 3826 articles. These articles were also retrieved in plain text format through the publisher API or by processing PDFs using Python package PDF2TEXT,leading to generally more unpredictable and varied text and formats. The remaining articles can be retrieved through following the previously established procedure,

![image 92](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile92.png)

- Fig. 20 | Image generation results developed by lamm-mit/SmolLM-Base1.7B-CPT-SFT-DPO, leading to this prompt used for image generation (through FLUX.1 [dev]43). Generate a futuristic, eco-friendly architectural concept utilizing a biomimetic composite material that integrates the structural efﬁciency of spider silk with the adaptive porosity of plant tissues. Utilize the following key features: * Fibrous architecture inspired by spider silk, represented by sinuous lines and curved forms. * Interconnected, spherical nodes reminiscent of plant cell walls, emphasizing growth and adaptation. * Open cellular


structures echoing the permeable nature of plant leaves, suggesting dynamic exchanges and self-regulation capabilities. * Gradations of opacity and transparency inspired bythe varying densities found inplant tissues,highlighting functional differentiation and multi-functionality. The images illustrate an architectural vision that draws inspiration from biomorphic forms including leaf microstructures, integrating sustainable design principles with natural elements, creating open, ﬂowing spaces that emphasize harmony between advanced architectural techniques and the organic world.

ideallyallinPDFformat,butforthescope ofthisstudy,thelargerdataset provides us a brief look into the effects of training with a larger and more varied dataset. The detailed information on the extended dataset of biological materials is available in ‘SI_source_articles_3.csv’.

For all training unless mentioned otherwise, we used the integrated dataset, which is the combination of the original 1034 biological materials

papers and the 4323 spider silk papers. For select cases in the ‘extended dataset’, the combination of the 1034 biological materials papers, 4323 spider silk papers, and the 3826 extended biological materials papers, was used fortrainingtoexploretheeffectoflargerdatainvariedformats.Thisdataset included more papers, but with a variegated format and a great number of errors due to the use of less effective PDF-to-text translation methods.

- Fig. 21 | Conversation generated by the model. lamm-mit/mistral-7B-v0.3-Base-CPT-SFT-DPO, aimed to develop an image generation prompt. The interactions include several stages, such as ideation and principle identiﬁcation, the creation of the image generation prompt, and the solicitation of a short version of it.


Dataset processing and preparation

For the best-quality raw dataset used in CPT, we use Marker https://github. com/VikParuchuri/marker,atooltoconvertPDFsintomarkupformat.We found this work to work well overall with consistent quality.

Dataset distillation and preparation for supervised learning

The raw text from the scientiﬁc papers is processed using general-purpose LLMs(mostlyGPT-4oorGPT-4o-mini)indifferentwaystoyieldhigherquality data, including data suitable for supervised learning consisting of question-answer pairs. We used the following strategies and objectives:

- 1. Question-answer pairs: Based on chunks of text, we developed question-answer pairs
- 2. Quantitative material property extraction: We extract quantitative materialpropertiesfrompapers,yieldingalistoffactsandpropertiesof materials


- 3. Extraction of summaries: Based on chunks of text, we developed summaries of content for a well-reasoned, clean description of content
- 4. Organizing the research content in papers into structured JSON format, with the following key components:


- • Title: The title key contains the title of the article, summarizing the study’s primary focus.
- • Insights: The insights key includes an array of key ﬁndings or interpretations derived from the research. Each entry in this array provides a brief summary of signiﬁcant insights.
- • Facts: The facts key consists of an array of factual statements based on observations or results obtained during the study. These entries present concise, veriﬁable information.


![image 93](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile93.png)

- Fig. 22 | Image generation results developed by lamm-mit/mistral-7Bv0.3-Base-CPT-SFT-DPO, leading to this prompt used for generation (through FLUX.1 [dev] AI43). Generate an image of a golden spiderweb network intertwined with collagen veins, forming a


dynamic, leaf-inspired microstructure amidst a lush green background. The images show a novel design of leaf-like structures with prominent vein structures, some of which exhibit intricate spider-web-like patterns, all set on a green background.

- • Details: The details key offers a more detailed exploration of speciﬁc aspects of the research. This array includes information on methods, structural characteristics, and other technical elements relevant to the study.
- • Comparisons: The comparisons key comprises an array of comparativeanalysesmadewithintheresearch.Thesecomparisons may involve structural similarities with other proteins or evolutionary analogies.
- • Questions: The questions key lists the primary research questions that the study aimed to address. Each entry corresponds to a signiﬁcant inquiry within the research framework.


• Answers: The answers key provides corresponding answers to the research questions listed under the questions key. These entries summarizethestudy’sconclusionsorﬁndingsrelatedtoeachquestion.

This approach involves extracting research content from scientiﬁc papers,allowingforclearandconcisedataextractionfromtheentirecontext ofthescientiﬁcpaper.Theprocessbeginswiththedevelopmentofquestionanswer pairs to address speciﬁc research inquiries. Additionally, quantitative material properties are extracted to compile veriﬁable facts and key ﬁndings. Summaries of the content are generated to provide well-reasoned, clean descriptions of the research.

The JSON format includes key components such as the title of the paper,insights,factualstatements,detailedmethods,comparisons,research questions, and corresponding answers, creating a comprehensive and

organized representation of the study. As an example:

For use in DPO/ORPO,we additionally construct a rejected answerby instructing the LLM to develop a scientiﬁcally incorrect, wrong answer. Here is an example:

Benchmark development and prompting

In our benchmarking strategy, we evaluated the model’s ability to select the correct answer by employing a structured prompting approach. The pri-

Theentirescientiﬁcpaperisusedtoconstructthisstructureddata.Five distinct sets are prepared for each paper, resulting in around 21,000 for the spider silk dataset and 5000 for the bio-inspired materials dataset.

This structured approach ensures that the dataset encapsulates both high-level insights and detailed factual information, facilitating comprehensiveanalysisandeffectivetraining.DuringCPT,thishigh-qualitydatais usedtogetherwiththeraw text(seeTable 6foradetailedbreakdown;where unstructured text means that we simply concatenate question-answers, summaries,andothercontent).ForSFT,weonlyusequestion-answerpairs. For DPO/ORPO, triples of prompt, response, rejected response, are used. Details on the speciﬁc training sets used for each model and training stage are indicated for each model as shown in Table 6.

mary prompt function instructed the model as follows:

You respond with one word or letter. Select the correct answer to this question: {q}

followed by:

The correct answer is:

![image 94](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile94.png)

- Fig.23|Sampleimagesspeciﬁcallyprompting themodeltodevelopurbandesign ideas based on a set of biological materials, speciﬁcally spider silk, collagen and leaves, developed using lamm-mit/SmolLM-Base-1.7B-CPT-SFT-DPO. The images, generated through FLUX.1 [dev]43, illustrate conceptual urban designs integrating biomimetic architecture and ecological sustainability. The left image depicts spiraling vertical towers with embedded greenery, evoking natural patterns (generation prompt: Utilize the spiral geometry of a nautilus shell to construct a series of interconnected, curved towers that form the city's skyline. The towers' spiraling walls house lush greenery, generating a perpetual canopy of foliage that ﬁlters sunlight and provides shade. Atop each tower stands a sleek, aerodynamicdomehousingastate-of-the-artresearchfacility, promotingcollaborationamongscientistsandinnovatorsacross


disciplines). The center image showcases interconnected cylindrical structures through elevated walkways, enhancing both social and ecological connectivity (generation prompt: Imagine a cityscape where towering skyscrapers twist and curve along the dual axis grid, their rooftops adorned with lush greenery and shimmering solar panels. At the heart of each tower lies a vibrant, neon-lit hub - a Circular Economy Center housing cutting-edge research and innovation in sustainable technologies. Connected by elevated walkways and hoverbikes, this city fosters a thriving ecosystem of collaboration and progress). The right image presents a broader urban layout, where domed buildings and landscaped water features are seamlessly integrated, reﬂecting a holistic approach to urban planning that prioritizes regeneration and biodiversity. The prompt used for this case is much longer and included as Box 1.

This constrained the model’s response to one word or letter, ideal for multiple-choice or binary (True/False) questions. The benchmarking was conducted with a deterministic setup without sampling (that is, T = 0) to ensureconsistencyinresults.Theanswersweresummarizedusingacustom answer check that converted the model’s response to a single letter corresponding to the correct choice (e.g., A, B, C, as well as T, or F).

The benchmarks contain a diverse set of multiple-choice (MC) and true/false (TF) questions focused on biological material properties, applications, and production, categorized under topics like biology, materials science, gene studies, and methodologies. The questions assess understanding of both factual and conceptual information, with some involving numerical calculations or experimental techniques. Scenario-based questions explore, for instance, how spiders adapt their web designs to environmental factors, while logic-related and paraphrasing tasks evaluate reasoning skills. The content emphasizes biological material potential in advanced applications, such as biotechnology and materials engineering.

Furthermore, the focus on Q/A-style benchmarks provides a relatively holistic measure of a model’s utility in real-world scientiﬁc scenarios compared to standalone text-based tasks. Notably, additional text-analysis

functionalities are inherently integrated into the Q/A framework. For example,textclassiﬁcationis utilizedtodeterminetheintentandtypeofuser questions, aiding in contextual understanding; named entity recognition is employed to extract key entities from user input, ensuring that relevant information is highlighted for accurate responses; and relation extraction identiﬁes logical and contextual relationships between entities, enabling the model to establish connections critical for comprehensive answers.

However, it is important to emphasize the signiﬁcance of preserving downstream task performance even after ﬁne-tuning. Therefore, a simple experimentanditsresultsonthemodel’sperformanceintheentityextraction task were conducted. While LLMs are generally expected to perform well on these tasks, this experiment was designed to ensure that the ﬁne-tuning process does not degrade their ability to do so. Published abstracts were obtainedbysearchingforrecentliterature(from2024)usingthesearchterms “biological material mechanics." The ﬁne-tuned model was then tasked with extracting key items from the abstracts, including the biological material(s) studied, the material properties of interest in the study, and the experimental methodsemployed.Thefollowingpromptwasusedandtestedonlamm-mit/ Llama3.1-8b-Instruct-CPT-ORPO-SLERP model:

- Table 4 | Summary of ﬁne-tuning strategies and best base models used


Model family Base model FT strategy Llama (8B) Instruct CPT-SFT-ORPO-SLERP Mistral (7B) Base CPT-SFT-SLERP SmolLM (1.7B) Base CPT-SFT-DPO

For all cases, CPT-SFT is a critical step, but some model architectures show great improvements with additional DPO or ORPO steps. Model merging is effective primarily in larger models, whereas it has a detrimental effect in the smallest model considered (Fig. 13).

![image 95](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile95.png)

- Fig. 24 | Summary of performance and performance gains. A Comparison of performance scores between non-ﬁne-tuned and ﬁne-tuned models across three model families: Llama, Mistral, and SmolLM. Fine-tuned models consistently outperform their non-ﬁne-tuned counterparts, with the Llama model showing the highest performance overall. B Relative improvement in performance over the base

models for each model family. SmolLM exhibits the greatest relative improvement, followed by Mistral and Llama, indicating that the ﬁne-tuning process signiﬁcantly enhances performance, particularly for the SmolLM model. The color palette transitions from light blue (non-ﬁne-tuned) to dark blue (ﬁne-tuned), visually emphasizing the performance gains achieved through ﬁne-tuning.

![image 96](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile96.png)

- Fig. 25 | Performance over the number of pre-training tokens (1 trillion for SmolLM, 8 trillion for Mistral, and 15 trillion for Llama-3.1). This is an approximate analysis as each model/architecture has unique features to it, but an overall trend can be observed that more pre-training yields better performance, but also diminishes relative improvements that can be achieved.


Table 5 presents the results for ﬁve abstracts, conﬁrmed to not exist within the original datasets. For reference, the DOI and title of each article are includedin place of the abstracttext. Theresults demonstrate consistent performance across all abstracts, with the model accurately extracting relevant entities within the limitations of the provided text.

This experiment exempliﬁes named entity extraction, as the model effectively identiﬁed domain-speciﬁc entities such as biological materials, material properties, and experimental methods. Many of these entities are describedusinguncommonbinomialnomenclature,furtherdemonstrating the model’s ability to handle domain-speciﬁc language. Notably, this demonstratesthatthemodelperformswellondownstreamtaskslikenamed entity extraction, even though it was not explicitly trained for this purpose. This highlights the robustness of the ﬁne-tuned model and its potential utility for similar domain-speciﬁc applications.

Nonetheless, future research could explicitly explore additional benchmark tasks to provide a more granular understanding of model performance across diverse linguistic and scientiﬁc challenges, including more complex linguistic operations to further evaluate and enhance the model’s capabilities.

Benchmark development for model assessment

Two benchmark datasets were developed, one focused on silk materials ("Spider silk benchmark”, available at lamm-mit/spider-silk-benchmark) and the other one general biological and bio-inspired materials

- Table 5 | Results from abstract named entity extraction task


Article Title Extracted “Biological material(s)"

Extracted “Property(s) of Interest"

Extracted “Experimental Method(s)"

Mechanical and elemental characterization of ant mandibles: consequences for bite mechanics50

Young’s modulus, mechanical properties

Nanoindentation to test the mechanical properties of mandibles, energy-dispersive X-ray spectroscopy to characterize elemental composition, ﬁnite-element analysis (FEA) to investigate the effects of cuticular variation in Young’s modulus under bite loading

Mandibles of the ant species Formica cunicularia

Date palm ﬁber Tensile strength, tensile modulus, strain, tear resistance, mechanical hardness, compression behavior

Mixing process using a Brabender internal mixer, followed by rolling. Various reinforcement materials and processing conditions were employed to characterize and analyze the mechanical properties of the composites.

Investigating the mechanical performance and characteristics of nitrile butadiene rubber date palm ﬁber reinforced composites for sustainable bio-based materials51

Development of Rice Husk and Sawdust Mycelium-Based Bio-composites: Optimization of Mechanical, Physical and Thermal Properties52

Physical,mechanical,thermal, and ﬁre safety properties

Box-Behnken experimental response surface methodology design was used to optimize the effect of substrate type, water content, and incubation time on resultant properties.

Pleurotus ostreatus (fungi) as binder to rice husks and sawdust

Cholla cactus wood (Cylindropuntia imbricata): Hierarchical structure and micromechanical properties53

Cholla cactus wood Stiffness, hardness, toughness X-ray tomography, scanning electron microscopy (SEM), scanning probe microscopy (SPM), nanoindentation, ﬁnite-element simulations

Nanocrystal residual strains and density layers enhance failure resistance inthe cleithrumbone of evolutionary advanced pike ﬁsh54

Cleithrum bone of the northern pike (Esox lucius)

Failure resistance, strength, damage tolerance, Young’s modulus, yield stress, compressive residual strains

X-ray, electron, and optical imaging, mechanical characterization techniques

Box 1 | Image generation prompt based on a task given to lamm-mit/SmolLM-Base-1.7BCPT-SFT-DPO, to think about speciﬁc design principles you can extract from combining dragline silk and collagen ﬁbers to make a resilient, organic and living material and to incorporate design cues from leaf microstructures, to ultimately yield an image generation prompt for a futuristic city design

extracted from relevant articles in the ﬁeld. The benchmarks developed in this study each contain a question and answer, question types, knowledge categories, assessment areas, and referenced papers, if any, used for question development. New benchmarks were developed for spider silk to assess the new training corpus, and the original

("Bio-inspired/biologicalmaterialsbenchmark”,availableatlamm-mit/bioinspired-benchmark).

The general benchmark development process follows earlier work14 and included developing multiple-choice questions. The questions were developed by domain experts, based on knowledge

benchmark for bio-inspired materials was extended to include double the number of questions.

Firstly, we established a benchmark speciﬁcally for spider silk, comprising 159 question-answer pairs designed to evaluate model performance. The question types include both multiple choice and true or false, and can be divided into two sets, each designed for different purposes: (1) 105 basic questions primarily assess knowledge and understanding of spider silk, while (2) the remaining 54 advanced questions explore various scenarios involving logic, reasoning, and more. This spider silk-speciﬁc benchmark is designedto evaluate notonly knowledge recall but also the model’s capabilities in logic, reasoning, and creativity, ensuring a comprehensive assessment of the LLMs’ cognitive and reasoning abilities. The benchmark query set is documented as supplementary information, with each entry containing question and answer, question type, knowledge category, assessment area, and referenced paper, if any, used for question development. Box 2 shows a few sample questions.

The details of the spider silk benchmark are as follows:

1. Basic Query Set: We ﬁrst prepared a query set that focuses on the knowledge understanding of spider silk, consisting of 105 questionanswer pairs, which includes 50 multiple-choice questions and 55 true or false questions. These questions were further classiﬁed into

descriptive, conceptual, analytical, numerical, comparative, and experimental categories, covering knowledge in various research areas such as materials, biology, application, gene, production, and methodology.

2. Advanced Query Set: To further access different scenarios involving logic, reasoning, and creativity, 54 additional questions were designed. These were categorized by question types into 31 multiple-choice and 23 true or false questions. Additionally, this advanced query set was organized by task types, including (1) scenario-based questions (e.g., experiment designs under speciﬁed scenarios, spider behavior or the mechanicalperformanceofwebsandsilksunderspeciﬁedconditions), (2) advanced reasoning questions (e.g., reading comprehension, summarization/simpliﬁcation, paraphrasing, numerical calculation), and (3) logic-related questions (e.g., fallacy identiﬁcation, negation, semantic parsing, contradiction).

Then, we developed a benchmark speciﬁcally for biological materials. In earlier work, a 100 multiple-choice question benchmark was developed withchallengingquestionsfocusingon biologicalmaterialmechanics.Since biological materials capture a large span of species and materials, four categoriesweredevelopedforthisdomain,whicharesummarizedbelow.In thiswork,weexpandedthebenchmarkanddoubledthepreviousnumberof

- Box 2 | Sample questions from the spider silk benchmark


- Box 3 | Sample questions from the bio-inspired/biological materials benchmark


![image 97](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile97.png)

- Fig. 26 | Paper collection process, here exempliﬁed for the spider silk dataset. A total of 4323 spider silk-related papers were collected and downloaded in PDF format. The process involved four key steps: collecting 4520 papers from Web of Science, performing Digital Object Identiﬁer (DOI) lookups for missing entries


using the habanero.Crossref Python client, screening for duplicates and irrelevantentries,andﬁnally,downloadingthepapersthroughpublisherapplication programming interfaces (APIs), manual downloads, and library requests. The ﬁnal yield was 95.6%. Image adapted from ref. 56 with permission.

- Table 6 | Datasets used for training different stages of Llama (8 billion parameters), Mistral (7 billion parameters) and SmolLM (1.7 billion parameters) models


Stage Dataset Fraction used Llama 8B and Mistral 7B (Base/Instruct model based) CPT lamm-mit/bio-silk-mech-mix-80K 2.0

Raw text biological materials papers (lamm-mit/raw-text-bio-markera)

1.0

Raw text spider silk materials papers (lamm-mit/raw-text-silk-markera)

1.0

lamm-mit/bio-materials-text-60K 1.0 SFT lamm-mit/HuggingFaceH4-

1.0

ultrachat_200k

lamm-mit/bio-silk-mech-mix-q-a-35K 1.0

DPO/ORPO lamm-mit/orpo-dpo-mix-40k 1.0 lamm-mit/bio-inspired-DPO 1.0 lamm-mit/spider-silk-DPO 1.0

SmolLM-1.7B (only Base model based) CPT lamm-mit/bio-silk-mech-mix-80K 1.0

Raw text biological materials papers (lamm-mit/raw-text-bio-markera)

1.0

Raw text spider silk materials papers (lamm-mit/raw-text-silk-markera)

1.0

lamm-mit/bio-materials-text-60K 2.0 SFT HuggingFaceTB/Magpie-Pro-300K-

1.0

Filtered-H4

HuggingFaceTB/self-oss-instructsc2-H4

1.0

HuggingFaceTB/OpenHermes-2.5-H4 0.001

HuggingFaceTB/everydayconversations-llama3.1-2k

1.0

HuggingFaceTB/instruct-data-basicssmollm-H4

1.0

lamm-mit/bio-silk-mech-mix-q-a-35K 1.0

DPO/ORPO lamm-mit/orpo-dpo-mix-40k 1.0 lamm-mit/bio-inspired-DPO 1.0 lamm-mit/spider-silk-DPO 1.0

TheMistral-basedtrainingstrategyusesthesamedataset,withtheCPT phaseanddomain-speciﬁcSFT andORPO/DPOdataadded,as inthedevelopmentof theZephyrmodel55. TheSmolLMmixof data isdifferentaswefollowthedistributionanduseofdataasinthedevelopmentoftheSmolLM-Instructmodel(HuggingFaceTB/SmolLM-1.7B-Instruct);however,withourdomain-speciﬁcdataaddedduring the SFT phase. The DPO phase had not been used in the original SmolLM-Instruct model.

aFor the list of paper references in this dataset, see Supplementary Information.

questions, following the same categories as outlined above. Box 3 shows a few sample questions.

- 1. General Questions (80): Cover broad topics and general trends
- 2. SpeciﬁcQuestions(80):Focusonuniquebiologicalmaterialmechanics or article-speciﬁc phenomena
- 3. Numerical Questions (20): Ask for speciﬁc quantitative values documented in the literature
- 4. Non-Biological Questions (20): Probe the model to distinguish between synthetic and biological materials, a common weakness noticed in foundational LLMs


Training approach

- Table 6 summarizes the datasets used for each of the stages of training. While we use the same data to train the Llama and Mistral models, we alter the mix of SFT and DPO/ORPO training data to match the original SmolLM-Instruct model development, but with the domain-speciﬁc data added into it.


Training of the Llama and Mistral models was conducted on one 8xH100 node with 8 GPUs, whereas the SmolLM model was trained on a single GPU. All training was conducted using the Hugging Face alignment handbook (https://github.com/huggingface/alignmenthandbook), using TRL trainers (for SFT, DPO, and ORPO). Additional details pertaining to each of the training stages is provided below.

- 1. Continued pre-training (CPT) During CPT, we provide raw text to the model. A start token is added at the beginning of each chunk. We enhance training efﬁciency by using sample packing, where multiple short examples are packed into the same input sequence to match the total sequence length used. Training scripts that specify all parameters used are available at https:// github.com/lamm-mit/LLM-ﬁnetuning.
- 2. Supervised ﬁne-tuning We use the relevant chat template associated with each model to provide samples in question-answer format, where the user role is used for the question and the


assistant role for the answer. As in CPT, we use sample packing, whereby multiple short examples are packed together to match the total sequence length used. Training scripts that specify all parameters used are available at https://github.com/lamm-mit/ LLM-ﬁnetuning.

- 3. DPO training We employed Direct Preference Optimization (DPO) as a ﬁne-tuning strategy to enhance our language model’s ability to generate preferred responses based on human feedback. As introduced in ref. 24 DPO ﬁne-tuning uses a dataset with chosen and rejected samples. In each prompt, one response was labeled as “chosen” (the preferred option) and the other as “rejected” (the less preferred option). This preference data trains the model to distinguish and prioritize responses that align with desired outputs. The Hugging Face DPO trainer of the Transformer Reinforcement Learning library was utilized to ﬁne-tune the model by directly maximizing the log-likelihood of the DPO loss. This optimization process is speciﬁcally designed to enhance the model’s ability to replicate the preferences indicated by the data. The training was facilitated through the speciﬁc model chat template, which enabled interaction-based ﬁne-tuning by incorporating direct feedback into the model’s learning process. This method ensured that the model was trained not only on generating correct responses but also on aligning with human and scientiﬁc preferences in a conversational context. Training scripts that specify all parameters used are available at https://github.com/lamm-mit/LLM-ﬁnetuning.
- 4. Odds Ratio Preference Optimization (ORPO) training We employed Odds Ratio Preference Optimization (ORPO)25 as a preference alignment strategy to ﬁne-tune our model. ORPO streamlines the process of preference-aligned supervised ﬁnetuning (SFT) by directly optimizing the model using a log odds ratio term appended to the negative log-likelihood (NLL) loss, thus eliminating the need for an additional reference model or preference alignment phase (realizing a form of preferencealigned SFT). This approach reduces computational and memory overhead while maintaining strong preference adaptation. This simpliﬁes the process of aligning language models with human preferences, eliminating the need for complex reinforcement learning frameworks like RLHF (Reinforcement Learning from Human Feedback). Instead of ﬁtting a reward model and then optimizing it, DPO directly adjusts the model’s parameters by maximizing the log-likelihood of the preferred response relative to the dispreferred one. This approach results in a more stable, efﬁcient, and computationally lightweight method for aligning language models with human preferences, often outperforming traditional RL-based methods as shown in ref. 25. In our ORPO training, we used datasets formatted identical to that required for DPO training, containing three key components: prompt, chosen, and rejected. For each prompt, a pair of responses was provided, with one labeled as “chosen” (the preferred response) and the other as “rejected” (the less preferred response). This dataset structure allowed the ORPOTrainer to optimize the model by minimizing the NLL loss, with an additional penalty applied to the rejected responses and a strong adaptation signal applied to the chosen responses. The Hugging Face ORPO trainer of the Transformer Reinforcement Learning library was utilized leveraging the ORPO algorithm to ﬁne-tune the model without the need for a reference model. This setup enabled efﬁcient preference optimization by integrating the log odds ratio directly into the training process, allowing the model to learn from human preferences in a streamlined manner. The use of a chat template facilitated the interaction-based ﬁnetuning, ensuring that the model was optimized for generating


responses that align with the desired outputs in a conversational and scientiﬁcally accurate context. Training scripts that specify all parameters used are available at https://github.com/lammmit/LLM-ﬁnetuning.

5. End and padding token During SFT, ORPO and DPO phases, we set the pad token to be distinct from the EOS token to ensure that end tokens are not masked out during training.

Model merging

We use MergeKit29 to merge models. The primary method for model merging is Spherical Linear Interpolation (SLERP), which we found to perform best overall. Given two sets of model parameters θ1 and θ2, SLERP interpolates between them as follows. Both sets of parameters are ﬁrst normalized to lie on the unit hypersphere:

θ1 kθ1k

θ2 kθ2k

^θ1 ¼

; ^θ2 ¼

The cosine of the angle ω between the two parameter vectors is computed using the dot product:

cosðωÞ ¼ ^θ1 ^θ2

The interpolation between the two vectors on the unit hypersphere is then given by:

sinðð1 tÞωÞ sinðωÞ

sinðtωÞ sinðωÞ

^θ1 þ

^θ2

SLERPðtÞ ¼

wheret∈[0,1]istheinterpolationparameter.Whent = 0,SLERP(t)returns ^θ1, and when t = 1, it returns ^θ2.

Theﬁnalinterpolatedparametervectoristhenre-scaledtotheoriginal magnitude:θinterpolated = ∥θ1∥1−t∥θ2∥t × SLERP(t)SLERPallowsustomerge neural network weights in a way that respects the underlying geometry of the weight space. By interpolating along a spherical path, SLERP avoids the pitfallsoflinearinterpolation,suchaspassingthroughregionsofhighlossin theparameterspace,leadingtoasmootherandmoreeffectivemerge30.This method is beneﬁcial in scenarios like transfer learning, ensemble methods, or creating hybrid models that combine the strengths of different pretrained models.

The effectiveness of SLERP can be linked to principles observed in overparameterization and ensemble methods. Overparameterized neural networks tend to generalize well due to their high capacity, even when trained to near-zero error34. SLERP leverages this capacity by non-linearly combining parameters, enabling the emergence of new capabilities through complex interactions that linear interpolation might miss.

Additionally, SLERP shares similarities with ensemble methods, which beneﬁt from the diversity among models35. The interpolation process in SLERP acts as a continuous ensemble, where the nonlinear combination of model parameters across the spherical path can activate new features that neither model exhibited individually. This process is particularly effective when the models being merged have learned complementary features, allowing SLERP to synergistically enhance their strengths and produce novel functionalities.

The overall effectiveness of SLERP in discovering new capabilities and improving performance can be speculated to scale with the diversity between the models being merged and their overall parameter count49.

A sample merge script for SLERP merges, for MergeKit, is:

The chat template used for the Llama models is

The vocabulary size of the Llama family models is 128,000. The chat template used for the Mistral models is

The vocabulary size of the Mistral family models is 32,768.

The chat template used for the SmoLM models is

The vocabulary size of the SmoLM family models is 49,152.

- Table 7 | Deﬁnitions of parameters used in the clustering and dendrogram analysis


Parameter Deﬁnition Pmerged Performance of the merged model.

- P1 Performance of the ﬁrst parent model.
- P2 Performance of the second parent model.


Ei Expected score for the i-th merged model, deﬁned as the average of P1 and P2.

Ai Actual score for the i-th merged model, equal to Pmerged. μE Mean of the expected scores across all merged models. σE Standard deviation of the expected scores across all merged

models. μA Mean of the actual scores across all merged models. σA Standard deviation of the actual scores across all merged models. ZE

Standardized expected score for the i-th merged model. ZA

i

Standardized actual score for the i-th merged model.

i

Clustering analysis and dendrograms

In this analysis, we standardized the performance scores of the merged models to facilitate meaningful comparisons across different models. The performance of a merged model is denoted as Pmerged, while the performance of the two parent models is denoted as P1 and P2. The standardized scores were computed as follows.

The expected score Ei for the i-th merged model was calculated as the average of the performances of the two parent models:

P1 þ P2 2

Ei ¼

Let μE and σE represent the mean and standard deviation of the expected scores across all merged models, respectively. The standardized expected

score for the i-th merged model, denoted as ZE

, was then calculated using the formula:

i

P1þP2

Ei μE σE ¼

2 μE σE

ZE

¼

i

The actual score Ai for the i-th mergedmodel is deﬁned as itsobserved performance:

Ai ¼ Pmerged

Let μA and σA represent the mean and standard deviation of the actual scores across all merged models, respectively. The standardized actual score for the i-th merged model, denoted as ZA

, was calculated using the formula:

i

Pmerged μA σA

Ai μA σA ¼

ZA

¼

i

See Table 7 for a summary of key parameters and deﬁnitions.

Summary of best-performing model releases on Hugging Face

The models with the best performance, along with their corresponding Hugging Face hub IDs, are summarized in Table 8.

Multi-turn human-AI conversations

We deﬁne human input and system prompts consistently for all experiments. We use topk = 512, topp = 0.9, and repetition_penalty = 1.1. We set the maximum number of generated tokens to 1024 to allow for long, detailed outputs during multi-turn conversations.

Image synthesis

Imagesynthesisisconductedusinglamm-mit/leaf-FLUX.1-dev.Thismodelis aﬁne-tunedversionoftheblack-forest-labs/FLUX.1-devbasemodelusingleaf images with a keyword ‘<leaf microstructure>’, following the concept proposed in ref. 43. The training set can be found at lamm-mit/leaf-ﬂux-imagesand-captions. The model was trained for N=2000 steps using adamw8bit, at a learning rate of 0.0001, and LoRA adapters applied to all linear layers of rank r=16, with α= 16. The purpose of demonstrating the use of an image generation model utilizing biologically inspired cues is to steer solutions towards organic, abstract, biological forms. Image generation is typically conducted with 25 denoising steps and guidance scale =3.5. An alternative modelisavailableatlamm-mit/leaf-L-FLUX.1-dev,trainedforN=4000steps usingadamw8bit,atalearningrateof0.0001,andLoRAadaptersappliedto alllinearlayers of rankr=64, withα =64.Thelarger FLUX modelprovidesa stronger effect of inducing leaf microstructure patterns.

- Table 8 | Overview of best-performing models and associated hub ID on Hugging Face


Model Hugging Face Hub ID Notes lamm-mit/Llama3.1-8b-Instruct-CPT-ORPO-SLERP_Var_G lamm-mit/Llama3.1-8b-Instruct-CPT-SFT-ORPO-SLERP_Var_G-09022024 lamm-mit/Llama3.1-8b-Instruct-CPT-ORPO-SLERP lamm-mit/Llama3.1-8b-Instruct-CPT-SFT-ORPO-SLERP-09022024 lamm-mit/mistral-7B-v0.3-Base-CPT-SFT-SLERP lamm-mit/mistral-7B-v0.3-Base-CPT-SFT-SLERP-09022024 lamm-mit/mistral-7B-v0.3-Base-CPT-SFT-DPO lamm-mit/mistral-7B-v0.3-Base-CPT-SFT-DPO-09022024 lamm-mit/SmolLM-Base-1.7B-CPT-SFT-DPO lamm-mit/SmolLM-Base-1.7B-CPT-SFT-DPO-09022024

For conversations targeted for image synthesis, we use topk = 512, topp = 0.9, and repetition_penalty = 1.1. We set the maximum number of generated tokens to 1024 to allow for long, detailed outputs of the models.

Data availability

Training data is available as listed in Table 6. References and DOI numbers of the downloaded papers used to construct the dataset are attached as Supplementary Information (‘SI_source_articles_1.csv’, ‘SI_source_articles_2.csv’ and ‘SI_source_articles_3.csv’).

Code availability

Training scripts are available at https://github.com/lamm-mit/LLMﬁnetuning. Model weights can be found at https://huggingface.co/ lamm-mit.

Received: 5 September 2024; Accepted: 2 March 2025;

![image 98](Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling_images/imageFile98.png)

References

- 1. Vaswani, A. et al. Attention is all you need https://papers.nips.cc/ paper/7181-attention-is-all-you-need (2017).
- 2. Radford, A., Narasimhan, K., Salimans, T. & Sutskever, I. Improving language understanding by generative pre-training https:// gluebenchmark.com/leaderboard (2018).
- 3. Xue, L. et al. ByT5: towards a token-free future with pre-trained byteto-byte models. Trans. Assoc. Comput. Linguist. 10, 291–306 (2021).
- 4. Jiang, A. Q. et al. Mistral 7B. Preprint at http://arxiv.org/abs/2310. 06825 (2023).
- 5. Phi-2: The surprising power of small language models - Microsoft Research. https://www.microsoft.com/en-us/research/blog/phi-2the-surprising-power-of-small-language-models/.
- 6. Dubey, A. et al. The llama 3 herd of models. Preprint at https://arxiv. org/abs/2407.21783 (2024).
- 7. Buehler, M. J. MeLM, a generative pretrained language modeling framework that solves forward and inverse mechanics problems. J. Mech. Phys. Solids 181, 105454 (2023).
- 8. Singhal, K. et al. Large language models encode clinical knowledge. Nature 620, 172–180 (2023).
- 9. Qu, J. et al. Leveraging language representation for materials exploration and discovery. npj Comput. Mater. 10, Article 58 (2024).
- 10. Yu, S., Ran, N. & Liu, J. Large-language models: the game-changers for materials science research. AI Chem. Eng. 2, 100076 (2024).
- 11. Hu, Y. & Buehler, M. J. Deep language models for interpretative and predictive materials science. APL Mach. Learn. 1, 010901

- (2023).

12. Buehler, E. L. & Buehler, M. J. X-LoRA: mixture of low-rank adapter experts, a ﬂexible framework for large language models with applications in protein mechanics and design. APL Mach. Learn. 2

- (2024).


- 13. Buehler, M. J. MechGPT, a language-based strategy for mechanics and materials modeling that connects knowledge across scales, disciplines and modalities. Appl. Mech. Rev. 76, 021001 (2024).


- 14. Luu, R. K. & Buehler, M. J. BioinspiredLLM: conversational large language model for the mechanics of biological and bio-inspired materials. Adv. Sci. https://doi.org/10.1002/advs.202306724 (2023).
- 15. Cranford, S. W. & Buehler, M. J. Biomateriomics (Springer Netherlands, 2012).
- 16. Groen, N., Cranford, S., de Boer, J., Buehler, M. & Van Blitterswijk, C. Introducing Materiomics. (Cambridge University Press, 2011).
- 17. Lee, N. A., Shen, S. C. & Buehler, M. J. An automated biomateriomics platform for sustainable programmable materials discovery. Matter 5, 3597–3613 (2022).
- 18. Arevalo, S. E. & Buehler, M. J. Learning from nature by leveraging integrative biomateriomics modeling toward adaptive and functional materials. MRS Bull. 48, 1140–1153 (2023).
- 19. Smith, P. T., Wahl, C. B., Orbeck, J. K. & Mirkin, C. A. Megalibraries: supercharged acceleration of materials discovery. MRS Bull. 48, 1172–1183 (2023).
- 20. Buehler, M. J. Accelerating scientiﬁc discovery with generative knowledge extraction, graph-based representation, and multimodal intelligent graph reasoning. Mach. Learn. Sci. Technol. 5, 035083

(2024).

- 21. Hu, E. J. et al. LoRA: low-rank adaptation of large language models. ICLR 1, 3. Preprint at https://arxiv.org/abs/2106.09685v2 (2022).
- 22. Buehler, M. J. MechGPT, a language-based strategy for mechanics and materials modeling that connects knowledge across scales, disciplines and modalities. Appl. Mech. Rev. https://doi.org/10.1115/ 1.4063843 (2023).
- 23. Siriwardhana, S. et al. Domain adaptation of llama3-70b-instruct through continual pre-training and model merging: a comprehensive evaluation. Preprint at https://arxiv.org/abs/2406.14971 (2024).
- 24. Rafailov,R.et al.Direct preference optimization: yourlanguagemodel is secretly a reward model. Adv. Neural Inf. Process. Syst. 36, 53728–53741 (2023).
- 25. Hong, J., Lee, N. & Thorne, J. Orpo: monolithic preference optimization without reference model. Preprint at https://arxiv.org/ abs/2403.07691 (2024).
- 26. Christiano, P. et al. Deep reinforcement learning from human preferences. NIPS'17: Proceedings of the 31st International Conference on Neural Information Processing Systems, 4302–4310, Preprint at https://arxiv.org/abs/1706.03741 (2017).
- 27. Garipov, T., Izmailov, P., Podoprikhin, D., Vetrov, D. & Wilson, A. G. Loss surfaces, mode connectivity, and fast ensembling of DNNs. NIPS'18: Proceedings of the 32nd International Conference on Neural Information Processing Systems, Preprint at https://arxiv.org/abs/ 1802.10026 (2018).
- 28. Utans, J. Weight averaging for neural networks and local resampling schemes.In Proc. AAAI-96Workshopon IntegratingMultiple Learned Models (AAAI Press, 1996).
- 29. Goddard, C. et al. Arcee’s mergekit: a toolkit for merging large language models. Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track, Preprint at https://arxiv.org/abs/2403.13257 (2024).
- 30. Shoemake, K. Animating rotation with quaternion curves. ACM SIGGRAPH Comput. Graph. 19, 245–254 (1985).


- 31. Grassia, F. S. Practical parameterization of rotations using the exponential map. J. Graph. Tools 3, 29–48 (1998).
- 32. Hanson, A. J. Visualizing quaternions. IEEE Comput. Graph. Appl. 26, 6–13 (2006).
- 33. Eberly, D. H. Game Physics (Morgan Kaufmann, 2003).
- 34. Belkin,M., Hsu,D., Ma, S. &Mandal, S.Reconcilingmodernmachinelearning practice and the classical bias-variance trade-off. Proc. Natl Acad. Sci. USA 116, 15849–15854 (2019).
- 35. Hansen, L. K. & Salamon, P. Neural network ensembles. IEEE Trans. Pattern Anal. Mach. Intell. 12, 993–1001 (1990).
- 36. Blecher, L., Cucurull, G., Scialom, T., Stojnic, R. & Ai, M. Nougat: neural optical understanding for academic documents. Preprint at https://arxiv.org/abs/2308.13418v1 (2023).
- 37. Liang, P. et al. Holistic evaluation of language models. Preprint at https://arxiv.org/abs/2211.09110 (2022).
- 38. Srivastava, A. et al. Beyond the imitation game: quantifying and extrapolating the capabilities of language models. Trans. Mach. Learn. Res. https://openreview.net/forum?id=uyTL5Bvosj (2023).
- 39. Chiang, C.-H. & Lee, H.-y. Can large language models be an alternative to human evaluations? Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics, Preprint at https://arxiv.org/abs/2305.01937 (Association for Computational Linguistics, 2023).
- 40. Zhang, Y. et al. Llmeval: a preliminary study on how to evaluate large language models. In the proceedings of the AAAI Conference on Artiﬁcial Intelligence by the Association for the Advancement of Artiﬁcial Intelligence (AAAI). Vol. 38, 19615–19622 (2024).
- 41. Chern, S., Chern, E., Neubig, G. & Liu, P. Can large language models be trusted for evaluation? Scalable meta-evaluation of LLMs as evaluators via agent debate. Preprint at https://arxiv.org/abs/2401. 16788 (2024).
- 42. Achiam, J. et al. GPT-4 technical report. Preprint at https://arxiv.org/ abs/2303.08774 (2023).
- 43. Ruiz, N. et al. Dreambooth: ﬁne tuning text-to-image diffusion models for subject-driven generation. Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, Preprint at https://arxiv.org/abs/2208.12242 (2023).
- 44. Kellert, S. R., Heerwagen, J. H. & Mador, M. L. Biophilic Design: The Theory,Science,andPracticeofBringingBuildingstoLife(Wiley,2008).
- 45. Wright, F. L.The Natural House (Horizon Press, 1954).
- 46. Buehler, M. J. Cephalo: Multi-modal vision-language models for bioinspired materials analysis and design. Adv. Funct. Mater. 34, 2409531 (2024).
- 47. Olah, C. et al. Scaling monosemanticity. Transform. Circ. https:// transformer-circuits.pub/2024/scaling-monosemanticity/ (2024).
- 48. run-llama/llama_index: LlamaIndex (formerly GPT Index) is a data framework for your LLM applications. https://github.com/run-llama/ llama_index (2022).
- 49. Kaplan, J. et al. Scaling laws for neural language models. Preprint at https://arxiv.org/abs/2001.08361 (2020).
- 50. Klunk, C. L., Heethoff, M., Hammel, J. U., Gorb, S. N. & Krings, W. Mechanical and elemental characterization of ant mandibles: consequences for bite mechanics. Interface Focus 14, 20230056

(2024).

- 51. El-Shekeil, Y. A., AL-Oqla, F. M., Refaey, H. A., Bendoukha, S. & Barhoumi, N. Investigating the mechanical performance and characteristics of nitrile butadiene rubber date palm ﬁber reinforced composites for sustainable bio-based materials. J. Mater. Res. Technol. 29, 101–108 (2024).
- 52. Mbabali, H., Lubwama, M., Yiga, V. A., Were, E. & Kasedde, H. Development of rice husk and sawdust mycelium-based biocomposites: optimization of mechanical, physical and thermal properties. J. Inst. Eng. Ser. D 105, 97–117 (2024).


- 53. Morankar, S. et al. Cholla cactus wood (cylindropuntia imbricata): hierarchical structure and micromechanical properties. Acta Biomater. 174, 269–280 (2024).
- 54. Sauer, K. et al. Nanocrystal residual strains and density layers enhance failure resistance in the cleithrum bone of evolutionary advanced pike ﬁsh. Acta Biomater. 179, 164–179 (2024).
- 55. Tunstall, L. et al. Zephyr: Direct distillation of lm alignment. Preprint at https://arxiv.org/abs/2310.16944 (2023).
- 56. Lu, W., Kaplan, D. L. & Buehler, M. J. Generative modeling, design, and analysis of spider silk protein sequences for enhanced mechanical properties. Adv. Funct. Mater. https://doi.org/10.1002/ adfm.202311324 (2023).


Acknowledgements

This work was supported in part by Google, the MIT Generative AI Initiative, USDA (grant number 2021-69012-35978), with additional support from NIH. This material is partially based upon work supported by the National Science Foundation Graduate Research Fellowship under Grant number 2141064.

Author contributions

M.J.B.designedtheoverallresearch,developedalgorithms,andcodes,and conducted the training, assessments, and analysis. M.J.B. developed and executed the distillation strategies to generate structured and adversarial data.W.L.andR.L.curatedthescientiﬁcpapersforthecorpusofrawtraining data, downloaded the papers, and designed the benchmark questions. M.J.B. wrote the initial paper draft with input from W.L. and R.L., and all authors edited and ﬁnalized the manuscript.

Competing interests

The authors declare no competing interests.

Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41524-025-01564-y.

Correspondence and requests for materials should be addressed to Markus J. Buehler.

Reprints and permissions information is available at http://www.nature.com/reprints

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afﬁliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modiﬁed the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence,unlessindicatedotherwisein acredit lineto thematerial. If material isnotincludedinthearticle’sCreativeCommonslicenceandyourintended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/bync-nd/4.0/.

© The Author(s) 2025

Wei Lu 1,2, Rachel K. Luu1,3 & Markus J. Buehler 1,2,4

1Laboratory for Atomistic and Molecular Mechanics (LAMM), Massachusetts Institute of Technology, Cambridge, MA, USA. 2Department of Civil and Environmental

Engineering,MassachusettsInstituteofTechnology,Cambridge,MA,USA.3DepartmentofMaterialsScienceandEngineering,MassachusettsInstituteofTechnology, Cambridge, MA, USA. 4Center for Computational Science and Engineering, Schwarzman College of Computing, Massachusetts Institute of Technology, Cambridge, MA, USA. e-mail: mbuehler@mit.edu

