Scientometrics (2023) 128:3473–3506 https://doi.org/10.1007/s11192-023-04690-w

Impacts of inter‑institutional mobility on scientific performance from research capital and social capital perspectives

Yitong Chen1 · Keye Wu1 · Yue Li1 · Jianjun Sun1

Received: 23 August 2022 / Accepted: 9 March 2023 / Published online: 18 May 2023 © Akadémiai Kiadó, Budapest, Hungary 2023

##### Abstract

Industries have gradually relied on basic scientific research and discovery in academia to produce innovative products and enhance innovation capabilities. This division of labor has promoted researchers’ mobility from academic research institutions to enterprises (aca. ind mobility), especially in the artificial intelligence domain. However, limited research has been conducted to explore the impact of aca.ind mobility on the researchers’ performance in this domain. The findings elucidate the motivation and necessary conditions of researchers’ aca.ind mobility in this domain based on bibliometric methods, propensity score matching (PSM), and regression analysis methods. The results also demonstrate the impact of this type of mobility on researchers’ performance compared to mobility between academic research institutions (aca.aca mobility) from a research capital perspective and social capital perspective. The results of this paper indicate that researchers in this domain need to accumulate more research publications and establish collaborative relationships with corporate researchers and high-impact researchers within a short academic age timeline to maximize the opportunities for aca.ind mobility. Furthermore, compared with the aca.aca mobility, which allows researchers to accumulate more research capital, aca. ind mobility seems to be more conductive to the accumulation of social capital. The aca. ind mobility not only helps researchers expand the scale of their scientific collaborative networks, but also establish collaborative relationships with more high-impact researchers. This research can help researchers plan their own career development. The results also provide suggestions for policy makers to formulate policies on talent recruitment, structure optimization, and evaluation of knowledge and innovation systems.

Keywords Scientific mobility · Scientific performance · Knowledge transfer and dissemination · Propensity score matching (PSM)

* Jianjun Sun sjj@nju.edu.cn Yitong Chen 18645686190@163.com

1 School of Information Management, Nanjing University, Nanjing, China

1 3

Vol.:(0123456789)

## Introduction

Researchers, as highly skilled human resources, have become the fundamental drivers for institutions to conduct scientific research and innovation. In particular, researchers have become the most important resources for building innovative and digital economics in some countries and regions (Baruffaldi & Landoni, 2016). The mobility of researchers has gradually become an important way to promote scientific development and innovation and realize knowledge dissemination and exchange between institutions (Baruffaldi & Landoni, 2016; Yue et al., 2020). From a micro perspective, researchers’ mobility is conducive to satisfying their personal research goals, seek advanced scientific equipment, and prestigious colleagues, thereby enhancing their own visibility and ability (Liu & Hu, 2021; Liu et al., 2021). From a macro perspective, researchers’ mobility has become a critical concern for policy makers, because it not only helps

- them make informed decisions about cultivating talent, structure optimization, and policy formulation, but also helps evaluators effectively evaluate countries’ external knowledge and innovation systems (Liu & Hu, 2021; Robinson-Garcia et al., 2019; Yue et al.,


- 2020). Researchers’ mobility has attracted extensive attention from scholars in various


domains, such as sociology, scientometrics, and ecology. Thus, the number of relevant publications has increased significantly (Liu & Hu, 2021; Verginer & Riccaboni, 2020). However, current research has mainly focused on factors that promote the mobility of researchers and the impact of mobility on performance. In addition, relevant research results on researchers’ mobility have developed from national and global perspectives (Xu et al., 2018). However, although existing research have explored the impact of researchers’ mobility on performance from an institutional perspective (Bolli & Schläpfer, 2015; Halevi et al., 2016), research results have mostly been limited to the mobility of researchers among academic research institutions because it is the most common type of mobility. Although enterprises invest fewer resources in basic research, they rely on basic scientific discoveries and research in academia to improve their own productivity and innovation capabilities to generate new products, new industries, and new investment opportunities (Bikard & Marx, 2020). Research-driven innovation in industry has prompted many researchers in academic research institutions to move to enterprises to seek better working conditions and opportunities.

On this basis, compared with the mobility between academic research institutions (aca.aca), mobility of researchers across institutional types (from academic research institution to enterprises, aca.ind mobility pattern) drives knowledge dissemination, interaction, and integration between academic institutions and industry. Given the increasingly common occurrence of this type of mobility, more researchers have explored the impact of aca.ind mobility of researchers. However, the evaluation of performance in the relevant research seems to focus on the institutional level, and to explore the impact of such mobility on the innovation performance of target enterprises (Grimpe & Hussinger, 2013; Kaiser et al., 2018). The research results of them indicate that this type of researchers’ mobility is beneficial to the knowledge and technology transfer and also improves the innovation performance of enterprises. Studies have paid less attention to performance at the individual level. However, the mobility of researchers is often associated with the resource stock of individuals from a research capital perspective (the knowledge and skills of researchers) and social capital perspective (the researchers’ communication and collaboration with others), which help researchers gain

a competitive advantage. In this regard, it is essential to explore the impact of different types of mobility of researchers (aca.aca, aca.ind) on their individual performance.

AI refers to the technology of modeling intelligent behavior based on computer tools to minimize manual intervention (Luo et al., 2017). With the continuous progress of the Internet and computer technology, the development potential of AI has gradually emerged, attracting extensive attention from researchers and practitioners. As an emerging frontier technology, AI has become a national strategy for wide application in various domains, such as natural language processing, machine learning, and medical applications (Lei & Liu, 2019; Niu et al., 2016; Shao et al., 2020). In this process, competition and cooperation have promoted the development of the AI domain, and its rapid development has further consolidated cooperation between institutions (Shao et al., 2020). Researcher mobility in the AI domain is a popular form of such competition and collaboration between institutions, because researchers are gradually becoming one of the important resource advantages to facilitate the development of the AI industry and research. In this regard, researchers transform various AI cutting-edge research outcomes into practical applications with the continuous expansion of its application scale. This process exacerbates researchers’ mobility from academic to industry in this domain (Shao et al., 2020).

However, limited efforts have been made to explore and study the mechanism of researchers’ mobility in the AI domain. Shao et al. (2020) describe researchers’ mobility in this domain based on bibliometric methods. They emphasize that “brain circulation” (i.e., some researchers move from academia to industry and some researchers return to academia) in the AI domain is beneficial for development. However, studies lack an in-depth quantitative analysis of the impact of this type of mobility on researchers’ performance. Gureyev et al. (2020) also claim that the initial talent is the direct reason for researchers to obtain high-performance indicators after mobility, suggesting that researchers with higher work capacity and productivity before moving have better performance after the mobility. Such endogenous factors make it difficult to explore the causal relationship between mobility and research performance. Using the propensity score matching (PSM) method could effectively solve the endogeneity problem.

This paper clarifies the motivation and necessary conditions of aca.ind mobility of researchers to gauge the impact of this mobility on the researchers’ performance compared with aca.aca mobility. Bibliometric analysis methods are also adopted to study the two mobility patterns of researchers. This paper highlights the impact of the two mobility patterns on researchers’ performance from the perspectives of research capital and social capital based on the regression analysis method. In addition, this paper chooses the AI domain for further research, and weakens the influence of endogeneity of the regression results based on the PSM method.

This paper is divided into seven sections. The hypotheses are proposed in Sect "Research hypothesis". Section "Methods" sets up the variables and presents the model framework. Section "Data source and preprocessing" introduces the data source and processing of this paper. The quantitative research results are displayed in Sect. "Results". The discussion of this paper is presented in Sect. "Discussion", and Sect. "Conclusion" concludes this paper.

## Research hypothesis

Scientific literature is the most intuitive tool to reflect scientific endeavors (Verginer & Riccaboni, 2021). Research have increasingly conducted quantitative analyses on the mobility behavior of researchers from the perspective of bibliometrics based on scientific

Table 1 Description of the sample

Variables N Mean Var S.D Min Max

aca.aca 9950 0.721 0.201 0.448 0 1 aca.ind 9950 0.218 0.171 0.413 0 1 ind.ind 9950 0.061 0.057 0.238 0 1 ind.aca 9950 0.050 0.047 0.217 0 1 gender 9950 0.902 0.089 0.298 0 1 pre.aca.age 9950 6.147 22.406 4.734 1 38 pre.coauthors 9950 5.851 77.773 8.819 0 157 pre.ind.coauthors 9950 1.143 8.514 2.918 0 78 pre.inf.coauthors 9950 1.449 5.594 2.365 0 39 pre.pubs 9950 3.573 42.233 6.499 1 143 post.aca.age 9950 8.889 62.631 7.914 1 49 post.pubs 9950 7.491 189.258 13.757 1 190 post.correspond.pubs 9950 3.327 84.338 9.184 0 153 post.coauthors 9950 13.750 434.179 20.837 0 414 post.inf.coauthors 9950 1.820 15.395 3.924 0 77

literature (Robinson-Garcia et al., 2019). In addition to obtain more lucrative economic rewards, researchers have two other important purposes for choosing to move: to obtain better research equipment and opportunities, and to work with more prestigious colleagues to improve their work progress (Liu & Hu, 2021; Robinson-Garcia et al., 2019). Both purposes help them accumulate research capital and social capital. In this regard, quantity and quality of scientific publications and collaboration are two important criteria to measure talent mobility performance from the perspectives of research capital and social capital (Zhao et al., 2020). Therefore, this paper measures the performance of researchers’ aca.aca and aca.ind mobility from these two perspectives. As shown in Table 1 in Sect."Benchmark regression analysis" , the sample sizes of mobility from enterprises to academic research institutions (ind.aca) and mobility between enterprises (ind.ind) are too small to draw convincing and general conclusions in the regression model. Therefore, these two types of mobility are not included in the subsequent assumptions and regression analysis.

Existing research results have shown that researchers’ mobility has a positive impact on the generation, accumulation, and transfer of tacit knowledge and is also beneficial to establish collaborative relationships among scientists (Gureyev et al., 2020). Considerable research has evaluated the scientific research performance after researcher mobility from a research capital perspective. Payumo et al. (2018) contend that domestic mobility of scientists brings about better research results, while their international mobility leads to more publications. Halevi et al. (2016) argue that the mobility between two institutions within a single country can have a positive impact on the number of publications of researchers, while cross-border mobility does not. However, Momeni et al. (2022) find that the international mobility is positively associated with their scientific outcomes. Bolli and Schläpfer (2015) explain the influence of mobility on scholars’ research performance based on their own capability and the prestige of the institution they belong to. In addition, the purpose of researcher mobility is to improve the match between researchers and the target institution (Jovanovic, 1979; Topel & Ward, 1992). Researchers are inclined to accept new job opportunities when the improvement in the research environment caused by mobility can offset the cost of relocation (Bolli & Schläpfer, 2015). At the same time, mobility can expose

