1234567890():,;

1234567890():,;

npj | digital medicine Article

Published in partnership with Seoul National University Bundang Hospital

https://doi.org/10.1038/s41746-025-01535-z

# Cross sectional pilot study on clinical review generation using large language models

![image 1](Luo et al._2025_Cross sectional pilot study on clinical review generation using large language models_images/imageFile1.png)

Check for updates

Zining Luo 1,2,3,4,5, Yang Qiao6,13, Xinyu Xu5,13, Xiangyu Li5,13, Mengyan Xiao5,13, Aijia Kang7,13, Dunrui Wang2,3,13, Yueshan Pang8,13, Xing Xie1,9,13, Sijun Xie1,9,13, Dachen Luo10,13, Xuefeng Ding11,13, Zhenglong Liu4,13, Ying Liu5,13, Aimin Hu12, Yixing Ren1,9,14 & Jiebin Xie 1,9,14

As thevolume of medicalliterature accelerates, necessitating efﬁcient toolsto synthesize evidence for clinical practice and research, the interest in leveraging large language models (LLMs) for generating clinical reviews has surged. However, there are signiﬁcant concerns regarding the reliability associated with integrating LLMs into the clinical review process. This study presents a systematic comparisonbetweenLLM-generatedandhuman-authoredclinicalreviews,revealingthatwhileAIcan quickly produce reviews, it often has fewer references, less comprehensive insights, and lower logical consistency while exhibiting lower authenticity and accuracy in their citations. Additionally, a higher proportion of its references are from lower-tier journals. Moreover, the study uncovers a concerning inefﬁciency in current detection systems for identifying AI-generated content, suggesting a need for more advanced checking systems and a stronger ethical framework to ensure academic transparency. Addressing these challenges is vital for the responsible integration of LLMs into clinical research.

The landscape of medical research is expanding at an unprecedented rate, characterizedbyadelugeofnewﬁndingsandclinicaltrialspublisheddaily1. Keepingabreastofthisever-expandingbodyofknowledgeposesadaunting task for healthcare professionals and researchers alike. In this context, the role of clinical reviews assumes paramount importance, as they synthesize evidence from a vast array of studies to inform clinical practice and guide future research directions2. However, the manual process of review generation is labor intensive and potentially unsustainable given the current pace of scientiﬁc discovery. To address this challenge, there is a growing interest in leveraging the capabilities of large language models (LLMs) to automate the clinical review process3.

These models, driven by machine learning and natural language processing, such as OpenAI’s ChatGPT-3.5, have sparked strong reactions upon their introduction4. These LLMs, capable of answering questions in naturallanguageandprovidinghigh-qualityresponses,havequicklygained market traction due to the unprecedented experiences they offer5. As LLMs are further explored, people have gradually realized and developed more innovative applications. In the ﬁeld of medical consultation today, from a patient’s perspective, LLMs can read medical records and view image reports to provide advice and diagnostic rationale comparable to that of professional doctors6. From a doctor’s perspective, LLMs can rapidly summarize medical information, swiftly organizing decades of a single

patient’s records into a PDF highlighting crucial information, signiﬁcantly reducing the workload for doctors7. From a hospital management perspective, researchers have demonstrated that LLMs can simulate the operation of an entire hospital on their own, thereby better enhancing hospital operational efﬁciency8.

LLMsholdtremendouspotentialforautomatingtheprocessofclinical reviews, as these models have demonstrated exceptional proﬁciency in understanding and generating text that is closely aligned with human writing9. The potential of LLMs to rapidly assimilate vast amounts of medical literature and produce structured, insightful reviews presents a promising avenue for managing the overwhelming inﬂux of new informationinthemedicalﬁeld10.However,thegrowingmomentumtointegrate LLMs into the clinical review process has been met with several controversies and concerns. First, the reliability of these generated clinical reviews represents a signiﬁcant concern. While these models are adept at processing and synthesizing vast amounts of data, they are not infallible11. ThequalityofanLLM-generatedreviewisheavilydependentonthequality anddiversityofthetrainingdataithasbeenexposedto12.Ifthetrainingdata are biased or incomplete, the resulting review may contain inaccuracies or overlook critical information, giving rise to quality degradation. Second, for academictaskslikeclinicalreviews,thereareveryhighdemandsforaccurate citation of references and in-depth elaboration to support one’s own

A full list of afﬁliations appears at the end of the paper. e-mail: yixingren@nsmc.edu.cn; xiejiebin84@126.com

viewpoints. However, current research has identiﬁed issues with false citations and fabricated references in the article generation process of LLMs13.

As the technology of LLMs continues to advance, specialized LLMbased review generation platforms have emerged to address these issues14. These platforms utilizetheir own literature databases to provide content for LLMs before output and employ web search15, semantic analysis16, and machine learning techniques to offer reliable reference materials to LLMs, thereby reducing hallucinations and serving academic purposes. They have gained signiﬁcant recognition for their exceptionally high citation accuracy andinsightfulcommentary14.However,Inthepast,althoughcertainaspects of the review generation process, such as search query construction17 and information extraction18, have been evaluated, direct evaluation of the generated clinical reviews generated by these platforms has not been undertaken due to the large workload, breadth of evaluation metrics, and multidirectional researcher collaboration. Meanwhile, ethical considerations in publishing also warrant attention19. There is a risk that these powerful tools could be exploited by those with less than noble intentions. For example, some individuals or groups may use LLMs for bulk paper publishing. This possibility was supported by the recent AI prompt publishing incident20. However, to date, research on whether traditional reassessment tests and the recent advent of AIGC (Artiﬁcial Intelligence Generated Content) tests are effective in detecting and intercepting these generated clinical reviews is lacking.

In this study, we aimed to systematically assess the gaps between clinical reviews generated by existing platforms and those written by humans and to test whether existing checking systems and AIGC tests are effective in intercepting the generated manuscripts. We hope thatthis study will serve as a valuable reference for medical researchers and policy makers.

Results

Baseline characteristics of the generated clinical reviews

A total of 2439 clinical reviews were generated, after manually excluding reviews with signiﬁcant discrepancies in the number of paragraphs or characters, as well as those with zero references, a total of 2169 articles were included in the analysis.

Covering the circulatory system (n = 365), digestive system (n = 309), endocrine system (n = 196), immune system (n = 323), nervous system (n = 256), reproductive system (n = 102), respiratory system (n = 271), urinary system (n = 97), and other comprehensive types (n = 250).

Overall overview

Regarding the consistency of expert evaluation in various subjective indicators, the Single Measures results range from 0.858 to 0.932, showing high consistency among experts (see details in Supplementary Table 6).

In terms of basic quality, AI-generated clinical reviews have signiﬁcantly fewer paragraphs, and references, and are less comprehensive, authentic,andaccuratecomparedtothosewrittenbyhumans.Althoughthe authenticity of references is slightly lacking, the overall difference from human-written reviews is not substantial. For various subjective indicators, AI’s performance is far inferior to that of humans. Regarding the distributionof references,theproportionof referencesfromthepast ﬁve yearsinAI articles is relatively high. Meanwhile, AI articles have a lower proportion of high-impactfactororCiteScorearticles.ThecitationrateofreferencesinAI shows no difference compared to that of humans. Lastly, in terms of risks associated with academic publishing, Ai demonstrates a relatively low plagiarism detection rate and a highly variable AIGC detection rate.

The analysis results of the three indicators that have statistical signiﬁcance (p < 0.001) are presented in Fig. 1 (see details in Supplementary Table 3).

Basic quality of the article

Compared to human-written clinical reviews, AI clinical reviews exhibit fewer paragraphs (AI: 13.000 [7.000, 83.000], Human: 36.000 [29.000, 48.000]), lower numbers of references (AI: 20.000 [8.000, 78.000], Human: 87.000 [71.000, 115.000]), lower comprehensiveness of references (%) (AI:

0.367 [0.055, 2.041], Human: 2.113 [0.723, 4.285]), and lower authenticity (AI: 100.000 [70.550, 100.000], Human: 100.000 [100.000, 100.000]) and accuracy of references (%) (AI: 100.000 [73.550, 100.000], Human: 100.000 [100.000, 100.000]) (see Fig. 1). Additionally, on subjective indicators, AI clinical reviews demonstrate lower language quality (AI: 80.000 [70.000, 82.000], Human: 100.000 [100.000, 100.000]), lower depth of reference evaluation (AI: 75.000 [65.000, 78.000], Human: 100.000 [100.000, 100.000]),lowerlogicalability(AI:78.000[70.000,80.000],Human:100.000 [100.000, 100.000]), lower innovative ability (AI: 70.000 [60.000, 73.000], Human: 100.000 [90.000, 100.000]), and lower overall quality (AI: 78.000 [70.000, 80.000], Human: 100.000 [99.000, 100.000]).

Distribution of references

Compared to human-written clinical reviews, the proportion of references from the past ﬁve years in AI reviews is relatively high (AI: 46.700 [37.800, 67.100], Human: 36.905 [25.000, 54.054]), Meanwhile, regarding the JCR zone, there is a signiﬁcant difference in the proportion of references in the Q1sectionofAIclinicalreviewsintheJCRpartition(%)(AI:34.300[25.600, 44.898], Human: 60.355 [47.959, 70.370]). Furthermore, in terms of impact factor, AI’s high-impact factor references have a lower proportion (%) (impact factor 0-3: AI: 28.571 [18.800, 37.100], Human: 7.368 [5.769, 13.776]; impact factor 3-5: AI: 16.100 [9.500, 23.333], Human: 15.278 [9.524, 22.321]; impact factor 5-10: AI: 14.286 [7.700, 20.800], Human: 15.686 [8.850, 22.500]; impact factor ≥10: AI: 12.300 [6.400, 18.750], Human: 30.233 [19.355, 45.833]). Similarly, AI’s high CiteScore references also exhibited a lower proportion (%) (CiteScore ≥10: AI: 33.100 [20.000, 46.800], Human: 52.778 [38.776, 64.045]).

Quality of references

Comparedtomanualclinicalreviews,thereisnosigniﬁcantdifferenceinthe cumulative citation of all references (p = 0.004) and the average number of citations per reference (p = 0.211).

Academic publishing risk

TheresultoftheplagiarismchecksisvisuallydisplayedinFig.2.Speciﬁcally, AIhasa low plagiarismdetectionrate (%)of 28.000[16.000,45.000]. Figure 3 illustrates the overview of the performance of eight AIGC detection platformsin AI-generated reviewsandhuman-written reviews. Speciﬁcally, human-writtenreviewsexhibitedalowerAIdetectionratecomparedtoAIgenerated reviews. However, the AI detection rate for AI-generated reviews showedasigniﬁcantrangeofﬂuctuation(MinimumAIGCDetectionRateMaximum AIGC Detection Rate: 8-100) (see details in Supplementary Table 7).