researchers to the ideas of new colleagues (Bäker, 2013; Hoisl, 2007). The combination of these ideas with their prior knowledge and skills helps them to arrive to new insights (Bolli & Schläpfer, 2015; Katz & Martin, 1997). A better match with the target institution may allow researchers to have more opportunities and better conditions to conduct their own research. In this process, the probability that the researcher publish literatures as a corresponding author may increase after aca.aca mobility. Zhao et al. (2020) also reached a similar conclusion. In conclusion, we propose Hypothesis 1:

- H 1 The aca.aca mobility of researchers has a positive impact on the accumulation of their research capital.

- H 1.1 The aca.aca mobility of researchers is conductive to an increase in their number of publications.
- H 1.2 The aca.aca mobility of researchers is conductive to an increase in the number of publications as corresponding authors.


Existing research has also explored the impact of the aca.aca mobility of researchers on their performance from a social capital perspective. Jonkers and Tijssen (2008) find that overseas experience is conductive to the accumulation of scientific social capital. They suggest that researchers’ overseas mobility experiences increase the number of their copublications and further help them to expand their research collaborative networks. Extant research also suggests that scientists’ international mobility helps them participate in international projects more frequently, which helps them identify foreign collaborators and publish more publications in more influential journals in this process (Scellato et al., 2012). The mobility between academic research institutions can also provide more opportunities for researchers to collaborate with high-impact researchers. Based on these research results, we propose Hypothesis 2:

- H 2 The aca.aca mobility of researchers has a positive impact on the accumulation of social capital.


- H 2.1 The aca.aca mobility of researchers is conductive to more collaborators.
- H 2.2 The aca.aca mobility of researchers is conductive to more high-impact collaborators.


In contrast to aca.aca mobility, the aca.ind mobility of researchers may not be conductive to the accumulation of research capital. An academic research institution is a research unit with clear research directions and tasks. However, when researchers move to an enterprise, they may fine-tune the direction and purposes of their research, which may result in a reduction in the number of publications of them. Nevertheless, there are advantages. Shao et al. (2020) claim that in the process of knowledge moving from academia to industry, enterprises acquire cutting-edge technologies, and researchers may turn their own research results into products. In this process, it may also reduce the number of publications of researchers. van Rijnsoever et al. (2008) reach a similar conclusion. In addition, scientific research stars are often the ones who move from academic research institutions to enterprises (Bikard & Marx, 2020). They may not need to have a long research career, but they may already be budding or influential in their field. Enterprises recruit researchers who

have achieved certain achievements to undertake the responsibility of transforming scientific knowledge into practical applications in a new or existing innovation teams. Changes in research goals and requirements have resulted in a reduction in the number of scientific publications, which have also resulted in a reduction in the publication number as corresponding author. Therefore, we propose Hypothesis 3:

- H 3 The aca.ind mobility of researchers has a negative impact on the accumulation of research capital.

- H 3.1 The aca.ind mobility of researchers is not conductive more publications.
- H 3.2 The aca.ind mobility of researchers is not conductive more publications as corresponding authors


Scientists move to enterprises to seek possible resources that they have not been exposed to before (Barney, 1991). In this process, researchers combine their academic background with advanced equipment, financial resources, and high-quality partners provided by enterprises to improve their research capabilities and quality (Edler et al., 2011). Mobility seems to be an effective way to achieve these purposes by expanding their research social network and building quality partnerships. Through aca.ind mobility, researchers focusing on similar topics exchange knowledge in the network because they share tacit knowledge, nurture new knowledge, and advance innovation (van Rijnsoever et al., 2008). Furthermore, relational capital is basic assets of firms (Welbourne & Pardo-del-Val, 2009). Firms place a high value in relational capital because they incline to solve complex problems through collaboration (Shang et al., 2006; Welbourne & Pardo-del-Val, 2009). In this process, the disciplinary boundaries of members are weakened by close collaboration. Thus, aca.ind mobility may also have an advantage in helping researchers to accumulate collaborators in different research directions compared with researchers’ aca.aca mobility. Therefore, we propose Hypothesis 4:

- H 4 The aca.ind mobility of researchers has a positive impact on the accumulation of social capital.


- H 4.1 The aca.ind mobility of researchers is conductive to more collaborators.
- H 4.2 The aca.ind mobility of researchers is conductive more high-impact collaborators.


## Methods

This section describes the variables and introduces PSM method and the framework for the regression models used in this paper.

### Variables

Scientific mobility can impact research capital and social capital (Gureyev et al., 2020). Research capital refers to the knowledge and skills of researchers. After the mobility, researchers experience changes in the degree of mastery and understanding in their

discipline-related literatures and research methods, thus affecting the quantity and quality of their subsequent research results. Social capital represents the researchers’ communication and collaboration with others. After the mobility, researchers may experience changes in their ability to obtain necessary information from colleagues, which affects the number of subsequent collaborators and collaborative publications (Gureyev et al., 2020). Since these two important factors affect researchers’ careers, they are often used as indicators to measure the mobility performance of researchers in relevant scientific research (Murakami, 2014; Trippl, 2013). Therefore, this paper evaluates the individual research performance of researchers after mobility from the perspectives of research capital and social capital, respectively.

The number of publications a researcher produces is one of the most commonly used basic indicators of researcher performance (Halevi et al., 2016; Verginer & Riccaboni,

- 2021). As collaboration has become one of the most common forms in which scientific publications are presented, it also become a common way to judge the contribution an author makes to the publications, based on the byline position of an article (Grácio et al., 2020; Mattsson et al., 2011). Specifically, the corresponding author, as the main contributor to the research, is regarded as an effective proxy for scientific leadership (Grácio et al., 2020). Therefore, compared with the indicator of the number of publications, the number of publications as the corresponding author can better represent a researcher’s position and importance in scientific groups. Furthermore, extensive research has explored the impact of scientific mobility on the researchers’ collaboration (Liu & Hu, 2021). They claim that mobility can expand a researcher’s social network to further enhance their creativity and influence. Therefore, from the above two perspectives, this paper selects the overall number of publications and the number of publications as corresponding author as proxies for research capital. In addition, we use the number of coauthors and the number of high-impact coauthors as proxies for social capital to measure the research performance after scientific mobility.


Citation count is one of the most commonly used metrics to measure a scientist’s influence (Garfield & Merton, 1979). It is based on the underlying logic that if a given individual publishes breakthrough research results, it will receive citations from others. The more citations, the greater the impact (Feitelson & Yovel, 2004). Citation counts are therefore often used to rank individual researchers, institutions and countries. In the early of this century, Clarivate Analytics (formerly Thomson Reuters) identified a list of highly cited researchers (HCR) based on the citation counts of journal articles and reviews in nature and social science domains over a period of about 20 years (Bornmann et al., 2017; Martinez & Sá, 2020). The top 1% of most cited literatures in a specific discipline are screened out and corresponded to the researchers (Bornmann & Bauer, 2015; Martinez & Sá, 2020). The more highly cited literatures belonging to a researcher, the higher their ranking in a specific discipline (Bornmann et al., 2017). Afterward, this list is updated continuously as it is applied to different scenarios and methodological rules (Must, 2020).

Referring to the above classification and ranking methods, this paper confirms the number of researchers in top 1%, 5% and 10%, which account for 30.1%, 62.4% and 77.8% of total, respectively. Given the limitation of the total sample size, the small scope of high-impact researchers is not conductive to subsequent analysis. Therefore, we expand the threshold to 10% in this paper and identify them as high-impact researchers in this domain. Descriptions of the four dependent variables in this paper are described below.

#### Dependent variables

Post.pubs represents the number of publications of researchers after mobility. The number of literatures is a common indicator of research performance from the perspective of research capital. Considering the impact of mobility on research performance, we adopt the number of publications after mobility as a proxy for performance.

Post.correspond.pubs is the number of publications of researcher as the corresponding author after mobility. The number of publications of researchers as the corresponding author can distinguish their research contributions to further explore their research performance.

Post.coauthors represents the number of coauthors after mobility. When researchers move to a new institution, new colleagues will have the opportunity to become their collaborators. New collaborators broaden the researchers’ social circle, and their collaborators become potential collaborators of this researchers (Kong et al., 2019; Liu & Hu, 2021). These new opportunities facilitate research exchange among researchers. The increase in collaboration pushes researchers to break the generalized friendship paradox, thereby making researchers more dominant in their social network than others (Kong et al., 2019). In addition, a researchers’ dominance in a collaborative network can affect their citation counts (Sarigöl et al., 2014). The increase in the number of citations (one of the indicators for evaluating a scholars’ influence), also increases the visibility of the scholars’ future work.

Post.inf.coauthors is the number of high-impact coauthors after mobility. Based on the six-degree separation theory and “Bacon” theory (derived from the “Erdos number”), Kong et al. (2019) conclude that as the number of collaborators increases, the researchers’ Bacon number decreases from 5.36 to 3.5 on average. It means that more collaboration can shorten the distance between researchers and “Bacon researchers (represents influential researchers in the scientific research collaborative network)”. At the same time, more collaboration has also increased the importance and influence of the researchers’ social circle. Furthermore, the preferential attachment principle in scientific research collaborative network suggests that a researcher is more likely to collaborate with researchers with more collaborators than with fewer collaborators. High-impact researchers in collaborative networks are generally more likely to attract more collaborators due to their outstanding performance and higher ranking in social circles (Kong et al., 2019; Zhang et al., 2018). Therefore, the collaboration between scholars and high-impact researchers is easier to narrow the distance between the two in the collaboration network, and help scholars to obtain more potential collaborators, expand the social circle, and further enhance their importance in the network.

#### Independent variables

In the current knowledge economy, science has an increasingly profound impact on innovation, especially in knowledge-intensive industries that continue to grow (Arvanitis et al., 2011). The industrial sector benefits from the scientific knowledge generated by the academic sector and thus enhances their ability to develop new products and technology innovations (Grimpe & Hussinger, 2013). This knowledge and technology exchange model not only strengthens the interaction and collaboration between academic and industrial sector, but also drives the transfer of related human and material resources. Researchers’ mobility

is one of the main forms of human resource transfer. However, the further interaction of knowledge and technology promoted by the mobility of researchers has a lag period to some degree (Grimpe & Hussinger, 2013; Kaiser et al., 2018). Researchers need time to integrate into the new environment after a move, and the target institutions need time to accept and absorb the mobile researchers. Therefore, it is important and necessary to assess the impact of researchers’ mobility on performance.

Considering the direction of the mobility, this paper divides the mobility of researchers between academic and industrial sectors into four variables, each of which is a binary variable. It takes the value 1 when mobility occurs, and 0 otherwise. The variables are described as follows:

Aca.aca refers to the mobility of researchers from one academic research institution to another. It is the most common form of mobility in the scientific field.

Aca.ind represents when researchers move from academic research institutions to enterprises. Researchers with work experience in academic research institutions can promote the dissemination and diffusion of knowledge to enterprises in a formal or informal way through mobility (Grimpe & Hussinger, 2013).

Ind.ind is the process of mobility of researchers from one enterprise to another. Both of aca.aca and ind.ind modes are the mobility among the same type of institutions.

Ind.aca is the mobility of researchers from enterprises to academic research institutions.

#### Variables used for matching

To estimate the propensity scores between the two sets of variables, this study uses for matching (aca.aca, aca.ind), a series of observable characteristics that affect both the treatment and control group are selected as variables of matching and brought into the regression model (Roman & Popescu, 2014).

Gender of the researcher is a key variable affecting their mobility and research performance (Aceituno-Aceituno et al., 2018; Baker et al., 2019) in many previous studies. Therefore, this paper selects this variable as one of the variables of matching. Researchers’ gender is a binary variable; the value is 1 when the researcher is male and 0 otherwise.

Pre.aca.age can be expressed by how long researchers engage in scientific research activities before mobility. Academic age is one of the important variables associated with researcher’s performance (Kwiek & Roszka, 2022). There are two ways of calculation of academic age, including the time elapse from the first publications of researchers and the time elapse from obtaining a doctorate degree (Chan & Torgler, 2020; Kwiek & Roszka, 2022; Savage & Olejniczak, 2021; Simoes & Crespo, 2020).

This paper chooses the publication numbers as one of the key indicators to measure the researchers’ performance. We believe that the publications of researchers during their student period also belong to the early scientific accumulation of them. Compared with a simple study of the post-employment of scientific stage, research based on the time periods after the first publication appear to provide the full picture of researchers’ career. In this regard, this paper adopts the time elapsed from the first publication as the proxy of researchers’ academic age. It is divided into two stages with the mobility as a critical point in this paper.

Pre.coauthors represents the number of coauthors before the researcher moves. A researcher’s collaborative network will change accordingly when they move. The scientific research social network in which a scholar is located before mobility will have a certain impact on their mobility behavior (Singh et al., 2021), and the number of collaborators

is an important indicator in the analysis of a research collaboration network (Kong et al., 2019; Liu & Hu, 2021). Therefore, this paper chooses coauthors before the move as one of the variables of matching.

Pre.pubs refers to the number of publications of researchers before the mobility. The number of publications has been an effective indicator to measure the scientific research performance of researchers (Zhao et al., 2020). In addition, the accumulation of scholars’ previous research results may become one of the factors affecting their future research production performance (Wu et al., 2022). To better control for the influence of the number of publications of researchers before the mobility on their research performance, we add this factor as one of the variables into the matching and regression model for the further analysis.

Pre.ind.coauthors refers to the collaborators with enterprise working experience among all the collaborators before the mobility. Collaborating with researchers with enterprise working experience before scholars’ mobility may have more opportunities to expand corporate social networks. They may be closer to the opportunities of mobility than researchers who have not been exposed to corporate researchers, and may have a greater probability of mobility to enterprises. Therefore, this paper chooses pre.ind.coauthors to control for this selection bias.

Pre.inf.coauthors refers to the number of high-impact collaborators of researchers before the mobility. Scholars establish collaborative relationships with more high-impact researchers before they move, the closer they seem to be to influential nodes in the scientific research social network. It seems that the position they occupy in the network is also more important. When recruiting employees, the impact of researchers also seems to be one of the important indicators for enterprises to consider. Therefore, researchers who are more important or influential in the network are more likely to be discovered and mined by enterprises. Therefore, this variable is also selected by this paper to control for the selection bias.

#### Control variable

Post.aca.age has an influence on the dependent variable in the regression model. It is expressed as the time interval for researchers to engage in scientific research activities from the time of the move to the present. In addition to the mobility factor, the number of publications and collaborators are also directly affected by the post.aca.age factor. Therefore, this paper controls the time factor of researchers engaged in scientific research activities after the mobility, to better explore the influence of independent variables on dependent variables. The specific calculation formula of this indicator is: (data cut-off year-the flow year + 1).

### Model

The purpose of the matching techniques is to estimate the specific influence of the independent variable on the dependent variable when other variables remain consistent under control (Bouoiyour & Miftah, 2015). The PSM method is different from the traditional heterologous matching method, which condenses the features of multiple dimensions into propensity score factors, and then matches the samples with the control samples that have similar characteristics from multiple dimensions. The results can be drawn from a comparison of the two groups of samples. To explore the influence of the aca.ind mobility on researchers’ performance

compared to aca.aca mobility, this paper uses the PSM method to control the consistency of other variables, and then adopts regression analysis to evaluate researchers’ performance based on the matched data.

The calculation of the propensity score is the key to the matching process. This article adopts the open source R package MatchIt for matching. The process is as follows. First, logistic binary regression is used to calculate the regression coefficient of variables of matching, as shown in formula (1), where ﬂowi is the independent variable. If the variable is in the treatment group, the value is 1, and 0 otherwise; xj represents variables of matching; and j represents the regression coefficient of the corresponding variables of matching. Second, based on the regression coefficient obtained by formula (1), the logit model is adopted to estimate the propensity score (the logit model is used by default in the MatchIt package to calculate the propensity score), which is described as formula (2). The other variables are consistent with formula (1), and h(xi) represents the functional relationship between the variables of matching and independent variables, which is formula (1)

ﬂowi = 1xi1 + 2xi2 + ⋯ + dxid + i (1)

Pr ﬂowi = 1 xi = e h(xi)∕1 + e h(xi) (2)

The two dependent variables selected in this paper are all discrete variables. Based on the matched data, this paper uses regression analysis to explore the impact of aca.ind mobility on scholars’ research performance compared to aca.aca mobility. Therefore, Poisson regression and negative binomial regression could be selected for estimation (Yin & Zong, 2022). However, the Poisson regression model is not suitable for variables that are too discrete, and the criterion is whether the variance of the variable is equal to the expectation. Table 1 shows that the mean and variance of post.pubs, post.correspond.pubs and post.inf.coauthors are not equal. Therefore, the subsequent analysis in this paper adopts the negative binomial regression model.

In the model, the aca.aca and aca.ind mobility of researchers is the main influencing factor. Taking each scholar as a research unit, their gender, academic age, publication numbers and collaborator information before mobility are all endogenous factors that affect independent variables, so it is necessary to control the impact of these variables on research performance. Therefore, these variables are adopted as multidimensional features for PSM, and they also become variables of matching in the model. In addition, the researchers’ performance after the mobility (such as the number of publications and influential collaborators) is directly related to the accumulation of time. Therefore, this paper incorporates post.aca.age into the model as a control variable. Based on this framework, we present the negative binomial regression model constructed in this paper as follows:

performancei = + ∙ ﬂowt + ∙ Xi + i + (3)

where i represents the ith researcher, t refers to the type of flow, ranging from 1 to 3; Xi is a vector of variables for matching; and i represents the control variables. The framework of the regression model is shown in Fig. 1.

![image 1](Chen et al._2023_Impacts of inter-institutional mobility on scientific performance from research capital and social c_images/imageFile1.png)

- Fig. 1 Regression model framework


## Data source and preprocessing

The Microsoft academic graph (MAG) database is a massive academic dataset generated by Microsoft Research (Luo et al., 2018; Sinha et al., 2015). It processes online publications using natural language processing technology and constructs a heterogeneity graph based on connections between the entities (Wang et al., 2020). As an open source dataset, MAG covers conference proceedings as well as academic journals. AI papers are often published in conference proceedings (Frank et al., 2019). Therefore, the MAG database is an appropriate data source for this paper.

Researcher mobility seems a more common phenomenon among academic stars in certain fields, and research on their mobility and research performance is also a common focus of discussion among scholars (Bikard & Marx, 2020). To obtain information on the mobility of well-known scholars in the AI domain, this paper extracts 91,557 publications from the MAG database from top international academic journals and conferences in the AI domain1 as recommended by the Chinese Computer Society in 2019. Each publication contains 20 fields of information, including the author’s ID (the identification of the author in the MAG database), the author’s name, and the institutions to which the author belongs. Because the research target of this paper is the mobility of researchers between different institutions, it is necessary to identify the research unit from the literature for each researcher. Thus, we attempt to disambiguate author names.

This paper adopts a two-stage author name disambiguation framework to solve the problem of author name ambiguity. The disambiguation work in the first stage is based on

- 1 We extracted relevant studies from 4 top international academic journals and 7 top international academic conferences in the MAG database. The 4 academic journals are Artificial Intelligence (AI), IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), International Journal of Computer Vision (IJCV), Journal of Machine Learning Research (JMLR), and the 7 academic conferences are AAAI Conference on Artificial Intelligence (AAAI), Annual Conference on Neural Information Processing Systems (NeuriPs), Ammual Meeting of the Association for Computational Linguistics (ACL), IEEE Conference on Computer Vision and Pattern Recognition (CVPR), International Conference on Computer Vision (ICCV), International Conference on Machine Learning (ICML), and International Joint Conference on Artificial Intelligence (IJCAI).


the authors’ information provided in the MAG database, including collaborators’ information and institutional information. In the second stage, this paper crawls the data based on the application programming interface (API) provided by ORCID’s official website, to associate the external data with local data and use ORCID as the authors’ unique identifier for author disambiguation. Asian names are difficult to distinguish. Drawing on the verification method of Zhang and Al Hasan (2017) for the disambiguation process, we validate the results for researchers with “Asian names” that appeared more frequently but are more difficult to distinguish. We select 15 of the researchers with “Asian names” from those with a high number of publications for validation. The reason for selecting researchers with high number of publications is that we determine the mobile information of researchers based on their publications. The higher the number of publications, the greater the impact ambiguity in the authors’ names on our results. The results of test are presented in Table 6 in the Part 1 of Appendix. The results demonstrate that the disambiguation work in this paper has a significant effect on the data.