Subgroup analysis

Subgroup analyses were conducted within AI-generated reviews across several factors: different journals as sources for control articles, diverse clinical domains, distinct methods of generation, and different platforms/ models of generation (see details in Supplementary Table 4).

For different journals, in terms of the basic quality of articles, The Lancet demonstrates a higher character count (12,803.000 [4716.000, 67,414.000]) and number of paragraphs (12.000 [6.000, 83.000]), while NEJM shows better authenticity of references (100.000 [80.530, 100.000]) and BMJ exhibits higher reference accuracy (100.000 [82.120, 100.000]). TheoverallqualityofarticlesfromTheLancetisthehighest(78.000[70.000, 80.000]). Regarding the distribution of references, NEJM has a higher proportion of references from the past ﬁve years (56.000 [38.200, 73.400]) andagreaterproportionofreferencesinQ4journals(6.400[1.900,11.538]). There is no statistically signiﬁcant difference in the quality of references.

For different clinical domains, AI exhibits a certain bias. In terms of basic quality, the nervous system (70.000 [65.000, 75.000]), respiratory system (70.000 [65.000, 75.000]), and urinary system (70.000 [65.000, 75.000]) demonstrate a relatively high level of innovation in AI-generated reviews.ArticlesrelatedtothedigestivesystemgeneratedbyAIdemonstrate the higher authenticity (Authenticity (References) (%): 100.000 [93.460,

![image 2](Luo et al._2025_Cross sectional pilot study on clinical review generation using large language models_images/imageFile2.png)

Fig. 1 | The analysis results of the three indicators. The boxplot illustrates the data distribution: the box represents the interquartile range (IQR) from the ﬁrst quartile (Q1) to the third quartile (Q3), with the line inside indicating the median and a square symbol marking the mean. The whiskers extend up to 1.5 times the IQR, and anypointsbeyond thisrangearemarked asoutliers. Interms of objectivemetrics, AI

demonstrates lower paragraph count, number of references, comprehensiveness, authenticity,and accuracycompared tohumans.Onsubjectivemetrics,AIperforms worse than humans across all levels. However, there is no signiﬁcant difference between the two in terms of the cumulative and the average citation count of references, while the references exhibit different distribution patterns.

![image 3](Luo et al._2025_Cross sectional pilot study on clinical review generation using large language models_images/imageFile3.png)

- Fig. 2 | The result of plagiarism checks. AI demonstrates a low plagiarism checking rate.


100.000]). Additionally, the accuracy of references is highest in clinical reviews of both the digestive system and other comprehensive types (Accuracy (References) (%): Digestive System: 100.000 [95.000, 100.000], Other: 100.000 [95.000, 100.000]).

For different generation methods, compared with the objective method, the outline method signiﬁcantly increases the word count (64,691.000 [37,172.000, 82,797.000]), paragraph count (82.000 [25.000, 116.000]),andnumberofreferences(77.000[36.000,124.000]).Meanwhile, all subjective scores within the basic quality dimension improved. (overall quality: objective: 78.000 [50.000, 80.000], outline: 80.000 [72.000, 80.000]). Regarding the distribution of references, the use of the outline method has led to a decrease in the proportion of articles published in the past year (20.900 [9.600, 31.200]). The proportion of articles with an impact factor ≥10 has increased (12.300 [7.300, 18.100]), while the proportion of articles with a CiteScore ≥10 has decreased (31.600 [19.672, 45.300]).

For AI platforms and AI models, Overall, in terms of the Basic quality of the article, LLMs demonstrate higher numbers of characters (45,857.000 [5174.000,74,638.000]),paragraphs(19.000[9.000,99.000]),andreferences (23.000 [8.000, 99.000]), as well as outperforming generative platforms across all ﬁve subjective metrics. However, their performance is inferior to generativeplatformsintermsofauthenticity(95.000[47.800,100.000])and accuracy of references (95.000 [51.220, 100.000]). Regarding the distribution of references, LLMs have a higher proportion of references from the past ﬁve years (58.400 [40.700, 73.000]), but a lower proportion of Q1 references (32.900 [25.300, 41.300]) and references with an impact factor ≥10 (11.500 [6.500, 17.000]) compared to generative platforms. In terms of reference quality, references generated by LLMs exhibit a higher Average number of citations per reference and cumulative citations of all references. Speciﬁcally, for each platform, o1-mini has the highest word count in terms ofbasicarticlequality(72,985.000[5153.000,10,6627.000]),whileclaude-35-sonnethasthehighestnumberofparagraphs(147.000[17.000,182.000]).

![image 4](Luo et al._2025_Cross sectional pilot study on clinical review generation using large language models_images/imageFile4.png)

- Fig. 3 | The result of AIGC detection tests. The boxplot illustrates the data distribution: the box represents the IQR from the Q1 to the Q3, with the line inside indicating the median and a square symbol marking the mean. The whiskers extend up to 1.5 times the IQR, and any points beyond this range are marked as outliers. On the left side of the boxplot, a scatterplot displays the distribution of the data points. Among all the submitted articles, AI exhibited a high variability in detection rates and a high detection rate.


o1-previewhasthehighestnumberofreferences(39.000[16.000,252.000]), and claude-3.5-haiku demonstrates the lowest reference authenticity (%) (31.120 [16.890, 45.330]) and accuracy (%) (38.050 [21.340, 50.360]). o1preview achieves the highest overall quality score (80.000 [80.000, 82.000]). In terms of reference distribution, AskYourPdf-2 has the highest concentration of references from the past decade (%) (100.000 [85.714, 100.000]), while GPT-4o has the highest proportion of references from the past year (%) (31.900 [20.000, 40.400]). Template.net has the highest proportion of Q1 journal references (44.872 [32.258, 51.163]), AskYourPdf-1 has the highest proportion of references with an impact factor ≥10 (34.483 [20.000, 55.556]), and the highest proportion of references with a CiteScore ≥10 (57.143 [42.308, 70.000]). Regarding reference quality, AskYourPdf-1 has the highest cumulative citation count across all references (8255.000 [2021.000, 20,401.000]) and the highest average citation count (428.000 [208.000, 823.000]).

Discussion

To date, this study is the ﬁrst to systematically compare human-authored and AI-generated clinical reviews while also pioneering the publication risk assessment of AI-generated clinical reviews. On the one hand, the overall results indicate that, compared to human-written reviews, AI-generated clinical reviews exhibit signiﬁcant deﬁciencies in most basic article quality metrics,includingthenumberofparagraphs,thequantityofreferences,and the authenticity, comprehensiveness, and accuracy of the references. Additionally, they fall short in ﬁve major subjective criteria encompassing language quality, depth of reference evaluation, logical capability, Innovation degree, and overall quality. In addition, although clinical reviews generatedbyAIexhibitdifferentpatternsincitationdistribution,particularlyin theproportionofpublicationsinhigh-impactjournals,thereisnostatistical differencebetweenAIandhumanexpertsintermsoftheaveragenumberof citations per article and the cumulative citations of all references. This indicates that the quality of references cited by AI does not signiﬁcantly differ from that of humans. Lastly, in terms of publication risk assessment, existing publication detection systems face signiﬁcant challenges. The AIgenerated literature exhibits low plagiarism and high volatility AIGC detection rates, suggesting that current inspection systems may not effectively prevent their inﬁltration into human-written clinical reviews. On the

other hand, results from the subgroup analysis indicate that AI exhibits a noticeable bias. There is a signiﬁcant difference across various journals. Different journals exhibit signiﬁcant differences. The Lancet demonstrates better overall quality and metrics related to article structure, such as word count and number of paragraphs, while other selected journals show variations in the authenticity, accuracy, and distribution of references. At the same time, on speciﬁc topics, general topics achieve signiﬁcantly better authenticity and accuracy of references compared to topics focused on a particular human system. In the conﬁguration of the model, high-training models have not shown a weakening in the accuracy of references due to hallucination. Seamless-2, based on GPT-4.0, demonstrates better performance in terms of word count and has seen an improvement in the comprehensiveness of articles compared to Seamless-1. Its overall quality is consistent with Seamless-1, and there has been a marked enhancement in thelogicalityofsummaries.TheperformanceofplatformssolelyusingGPT generationisnoticeablyinferiortothecurrentadjustedgenerationplatform. Speciﬁcally, AskYourPdf-2 accesses the GPT store and uses the native GPT and APIs provided by AskYourPdf to respond. Although it saw some improvement in comprehensiveness, it lagged behind AskYourPdf-1 in the Depth of Reference Evaluation, Logical Capability, Innovation Degree, and Overall Quality.

The results of the research can be interpreted from the following perspectives. First, Hewitt and others have previously proposed the limitation of LLMs in producing longer texts. Speciﬁcally, the scarcity of long output examples from Supervised Fine-Tuning (SFT) somewhat affects the results’ length21. For instance,we can ﬁnd many short question-and-answer dialogs as sourcesfor model training in the comment sections of ubiquitous social media. However, while we can ﬁnd many papers and novels online as long dialog responses, they are not clearly deﬁned for use as long output example questions. Meanwhile, these potential long output contents are oftenprotectedbycopyright,preventingtheirarbitraryinclusionintraining datasets, making long output examples even scarcer22. Moreover, since today’s advanced models are often closed source and deployed on commercial servers, providers inevitably limit output length and complexity to minimize computational costs23. The direct consequence of reduced text length is a decrease in the number of paragraphs and references.

According to the platform’s introduction, in order to avoid hallucination problems in LLMs, the aforementioned review generation platforms do not directly ﬁne-tune the original LLMs for direct output. For example, Seamless attempts to use machine learning programs to match literature within the platform’s reserved literature database ﬁrst and then allow LLMs to perform the ﬁnal output based on these contents combined with user input. However, while this largely resolves past inconsistencies between LLMs’ outputs and cited references, it places higher demands on the quality of the company’s own reserved literature database. From a business perspective, these generation platforms typically prioritize purchasing rights from publishers with lower copyright fees, as their journals have lower visibility, and the purchase costs are not high. In contrast, acquiring copyrightsfromlargeracademicpublishersusuallyinvolvessigniﬁcantcosts,and despite their journals having higher impact factors or CiteScores, they may not be prioritized due to cost constraints and are thus not included in these reserved article databases. Therefore, a possible assumption about the output is that these generation platforms cite lower-impact and lowerquality articles more frequently than humans because such articles constitute a much larger proportion of their knowledge base.