After solving the author disambiguation problem, we identify 102,022 unique authors from 91,557 publications. The institution information they belonged to is also extracted to further identify the type of institution and the type of mobility. The mobility of researchers between academic (academic research) institutions and industrial (enterprises) institutions is the focus of this paper, so we need to judge whether an institution falls into any of the above types. We extracted institutional information from mobile researchers. After merging and removing duplicates, 3465 institutions are remained for further analysis. Based on the manual annotation (we put the institutions name into search tools such as Wikipedia and Google search to determine its institutional type through manual retrieval), this paper extracts the high-frequency keywords which can be regarded as the proxies of these two institution types (for example, ‘universities’, ‘college’, ‘academic’, ‘academy’, ‘school’ represent academic research institutions; ‘corporation’, incorporation’, ‘company’, ‘inc’ represent industrial institutions). Then, further identification and judgement of institution type is performed based on these keywords. In this process, except for these two types of institutions mentioned above, the remaining institutions are classified as “others” category, including government department, hospitals and so on (which account for 5.8% of the total). We present the part of the classification results in Table 7 in the Part 2 of Appendix section.

Then, this paper arranges the institutions to which each author belongs in chronological order of the publications. The time of the first change of researchers’ institution is the time of their move. We identified 9950 mobile researchers in this process. In addition, based on the time when the mobility first occurred, this paper judges the types of institutions before and after the mobility. After considering the direction of mobility, the 9950 researchers can be divided into four types of mobility: aca.aca mobility, aca.ind mobility, ind.aca mobility, and ind.ind mobility. The last two types of mobility are not included in subsequent regression analyses due to the small sample sizes (the detail description of the reasons is presented in the first paragraph of Sect. "Benchmark regression analysis"). The data preprocessing steps are shown in Fig. 2.

Since we focus on the impact of different types of mobility on researchers’ performance based on the variable setting and model construction, this paper uses the time when mobility occurs as a dividing point to explore the changes in researchers’ performance before and after mobility. Since the gender of researchers cannot be obtained directly from the MAG database, this paper uses an open-source Python package (i.e., gender-guesser) to infer the researchers’ gender based on their given (first) name (Zhao et al., 2021). The gender information of most researchers is confirmed. The proportion of male researchers is

![image 2](Chen et al._2023_Impacts of inter-institutional mobility on scientific performance from research capital and social c_images/imageFile2.png)

- Fig. 2 Steps of data preprocessing


87.6% of total, and the proportion of female is only 9.86% of total. Considering that it is difficult to distinguish researchers’ gender based on some names, we also obtain some null values in this variable, which account for 2.57% of the total. Taking the prior distribution of gender into account to ensure that the matching and regression results are not affected, we do not discard the null values that account for a small proportion but is needed in the subsequent matching analysis. In addition, there is a high probability that they are the same gender (i.e., male).

## Results

This section starts with a descriptive statistical analysis of the variables. After a simple baseline regression model analysis, the two sets of observations of aca.aca and aca.ind mobility are matched based on the PSM method, and the matching results are brought into the regression model for further analysis.

- Fig. 3 The distribution of flow types


![image 3](Chen et al._2023_Impacts of inter-institutional mobility on scientific performance from research capital and social c_images/imageFile3.png)

### Descriptive statistical analysis of the variables

This paper discusses the impact of different types of mobility on researchers’ performance. Based on the variable description in Sect. "Methods", we obtain four types of mobility, and the distribution of the proportion of mobile researchers in each type of mobility as presented in Fig. 3. In the AI domain, 74.48% of the mobile researchers moved between the same type of institution (aca.aca and ind.ind). Mobility of aca.aca is the highest at 68.72%. The results demonstrate that the researchers’ mobility between academic research institutions is the most common form in the AI domain. Furthermore, 25.52% of all mobile researchers experienced the mobility between different types of institutions (aca.ind and ind.aca). Among them, 20.79% of mobile researchers experience aca.ind mobility in the AI domain. Compared with the ind.aca mobility, the aca.ind mobility of scholars occupy a larger proportion. The possible reasons for this mobility choice of researchers are that they seek resource enhancement to improve their competitive advantage or that they are influenced by the original institutions’ background (the original institution support or constraint their academic research activities) (Barney, 1991; Edler et al., 2011).

To observe the academic age status and trend changes of researchers more intuitively in the AI domain before and after the mobility, this paper presents the distribution characteristics with the academic age of the researchers as the horizontal axis and the number of researchers as the vertical axis, as shown in Fig. 4. The bars in Fig. 4 represent the overall distribution of researchers’ academic age, and the lines display the distribution before and after the mobility, respectively. Overall, the academic age of researchers roughly shows a positive-skewed distribution (the skewness coefficient is 0.254). Most researchers’ academic age falls into the range of 3–20 years, which accounts for 76.31% of total. Researchers (650) with an academic age of 10 are the most. A small proportion of researchers have an academic age less than 3 years or more than 20 years, especially more than 30 years. Furthermore, since the academic ages of most researchers are between 3 and 20 years, regardless of before or after the mobility, the distributions of the academic ages of most researchers are positive-skewed. However, there are still subtle differences in the distribution of these two mobile patterns. We calculate that the average academic age of

![image 4](Chen et al._2023_Impacts of inter-institutional mobility on scientific performance from research capital and social c_images/imageFile4.png)

- Fig. 4 The distribution of researchers’ academic age at different stages


researchers in the AI domain is 15 years, while the average academic age of researchers before the mobility is 6 years and after the mobility is 9 years. It suggests that researchers in this domain are more likely to be mobile early in their careers. Similar statistics are shown Fig. 4. (There are more researchers before mobility with academic age within 10 years than researchers after mobility; there are more researchers after mobility with academic age not less than 20 years than researchers before mobility.) Before the mobility, a large proportion of researchers had a shorter academic age, and the distribution curve after the mobility is flatter.

This paper also describes the collaboration of researchers in detail before the mobility. This paper presents the distribution and proportion of researchers’ collaborators in four different types of mobility modes in Fig. 5. As we know, the aca.aca mobility pattern has a larger share of all mobile researcher, as shown in Fig. 3. Therefore, it is quite reasonable that mobile researchers in this group have more pre.coauthors than others due to the large base size. However, the number of pre.ind.coauthors of aca.aca mobile researchers is lower than mobile researchers in aca.ind group. Researchers who move out of enterprises are more likely to collaborate with ind-coauthors. Therefore, it is not surprising that pre.ind.coauthors have a higher proportion in the ind.aca and ind.ind patterns. However, the proportions of pre.ind.coauthors in the aca.aca and aca.ind patterns are quite different: 11.70% and 24.94%, respectively. In addition, the proportion of pre.inf.coauthors in the aca.ind pattern is also the highest compared to the other patterns. The results show that establishing collaborative relationships with enterprise collaborators may be one of the important factors in facilitating the aca.ind mobility of researchers. In other words, collaboration with corporate researchers seems to provide more possibilities and opportunities for researchers to move to enterprises.

### Benchmark regression analysis

After a basic descriptive statistical analysis, this paper briefly describes the variables mentioned in Sect. "Variables". Table 1 presents the sample size, mean, variance, standard deviation, and the minimum and maximum values of these variables. Table 1 shows that

![image 5](Chen et al._2023_Impacts of inter-institutional mobility on scientific performance from research capital and social c_images/imageFile5.png)

- Fig. 5 The distribution of coauthors before mobility


the outward mobility from academic research institutions is the main mobile direction of researchers in the AI domain. The researchers’ mobility information we extracted is based on their publications in top journals and conferences. As can be seen from the Fig. 3, these researchers are mainly concentrated in academic research institutions rather than enterprises (because 68.72% researchers still belong to the aca.aca mode of mobility). It results in a relatively small sample size of corporate researchers that we can obtain. The results of regression analysis based on the too small samples size have a weak statistical significance. In addition, this paper mainly focuses on the differences in performance of researchers under the two mobility modes (which are aca.aca and aca.ind mobility). Therefore, the mobility of corporate researchers is not included in the subsequent regression analysis.

Furthermore, from Table 1, the mobility of male researchers seems to be more common in the AI domain than female researchers. The mean of researchers’ academic age before (6.147) and after (8.889) mobility also confirms our conclusion that researchers tend to move early in their careers. In addition, the average number of publications of researchers after they move (7.491) is twice as high as before (3.573). Similar conclusions also appear in the changes in the number of collaborators before (5.851) and after researchers’ mobility (13.750). It seems to indicate that inter-institutional mobility not only improves the research capacity of researchers but can also enrich their collaborative networks.

After a brief description of the variables, this paper presents the correlation between variables in the form of a matrix diagram,2 as shown in Fig. 6. The squares where the two variables overlap are marked with their correlation coefficients. The changes in the color of the squares show the difference in the strength of the correlation between the two variables. The blue in the scale axis on the right of Fig. 6 represents a positive correlation between the variables, while the red refers to a negative correlation. As seen in Fig. 6, pre.coauthors, pre.inf.coauthors, pre.ind.coauthors and pre.pubs are positively correlated with pre. aca.age, but negatively correlated with post.aca.age. It seems to suggest that researchers’

- 2 We adopt the default calculation method of “cor function” in R language to calculate the correlation coefficient between variables, which is Pearson correlation.


![image 6](Chen et al._2023_Impacts of inter-institutional mobility on scientific performance from research capital and social c_images/imageFile6.png)

- Fig. 6 Correlation of variables


research capital and social capital gradually accumulate with their academic age. Furthermore, the aca.aca mobility is negatively correlated with pre.coauthors, pre.ind.coauthors, pre.inf.coauthors, pre.pubs and pre.aca.age, but positively correlated with post.aca.age. It demonstrates that the accumulation of previous scientific research capabilities, influence, and cooperative relationships may reduce the motivation of researchers’ aca.aca mobility, but such mobility could prolong their academic age. However, the aca.ind mobility is the opposite. The accumulation of early research capital and social capital encourages these researchers in academic research institutions to move to enterprises to seek higher income and better resources and opportunities, but it limits their time and efforts in scientific research activities.

After analyzing the correlation between variables, we conduct regression analysis for the whole samples to compare the differences of researchers’ performance in aca.aca mobility and aca.ind mobility modes. Since the sample size of corporate researchers’ mobility (ind.aca and ind.ind mobility patterns) is too small to be statistically significant for regression analysis, they are not included in the subsequent regression analysis. The results of the benchmark regression model are shown in Table 2. Table 2 demonstrates that the aca.aca mobility is positively associated with post.correspond.pubs, while it is negatively correlated with post.coauthors and post.inf.coauthors. In addition, the aca.ind mobility pattern is associated with post.correspond.pubs negatively, and it is linked to post. coauthors and post.inf.coauthors positively. These findings demonstrate that the aca.aca mobility may not associated with the number of publications after researchers’ mobility,

pre.aca.age− 0.049***− 0.049***− 0.007− 0.008*− 0.040***− 0.040***− 0.046***− 0.046***

pre.coauthors− 0.018***− 0.018***− 0.018***− 0.018***− 0.004− 0.004− 0.035***− 0.036***

(Intercept)0.992***1.028***− 1.010***− 0.801***2.119***1.999***− 0.150*− 0.406***

aca.ind− 0.033− 0.252***0.121***0.272***

pre.pubs0.074***0.074***0.101***0.103***0.047***0.047***0.045***0.045***

pre.inf.coauthors0.098***0.098***0.100***0.104***0.092***0.091***0.194***0.192***

post.aca.age0.074***0.074***0.121***0.120***0.042***0.042***0.067***0.067***

pre.ind.coauthors− 0.006− 0.008− 0.030**− 0.040***− 0.0040.0010.0120.021**

gender0.073*0.072*0.0770.0730.064*0.066*0.116*0.123*

N99509950995099509950995099509950

(1)(2)(3)(4)(5)(6)(7)(8)

Variablespost.pubspost.correspond.pubspost.coauthorspost.inf.coauthors

aca.aca0.0380.202***− 0.122***− 0.253***

‘.’p<0.1, ‘*’p<0.05, ‘**’p<0.01, ‘***’p<0.001

Benchmark regression modelTable 2

![image 7](Chen et al._2023_Impacts of inter-institutional mobility on scientific performance from research capital and social c_images/imageFile7.png)

- Fig. 7 The description of the matching procedure


but it is beneficial to increases the publication numbers of researchers as a corresponding author. The aca.ind mobility seems to help researchers expand their academic collaborative network while providing more opportunities for them to collaborate with high-impact collaborators. Furthermore, pre.pubs and pre.inf.coauthors are positively correlated with research performance after researchers’ mobility, indicating that researchers who publish more publications and increase collaboration with high-impact collaborators before mobility are more like to improve their research performance after mobility. In addition, post. aca.age is also positively linked with their research performance after mobility.

### Propensity score matching

This paper adopts the PSM method to screen the observations. After deduplication, 9950 mobile researchers are retained for further analysis. This paper classifies these researchers into two categories, including aca.ind and aca.aca of mobility. The inherent differences in performance between mobile and non-mobile researchers may also affect our research results. Therefore, we separately compare the differences in performance between these two types of mobile researchers (aca.aca mobility or aca.ind mobility) and non-mobile researchers based on the PSM. The complete matching process is shown in Fig. 8 of the Part 3 of Appendix. Due to space limitation, the matching results and the corresponding balance checks are also presented in the Table 8 and Table 9 of the Part 3 of Appendix. We

- then further explore the impact of aca.ind mobility on researchers’ performance compared
- to aca.aca mobility. In the following, we only report the first matching results and the balance check.


Among mobile researchers, the aca.ind mobility represents the treatment group, while the aca.aca mobility represents the control group. Then, based on the variables we choose for matching in Sect. "Variables" (which are shown in Fig. 7), we calculate the propensity scores of the control group relative to the treatment group (it represents that the probability that observations in the control group choose the aca.ind mobility when other conditions are consistent) and match them by exact matching method. Finally, 3912 observations are matched successfully in the first matching, including 795 observations in the treatment group and 3117 observations in the control group.

- Table 3 Balance of variables before and after matching Variables Before matching After matching

Means treated Means control Mean diff Means treated Means control Mean diff

gender 0.921 0.892 0.109 0.955 0.955 0.000 pre.aca.age 6.800 5.914 0.184 4.718 4.718 0.000 pre.coauthors 8.730 4.801 0.303 2.728 2.728 0.000 pre.pubs 5.830 2.842 0.283 1.687 1.687 0.000 pre.ind.coauthors 2.177 0.562 0.463 0.452 0.452 0.000 pre.inf.coauthors 2.385 1.125 0.351 0.790 0.790 0.000

- Table 4 The impact on the performance of research capital


Variables Post.pubs Post.correspond.pubs

(1) (2) (3) (4) (5) (6)

treat − 0.123** − 0.128** − 0.094* − 0.240** − 0.232** − 0.176* gender 0.201* 0.251** 0.142 0.215 0.304 0.094 pre.aca.age − 0.078*** − 0.086*** − 0.067*** − 0.057*** − 0.068*** − 0.023* pre.pubs 0.322*** 0.406*** 0.252*** 0.408*** 0.606*** 0.330*** pre.coauthors − 0.218*** − 0.058*** − 0.406*** − 0.123*** pre.ind.coauthors − 0.029 0.054 − 0.207** − 0.034 pre.inf.coauthors 0.228*** 0.123*** 0.354*** 0.165*** post.aca.age 0.063*** 0.107***

- (Intercept) 1.460*** 1.675*** 0.841*** 0.332 0.656*** − 0.919*** N 3912 3912 3912 3912 3912 3912


‘.’ p < 0.1, ‘*’ p < 0.05, ‘**’p < 0.01, ‘***’ p < 0.001

This paper also conducts a balance check for the matching results of the 6 variables, as shown in Table 3. The purpose of PSM is to reduce the difference between the two groups of observations through variable screening. As shown in Table 3, based on the exact matching method, the mean difference between these two groups of variables becomes 0 after matching. Furthermore, expect for the gender variable, the mean of these variables becomes smaller after matching. This result suggests that the distribution of the variables in the treatment group and control group is more balanced after matching, thus somewhat reducing the endogenous difference between them.

### Regression analysis after matching

This sub-section reports the regression analysis results based on the matched data. Tables 4 and 5 present the impact of aca.ind mobility on researchers’ performance compared with aca.aca mobility. Furthermore, we also report the impact of aca.aca mobility and aca. ind mobility on researchers’ performance separately compared with non-mobile researchers, which are shown in Table 10 and Table 11 of the Part 3 of Appendix. The results

- Table 4. The variable is 1 when the researcher is in the treatment group, and 0 otherwise. Based on the matching results, this paper discusses the impact of aca.ind mobility on researchers’ performance compared with aca.aca mobility from the perspective of research capital. The regression results are shown in Table 4. In addition to the researchers’ own characteristics (such as gender and pre.aca.age), model (1) and (4) adds the consideration of the research capital (such as pre.pubs) before the researchers’ mobility to show the impact of aca.ind mobility on their performance. Model (2) and (5) takes the social capital (pre.coauthors, pre.ind.coauthors and pre.inf.coauthors) of researchers into account before the mobility based on model (1) and (4). The results of regression analysis show that the researchers’ performance after mobility has a significant correlation with their post.aca. age. Therefore, model (3) and (6) adds the researchers’ academic age after the mobility into the model as a control variable.

Table 4 demonstrates that aca.ind mobility of researchers has a negative impact on the accumulation of the research capital. From model (1), researchers with shorter academic ages but more publications before the mobility seem to have greater research performance after the mobility (such as more publications and more publications of researchers as corresponding authors after mobility). From model (2), the more collaborators a researcher has before the mobility, the more unfavorable it seems to be for the accumulation of their research capital, whereas establishing partnerships with more high-impact collaborators has the opposite result. From model (3), although aca.ind mobility still has a negative

- Table 5 The impact on the performance of social capital


Variable Post.coauthors Post-inf-aocuthors

(1) (2) (3) (4) (5) (6)

Treat 0.115** 0.047 0.161* 0.301*** 0.171** 0.248* Gender 0.234** 0.137 0.137 0.556*** 0.446** 0.444** Pre.aca.age − 0.044*** − 0.049*** − 0.049*** − 0.066*** − 0.067*** − 0.067*** Pre.pubs 0.161*** 0.163*** 0.169*** 0.168*** Pre.coauthors 0.004 0.016 − 0.102*** − 0.087*** Pre.ind.coauthors 0.058 0.058 0.123* 0.169** Pre.inf.coauthors 0.096*** 0.096*** 0.290*** 0.247*** Post.aca.age 0.036*** 0.037*** 0.053*** 0.053 treat*pre.coauthors − 0.044 − 0.061 treat*pre.inf.coauthors 0.156 treat*pre.ind.coauthors − 0.126

- (Intercept) 2.315*** 1.716*** 1.686*** 0.056 − 0.686*** − 0.701*** N 3912 3912 3912 3912 3912 3912


‘.’ p < 0.1, ‘*’ p < 0.05, ‘**’ p < 0.01, ‘***’ p < 0.001

demonstrate that both aca.aca and aca.ind mobility have a positive impact on researchers’ performance from the perspectives of research and social capital. However, the aca.ind mobility has a weaker impact on the improvement of research capital of researchers than aca.aca mobility, while its impact on the improvement and accumulation of researchers’ social capital is greater than that of aca.aca mobility. The following regression analysis is aimed to further explore the differences in researchers’ performance resulting from these two mobility patterns.

For the matched data, treat is the independent variable in the model, as shown in

impact on the accumulation of the research capital of researchers, the control for the post. aca.age variable somewhat weakens the degree of this impact, indicating that it is a key factor that affects the number of publications of researchers after the mobility.

Table 5 discusses the impact of aca.ind mobility on researchers’ performance from the perspective of social capital. First, when no interaction term is included, the coefficient of the treat variable directly reflects the treatment effects. This result can be understood as the difference in the impact between aca.ind and aca.aca mobility on the researchers’ performance, as shown in models 1 and 4 in Table 5. Models 2 and 5 add the variables reflecting the research capacity (pre.pubs) and cooperation information (pre.coauthors, pre.ind. coauthors and pre.inf.coauthors) of the researchers before the mobility based on the models 1 and 4. The post.aca.age of researchers is also added in models 2 and 5 to control for differences in performance due to differences in the researchers’ own academic age after mobility. Finally, interaction terms between the treat variable and other relevant variables (treat*pre.coauthors, treat*pre.inf.coauthors, treat*pre.ind.coauthors) are incorporated into models 3 and 6 to serve as the subsequent detailed analysis.

Table 5 shows that aca.ind mobility has a positive impact on the accumulation of the social capital of researchers. The accumulation of publications before researchers’ mobility also has a positive impact on the development of their research collaborative network after the mobility. From row 5 in Table 5, it can be seen that the effect of pre.coauthors on post.coauthors is not significant in models 2 and 3. In the models 5 and 6, it even has a significant negative effect on post.inf.coauthors. However, in rows 6 and 7 of models 2, 3,

- 5, 6, pre.ind.coauthors and pre.inf.coauthors have a significant positive effect on the two dependent variables mentioned above. These findings demonstrate that the number of coauthors before aca.ind mobility occurs does not appear to be a key indicator influencing the expansion of social capital after researchers’ mobility. It also indicates that the cooperation with corporate collaborators and high-impact collaborators before aca.ind mobility helps researchers expand the cooperative relationship with high-impact collaborators after mobility.