In terms of AI-generated content detection rates, taking GPTZero, a widely known example we have access to, its founder Edward Tian explained that existing AI-generated content detection relies on two key indicators: “perplexity” and “burstiness.“24 Speciﬁcally, perplexity can be understood as predictability. When a detector can accurately predict the nextwordorsentenceinatext,thetext’sperplexityislower,makingitmore likely to be identiﬁed as AI-generated. Burstiness refers to the changes in sentence length and complexity. AI-generated sentences tend to have uniform length and structure, while human writing is more dynamic and freeform, which is why tutorials on “reducing AI detection” often mention

![image 5](Luo et al._2025_Cross sectional pilot study on clinical review generation using large language models_images/imageFile5.png)

- Fig. 4 | The comparison results of various AIGC detection platforms before and after using Merlin to reduce AIGC detection rates. The results indicate that after using this tool, the AIGC detection rates across all platforms decreased, with


reductions ranging from 21% to 82%. For most articles, the AIGC detection rate dropped below 50% (the threshold at which all platforms classify content as AIgenerated).

adding punctuation and changing long sentences to short ones. However, while these methods might be effective for integrated direct output LLMs, they may fall short for current academic generation platforms where multiple LLMs collaborate in multi-process handling. Not only is there signiﬁcant volatility in such detection results, but the emergence of AIGC detection products, similar to the earlier plagiarism detection rates, has also spurred the development of tools aimed at reducing AIGC detection rates. Although in our initial research, among the 8 AIGC detection platforms, SurferSEOachievedthebestperformance,withthehighestdetectionratefor AIGC reaching 100.000 [98.000, 100.000], on the platform we studied, Merlin offers both AIGC detection and AIGC detection reduction services, claiming to “bypass all AIGC detectors on the market.” We conducted a supplementary experiment where articles with an AIGC detection rate exceeding75%wereprocessedusingtheirtooltoreducetheAIGCdetection rate (see details in Supplementary Table 7). The results, shown in Fig. 4, indicate that after using this tool, the AIGC detection rates across all platforms decreased, with reductions ranging from 21% to 82%. For most articles,theAIGCdetectionratedroppedbelow50%(thethresholdatwhich all platforms classify content as AI-generated). This raises concerns about the reliability of current academic detection systems. Regarding plagiarism detection rates, past detection heavily relied on the similarity of sentence meaningandstructurewithinduplicationdatabases25.LLMshavetheability togeneratedifferentsentencestructuresbyvaryingprompts,evenunderthe sametopic.Thisﬂexibilitymakesitdifﬁcultfortraditionaldetectionsystems to identify LLM-generated content using conventional methods. Furthermore, in more complex generation environments, the collaboration of multiple LLMs and the integration of LLMs with other technologies further increases the difﬁculty of detection. These factors combined make traditional detection methods increasingly inadequate when dealing with modern AI-generated content.

A series of recent LLMs, whether open-source or closed-source, have undeniably shortened the character count, paragraph count, and reference count of generated summaries, bringing them closer to human-written literature while signiﬁcantly improving aspects such as language quality, depth of reference evaluation, logical capability, innovation degree, and overallquality.However,duetotheissueofhallucination,theauthenticityof references generated by these models ﬂuctuates greatly, with numerous mismatches between reference titles, authors, and publication years. Compared to these models, literature generated by platforms operating within standardized frameworks, while addressing the issue of false references, performs poorly in the ﬁve subjective metrics. Thus, future

development urgently requiresﬁnding an effective balancebetween the two approaches to maximize the beneﬁts of generated content. On the other hand,modelsdesignedforgeneralcommercialusers,suchasGPT-4o-mini, and small-scale open-source models targeted at small businesses, like Llama-3.1-8b, do not exhibit signiﬁcant differences in performance compared to their upgraded versions. Therefore, for tasks like clinical review generation, current users or small businesses do not need to invest more in deploying advanced models to achieve better results. However, it is important to note that specialized open-source models, such as PalmyraMed, which focuses on healthcare, and Galactica, which specializes in scientiﬁc research, are constrained by token length and the speciﬁc task types theytarget. As such, they are not suitable for completing this particular task and,atleastatthisstage,shouldnotbeconsideredasagoodchoiceforthese types of tasks.

The conﬁguration of prompts and parameters has a signiﬁcant impact on traditional AI tasks. In the preliminary consistency exploration prior to the study, different prompts had a substantial inﬂuence on the quality of reviewgeneration (see details in Supplementary Note 3). Providing detailed guidance on the approximate content of each paragraph in the review yieldedbetterresults.Regardingparameterconﬁguration,updatingthebase model to newer versions, such as transitioning from Seamless-1’s GPT-3.5 to Seamless-2’s GPT-4.0, delivered predictably better results. For model parameters, some exploration of temperature values was conducted. For proprietary models, multiple sets of temperature and top_p values were tested,rangingfrom0to1in0.2intervals,tooptimizegeneration.However, this did not resolve issues of suboptimal outputs or the inability to understandtaskintent.Forgeneral-purposemodels,simplepost-hocexperiments were conducted on both open-source and closed-source models (see details in SupplementaryNote5). The resultsgeneratedby the two typesofmodels under different temperature and top_p values did not show statistically signiﬁcant differences. Therefore, default conﬁgurations can be considered for experiments in this type of task.

This study aims to provide a reference model for the application of LLMs in clinical reviews across various subﬁelds in the future. However, given the highly diverse and complex nature of research directions in the medicalﬁeld, the methodologyof this studyisconstrainedby workloadand the breadth of expertize, and it does not encompass all medical ﬁelds or make targeted adjustments to evaluation metrics for speciﬁc research areas. This is a process that requires the joint efforts of international researchers from various ﬁelds. The application of the conclusions from this study to different domains must be supplemented and interpreted in light of their

![image 6](Luo et al._2025_Cross sectional pilot study on clinical review generation using large language models_images/imageFile6.png)

- Fig. 5 | Supplementary research directions for the speciﬁed application-oriented research in the future. The workﬂow diagram above illustrates how to conduct supplementary investigations in designated research areas, particularly those that rely on a limited number of authoritative references.


speciﬁc characteristics, particularly in areas that heavily rely on a small number of authoritative references. The methodology of this study is constrained by workload limitations, making it impossible to cover all medical domains. Additionally, analyzing and statistically accounting for instances where authoritative references are indirectly cited in generated literature presents certain challenges. When applying the conclusions of this study or using AI clinical reviews in one’s own research ﬁeld, in addition to referring to the conclusions already drawn in this study, It is recommended to incorporate the following measure to further evaluate LLM-generated reviews in speciﬁc research area (see details in Fig. 5): First, conduct bibliometric analyses of literature within the speciﬁc domain, such as using tools like CiteSpace to identify key publications at critical time points. Second, after the LLM generates a review, perform an overlap analysis between the cited references and key publications to ensure sufﬁcient citationofauthoritativesources.Third,toaddresstheissueofindirectcitationof authoritative references, manual screening can be introduced to ensure direct citation of key publications. Finally, compare the citation quality and overall quality of LLM-generated reviews with those of manually written reviews, thereby evaluating the practical application of LLM reviews in the domainandpromotingtheirimplementation.Throughthesemeasures,the applicabilityandreliabilityofLLMsingeneratingreviewswithinthespeciﬁc medical ﬁeld can be further enhanced, providing more effective reference methods for generating reviews in specialized subﬁelds.

The articles generated from the themes of the four journals exhibit signiﬁcant differences. Taking overall quality as an example, The Lancet demonstrates better overall article quality. Speciﬁcally, this higher quality is reﬂected in several subjective indicators, including language quality (80.000 [60.000, 82.000]), depth of reference evaluation (74.000 [60.000, 78.000]), logical coherence (78.000 [70.000, 81.000]), and degree of innovation (70.000 [60.000, 75.000]). Further analysis of these differences reveals that The Lancet tends to focus more on topics exploring disease mechanisms, futureoutlooks,orinnovationsinitsselectedthemes.Incomparison,JAMA

emphasizes clinical practice and diagnostic treatment in its extracted themes, BMJ focuses on summarizing the latest treatments, and NEJM emphasizesthelatestresearchanddetailsrelatedtodiseases.Afterremoving these speciﬁc themes for reanalysis (deleted themes include: “The future of cystic ﬁbrosis therapy: from disease mechanisms to novel,” “Dilated cardiomyopathy: etiology, mechanisms, and current and future approaches to treatment,”and“Innovationininfectionpreventionandcontrol—revisiting Pasteur’s vision”), the overall quality no longer showed statistically signiﬁcant differences (p = 0.105). This reﬂects biases in the platform and the ﬁne-tuning of proprietary models during the training process of LLMs, potentially due to the inclusion of more training data that discusses disease mechanisms, future outlooks, or innovation-related topics. This phenomenon is also evident in the differences in the distribution of references mentioned in the study and the subsequent variations observed across different clinical ﬁelds or human systems.

The outline method and the objective method exhibit certain differences. Since the outline method involvesmultiple rounds of generation, it is not difﬁcult to understand its increases in word count, number of paragraphs, and number of citations. From the perspective of subjective quality dimensions, articles generated using the outline method generally exhibit higher overall quality.Thismaybe because outlines help betterorganizethe structure of the article, making the content more logically clear and coherent, thereby performing better in aspects suchas language quality and the depth of citation evaluation. Under the outline method, topic coverage tendstobeaddressedatamoredetailedlevel.Forexample,whendiscussing oral cancer, the objective method presents a prompt in the form of introducing treatments for oral cancer, whereas the outline method would delve into more speciﬁc aspects, such as surgical treatments for oral cancer. This reﬂects the importance of more detailed prompts in the generation process. However, it is important to note that this approach may also lead to the observed bias in citations distribution due to insufﬁcient coverage in the trainingdata.Therefore,to someextent,theoutlinemethod,asatemporary

tool to address differences in word count compared to manually written articles, is not suitable for long-term use.

Despite the results, both these review generation platforms and the current detection systems have clear limitations, our research provides insights for researchers, AI startups, and publishers. Firstly, for medical researchers, AI tools offer a means of quickly grasping the content in their ﬁeld.OurstudysupportspreviousrecommendationsthatAItoolsserveasa reliable resource to facilitate research and learning. In the past, there were concerns about hallucinations in LLMs causing false citations, which was also found in previous studies using pure LLMs26. However, this issue has been resolved in several platforms we tested. For instance, AI-generated reviewscanprovideaccuratereferences,asdemonstratedbytheAIplatform Seamless AI, which boasts near 100% citation accuracy. Additionally, over the past year, the proportion of references in its clinical reviews has been signiﬁcantly higher than those generated by humans. Secondly, for AI startups, a key consideration is how to adapt their models to various clinical research ﬁelds. In our study, the references in AI clinical reviews have lower impact factors and CiteScores, although their average cumulative citation counts do not differ signiﬁcantly from those of reviews written by humans. However, foundational and signiﬁcant articles typically appear in wellknown journals. Therefore, startups need to consider whether to negotiate the purchase of speciﬁc high-quality top journal articles to balance the cost of journal subscriptions, rather than acquiring the entire publisher’s copyright usage, to alleviate ﬁnancial burdens while enhancing a higher quality literature repository. Meanwhile, our research found signiﬁcant differences in the models’ ability to review speciﬁc human systems and journal topics, which might be due to a lack of ﬁne-tuning or signiﬁcant biases in the datasets used for ﬁne-tuning. Startups could consider involving clinically diverse frontline physicians to participate in cross-disciplinary efforts, developing high-quality proprietary datasets for speciﬁc human system reviews for ﬁne-tuning27. Furthermore, AI companies need to address the problem of generating shorter articles, which can severely impact article qualityand overlook key references. Although using an outline approach to generate longer outputs partially mitigates this limitation, it is not an effective and enduring solution. Hence, the solutions proposed in existing studies to overcome character limitations in outputs warrant consideration and further exploration28–30. In the past, publishers attempted to detect or check for duplication in LLM articles in a manner similar to GPTZero. However, we must acknowledge that LLMs are advancing rapidly, altering sentence structures, and becoming more unpredictable in numerous ways. Sadasivan et al. assert that as language models become more complex and adept at mimicking human text, even the best detectors’ effectiveness will signiﬁcantlydiminish31.ThisisevidentfromOpenAI’sdecisiontowithdraw its own detector32; therefore, publisher should recognized that we cannot evaluate a paper in the same way we use to do.

Our research has several beneﬁts. First, collaboration across multiple interdisciplinary ﬁelds, such as computer science and medicine, enables us to comprehensively evaluate different clinical reviews in four major dimensions. In the past, manually gathering citation distributions and paragraph statistics for individual articles was laborious and timeconsuming due to the lack of ready-to-use batch extraction tools. Additionally, evaluating clinical reviews from different directions is also very challenging. Second, the multidimensional evaluation conducted incorporates subjective indicators as well as dimensions such as reference distribution, reference quality, and academic publishing risk, which were generally lacking in previous studies. Finally, the selection of top-quality articles from the top four most recognized medical journals ensures the robustness of the comparison results and the representativeness of the benchmark. However, despite these efforts, our research still has some limitations. On the one hand, we select representative internationally accessible review generation platforms within an appropriate workload, whichmaynotcoverregion-speciﬁcgenerationplatformsinadvertisements or future updated LLMs. Therefore, the interpretation of results should be approached with caution, meanwhile, due to the lack of a universally accepted standard for clinical reviews of average quality, our study did not

explorethegapbetweenAI-generatedclinicalreviewsandhuman-authored ones of average quality. On the other hand, since experts with different researchbackgroundsinthesameﬁeldmaycomefrommanycountries,the participation of Chinese and British experts might not fully cover all directions, especially topics in less prominent areas. Therefore, caution is needed when applying the results of this study to less prominent topics outside the scope of the research.

Future research should comprehensively consider both the iterative development of LLM-generated reviews and detection systems. Firstly, regarding the review generation by LLMs, on the one hand, although the current resolution of the reliability of references is encouraging, the overall quality of the articles still poses signiﬁcant issues in fully serving clinical purposes. From the current models of major platforms, a noticeable problem is that the review generation is overly adapted to the commercial deployment of LLMs. Despite the introduction of human knowledge bases and other auxiliary technologies, the ultimate goal remains a one-time uniﬁed output by LLMs. However, this generation method does not align with traditional review writing practices. Traditionally, after selecting a topic, a search-based construction is conducted, involving database searches, specifying inclusion and exclusion criteria, and then excluding articles based on titles and abstracts, followed by reading and summarizing each article33.Thistraditionalresearchmodelisentirelyworthlearningfromand emulating. It is possible to attempt to have LLMs serve several segments of the humanized process rather than altering traditional processes to ﬁt the LLMs. We randomly selected several topics related to various human systems involved in this study for a simple post-hoc exploratory study. The improvement in results was signiﬁcant, ensuring the reliability of the cited references while greatly enhancing the overall quality of the review, with no statisticaldifferencesinparagraphandwordcountcomparedtotheoriginal text (see details in Supplementary Note 4). On the other hand, due to the rapid iteration of models in the current LLM ﬁeld, the performance of different models on the same task varies. Although this article incorporates thelatestmodels available atthetime for exploratoryresearch, future studies should not only focus on this aspect but also explore more efﬁcient generationframeworkstoenabletheswiftintegrationofthelatestmodels,rather than repeatedly conducting similar experiments. Additionally, regarding detection systems, a new detection system framework urgently needs to be established. In the past, the current detection systems were placed in opposition to LLMs, akin to the captcha wars used to block web crawlers34. More and more academic publishers and professional detection agencies are launching their own “AI checking rates“35. We seem to have fallen into a misconception that academic papers must be completed by humans or mostly by humans; otherwise, they should not be recognized. This overly proﬁt-driven mindset overlooks the fact that every article, regardless of its author, should be valued if its conclusions are reliable and contribute to life. LLMs offer us a new perspective, as they can help complete review articles and potentially assess the value of a review in advancing the industry or its educational value for future researchers. From a non-proﬁt perspective, leveraging LLM to establish a detection system based on the contribution of papers in speciﬁc ﬁelds, rather than overly focusing on whether they are completed by AI, should be directed towards research on whether they serve everyday life. This should become a focal point of future research.

Methods

This comparison study is part of a collaborative project involving North Sichuan Medical College, the University of Electronic Science and Technology, and the University of Glasgow. This study was reviewed by the Institutional Review Board of North Sichuan Medical College. Since it does not involve any human subjects or tissue materials, no additional ethical approval is required. Prior to the start of the study, nine experts with backgrounds in different human systems (see details in Supplementary Table 1) composed the expert evaluation panel. Each expert had extensive clinical research experience in their respective ﬁelds, with a median of 12.5 years, ranging from 2 to 18 years. In addition, a linguist and two computer PhD were responsible for the follow-up language-related discussions of the

![image 7](Luo et al._2025_Cross sectional pilot study on clinical review generation using large language models_images/imageFile7.png)

- Fig. 6 | Flowchart of the overall study design. After determining the themes of the articles in the journal, generate clinical reviews and then evaluate them based on the Basic quality of the article, Distribution of references, Quality of references, and Academic publishing risk.


study and the software production involved in the study, respectively. The overall design of the study is illustrated in Fig. 6.

Generation sources

Wenarrowdownthescopeandultimatelydeterminethesourcejournalsfor the generation of topics through the following three stages.

First, we attempt to deﬁne the basic classiﬁcation range of journals, categorizing them into low-quality, medium-quality, and high-quality. Unfortunately, there is no uniﬁed standard today to distinguish between low-qualityandmedium-qualityjournals.However,intheﬁeldofmedicine, numeroustop-tierjournals,widelyrecognized,publishhigh-qualityarticles, including Nature, Science, The New England Journal of Medicine (NEJM), The Lancet, and npj Digital Medicine. Most articles in these journals are generally considered high-quality by the academic community. Therefore, we decided to make our selection from these top-tier journals.

Second, given the numerous recognized top-tier journals, comprehensivelyevaluatingeachjournalisimpractical.Thus,weselectedthetop10 journals ranked by their 2023 impact factor (https://jcr.clarivate.com/jcr/) for our study. To ensure a comprehensive selection of topics, we chose clinical comprehensive journals.

Third, to enhance the reading experience, we prefer journals with a certain historical association.

Finally, NEJM, The Lancet, the British Medical Journal (BMJ), and the Journal of the American Medical Association (JAMA)36, all of which were

founded in the 19th century and are clinical comprehensive journals, were selected to be showcased in the main text. Moreover, to ensure comprehensivenessof results, same research wasconducted onother top 10ranked clinical comprehensive journals, including Nature Reviews Disease Primers and its related journal Nature Medicine (see details in Supplementary Table 5).

Generation topics

Theexpertpanelselectedclinicalreviewsfromthetopfourmedicaljournals (TFMJ). The selection criteria were as follows: 1) The reviews were clinical reviews. 2) At least one member of the expert panel had previously been involved in research similar to the topic under review. 3) The publication date was within the last 5 years.

The quality assessment was conducted on the selected clinical reviews (see details in Supplementary Table 3). Clinical reviews were ultimately included in this study when the average scores for unidirectional quality in Language Quality, Reference Evaluation Depth, Logical Capability, and Innovation Degree were greater than 90 points.

A total of 62 clinical reviews were ultimately included (see details in Supplementary Table 2).

Generation platforms and models

We generated relevant reviews based on review generation platforms and the current mainstream models.

- Table 1 | The search expressions used in the selected search engine and the total number of entries on the ﬁrst ﬁve pages of each search engine


Search expression The total number of entries on the ﬁrst ﬁve pages Bing Google Yandex Yahoo Baidu

Clinical literature review generator

50 64 50 35 46

Clinical literature review llm 50 66 50 45 50 Clinical literature review ai 50 65 50 45 46 Clinical literature review artiﬁcial intelligence

50 66 50 40 50

Clinical literature review large language models

50 68 50 36 50

Clinical literature review large language model

50 66 50 36 50

Clinical literature review generation

- 50 66 50 35 50

Clinical literature review generation platform

- 50 67 50 40 50


Clinical review generator 50 66 50 38 50 Clinical review llm 50 67 50 40 50 Clinical review ai 50 67 50 40 50 Clinical review artiﬁcial intelligence

50 66 50 43 50

Clinical review large language models

50 68 50 36 50

Clinical review large language model

50 66 50 35 46

Clinical review generation 50 65 50 35 46 Clinical review generation platform

50 66 50 37 50

A total of 4059 entries were ultimately retrieved across all platforms, with 9–15 entries per page.