In addition, although the effect of pre.coauthors on post.coauthors is not significant in model 3, the interaction term treat*pre.coauthors turns the original positive effect into a significant negative effect. It demonstrates that pre.coauthors numbers weaken the impact of aca.ind mobility on the researchers’ performance. In contrast, pre.inf.coauthors show a significant positive effect on post.coauthors. These results indicate that the number of collaborators before aca.ind mobility does not seem to be the key factor for the expansion of their social network after mobility. Too many collaborators may even hinder the expansion of the research network after aca.ind mobility. It may be that high-impact collaborators help researchers accumulate social capital after aca.ind mobility.

## Discussion

In this section, we summarize the research results of this paper from three perspectives, including descriptive statistical analysis, benchmark regression analysis, and matched regression analysis. We then discuss the impact of aca.ind mobility compared to aca.aca mobility on the researchers’ performance in the AI domain.

The descriptive statistical analysis reveals that aca.aca mobility is still the most common type of mobility for researchers in the AI domain, accounting for 68.72% of all researchers in our sample. The mobility of researchers between different types of

institutions accounts for 25.52% of the total, of which aca.ind mobility accounts for 20.79% indicating that aca.ind mobility accounts for a higher proportion of cross-institution-type mobility in the AI domain. Second, the academic age of researchers has a positive-skewed distribution, and the researchers’ academic age are mainly distributed between 3–20 years. However, the average academic age of researchers before the mobility is 6 years and after the mobility is 9 years, which demonstrates that researchers tend to move throughout the early stages of their careers. Finally, under the aca. ind mobility, the proportion of the number of corporate collaborators and high-impact collaborators before the mobility is higher than that of aca.aca mobility. In general, we believe that researchers need to accumulate more corporate or high-impact collaborators in a relatively short period of time before they move, so they have more opportunities to move from academic research institutions to enterprises.

Based on the variable description and analysis results of the benchmark regression model, the mobility of male researchers is more common in the AI domain, accounting for about 90.16% of the sample. The accumulation of research capabilities and cooperative relationships before the mobility may weaken the motivation of researchers to choose aca.aca mobility, but this mobility behavior may prolong their academic age. There is an opposite trend in the aca.ind mobility pattern; that is, researchers need to accumulate some research capital and social capital before the mobility to maximize the opportunity of aca.ind mobility. However, this type of mobility may shorten their academic age. Finally, aca.aca mobility increases the number of publications of researchers as corresponding authors (H1.2 is accepted), and aca.ind mobility is more beneficial to expand their scientific cooperative network. This expansion is not only reflected in the increase in the number of collaborators after the mobility, but also in the improved quality of collaborators. In sum, the accumulation of research capacity and the increase of the corporate and high-impact collaborators before the mobility is conducive to promoting aca.ind mobility of researchers. In addition, compared with obtaining more scientific publications, the aca.ind mobility pattern seems to be more beneficial to researchers to expand their scientific collaborative network, both in the number and quality of collaborators.

The aca.ind mobility can increase the number of publications only in terms of a change in the average number of publications before (3.573) and after (7.491) the mobility. However, this change may be directly due to the differences between the two groups of samples. For example, researchers who can move from academic research institutions to enterprises may have more outstanding research capabilities than others, which can also lead to differences in the number of publications after the mobility. Thus, this paper adopts the PSM method to narrow the endogeneity difference between the two groups of samples, and only observe the effect of aca.ind mobility on the researchers’ performance. It turns out that the regression analysis based on matched samples shows the opposite conclusion. The regression analysis results based on the matched data demonstrate that the aca.ind mobility pattern has a negative impact on the accumulation of the research capital of researchers (H3.1 and H3.2 are accepted). In addition, adding the control variable post.aca.age to the model may somewhat weaken the impact. Furthermore, researchers accumulate more publications and strengthen their collaboration with high-impact researchers in a short period of time before the mobility, which seems to improve their scientific research capabilities and expand their collaborative network after the mobility. In addition, the aca.ind mobility pattern also has a positive impact on the accumulation of the researchers’ social capital (H4.1 and H4.2 are accepted).

## Conclusion

Talent flow has become a main mean to maintain a competitive advantage in modern society with the progress and development of science and technology (Baruffaldi & Landoni, 2016). The mobility of researchers, as a manifestation of talent flow in the field of scientific research, has been widely examined by researchers in various domains due to its advantages in scientific innovation and knowledge dissemination and exchange. The AI domain is no exception. As the main form of competition and collaboration among institutions in the AI field, the mobility of researchers has increasingly attracted the interest of scholars and practitioners.

However, there is limited research on researchers’ mobility mechanisms in this field. Specifically, few studies have discussed the impact of aca.ind mobility on researchers’ individual performance from research capital and social capital perspectives. In addition, existing studies have mainly expounded on researchers’ mobility based on the correlation of research units, but they have not examined the impact of aca.ind mobility on researchers’ performance under the premise of limiting endogenous effects.

Thus, it is valuable to study the interactions between academic research institutions and enterprises and the impact of such interactions on researchers’ performance. It is not only beneficial to study and explore the career prospects of scholars with different work experience, but it also can provide decision support for the formulation of innovation incentive policies.

This paper limits the interference of endogenous factors based on the PSM method, and uses quantitative analysis methods to explore the impact of different types of mobility of AI researchers in terms of their research performance from research capital and social capital perspectives. For both aca.aca mobility and aca.ind mobility, researchers in the AI domain seem to move in the early stages of their careers. The aca.ind mobility of researchers requires that they accumulate more scientific publications and strengthen their collaboration with corporate collaborators and high-impact collaborators to shorten their academic age before moving to industry.

Our findings are somewhat different from van Rijnsoever et al. (2008) who show that scholars may increase their interaction with industry in the later stages of their careers and reduce their cooperation with younger colleagues in their scientific communities. Their conclusion indicates that researchers in academic research institutions need to accumulate certain scientific research capabilities and collaborative relationships before they move from academic research institutions to enterprises. However, this process has clearly been accelerated in the AI domain. Since AI is a high-tech domain with a rapid update rate, it is more suitable for younger researchers’ development. The interaction of science and technology in this domain also seems to be more common and closer than other domains. This domain has higher requirements for young scholars in academic research institutions in this field, which has implications for talent mining and forming policies to promote the interaction and integration of science and technology.

Another key finding is that the aca.ind mobility of researchers in the AI domain is not conductive to the accumulation of research capital. However, it is conductive to the accumulation of social capital. The aca.ind mobility can help researchers expand their scientific collaboration network after the mobility, and to establish cooperative relationships with more high-impact collaborators. This type of expansion of scientific collaborative networks does not appear to be directly and positively affected by the number of collaborators before the mobility. This finding may also verify that researchers in this field are inclined to convert scientific results into industry applications through the aca.ind mobility (Grimpe & Hussinger, 2013; Shao et al., 2020, 2021). In addition, they accumulate the social capital that may be

lacking in academic research institutions through mobility to enhance their own influence. In this process, they may somewhat ignore the desire to improve their own research ability. These conclusions suggest that governments need to allocate human resources rationally and promote further integration and interaction of science and technology in the AI domain.

This paper has some limitations. First, the influence of endogenous factors cannot be avoided, because we cannot enumerate all the factors that have an impact on independent variables and dependent variables and control them effectively. What we can do is reduce this influence based on our matching methods. Furthermore, we have selected commonly used indicator proxies of researcher performance, but the reliability of these metrics remains controversial. The discussion on which indicators can effectively represent researchers’ performance needs to be further explored in future research.

## Appendix

- Part 1: The results presented in Table 6 correspond to Part 1 of the Appendix. It can be seen


from Table 6 that a small number of “Asian name” have reached the bset accuracy after the first stage of disambiguation, while most of them achieve best effect after the second stage of disambiguation. It means that our work can solve the problem of ambiguity of the author name to some degree.

- Table 6 Results on the accuracy of name disambiguation for mobile researchers


Name Original data First stage results

Second stage results

P R F1 P R F1 P R F1

Zhiwei Li 1.0 0.33 0.41 1.0 1.0 1.0 1.0 1.0 1.0 Tim Oates 1.0 0.33 0.44 1.0 0.5 0.58 1.0 0.5 0.58 Wei Wang 0.96 0.57 0.63 0.94 0.70 0.72 0.94 0.74 0.77 A. Huertas 1.0 0.25 0.35 1.0 1.0 1.0 1.0 1.0 1.0 Wei Pan 0.86 0.4 0.49 0.86 0.4 0.49 0.82 0.53 0.62 En Zhu 1.0 0.5 0.64 1.0 1.0 1.0 1.0 1.0 1.0 Ke Xu 1.0 0.71 0.77 1.0 0.83 0.87 1.0 1.0 1.0 Xin Li 0.95 0.66 0.70 0.84 0.62 0.65 0.82 0.66 0.68 Zhe Li 1.0 0.83 0.88 1.0 0.83 0.88 1.0 1.0 1.0 He Wang 0.91 0.66 0.73 0.91 0.66 0.73 0.96 0.80 0.84 Jie Zhang 0.91 0.73 0.75 0.89 0.86 0.83 0.84 0.83 0.77 Ning Xu 0.92 0.80 0.82 0.91 0.94 0.91 0.95 1.0 0.97 Li Zhang 0.92 0.81 0.83 0.91 0.83 0.85 0.84 0.10 0.71 Hongtao Lu 0.96 0.5 0.56 0.85 0.4 0.49 0.95 1.0 0.97 E. Morales 1.0 0.67 0.78 1.0 0.67 0.78 1.0 0.67 0.78 Means 0.96 0.58 0.65 0.94 0.75 0.79 0.94 0.79 0.85

Table 6 presents the accuracy of the results of the two-stage author name disambiguation, which are based on the 15 “Asian name” selected in this paper. The result of accuracy is between 0 and 1, the closer to 1 the value, the better its effect. We present the optimal effects of different stages in the form of [bold]

- Part 2:


NametypeNametypeNametype

Imdea0university of oslo1wildlife conservation society3

Fujifilm0university of the pacific1va boston healthcare system3

Exxonmobil0ohio state university1united states patent and trademark office3

Nokia0fudan university1united states department of the interior3

Microsoft0nanjing normal university1united states department of the army3

Centaur technology0dokkyo medical university1tri service general hospital3

texas instruments0drexel university1toronto general hospital3

Philips0nanjing agricultural university1the research institute at nationwide children s hospital3

fmc corporation0silesian university of technology1tenri hospital3