Ononehand,theselectionofreviewgenerationplatformsfollowedthe general logic of user usage: 1) choosing a search engine, 2) entering search queries, and 3) conducting searches to select usable platforms. First, on January10,2024,wevisitedStatCounter37,aglobalwebsiteforsearchengine market share statistics, to determine commonly used search engines and selected the top ﬁve: Google38, Bing39, Yandex40, Yahoo!41, and Baidu42 (the sixth-rankedsharelabeledas“Other”doesnotrepresentasingleengineand was not selected). Subsequently, we designed search queries referencing PubMed’s43MeSHtermsandEmbase’s44EmtreetermsrelatedtoLLMs.The search queries included terms such as “clinical literature review generator,” “clinical literature review generation,” and “clinical review large language model.” Finally, to avoid potential selection bias caused by commercial promotion, the screening scope was appropriately expanded. Speciﬁcally, using the search queries, we reviewed every item on the ﬁrst ﬁve pages of search results for the international versions of theseﬁve search engines. The selection criteria were any tool-based platforms capable of generating medical reviews, with no language restrictions. To ensure the timeliness of the research, we conducted an updated second round search on January 7, 2025. A total of 4059 entries were ultimately retrieved across all platforms, with9-15entriesperpage(seeTable1fordetails).Aftercross-screeningand validation by three researchers, seven currently available review generation platforms were selected: Seamless45, Paper Digest46, AskYourPdf47, EasyPeasy.AI48,HyperWrite49,LitReview50,andTemplate.net51.Itisimportantto note that currently, no dedicated platforms for generating clinical reviews have been identiﬁed; they are all general review generation platforms. In terms of their respective characteristics, Seamless offers GPT-3.5 and GPT4.0 as the foundation for generation52. AskYourPdf provides generation

services through its website or the OpenAI application store53. EasyPeasy.AI offers GPT-4.0 as the foundation for generation. These platforms represent nearly all internationally accessible and usable review generation platforms. We categorized these platforms into nine corresponding generation sources: Seamless-1 (Seamless using GPT-3.5), Seamless-2 (SeamlessusingGPT-4.0),AskYourPdf-1(AskYourPdfusingtheofﬁcialwebsite), AskYourPdf-2 (AskYourPdf using the OpenAI application store), and Paper Digest from the ﬁrst round of selection, as well as Easy-Peasy.AI (Easy-Peasy.AI using GPT-4.0), HyperWrite, LitReview, and Template.net from the second round. Among them, LitReview and Template.net are free platforms,while the othersarepaidorpartiallypaid.Additionally,although someplatformslabeltheirmodelversionnumbers,theseplatformshavenot updated their model versions as of now.

On the other hand, to address the issue of outdated domain relevance caused by older platform models, mainstream LLMs were included for review generation. First, we visited the top-ranking lists of Hugging Face54 and OpenCompass55, selecting the top 10 open-source and closed-source modelsascandidates,withthescopeextendingtoDecember2024.Then,the selection of relevant LLMs was considered from the following aspects: 1) Closed-source commercial models: To accommodate the usage habits of bothgeneralandsubscription-basedusers,weselectedmodelswithdifferent user orientations from the same company, such as GPT-4o for subscription users and GPT-4o-mini for general users. Additionally, to avoid selection bias toward a single company, we chose models from several mainstream companies, including Anthropic, OpenAI, and Google. 2) Open-source models: To cater to enterprises with varying hardware capabilities, we selected models with different user orientations from the same company, such as Llama-3.1-8B for general enterprises and Llama-3.1-405B for enterprises with better hardware. Additionally, we selected the specialized medical open-source model Palmyra-Med-70B as a professional candidate. 3) Expert consensus-oriented models: Based on recommendations from review experts, we adopted Bloom and Galactica as supplementary models for specialized use cases. The ﬁnal selected models included GPT-4o, Claude-3.5-Sonnet, Claude-3.5-Haiku, Gemini-1.5-Pro, GPT-4o-mini, Llama-3.1-405B, Llama-3.1-8B, o1-mini, o1-preview, Palmyra-Med-70B, Qwen2.5-72B, Bloom, and Galactica-120B. Their respective version numbers and usage documentation are provided in Table 2.

All models and platforms were invoked using default parameters, except for the maximum token count, which was set to the maximum to avoidtruncation.Theinﬂuenceofparameteradjustmentsisdiscussedinthe supplementary research displayed in the article discussion section.

Generation prompts

Regarding prompts, since Seamless, Paper Digest, Easy-Peasy.AI, HyperWrite, LitReview, Template.net and AskYourPdf-1 do not accept custom prompts and only accept direct review topics or purposes, a specialized prompt was designed for AskYourPdf-2, GPT-4o, Claude-3-5-sonnet, Claude-3.5-haiku, Gemini-1.5-pro, GPT-4o-mini, LIaMA-3.1-405B, LIaMA-3.1-8B, o1-mini, o1-preview, Palmyra-Med-70B, Qwen2.5-72B, Bloom and Galactica. Before the study began, ZNL, DRW, JBX, YSP, and YXR constructed the prompts. ZNL is a certiﬁed Prompt Engineer at Datawhale (https://github.com/datawhalechina), with certiﬁcation number DWPE011528. DRW holds positions at multiple computing centers, while JBX, YSP, and YXR are attending physicians in the expert group. Speciﬁcally, we constructed prompts focusing on logic, stability, and optimal performance release.

ZNL and DRW identiﬁed an initial set of prompts and selected ﬁve articlesfromthetopicstobegeneratedforprompttesting.Theprinciplesfor constructing prompt words have been explained elsewhere56. Each prompt was inputted to execute repeated outputs three times. The average of expert evaluation results formed the score for each output, and the consistency of thethreerepeatedoutputswastested.Fromthissetofprompts,theonewith the best overall properties was selected and optimized multiple times, repeating the above process until the score difference between the clinical reviewgeneratedbytheoptimizedpromptandtheoriginalreview’sprompt

- Table 2 | Details of the models used in generating clinical reviews


Model Call method Version Parameter Conﬁguration URL

- o1-preview OpenAI API o1-preview-2024-09-12 Default* https://openai.com/index/introducing-openai-o1preview/
- o1-mini OpenAI API o1-mini-2024-09-12 Default* https://openai.com/index/openai-o1-mini-advancingcost-efﬁcient-reasoning/


GPT-4o OpenAI API GPT-4o-2024-11-20 Default* https://openai.com/index/hello-gpt-4o/ GPT-4o-mini OpenAI API gpt-4o-mini-2024-07-18 Default* https://openai.com/index/gpt-4o-mini-advancing-cost-

efﬁcient-intelligence/ Claude-3.5-Sonnet Anthropic API claude-3-5-sonnet-

Default* https://www.anthropic.com/claude/sonnet

20241022

Default* https://www.anthropic.com/claude/haiku

Claude-3.5-Haiku Anthropic API claude-3-5-haiku20241022

Gemini-1.5-Pro Google API Gemini-1.5-pro-latest Default* https://deepmind.google/technologies/gemini/pro/ Llama-3.1-8B Llama API / Default* https://huggingface.co/meta-llama/Llama-3.1-8B Llama-3.1-405B Llama API / Default* https://huggingface.co/meta-llama/Llama-3.1-405B Palmyra-Med-70B Server Deployment† + API / Default* https://huggingface.co/Writer/Palmyra-Med-70B Qwen2.5-72B Server Deployment† + API / Default* https://huggingface.co/Qwen/Qwen2.5-72B-Instruct Bloom Hugging face API / Default* https://huggingface.co/bigscience/bloom Galactica-120B Server Deployment† + API / Default* https://huggingface.co/facebook/galactica-120b

Server Deployment†:Chassis: 4U RackmountChassis,178 mm × 437 mm ×737 mm(H × W ×D) CPU: AMD EPYC7642,48 Cores,2.3 GHz×2 Memory:32GB DDR43200 MHz ECCREG×8 SystemDrive: 500GB M.2 NVMe SSD× 1 Storage Drive: 8TB 7200RPM SATA Enterprise-grade HDD (256MB cache) × 1 GPU: NVIDIA Tesla A100, 80GB × 4 Network Card: Single-port 200 Gb Inﬁniband Card × 1 Application Software: Pre-installed TensorFlow, PyTorch, and other supported software with technical support Operating System: Linux 64-bit Enterprise Edition Default*: When invoking the model, parameters such as temperature are not speciﬁcally adjusted. Only set the token count to the maximum to avoid truncation. The discussion section includes an analysis of the impact of parameter changes and corresponding supplementary research. The ﬁnal selected models included GPT-4o, Claude-3.5-Sonnet, Claude-3.5-Haiku, Gemini-1.5-Pro, GPT-4o-mini, Llama-3.1-405B, Llama-3.1-8B, o1-mini, o1-preview, Palmyra-Med-70B, Qwen2.572B, Bloom, and Galactica-120B.

was less than 5 points on several quantitative subjective indicators. Our deﬁnitions of logicality, stability, and optimal performance release are as follows: 1) Regarding logicality, we focus on the logical rationality of applying this technology to actual clinical environments in the future. Speciﬁcally, from the perspective of prompt development, further elaborating on the objectives or deeply explaining the current focus of topics related to these objectives might enable LLMs to perform better. However, fromaclinicallogicstandpoint,individualsconductingclinicalreviewsmay not always have scholars proﬁcient in this ﬁeld to guide or assist them. Therefore, to better align with future clinical scenarios, the extracted objectiveswerenotgivenfurtherguidance.2)Concerningstability,giventhe inherent uncertainty in LLM outputs, it is critically important to ensure whether these different outputs yield results that are either identical or have minimal variation (within a ﬁve-point margin). This is to guarantee the quality stability of outputs in a working environment. 3) With respect to optimal performance release, varying prompts have been shown to signiﬁcantlyimpactperformanceonmedicaltasks57.Weaimtoselectaprompt that maximally enhances performance by adjusting the prompt itself. Although testing every conceivable prompt is regarded as impossible, we have referencedNature’s research on LLMs58. As these generative platforms willbeupdatedinthefuture,thepromptswetestmaynotentirelytransferto newmodels.Additionally,inclinicalsettings,clinicalscholarsareunlikelyto immediately ﬁnd the best prompt but rather seek a prompt with relatively good performance. Considering these factors, we developed and tested prompts under conditions closely aligned with real-world scenarios. Examples of iterative results for prompts on a single model or platform are shown in Table 3. More details on this can be found in Supplementary Note 3.

Generation methods

Tomitigatebiasfromsigniﬁcantlyshorterarticles,clinicalreviewgeneration employs two methods: 1) The objective method, where well-trained research assistants manually extract the research objectives of each study and input them into the platform to generate the ﬁnal text. 2) The outline method, where well-trained assistants manually extract the objectives of