Union pacific railroad0tokyo university of technology1tan tock seng hospital3

Investment technology group inc0beijing wuzi university1swedish defence research agency3

Sidi0kaunas university of technology1suny downstate medical center3

Insight enterprises0university of applied sciences technikum wien1spanish national research council3

Goodrich corporation0university of lyon1scientific and technological research council of turkey3

Hyundai mobis0university of genoa1ottawa hospital3

Aster0ton duc thang university1national bureau of economic research3

ntt docomo0university of siegen1mexican institute of petroleum3

ibm0zhejiang normal university1federal ministry of health3

System planning corporation0university of zurich1memorial hospital of south bend3

Deloitte0university of california santa cruz1los angeles county sheriff s department3

Osram0university of oregon1lincoln hospital3

Polaris industries0university of osnabruck1lahey hospital medical center3

Oki electric industry0joseph fourier university1johns hopkins bayview medical center3

Air france0marquette university1international center for tropical agriculture3

Part of results of identification of institutions’ typeTable 7

Note: industrial institutions (such as enterprises) are represented by 0; academic research institutions (such as universities) are represented by 1; other types of institutions are

NametypeNametypeNametype

Dolby laboratories0southwest university1huntington hospital3

Fujitsu0southern illinois university edwardsville1guy s hospital3

Fiat automobiles0university of debrecen1great ormond street hospital3

United aircraft corporation0university of massachusetts lowell1european space operations centre3

Twitter0university of west florida1el camino hospital3

Analog devices0xidian university1council for scientific and industrial research3

Yokogawa electric0nanjing university1chicago zoological society3

Ceremade0manonmaniam sundaranar university1champalimaud foundation3

National presto industries0california state university fullerton1butler hospital3

Nvidia0liaoning normal university1boston children s hospital3

Valeo0university of waikato1boca raton regional hospital3

Telcordia technologies0northwest university1biotechnology and biological sciences research council3

Serc reliability corporation0alexandria university1australian national drag racing association3

htc0national university of malaysia1association of research libraries3

China mobile0kazan federal university1american museum of natural history3

Huawei0kettering university1allegheny general hospital3

(continued)Table 7

represented by 2

![image 8](Chen et al._2023_Impacts of inter-institutional mobility on scientific performance from research capital and social c_images/imageFile8.png)

- Fig. 8 Complete process of matching procedure


- Part 3: The complete process of matching procedure are presented in Fig. 8. The variables


chosen for matching in this paper are mainly publication and collaboration indicators of researchers before mobility. As these indicators relate to the time of mobility, they cannot be calculated for non-mobile researchers. In this regard, we first screen out non-mobile researchers who have similar characteristics to the two types of mobile researchers separately to determine a virtual year of mobility for them.

The conditions used for screening include: 1. the first publication of the non-mobile researchers is published at the same time as the mobile researchers; 2. The non-mobile researchers belong to the same type of institution as the mobile researchers before their nobility; 3. The non-mobile researchers belong to the same discipline as the mobile researchers (the discipline of the researchers is judged based on the department of the institution to which the researchers belong). The aca.aca and aca.ind mobile researchers are embedded in the above conditions to find the non-mobile researchers who meet the conditions, respectively. There are 22994 non-mobile researchers meeting the above conditions. We then assign virtual mobility years to the screened non-mobile researchers based on the year of mobility of mobile researchers. We calculate the metrics used for matching based on their virtual mobility year.

Based on the PSM, we obtain two additional sets of matching results. In the second match, the aca.aca mobile researchers represent the treatment group, while the non-mobile researchers represent the control group. 15640 observations are matched successfully in the second matching, including 4758 observations in the treatment group and 10882 in the control group. In the third match, the aca.ind mobile researchers represent the treatment group, while the non-mobile researchers also represent the control group. 4530 observations are matched successfully in the third matching, including 805 observations in the treatment group and 1366 in the control group.

Table 8 presents the balance check for the second matching results. From Table 8, the mean difference between the treatment and control group becomes 0 after matching. The means of most of variables also become smaller after matching. It demonstrates that the distribution of the variables in the treatment and control group is more balanced after matching. Similar conclusions are also presented in Table 9.

- pre.inf.coauthors 0.072*** − 0.088*** 0.072*** 0.262*** post.aca.age 0.039*** 0.086*** 0.019*** 0.044*** (Intercept) 0.154*** − 1.837*** 1.151*** − 1.659*** N 15,640 15,640 15,640 15,640

- Table 8 Balance of variables before and after matching Variables Before matching After matching

Means treated Means control Means diff Means treated Means control Mean diff gender 0.892 0.9119 − 0.064 0.9208 0.9208 0

- pre.aca.age 5.9143 3.6139 0.5027 4.323 4.323 0 pre.coauthors 4.8005 4.5293 0.0415 2.8628 2.8628 0 pre.pubs 2.8419 2.1734 0.1568 1.5902 1.5902 0 pre.ind.coauthors 0.5617 0.4537 0.082 0.1967 0.1967 0

pre.inf.coauthors 1.1251 0.8554 0.1643 0.6257 0.6257 0

Table 9 Balance of variables before and after matching Variables before matching after matching

Means treated Means control Mean diff Means treated Means control Mean diff gender 0.9212 0.9157 0.0204 0.9528 0.9528 0

- pre.aca.age 6.7996 4.0616 0.5703 4.3863 4.3863 0 pre.coauthors 8.7296 4.9943 0.2876 2.9938 2.9938 0 pre.pubs 5.8296 2.4681 0.3184 1.7814 1.7814 0 pre.ind.coauthors 2.1773 0.546 0.4674 0.4758 0.4758 0




- pre.inf.coauthors 2.3846 0.9239 0.4066 0.8224 0.8224 0


- Table 10 Impact of aca.aca pattern on the performance of research and social capital


Post pubs Post correspond pubs Post coauthors Post inf coauthors

treat 0.811*** 0.816 *** 0.685*** 1.029*** gender 0.178*** 0.201*** 0.097*** 0.230***

- pre.aca.age − 0.038*** 0.040*** − 0.018*** − 0.014* pre.pubs 0.215*** 0.283*** 0.079*** 0.070*** pre.coauthors − 0.025*** − 0.022* 0.052*** − 0.019* pre.ind.coauthors 0.024 − 0.085* 0.008*** 0.141***


‘.’ p < 0.1, ‘*’ p < 0.05, ‘**’ p < 0.01, ‘***’ p < 0.001

After passing the balance check, the matched data is used in the regression analysis. Table 10 presents the impact of aca.aca mobility on researchers’ performance compared to non-mobile researchers. In the first two columns of Table 10, the results are presented from the research capital respective, while the last two columns are presented the results from the perspective of social capital. As can be seen from the Table 10, aca.aca mobility of researchers seems to have a significance positive impact on the improvement and accumulation of their research and social capital compared to non-mobile researchers.

- Table 11 Impact of aca.ind pattern on the performance of research and social capital


Post pubs Post correspond pubs Post coauthors Post inf coauthors

treat 0.754*** 0.635*** 0.757*** 1.270*** gender 0.122 0.219 0.006 0.238

- pre.aca.age − 0.039*** 0.049*** − 0.015* − 0.028 pre.pubs 0.189*** 0.237*** 0.050** 0.064 pre.coauthors − 0.016 − 0.005 0.080*** -0.031 pre.ind.coauthors 0.013 0.006 0.026 0.073 pre.inf.coauthors 0.097*** − 0.072 0.059** 0.258*** post.aca.age 0.050*** 0.109*** 0.025*** 0.054*** (Intercept) 0.124 − 2.076*** 1.153*** − 1.679*** N 4530 4530 4530 4530


‘.’ p < 0.1, ‘*’ p < 0.05, ‘**’ p < 0.01, ‘***’ p < 0.001

Table 11 presents the impact of aca.ind mobility on researchers’ performance compared to non-mobile researchers. Table 11 presents similar findings to Table 10. The above regression results indicate that the performance of mobile researchers is better than that of non-mobile researchers when other variables remain consistent under control. It means that both aca.aca and aca.ind mobility have a positive impact on researchers’ performance from the perspectives of research and social capital. As can be observed from the magnitude of the regression coefficients alone, aca.ind mobility has a weaker impact on the improvement of research capital of researchers than aca.aca mobility, while its impact on the improvement and accumulation of researchers’ social capital is greater than that of aca. aca mobility. To further explore the differences in researchers’ performance resulting from these two mobility patterns, we further conduct the regression analysis based on them.

Acknowledgements This work was supported by the National Science Foundation of China (NSFC No. 71874077).

Author contributions The study conception and design were conducted by JS. The first draft of the study was written by YC. Material preparation, data collection and analysis were performance by KW, YL, YC and JS. All authors read and approved the final manuscript.

## Declarations

Conflict of interest All authors certify that they have no affiliations with or involvement in any organization or entity with any financial interest or non-financial interest in the subject matter or materials discussed in this manuscript.

## References

Aceituno-Aceituno, P., Danvila-Del-Valle, J., González García, A., & Bousoño-Calzón, C. (2018). Entrepreneurship, intrapreneurship and scientific mobility: The Spanish case. PLoS ONE, 13(9), e0201893. https://doi.org/10.1371/journal.pone.0201893

Arvanitis, S., Kubli, U., & Woerter, M. (2011). Knowledge and technology transfer activities between firms and universities in Switzerland: An analysis based on firm data. Industry and Innovation, 18(4), 369–392.

Bäker, A. (2013). The impact of changes of affiliation on publications: An analysis of the role of research discipline and institutional size. Working Paper Series.

Baker, S. K., Kamata, A., Wright, A., Farmer, D., & Nippert, R. (2019). Using propensity score matching to estimate treatment effects of afterschool programs on third-grade reading outcomes. Journal of Community Psychology, 47(1), 117–134.

Barney, J. (1991). Firm resources and sustained competitive advantage. Journal of Management, 17(1), 99–120. Baruffaldi, S. H., & Landoni, P. (2016). Mobility intentions of foreign researchers: The role of noneconomic motivations. Industry and Innovation, 23(1), 87–111. Bikard, M., & Marx, M. (2020). Bridging academia and industry: How geographic hubs connect university science and corporate technology. Management Science, 66(8), 3425–3443. Bolli, T., & Schläpfer, J. (2015). Job mobility, peer effects, and research productivity in economics. Scientometrics, 104(3), 629–650.

Bornmann, L., & Bauer, J. (2015). Which of the world’s institutions employ the most highly cited researchers? An analysis of the data from highlycited.com. Journal of the Association for Information Science and Technology, 66(10), 2146–2148.

Bornmann, L., Bauer, J., & Schlagberger, E. M. (2017). Characteristics of highly cited researchers 2015 in Germany. Scientometrics, 111(1), 543–545. Bouoiyour, J., & Miftah, A. (2015). The impact of migrant workers’ remittances on the living standards of families in Morocco: A propensity score matching approach. Migration Letters, 12(1), 13–27. Chan, H. F., & Torgler, B. (2020). Gender differences in performance of top cited scientists by field and country. Scientometrics, 125(3), 2421–2447. Edler, J., Fier, H., & Grimpe, C. (2011). International scientist mobility and the locus of knowledge and technology transfer. Research Policy, 40(6), 791–805. Feitelson, D. G., & Yovel, U. (2004). Predictive ranking of computer scientists using CiteSeer data. Journal of Documentation, 60(1), 44–61. Frank, M. R., Wang, D., Cebrian, M., & Rahwan, I. (2019). The evolution of citation graphs in artificial intelligence research. Nature Machine Intelligence, 1(2), 79–85. Garfield, E., & Merton, R. K. (1979). Citation indexing: Its theory and application in science, technology, and humanities. Wiley.

Grácio, M. C. C., de Oliveira, E. F. T., Chinchilla-Rodríguez, Z., & Moed, H. F. (2020). Does corresponding authorship influence scientific impact in collaboration: Brazilian institutions as a case of study. Scientometrics, 125(2), 1349–1369.

Grimpe, C., & Hussinger, K. (2013). Formal and informal knowledge and technology transfer from academia to industry: Complementarity effects and innovation performance. Industry and Innovation, 20(8), 683–700.

Gureyev, V. N., Mazov, N. A., Kosyakov, D. V., & Guskov, A. E. (2020). Review and analysis of publications on scientific mobility: Assessment of influence, motivation, and trends. Scientometrics, 124(2), 1599–1630.

Halevi, G., Moed, H. F., & Bar-Ilan, J. (2016). Does research mobility have an effect on productivity and impact? International Higher Education, 86, 5–6. Hoisl, K. (2007). Tracing mobile inventors—the causality between inventor mobility and inventor productivity. Research Policy, 36(5), 619–636. Jonkers, K., & Tijssen, R. (2008). Chinese researchers returning home: Impacts of international mobility on research collaboration and scientific productivity. Scientometrics, 77(2), 309–333. Jovanovic, B. (1979). Job matching and the theory of turnover. Journal of Political Economy, 87(5), 972–990.

Kaiser, U., Kongsted, H. C., Laursen, K., & Ejsing, A. K. (2018). Experience matters: The role of academic scientist mobility for industrial innovation. Strategic Management Journal, 39(7), 1935–1958.

Katz, J. S., & Martin, B. R. (1997). What is research collaboration? Research Policy, 26(1), 1–18. Kong, X., Mao, M., Jiang, H., Yu, S., & Wan, L. (2019). How does collaboration affect researchers’

positions in co-authorship networks? Journal of Informetrics, 13(3), 887–900.

Kwiek, M., & Roszka, W. (2022). Academic vs. biological age in research on academic careers: A large-scale study with implications for scientifically developing systems. Scientometrics, 127, 3543–3575.

Lei, Y., & Liu, Z. (2019). The development of artificial intelligence: A bibliometric analysis, 2007–

2016. In Journal of Physics: Conference Series, 1168(2), 022027.

- Liu, M., & Hu, X. (2021). Will collaborators make scientists move? A generalized propensity score analysis. Journal of Informetrics, 15(1), 101113.
- Liu, N., Shapira, P., & Yue, X. (2021). Tracking developments in artificial intelligence research: Constructing and applying a new search strategy. Scientometrics, 126(4), 3153–3192.


Luo, C., Zhou, L., & Wei, Q. (2017). Identification of research fronts in artificial intelligence. In 2017 2nd Asia-Pacific Conference on Intelligent Robot Systems (ACIRS). Wuhan: IEEE, 104–108.

Luo, F., Sun, A., Erdt, M., Sesagiri Raamkumar, A., & Theng, Y. L. (2018). Exploring prestigious citations sourced from top universities in bibliometrics and altmetrics: A case study in the computer science discipline. Scientometrics, 114(1), 1–17.

Martinez, M., & Sá, C. (2020). Highly cited in the south: International collaboration and research recognition among Brazil’s highly cited researchers. Journal of Studies in International Education, 24(1), 39–58.

Mattsson, P., Sundberg, C. J., & Laget, P. (2011). Is correspondence reflected in the author position? A bibliometric study of the relation between corresponding author and byline position. Scientometrics, 87(1), 99–105.

Momeni, F., Karimi, F., Mayr, P., Peters, I., & Dietze, S. (2022). The many facets of academic mobility and its impact on scholars’ career. Journal of Informetrics, 16(2), 101280.

Murakami, Y. (2014). Influences of return migration on international collaborative research networks: Cases of Japanese scientists returning from the US. The Journal of Technology Transfer, 39(4), 616–634.

Must, Ü. (2020). The highly cited researchers with researcher ID: Patterns of behavior through time. Journal of Scientometric Research, 9(2), 195–199.

Niu, J., Tang, W., Xu, F., Zhou, X., & Song, Y. (2016). Global research on artificial intelligence from 1990–2014: Spatially-explicit bibliometric analysis. ISPRS International Journal of Geo-Information, 5(5), 66.

Payumo, J. G., Lan, G., & Arasu, P. (2018). Researcher mobility at a US research-intensive university: Implications for research and internationalization strategies. Research Evaluation, 27(1), 28–35. Robinson-Garcia, N., Sugimoto, C. R., Murray, D., Yegros-Yegros, A., Larivière, V., & Costas, R.

(2019). The many faces of mobility: Using bibliometric data to measure the movement of scientists. Journal of Informetrics, 13(1), 50–63.

Roman, M., & Popescu, M. E. (2014). The effects of training on Romanian migrants’ income: A propensity score matching approach. Journal of Economic Computation and Economic Cybernetics Studies and Research, 49(1), 113–129.

Sarigöl, E., Pfitzner, R., Scholtes, I., Garas, A., & Schweitzer, F. (2014). Predicting scientific success based on coauthorship networks. EPJ Data Science, 3, 1–16.

Savage, W. E., & Olejniczak, A. J. (2021). Do senior faculty members produce fewer research publications than their younger colleagues? Evidence from Ph. D. granting institutions in the United States. Scientometrics, 126(6), 4659–4686.

Scellato, G., Franzoni, C., & Stephan, P. (2012). Mobile scientists and international networks. National Bureau of Economic Research. https://doi.org/10.3386/w18613

Shang, H., Anumba, C. J., & Bouchlaghem, D. M. (2006). An Intelligent Risk Assessment System for AEC. In 2006 10th International Conference on Computer Supported Cooperative Work in Design (pp. 1–6). IEEE.

Shao, Z., Yuan, S., & Wang, Y. (2020). Institutional collaboration and competition in artificial intelligence. IEEE Access, 8, 69734–69741. Shao, Z., Yuan, S., Wang, Y., & Xu, J. (2021). Evolutions and trends of artificial intelligence (AI): Research, output, influence and competition. Library Hi Tech, 40(3), 704–724. Simoes, N., & Crespo, N. (2020). A flexible approach for measuring author-level publishing performance. Scientometrics, 122(1), 331–355. Singh, H., Cascini, G., & McComb, C. (2021). Influencers in design teams: A computational framework to study their impact on idea generation. AI EDAM, 35(3), 332–352.

Sinha, A., Shen, Z., Song, Y., Ma, H., Eide, D., Hsu, B. J., & Wang, K. (2015). An overview of microsoft academic service (mas) and applications. In Proceedings of the 24th international conference on world wide web. New York: ACM press, 243–246.

Topel, R. H., & Ward, M. P. (1992). Job mobility and the careers of young men. The Quarterly Journal of Economics, 107(2), 439–479. Trippl, M. (2013). Scientific mobility and knowledge transfer at the interregional and intraregional level. Regional Studies, 47(10), 1653–1667. van Rijnsoever, F. J., Hessels, L. K., & Vandeberg, R. L. (2008). A resource-based view on the interactions of university researchers. Research Policy, 37(8), 1255–1266. Verginer, L., & Riccaboni, M. (2020). Cities and countries in the global scientist mobility network. Applied Network Science, 5(1), 1–16. Verginer, L., & Riccaboni, M. (2021). Talent goes to global cities: The world network of scientists’ mobility. Research Policy, 50(1), 104127.

Wang, K., Shen, Z., Huang, C., Wu, C. H., Dong, Y., & Kanakia, A. (2020). Microsoft academic graph: When experts are not enough. Quantitative Science Studies, 1(1), 396–413.

Welbourne, T. M., & Pardo-del-Val, M. (2009). Relational capital: Strategic advantage for small and medium-size enterprises (SMEs) through negotiation and collaboration. Group Decision and Negotiation, 18, 483–497.

Wu, J., Ou, G., Liu, X., & Dong, K. (2022). How does academic education background affect top researchers’ performance? Evidence from the field of artificial intelligence. Journal of Informetrics, 16(2), 101292.

Xu, H., Yu, Z., Yang, J., Xiong, H., & Zhu, H. (2018). Dynamic talent flow analysis with deep sequence prediction modeling. IEEE Transactions on Knowledge and Data Engineering, 31(10), 1926–1939. Yin, X., & Zong, X. (2022). International student mobility spurs scientific research on foreign countries: Evidence from international students studying in China. Journal of Informetrics, 16(1), 101227.

Yue, M. L., Li, R. N., Ou, G. Y., Wu, X., & Ma, T. C. (2020). An exploration on the flow of leading research talents in China: From the perspective of distinguished young scholars. Scientometrics, 125(2), 1559–1574.

- Zhang, B., & Al Hasan, M. (2017). Name disambiguation in anonymized graphs using network embedding. In Proceedings of the 2017 ACM on Conference on Information and Knowledge Management. New York: ACM press, 1239–1248.
- Zhang, C., Bu, Y., Ding, Y., & Xu, J. (2018). Understanding scientific collaboration: Homophily, transitivity, and preferential attachment. Journal of the Association for Information Science and Technology, 69(1), 72–86.


Zhao, Z., Bu, Y., Kang, L., Min, C., Bian, Y., Tang, L., & Li, J. (2020). An investigation of the relationship between scientists’ mobility to/from China and their research performance. Journal of Informetrics, 14(2), 101037.

Zhao, Z., Bu, Y., & Li, J. (2021). Characterizing scientists leaving science before their time: Evidence from mathematics. Information Processing & Management, 58(5), 102661.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