each study and input them into the predetermined best framework generationmodel(seedetailsinSupplementaryNote1),GeminiPro59,usingthe prompt“HerearetheresearchobjectivesfortheclinicalreviewIamwriting, please help me develop an outline.” Each outline title is then input into the platform separately, and ﬁnally, they are connected to form the subsequent testarticle.Meanwhile,tocomplywiththeusagelicenseofLLMcompanies, OpenAI and Google’s services are operated on the servers of UK by DRW from University of Glasgow using a private security service in Citrix Workspace.

Blind setting

Computer PhDs have developed a specialized evaluation system. After training on the hierarchical grading criteria, each expert receives a system account and is assigned a certain number of clinical reviews randomly in their respective research direction. During the evaluation process, the experts were not informed of the source of these articles.

Multilevel evaluation measures

Before the start of the study, an exploration of indicator selection was conducted (see details in Supplementary Note 2). Our aim was to provide a relativelycomprehensive evaluation of areview articleusing bothsubjective andobjectiveindicators.Thesubjectiveindicatorsweredeterminedthrough literature searches. Speciﬁcally, we selected the top 30 models and their corresponding company names from the OpenCompass model leaderboard, as well as relevant MeSH terms from PubMed and Emtree terms fromEmbase.Basedonthese,weconstructedsearchstrategiesandretrieved articles related to LLM evaluation published in the two databases since the release of OpenAI’s ChatGPT-3.5. From these, we identiﬁed two existing shortevaluationarticles60,61asthefoundationalreferencesforourevaluation indicators. On this basis, we preliminarily developed a subjective indicator system consisting of ﬁve major components, each scored on a 100-point scale. For the objective indicators, we conducted an initial exploration of existing scales. After excluding some scales that were clearly incompatible with the article type, we invited linguists to design the objective indicators. These indicators also incorporated factors such as the impact factor and

- Table 3 | Development and Iteration Process of Prompts


Version Prompt

- Version 1 Please write a clinical review article on [Insert Clinical Topic Here].
- Version 2 Pleasewriteadetailedclinicalreviewarticleon[InsertClinicalTopicHere]toguideclinicalpracticeorresearchactivities.Includecurrent evidence, recent advancements, and practical recommendations.
- Version 3 Please compose a comprehensive clinical review article on [Insert Clinical Topic Here], focusing on guiding clinical practice and research activities. Provide an overview of the topic, discuss current evidence and recent advancements, and include practical recommendations for clinicians and researchers.
- Version 4 Please write a comprehensive clinical review article on [Insert Clinical Topic Here] aimed at guiding clinical practice and research activities. The article should include an introduction, analysis of current evidence and recent advancements, discussion of clinical implications, and practical recommendations for clinicians and researchers. Ensure that the information is evidence-based and upto-date.
- Version 5 (The ﬁnal chosen version)


Composeathoroughclinicalreviewarticleon[InsertClinicalTopicHere],designedtoguideclinicalpracticeandresearchactivities.The article should include: Introduction: Outline the importance and relevance of the topic. Current Evidence: Provide a detailed review of recent studies, data, and advancements related to the topic. Clinical Implications: Analyze how the evidence impacts clinical practice and patient care. Practical Recommendations: Offer evidence-based guidance for clinicians and researchers. Conclusion: Summarize key points and suggest areas for future research. Ensure that the article is well-organized, evidence-based, and written in clear, professional language suitable for clinical professionals.

During the development process, the prompts ultimately used underwent several iterations.

journal ranking, which have historically inﬂuenced article evaluation systems. Finally, certain attention was given to the risks associated with academic publishing. Since most publishers have already disclosed their plagiarism detection platform, iThenticate62, this platform was directly used for plagiarism rate detection. However, for the recently emerging AIGC detection rate, there is currently no universally recognized and publicly available benchmark system among publishers. Instead, online AIGC detection platforms were used as substitutes. The process of selecting AIGC detection platforms was similar to the process of choosing platforms for generating clinical reviews (see details in Supplementary Note 6) and will not be elaborated here. Ultimately, eight platforms—Scribbr63, Typeset.io60, GPTZero61, Grammarly64, SurferSEO65, Decopy.ai66, AIHumanize67, and GetMerlin68—were selected for AIGC detection. To control detection costs, 1-2 reviews demonstrating the best performance for each human system were sampled and submitted for testing from each generation platform or model.

Theﬁnalevaluationcriteriaareasfollows:1)basicqualityofthearticle: word count, paragraph count, number of references, comprehensiveness of references, authenticity of references, accuracy of references, language quality,depthofreferenceevaluation,logicalability,levelofinnovation,and overall quality; 2) distribution of references: the percentage of references within 1 year, 3 years, 5 years, and 10 years of publication/generation of the article in the total number of references; the percentage of references in the Q1, Q2, Q3, and Q4 zones of the JCR among the total references; the percentage of references with impact factors of 0–3, 3–5, 5–10, and ≥10 in the total references; and the percentage of references with CiteScore of 0–3, 3–5, 5–10, and ≥10 in the total references3.) Quality of references: cumulative citations of all references, average number of citations per reference4.) Academic publishing risk: Plagiarism checks62 and AIGC checks. The deﬁnitions of each speciﬁc indicator are shown in Table 4.

Comparability control in reviews

To ensure the comparability of the ﬁnal results, the study implemented controlsforcomparabilityfromthefollowingaspects.First,expertswiththe same or similar research backgrounds were selected for evaluation. Speciﬁcally, subjective indicators within the same article, including overall quality, language quality, depth of reference evaluation, logical reasoning, and degree of innovation, were assessed by experts with the same or similar research experience within the expert group. Second, each article was evaluated through cross-assessment by at least two experts. Under the premise of maintaining the same or similar research background as the manually written literature, at least two experts were selected for crossassessment, and the average of their evaluations was taken as the ﬁnal evaluation result for these items. Additionally, we referred to two previous

studies69,70, expanding their baseline sample size by threefold and broadening the scope from a single topic to all human systems to avoid heterogeneitycausedbya singletopic. Finally,generalreviews withrelatively ﬁxed formats were selected for generation, avoiding biases introduced by methodological differences in specialized reviews, such as meta-analyses.

Statistical analysis

DataanalysiswasconductedusingSPSS(version29.2.1.0(171)).Theoverall analysis used the Mann‒Whitney U test. For subgroup analysis, the difference analysis of skewed data was conducted using the Kruskal‒Wallis H test, whereas normally distributed data were analyzed using analysis of variance (ANOVA). During multiple hypothesis testing, the Bonferroni correction method was used to adjust the p values. A p value less than 0.001 was considered to indicate statistical signiﬁcance. In addition, an intraclass correlation coefﬁcient was used for consistency testing. To ensure the generalizability of the results, a two-way random-effects model was chosen. Since the evaluation of the same article might involve two or more experts, when the number of evaluators exceeds two, pairwise combinations of the evaluation results from multiple experts are formed for consistency testing. Asinglemeasurementresultgreaterthan0.8isconsideredindicativeofhigh consistency. Finally, in the presentation of the results, the overall analysis includes all results from both generation methods across all platforms and models, collectively named Ai.

Data availability

The review used in this article can be downloaded from Google Drive (https://drive.google.com/drive/folders/1hEinwiqcNHvIhi_NejiUf11-

PLdpwWNL?usp=drive_link). Please note that before downloading, you should be aware of and conﬁrm that you have the necessary permissions to download and access articles from BMJ, JAMA, NEJM, Lancet, and Springer. We also provide step-by-stepscreenshots of the manual detection process for AIGC detection rates(https://drive.google.com/drive/folders/ 1wZkH-srMsgYU-ehaE6rIqnAXOaw74j_l?usp=drive_link). Please note that since some researchers are based in China, the default browser may translatethewebpageintoChineseduringthescreenshotprocess.However, this does not affect the original data. We are more than happy to provide language assistance. If you require assistance, you can contact Zining Luo (rosin@ai-research.group) for support.

Code availability

All the code involved in this study was written in VB.NET (.NET Framework4.8),andthe originalGUI interface was createdin Chinese. Itincludes two client applications and one server application deployed on a Windows server system. The VB.NET code can be requested from the corresponding

- Table 4 | Deﬁnitions of Various Indicators


Details of the indicators included in cross-platform comparison. Basic quality of the article Items Explanation Objective indicators Word count Length of a single review article (excluding references) Paragraph count The number of paragraphs in a single review article (excluding references) Number of references The number of references in a single review article Comprehensiveness (References) (%)

The number of references in a single review article The total number of literature in this research field ×100% (data from PubMed, the search query is constructed using NCBI’s ofﬁcial MeSH terms and entry terms) (Due to technical limitations, only commonly used databases are included, for reference only)

Authenticity (References) (%) The number of references that can be successfully queried in Crossref;PubMed;or OpenAlex

The number of references in a single review article ×100% (Due to technical limitations, only commonly used databases are included, for reference only)

Accuracy (References) (%) The number of references explained in the generated review is consistent with the original text

The number of references in a single review article ×100% (Manual judgments by multiple trained research assistants)

Subjective indicators Overall Quality 0–30: The article quality is poor, lacking depth and accuracy, with a disorganized structure.

31–50: The article quality is average, with basic content and structure, but there are many issues present. 51–70: The quality of the article is good, the content is quite substantial, the structure is reasonable, but there is still room for improvement. 71–90: The article is of excellent quality, the content is in-depth and accurate, and the structure is clear and logical. 91–100: The article is outstanding in quality, the content is comprehensive and profound, the structure is perfect, and there is hardly anything to criticize.

Language Quality 0–30: The language expression is chaotic, with numerous grammar errors and inappropriate word choices. 31–50: The language expression is average, with some grammar errors and inaccurate word choices. 51–70: The language expression is good, with minimal grammar errors and relatively accurate word choices. 71–90: The language expression is ﬂuent, the grammar is accurate, and the word choices are appropriate and rich. 91–100: The language expression is extremely excellent, with elegant writing, precise and creative word choices.

Depth of reference evaluation 0–30: Shallow understanding of citations, one-sided evaluation, or lack thereof. 31–50: Basic understanding and evaluation of citations, but lacking depth and breadth. 51–70: Demonstrating a good understanding and evaluation of citations with some depth. 71–90: A profound understanding and evaluation of citations, able to analyse from multiple perspectives. 91–100: An extremely deep understanding and evaluation of citations, demonstrating a high level of criticality and innovation.

Logical Capability 0–30: The article lacks logical structure, and the content is disorganized. 31–50: The article has average logic, lacks clear structure, and contains logical gaps. 51–70: The article has good logic, relatively clear structure, but there is still room for improvement. 71–90: The article has strong logic, rigorous structure, and clear organization. 91–100: The article exhibits extremely strong logic, perfect structure, and demonstrates a high level of cognitive ability.

Innovation Degree 0–30: The article lacks innovation, and its content is outdated. 31–50: The article is moderately innovative with a small amount of novel content. 51–70: The article demonstrates a certain level of innovation with novel insights or methods. 71–90: The article has a high level of innovation, proposing novel theories or methods. 91–100: The article is extremely innovative, proposing groundbreaking new theories or methods that are revolutionary.

Distribution of references Items Explanation References in the Past Year (%) The proportion of references in a review article that were published within one year prior to its generation/publication. References in the Last 3 Years (%) The proportion of references in a review article that were published within three years prior to its generation/publication. References in the Last 5 Years (%) The proportion of references in a review article that were published within ﬁve years prior to its generation/publication. References in the Last 10 Years (%) The proportion of references in a review article that were published within ten years prior to its generation/publication.

- Reference for Q1 (%) According to the JCR quartile classiﬁcation by Clarivate Analytics, the proportion of a single review article in the Q1 quartile in relation to all the reference articles. (Data is up to March 1, 2024)
- Reference for Q2 (%) According to the JCR quartile classiﬁcation by Clarivate Analytics, the proportion of a single review article in the Q2 quartile in relation to all the reference articles. (Data is up to March 1, 2024)
- Reference for Q3 (%) According to the JCR quartile classiﬁcation by Clarivate Analytics, the proportion of a single review article in the Q3 quartile in relation to all the reference articles. (Data is up to March 1, 2024)
- Reference for Q4 (%)


Table 4 (continued) | Deﬁnitions of Various Indicators

Distribution of references Items Explanation

According to the JCR quartile classiﬁcation by Clarivate Analytics, the proportion of a single review article in the Q4 quartile in relation to all the reference articles. (Data is up to March 1, 2024)

Impact factor (0-3) (%) According to the impact factor provided by Clarivate Analytics, the proportion of single review articles in the range of 0 to 3 impact factors among all references. (Data is up to March 1, 2024)

Impact factor (3-5) (%) According to the impact factor provided by Clarivate Analytics, the proportion of single review articles in the range of 3 to 5 impact factors among all references. (Data is up to March 1, 2024)

Impact factor (5-10) (%) According to the impact factor provided by Clarivate Analytics, the proportion of single review articles in the range of 5 to 10 impact factors among all references. (Data is up to March 1, 2024)

Impact factor ( ≥ 10) (%) Accordingto the impact factor provided byClarivate Analytics, the proportion ofsingle review articles in therangeof impact factors of 10 and above among all references. (Data is up to March 1, 2024)

CiteScore (0–3) (%) According to the CiteScore provided by Elsevier, the proportion of single review articles in the CiteScore range of 0 to 3 among all references. (Data is up to March 1, 2024)

CiteScore (3–5) (%) According to the CiteScore provided by Elsevier, the proportion of single review articles in the CiteScore range of 3 to 5 among all references. (Data is up to March 1, 2024)

CiteScore (5–10) (%) According to the CiteScore provided by Elsevier, the proportion of single review articles in the CiteScore range of 5 to 10 among all references. (Data is up to March 1, 2024)

CiteScore ( ≥ 10) (%) According to the CiteScore provided by Elsevier, the proportion of single review articles in the CiteScore range of 10 and above among all references. (Data is up to March 1, 2024)

Quality of references Items Explanation Cumulative citations of all references The sum of the citation counts of different references in a single article since their publication. (Data is up to March 1, 2024) Average number of citations per reference

The average citation counts of different references in a single article since their publication. (Data is up to March 1, 2024)

Academic publishing riska Items Explanation Plagiarism checks Using the iThenticate/CrossCheck platform (https://www.ithenticate.com/) to conduct plagiarism checks AIGC checks Using online platforms such as Scribbr (https://www.scribbr.com/ai-detector/), Typeset.io (https://typeset.io/ai-detector),

GPTZero (https://gptzero.me/), Grammarly (https://www.grammarly.com/ai-detector), SurferSEO (https://surferseo.com/aicontent-detector/), Decopy.ai (https://decopy.ai/ai-content-detector/), AIHumanize (https://aihumanize.com/ai-detector/), and GetMerlin (https://www.getmerlin.in/EN/ai-detection) to detect the AIGC rate.

aTo replicate the scenarios where these generated articles might pass the preliminary review of some journals, we selected the top 20 generated reviews from each source, ranked by Overall Quality, for checking. The indicators include four aspects: Basic quality of the article, Distribution of references, Quality of references, and Academic publishing risk.

author, Xie Jiebin (xiejiebin84@126.com). To facilitate the reproduction of the conclusions in this article, a Python version of the reproduction library and workﬂow is provided. Links to the platforms used in the article can be found in the URLs of the corresponding references. The prompts involved are listed in the tables. For the models, the libraries used for invoking each model include: GPT series (https://github.com/openai/openai-cookbook), Claude series (https://github.com/anthropics/anthropic-cookbook), Gemini series (https://github.com/google-gemini/cookbook), Bloom (https://huggingface.co/bigscience/bloom), Qwen2.5-72B (https:// huggingface.co/Qwen/Qwen2.5-72B-Instruct), Galactica-120B (https:// huggingface.co/facebook/galactica-120b), Llama series (https://docs.llamaapi.com/quickstart), and Polaris framework(https://drive.google.com/ drive/folders/1G5nxkV0LzJdCu7WEHycwg8fzc8QbsFWa?usp=sharing).

Please note that we only accept requestsfor research purposes. Commercial requestsarecurrentlynotallowed.WedonotprovidepaidAPIkeys,butwe are happy to offer technical and linguistic assistance. If you require related support, feel free to contact rosin@ai-research.group, and please specify your requirements when making the request.

Received: 30 April 2024; Accepted: 21 February 2025;

![image 8](Luo et al._2025_Cross sectional pilot study on clinical review generation using large language models_images/imageFile8.png)

References

1. Rita, G-M, Luca, S., Benjamin, M. S., Philipp, B. & Dmitry, K. The landscape of biomedical research. bioRxiv (2024).

- 2. Literature Review and Synthesis Implications on Healthcare Research, Practice, Policy, and Public Messaging. (Springer Publishing Company, New York, NY, 2022).
- 3. Thirunavukarasu, A. J. et al. Large language models in medicine. Nat. Med. 29, 1930–1940 (2023).
- 4. The New York Times. How ChatGPT Kicked Off an A.I. Arms Race. (https://www.nytimes.com/2023/02/03/technology/chatgpt-openaiartiﬁcial-intelligence.html) (2023).
- 5. Large Language Model Market Size, Share & Trends Analysis Report By Application (Customer Service, Content Generation), By Deployment, By Industry Vertical, By Region, And Segment Forecasts, 2024 - 2030. (https://www.grandviewresearch.com/ industry-analysis/large-language-model-llm-market-report)

(2024).

- 6. Zhiyao, R., Yibing, Z., Baosheng, Y., Liang, D. & Dacheng, T. Healthcare Copilot: Eliciting the Power of General LLMs for Medical Consultation. arXiv.org (2024).
- 7. Kathryn,G. B., Nicole, G. I., Ashley,G. O., Julien, O. T. & Andrew,G. R. Use of generative AI to identify helmet status among patients with micromobility-related injuries from unstructured clinical notes. Jama Netw. Open 7, e2425981 (2024).
- 8. Junkai, L. et al. Agent Hospital: A Simulacrum of Hospital with Evolvable Medical Agents. arXiv.org (2024).
- 9. Dergaa, I., Chamari, K., Zmijewski, P. & Ben Saad, H. From human writing to artiﬁcial intelligence generated text: examining the


prospects and potential threats of ChatGPT in academic writing. Biol. Sport 40, 615–622 (2023).

- 10. Tang, L. et al. Evaluating large language models on medical evidence summarization. NPJ Digit. Med. 6, 158 (2023).
- 11. Mugaanyi, J., Cai, L., Cheng, S., Lu, C. & Huang, J. Evaluation of large language model performance and reliability for citations and references in scholarly writing: cross-disciplinary study. J. Med. Internet Res. 26, e52935 (2024).
- 12. Soni, A., Arora, C., Kaushik, R. & Upadhyay, V. Evaluating the impact of data quality on machine learning model performance. J. Nonlinear Anal. Optim. 14, 13–18 (2023).
- 13. Walters,W.H. &Wilder,E. I.Fabricationanderrorsinthebibliographic citations generated by ChatGPT. Sci Rep.13, 14045 (2023).
- 14. Shubham, A., Issam, H. L., Laurent, C. & Christopher, P. LitLLM: A Toolkit for Scientiﬁc Literature Review. arXiv.org (2024).
- 15. Haoyi, X. et al. When Search Engine Services meet Large Language Models: Visions and Challenges. arXiv.org (2024).
- 16. Yousif, M. J. Systematic review of semantic analysis methods. Appl. Comput. J. 286-300 (2023).
- 17. Shuai, W., Harrisen, S., Bevan, K. & Guido, Z. Can ChatGPT Write a Good Boolean Query for Systematic Review Literature Search? arXiv.org (2023).
- 18. John, D. et al. Structured information extraction from scientiﬁc text with large language models. Nat. Commun. 15, 1418 (2024).
- 19. Koller, D. et al. Why we support and encourage the use of large language models in NEJM AI submissions. NEJM AI 1 (2024).
- 20. Zhang, M., Wu, L., Yang, T., Zhu, B. & Liu, Y. Retracted: the threedimensional porous mesh structure of Cu-based metal-organicframework - Aramid cellulose separator enhances the electrochemical performance of lithium metal anode batteries. Surf. Interfaces 46, 104081 (2024).
- 21. John, H., Christopher, D. M. & Percy, L. Truncation sampling as language model desmoothing. arXiv.org (2022).
- 22. Hughes, J. Size matters (or should) in copyright law. Soc. Sci. Res. Netw. 74, 575 (2005).
- 23. Sudhi,S. & Young, M. L. Challenges with developingand deployingAI models and applications in industrial systems. Discov. Artif. Intell.4, 55 (2024).
- 24. Tian, E. Perplexity, burstiness, and statistical AI detection. (https:// gptzero.me/news/perplexity-and-burstiness-what-is-it/) (2023).
- 25. Meo, S. A., Talha, M. Turnitin: is it a text matching or plagiarism detection tool? Saudi J. Anaesth. 13, S48-S51 (2019).
- 26. Junyi, L. et al. The dawn after the dark: an empirical study on factuality hallucination in large language models. arXiv.org (2024).
- 27. Saini,T. How doesa dataset affects performance of AI Model?(2023).
- 28. Jack, W. R., Anna, P., Siddhant, M. J. & Timothy, P. L. Compressive transformers for long-range sequence modelling. arXiv.org (2019).
- 29. Saurav, P. et al. The what, why, and how of context length extension techniques in large language models -- a detailed survey. arXiv.org

(2024).

- 30. Burtsev, M. The working limitations of large language models (https://readwise.io/reader/shared/01hh2cwcjt53r4er2vpzn7sy92/)

(2023).

- 31. Vinu, S. S., Aounon, K., Sriram, B., Wenxiao, W. & Soheil, F. Can AIGenerated Text be Reliably Detected? arXiv.org (2023).
- 32. Forlini, E. D. OpenAI quietly shuts down AI text-detection tool over inaccuracies. (https://www.pcmag.com/news/openai-quietly-shutsdown-ai-text-detection-tool-over-inaccuracies) (2023).
- 33. Iddagoda M. T., Flicker L. Clinical systematic reviews–a brief overview. BMC Med. Res. Methodol. 23, 226 (2023).
- 34. Bentley, P. How AI ﬁnally won its war on CAPTCHA images? (https:// www.sciencefocus.com/future-technology/ai-vs-captcha) (2024).
- 35. Staiman, A. Publishers, Don’t Use AI Detection Tools! (https:// scholarlykitchen.sspnet.org/2023/09/14/publishers-dont-use-aidetection-tools/) (2024).


- 36. Jinlin,W.etal.ChinesecontributiontoNEJM,Lancet,JAMA,andBMJ from 2011 to 2020: a 10-yearbibliometric study. Ann. Transl. Med. 10, 505 (2021).
- 37. Statcounter.SearchEngineMarketShareWorldwide-Dec2023-Dec 2024 (https://gs.statcounter.com/search-engine-market-share)

(2025).

- 38. Google. Google search engine. (https://www.google.com/) (2025).
- 39. Bing. Microsoft Bing (https://www.bing.com/) (2025).
- 40. Yandex search engine (https://yandex.com/) (2025).
- 41. Yahoo. Yahoo search engine (https://www.yahoo.com/) (2025).
- 42. Baidu. Baidu search engine (https://www.baidu.com/) (2025).
- 43. National Library of Medicine - National Center for Biotechnology Information (https://pubmed.ncbi.nlm.nih.gov/) (2025).
- 44. Elsevier. Welcome to Embase (https://www.embase.com/emtree)

(2025).

- 45. Draft your Literature Review 100x faster with AI (https://seaml.es/ science.html) (2024).
- 46. Theplatformtofollow,search,review&rewritescientiﬁcliteraturewith no hallucinations (https://www.paperdigest.org/) (2024).
- 47. AI Literature Review Writer Tool (https://askyourpdf.com/tools/ literature-review-writer) (2024).
- 48. Easy-Peasy.AI-Literature Review Generator (https://easy-peasy.ai/ presets/literature-review-generator) (2025).
- 49. HyperWrite. AI Literature Review Generator (https://www. hyperwriteai.com/aitools/ai-literature-review-generator) (2025).
- 50. Litreview. Academic Review Generator (https://litreview.slideai.net/ academic-review-generator) (2025).
- 51. Template.net-Super Charge with AI (https://www.template.net/ailiterature-review-generator) (2025).
- 52. Introducing ChatGPT (https://openai.com/index/chatgpt/) (2024).
- 53. Introducing the GPT Store (https://openai.com/blog/introducing-thegpt-store/) (2024).
- 54. Hugging Face is way more fun with friends and colleagues! (https:// huggingface.co/collections) (2025).
- 55. OpenCompass. CompassRank is dedicated to exploring the most advanced language and visual models, offering a comprehensive, objective, and neutral evaluation reference for the industry and research. (https://rank.opencompass.org.cn/home) (2025).
- 56. Liu, P. et al. Pre-train, prompt, and predict: a systematic survey of prompting methods in natural language processing. ACM Comput. Surv. 55, 1–35 (2023).
- 57. Yan,S.etal.Promptengineeringonleveraginglargelanguagemodels in generating response to InBasket messages. J. Am. Med. Inform. Assn. 31, 2263–2270 (2024).
- 58. Lexin,Z. et al.Larger andmore instructablelanguagemodelsbecome less reliable. Nature 634, 61–68 (2024).
- 59. Gemini Models (https://deepmind.google/technologies/gemini/)

(2024).

- 60. SCISPACE. Academic AI Detector. Catch GPT-4, ChatGPT, Jasper, and any AI in scholarly content (https://typeset.io/ai-detector) (2025).
- 61. GPTZero. More than an AI detector. Preserve what’s human. (https:// gptzero.me/) (2025).
- 62. Check for similarity with the tool trusted by the world’s leading publishers,researchers,andscholars.(https://www.ithenticate.com/)

(2024).

- 63. Scribbr. Free AI Detector. Identify AI-generated content, including ChatGPT and Copilot, with Scribbr’s free AI detector. (https://www. scribbr.com/ai-detector/) (2025).
- 64. Grammarly. AI Detector by Grammarly. Navigate responsible AI use withour AI checker,trained to identifyAI-generated text. A clear score showshowmuchofyourworkappearstobewrittenwithAIsoyoucan submit it with peace of mind. (https://www.grammarly.com/aidetector) (2025).
- 65. Surferseo. Free AI Detector (https://surferseo.com/ai-contentdetector/) (2025).


- 66. Decopy.ai. Free AI Content Detector(https://decopy.ai/ai-contentdetector/) (2025).
- 67. Aihumanize. Detect content from AI writing tools like ChatGPT (https://aihumanize.com/ai-detector/) (2025).
- 68. Getmerlin. Free AI Detector & AI Checker Tool With AI Humanizer (https://www.getmerlin.in/ai-detection) (2025).
- 69. Christopher, L. W. et al. Addition of dexamethasone to prolong peripheral nerve blocks: a ChatGPT-created narrative review. Reg. Anesthes. Pain Med.49, 777–781 (2023).
- 70. Choueka, D., Tabakin, A. L. & Shalom, D. F. ChatGPT in urogynecology research: novel or not? Urogynecology 30, 962–967 (2024).


Acknowledgements

We would like to express our heartfelt gratitude to Mr. Guangzhi Luo, who contributedsigniﬁcantlytotheoveralldesignofthisresearchinitsearlystages. Unfortunately, he passed away due to illness on the evening of September 27th at 9:15 PM. We are deeply thankful for the guidance he provided us as a mentor. At the same time, during the process of revising the article, Z.N.L. is deeplygratefultoXXYfor her companionshipduring hisemotional lowpoints. May I ask, would you be my girlfriend? Meanwhile, we would like to thank the fundingprovidedbytheNanchongCity-UniversityCooperationProject(Grant No. 22XQT0309), the Doctoral Research Start-up Fund of North Sichuan Medical College (Grant No. CBY22-QDA15), the Afﬁliated Hospital of North Sichuan Medical College (Grant No. 2022LC005), and the Key Cultivation Project of North Sichuan Medical College (Grant No. CBY23-ZDA10).

Author contributions

All authorsconceivedanddesigned the study.Z.N.L.and D.R.W.developed all the software and algorithms involved in the research. Y.Q., X.Y.X., X.Y.L., M.Y.X., A.J.K., and Z.N.L. were involved in the collection and preparation of all datasets during the ﬁne-tuning process. Z.N.L., J.B.X., Y.X.R., Y.L., Y.S.P.,D.C.L.,X.F.D.,X.X.,S.J.X.,andZ.L.L.participatedintheevaluationof expert indicators in the formal study. Z.N.L. and Z.Y.L. analyzed and validated all the indicators on the mobile phone. A.M.H., Z.N.L., J.B.X., and Y.X.R. had access to all the data in the study and drafted the manuscript.

Competing interests

The authors declare no competing interests.

Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41746-025-01535-z.

Correspondence and requests for materials should be addressed to Yixing Ren or Jiebin Xie.

Reprints and permissions information is available at http://www.nature.com/reprints

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afﬁliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modiﬁed the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence,unlessindicatedotherwisein acredit lineto thematerial. If material isnotincludedinthearticle’sCreativeCommonslicenceandyourintended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/bync-nd/4.0/.

© The Author(s) 2025

1Department of Gastrointestinal Surgery, Afﬁliated Hospital of North Sichuan Medical College, Nanchong, Sichuan, China. 2School of Electronics & Electrical Engi-

neering,UniversityofGlasgow,Glasgow,Scotland,UK.3SchoolofInformation&CommunicationEngineering,UniversityofElectronicScience&Technology,Chengdu, Sichuan,China.4SchoolofBasicMedicineandSchoolofForensicMedicine,NorthSichuanMedicalCollege,Nanchong,Sichuan,China.5DepartmentofStomatology, North Sichuan Medical College, Nanchong, Sichuan, China. 6Department of Biomedical Engineering, North Sichuan Medical College, Nanchong, Sichuan, China.

7DepartmentofAesthesia,NorthSichuanMedicalCollege,Nanchong,Sichuan,China.8DepartmentofGeriatrics,TheSecondClinicalMedicalCollegeofNorthSichuan Medical College, Nanchong Central Hospital, Nanchong, Sichuan, China. 9Department of General Surgery, and Institute of Hepato-Biliary-Pancreas and Intestinal Disease, AfﬁliatedHospitalofNorthSichuanMedicalCollege, Nanchong, Sichuan,China.10DepartmentofRespiratoryand CriticalCareMedicine, AfﬁliatedHospitalof North Sichuan Medical College, Nanchong, Sichuan, China. 11Department of Critical Care Medicine, Afﬁliated Hospital of North Sichuan Medical College, Nanchong, Sichuan, China. 12Department of Foreign Languages and Culture, North Sichuan Medical College, Nanchong, Sichuan, China. 13These authors contributed equally: YangQiao,XinyuXu,XiangyuLi,MengyanXiao,AijiaKang,DunruiWang,YueshanPang,XingXie,SijunXie,DachenLuo,XuefengDing,ZhenglongLiu,YingLiu.14These authors jointly supervised this work: Yixing Ren, Jiebin Xie.

e-mail: yixingren@nsmc.edu.cn; xiejiebin84@126.com

