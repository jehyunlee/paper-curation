PNAS Nexus, 2026, 5, pgag057

https://doi.org/10.1093/pnasnexus/pgag057 Advance access publication 6 March 2026

Research Report

# Interdisciplinary papers supported by disciplinary grants garner deep and broad scientific impact

Minsu Park a,b,c,d, Suman Kalyan Maity b,c,d, Stefan Wuchty e,f,g,h and Dashun Wang b,c,d,i,*

aDivision of Social Science, New York University Abu Dhabi, Abu Dhabi 129188, UAE bCenter for Science of Science and Innovation, Northwestern University, Evanston, IL 60208, USA cNorthwestern Institute on Complex Systems, Northwestern University, Evanston, IL 60208, USA dKellogg School of Management, Northwestern University, Evanston, IL 60208, USA eDepartment of Computer Science, University of Miami, Coral Gables, FL 33146, USA fDepartment of Biology, University of Miami, Coral Gables, FL 33146, USA gSylvester Comprehensive Cancer Center, University of Miami, Miami, FL 33136, USA hFrost Institute of Data Science and Computing, University of Miami, Coral Gables, FL 33146, USA iMcCormick School of Engineering, Northwestern University, Evanston, IL 60208, USA

*To whom correspondence should be addressed: Email: dashun.wang@northwestern.edu Edited By Erik Kimbrough

#### Abstract

Interdisciplinary research has emerged as a hotbed for innovation and a key approach to addressing complex societal challenges. The dominance of grant-supported research in shaping scientific advances, coupled with growing interest in funding interdisciplinary work, raises fundamental questions about the effectiveness of interdisciplinary grants in fostering high-impact interdisciplinary research outcomes. Here, we analyze 350,000 grants from 164 agencies in 26 countries, along with 1.3 million resulting papers published between 1985 and 2009, to examine whether interdisciplinary grants successfully cultivate high-impact interdisciplinary research. Although interdisciplinary grants tend to produce interdisciplinary papers as intended, they yield fewer papers on average. Furthermore, while interdisciplinary papers are generally associated with high impact, those supported by interdisciplinary grants show substantially lower impact compared with those funded by disciplinary grants. In contrast, highly interdisciplinary papers anchored in deeply disciplinary grants garner disproportionately more citations, both within their core disciplines and from broader fields. This impact advantage is not merely a consequence of funding size, reception of ideas within disciplinary boundaries, or collaborative formats. Amid the substantial rise of support for interdisciplinary work across the sciences, these results highlight the underexplored role of disciplinary grants in driving interdisciplinary advances, suggesting that interdisciplinary research may benefit from deep disciplinary expertise and investments.

Keywords: science of science, interdisciplinary research, research grants, scientific impact, science policy

##### Significance Statement

Do interdisciplinary grants indeed produce high-impact interdisciplinary research? Analyzing large-scale datasets linking grants to the papers that they produce, we find that while interdisciplinary grants tend to lead to interdisciplinary papers, they tend to have lower impacts compared with those supported by disciplinary grants. Somewhat counterintuitively, the deeply disciplinary grants are disproportionately more likely to produce high-impact interdisciplinary research. This finding underscores the critical role of deep domain expertise and focused investment in advancing scientific innovation, with implications for science policy and funding decisions, highlighting the need to balance interdisciplinary aspirations with disciplinary strengths to foster high-impact interdisciplinary advances.

## Introduction

Many scientific challenges today, from climate change to global pandemics, require interdisciplinary approaches that integrate expertise and resources across diverse perspectives (1–5). In response, amid the rapid growth in scale and complexity of the modern scientific enterprise (3, 4, 6), coupled with the increasing

specialization of individual expertise (7, 8), funding agencies and policymakers have been progressively focusing on grant programs that promote interdisciplinary work (2, 3, 9–11). Although funding plays a critical role in propelling scientific progress, our knowledge of how interdisciplinary grants shape the interdisciplinary research landscape remains limited. Yet, such understanding is

Competing Interest: The authors declare no competing interests. Received: October 9, 2025. Accepted: February 10, 2026

© The Author(s) 2026. Published by Oxford University Press on behalf of National Academy of Sciences. This is an Open Access article distributed under the terms of the Creative Commons Attribution-NonCommercial License (https://creativecommons.org/licenses/by-nc/4.0/), which permits non-commercial re-use, distribution, and reproduction in any medium, provided the original work is properly cited. For commercial re-use, please contact reprints@oup.com for reprints and translation rights for reprints. All other permissions can be obtained through our RightsLink service via the Permissions link on the article page on our site—for further information please contact journals.permissions@oup.com.

###### Downloaded from https://academic.oup.com/pnasnexus/article/5/3/pgag057/8509178 by Korea Inst of Sci & Tech user on 24 March 2026

essential for more productively supporting high-impact interdisciplinary endeavors, especially given the ensuing debates about the risks and benefits of interdisciplinary work among researchers and research institutions (9, 11–14).

Classic work in the sociology and philosophy of science emphasizes that disciplines are not merely administrative bins but epistemic communities with shared standards and a “knowledge core” that confers legitimacy on what counts as an advance (15, 16). From this perspective, interdisciplinary funding programs could increase the impact of boundary-spanning research by relaxing field-specific gatekeeping, assembling broader evaluative expertise, and underwriting the coordination and translation costs that often impede cross-field collaboration. At the same time, these same insights imply a countervailing force: To travel widely, novel claims often need to be recognized as rigorous and consequential by at least one disciplinary core, and removing (or weakening) that anchor may make it harder for interdisciplinary ideas to secure initial legitimacy, even when they integrate diverse inputs. In this sense, interdisciplinary work can face a “dual evaluative constraint”: It must satisfy disciplinary standards to be seen as a contribution somewhere while also spanning boundaries to achieve broad influence. These competing expectations prompt us to ask how the interdisciplinary orientation of grants relates to both the interdisciplinarity of resulting papers and the impact they ultimately achieve.

Prior studies have underscored the growing significance and impact of interdisciplinary work across scientific disciplines (1, 17–22) by employing measures to quantify the interdisciplinarity of research papers (21–24). However, as recent studies suggest, high levels of knowledge integration (diverse inputs derived from references) do not guarantee broad knowledge influence (broad uptake derived from citations) (21, 22, 25). Indeed, a paper may draw on diverse disciplinary sources yet fail to generate commensurately broad cross-disciplinary uptake. Parallel to this, another stream of research has examined the research outputs of “grants” (26–29). These studies typically rely on data from a single agency or country (29–34) and generally highlight the critical role of funding in propelling scientific progress, amid the growing scale and complexity of science (26, 35) and fiscal scarcity (32). While developing concomitantly, these two lines of research reveal an important gap in understanding the relationship between interdisciplinary grants and high-impact interdisciplinary advances they support.

This gap exists mainly due to the lack of a unified measurement approach to quantify the interdisciplinarity of “both” research grants and the resulting publications. To address this discrepancy, we combine data from two large-scale grant and publication databases—Dimensions (36) and the Microsoft Academic Graph (MAG) (37)—which are among the most comprehensive sources covering scientific grants and publications (38). We then introduce a new unified measurement framework that enables estimation of interdisciplinarity across both grants and papers under a common field classification scheme, and apply it to 350,000 grants from 164 funding agencies across 26 countries and 1.3 million papers that acknowledge these grants from 1985 to 2009 (see Materials and methods for more details). This approach allows us to systematically examine the longitudinal changes in the interdisciplinarity of both research grants and papers across disciplines, as well as the relationships between grant interdisciplinarity and their supported publications, with a particular emphasis on the impact of these publications based on the interdisciplinary attributes of both the publications and their supporting grants.

The key technical challenge here is that while measuring the interdisciplinarity of papers is well established through

bibliometric techniques based on references and citations (17, 18, 21–24, 39), existing methods cannot directly be applied to grants, partly due to the lack of a consistent field classification scheme and standardized reference systems in grants. To tackle this challenge, we use field classifications of papers and their abstracts in the MAG dataset (Fig. 1a) to learn text representations of each scientific field (Fig. 1b) with a supervised topic modeling method, labeled-latent Dirichlet allocation (labeled-LDA; see Materials and methods). Unlike methods that assign a single category, labeled-LDA estimates word associations for each field, enabling us to calculate the probabilities of a grant’s association across all potential fields based on its abstract (Fig. 1c). We validate our model through multiple approaches, including human ratings and out-of-sample predictions, demonstrating reliable model outputs (see Note S3). Finally, to determine the probability that a given publication is associated with a particular field, we use the fraction of its references or citations in that field as a proxy of topical inspiration or appeal, respectively (Fig. 1d; see Materials and methods), allowing us to express both grants and papers in probabilistic terms across multiple fields.

We then quantify the level of interdisciplinarity of individual publications and grants using the Rao–Stirling (RS) diversity as commonly operationalized in previous research (17, 18, 21–24, 39). This measure incorporates three sets of information (Fig. 1f), including the number of research fields (volume; Fig. 1c and d), their relative distribution (balance; Fig. 1c and d), and their differences (disparity; Fig. 1e), on a scale from 0 to 1, where 0 indicates deeply disciplinary work and 1 indicates the highest level of interdisciplinarity (see Materials and methods for more details). Together, these data and methods provide a unique opportunity to study grants and papers at a large scale under a unified field classification scheme.

## Results

To contextualize our investigation into the relationship between funding inputs and scientific outputs, we first examine the macrolevel trends of interdisciplinarity. Figure 2a shows an overall increasing trend in interdisciplinary research across the sciences over the past 25 years (see also Figs. S1 and S2), a result that is in line with previous observations (1, 11, 17). Notably, since the mid-1990s, papers that acknowledged grant support have exhibited a higher level of interdisciplinarity, hinting at the relevant role of funding in fostering interdisciplinary work (see Fig. S3 for the robustness of this result controlling for author prominence and team size).

We next test the common policy assumption that these interdisciplinary inputs naturally yield high-impact interdisciplinary outputs. We examine 2,213,187 grant-paper pairs, capturing 1,293,934 publications and 350,526 supporting grants. Initially, the data appear to support the intended policy goal: We observe that grants with higher interdisciplinarity tend to result in more interdisciplinary papers (Figs. 2b and S4), and papers supported by interdisciplinary grants are found to attract citations from a wide range of disciplines (inset, Fig. 2b). Additionally, by calculating the paper-level hit rate, defined as the probability of a paper being in the top 5% of citations in its field and year (40), we find that highly interdisciplinary papers tend to be more impactful (Figs. 2c and S5).

However, we observe the first signal of the “dual evaluative constraint” when looking at productivity and specific impact. When we consider all grants, regardless of whether they produced a paper, we find that interdisciplinary grants, on average, yield

###### Downloaded from https://academic.oup.com/pnasnexus/article/5/3/pgag057/8509178 by Korea Inst of Sci & Tech user on 24 March 2026

a

b c

e f

![image 1](Park et al._2026_Interdisciplinary papers supported by disciplinary grants garner deep and broad scientific impact_images/imageFile1.png)

![image 2](Park et al._2026_Interdisciplinary papers supported by disciplinary grants garner deep and broad scientific impact_images/imageFile2.png)

d

| | |
|---|---|
| | |


| | |
|---|---|
| | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |


![image 3](Park et al._2026_Interdisciplinary papers supported by disciplinary grants garner deep and broad scientific impact_images/imageFile3.png)

- Fig. 1. Quantifying the level of interdisciplinarity of individual publications and grants. Major publication databases assign each paper to certain scientific fields, while grant classifications are specific to individual funding agencies. a) We collect abstract and field labels of each publication from the MAG database to build a semi-supervised topic model. b) Based on a large-scale representative sample of publications, we associate each word in an abstract with the field of study labels of the corresponding paper and vice versa using labeled-LDA, allowing us to obtain a robust representation of word associations for each scientific field. c) Using our trained labeled-LDA model, we estimate the posterior probabilities that a grant belongs to a given scientific field based on the word distribution in the corresponding grant abstract. d) In turn, we calculate the probabilities that a paper belongs to a scientific discipline based on the fields of referenced and citing publications, respectively. e) We estimate the distances between scientific fields using cosine similarity between the reference (or citation) vectors that we obtain from corresponding publications in each field. Note that the reference- and citation-based distances are highly correlated with each other (Pearson’s r = 0.978, 95% CI 0.978–0.978, P < 0.001), suggesting that our result is insensitive to the measurement specification. f) Based on the field-relevance probabilities of grants and papers computed in c and d and distances between fields computed in e, we calculate the level of interdisciplinarity of each grant and paper with the RS diversity measure.


fewer papers compared with their disciplinary counterparts

- (Fig. 2d). More critically, despite an overall impact advantage of interdisciplinary papers (Fig. 2c), publications supported by interdisciplinary grants tend to have a significantly reduced impact
- (Fig. 2e). We confirm the robustness of these results across different sample frames, including variations in funding agencies, time periods, disciplines, and countries (see Note S5 and Figs. S9–S15). Together, the results in Fig. 2 highlight the importance of considering the interdisciplinary orientation of “both” grants and their supported papers to understand the success of grants and their research outcomes. These results paint a more nuanced picture of the role of interdisciplinary grants, suggesting that while they succeed in generating boundary-spanning work, the resulting research often falls short of achieving high impact. However, this unconditional analysis does not reveal whether the lower impact stems from the interdisciplinary nature of the papers themselves or from the interdisciplinary funding structure.


To directly test whether high-impact interdisciplinarity requires a strong disciplinary foundation, we investigate the joint distribution of grant-paper pairs, controlling for paper interdisciplinarity. We categorize grant-paper pairs based on the interdisciplinary orientations of both papers and their supporting grants and report the average hit rate of papers in each category (Fig. 3). While the hit rate tends to increase with the interdisciplinarity of publications (Figs. 2c and S5), Fig. 3a reveals that highest-impact papers are predominantly found in the upper

left corner, suggesting that interdisciplinary papers supported by disciplinary grants tend to garner disproportionately high impacts. Note that disciplinary grants are less likely to produce interdisciplinary papers on average (Figs. 2b and S4). Nevertheless, our findings indicate a systematic decline in the impact of papers as the interdisciplinarity of their supporting grants increases, even when controlling for the level of paper interdisciplinarity (Figs. 3b and S6). We further split our samples by different funding agencies, time periods, disciplines, and countries and repeat our analyses, pointing to the same results (see Note S5 and Figs. S9– S15). This confirms that stripping away the disciplinary core of the grant correlates with a loss of impact, supporting the view that innovation requires the legitimacy and structure of a disciplinary anchor to thrive.

We next consider whether this advantage of disciplinary anchoring is merely a consequence of resource disparity. One possibility is that disciplinary grants, born out of more established “core” funding mechanisms (2, 10), might receive larger funding support and therefore are more likely to produce higher-impact work. However, the data reject this material explanation. We find that interdisciplinary grants, on average, garner larger funding amounts compared with disciplinary grants (41) (Fig. 4a). Moreover, we observe increased publication productivity and impact for disciplinary grants even when controlling for funding size. Specifically, as the interdisciplinarity of grants increases, both the average number of outcome papers and their hit rate

###### Downloaded from https://academic.oup.com/pnasnexus/article/5/3/pgag057/8509178 by Korea Inst of Sci & Tech user on 24 March 2026

- a
- b c


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


| | | |
|---|---|---|
| | | |
| | | |
| | | |


d e

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


- Fig. 2. Impacts of interdisciplinary grants. a) Paper interdisciplinarity has been rising steadily from 1985 to 2009, and the increase of interdisciplinarity is more pronounced when we consider papers with grant support. b) Paper interdisciplinarity, as measured through paper references, increases as a function of the interdisciplinarity of supporting grants. The inset shows similar results when we consider paper interdisciplinarity based on citations. c) Papers with high interdisciplinary inspirations (i.e. reference-based paper interdisciplinarity) have a higher chance to be hit papers (dashed line as the baseline). This relationship also holds for grant-supported papers. The number of papers resulting from a grant (d) and the propensity to produce hit papers (e) systematically decrease as grant interdisciplinarity increases. In b–e, the x-axis represents grant or paper interdisciplinarity divided into 5-percentile intervals, ranging from the bottom 5% (left) to the top 5% (right), ensuring equal sample sizes across bins.


decrease sharply, regardless of grant size (Fig. 4b and c for largeand medium-sized grants, respectively). Note that this decreasing pattern is more pronounced with larger funding amounts while the baselines of productivity and impact rise with increasing funding size (Fig. S7).

Another potential explanation for the impact of disciplinary grants centers around the reception of ideas within disciplinary boundaries or the “home-field advantage.” For example, papers that were supported by deeply disciplinary grants may be better positioned to acquire citations from their own fields due to higher legitimacy. To investigate this, we trace the top and bottom 25% of papers and supporting grants ranked by their

interdisciplinarity. Then, we calculate the average number of citations that these papers received from within and outside their own field. Figure 4d reveals that papers supported by disciplinary grants (top and bottom left) indeed enjoy a home-field advantage, as they accumulate more citations than expected from their own field. More importantly, interdisciplinary publications supported by disciplinary grants (top left) tend to garner higher impact not just within their core disciplines but also from broad and distant fields. This finding suggests that deep disciplinary grounding (input) provides—or at least works as an indicator of—the necessary legitimacy to achieve both deep and broad scientific impact (outputs).

###### Downloaded from https://academic.oup.com/pnasnexus/article/5/3/pgag057/8509178 by Korea Inst of Sci & Tech user on 24 March 2026

### a b

| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


![image 4](Park et al._2026_Interdisciplinary papers supported by disciplinary grants garner deep and broad scientific impact_images/imageFile4.png)

![image 5](Park et al._2026_Interdisciplinary papers supported by disciplinary grants garner deep and broad scientific impact_images/imageFile5.png)

![image 6](Park et al._2026_Interdisciplinary papers supported by disciplinary grants garner deep and broad scientific impact_images/imageFile6.png)

- Fig. 3. Impact of interdisciplinary papers as a function of grant interdisciplinarity. a) Interdisciplinary papers from more disciplinary grants tend to be associated with higher impact. b) While the baseline average of impacts increases with paper’s interdisciplinarity (from quintile 1 to quintile 5), interdisciplinarity grants have an overall reduced probability of supporting impactful papers when controlling for papers with the same level of interdisciplinarity (based on references). In both panels, the x-axis represents grant interdisciplinarity divided into 5-percentile intervals, ranging from the bottom 5% (left) to the top 5% (right). In a, the y-axis (paper interdisciplinarity) is similarly divided into 5-percentile intervals.

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| | |
|---|---|
| | |


| | |
|---|---|
| | |


| | |
|---|---|
| | |
| | |


| | |
|---|---|
| | |


| | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | |


a b

d e

c

- Fig. 4. Disciplinary grants and high-impact interdisciplinary papers. a) Interdisciplinary grants tend to feature larger funding amounts. b) Considering only grants with large funding amounts (top 10%), we observe a sharp decline in both productivity and impact as a function of grant interdisciplinarity. c) A similar pattern of diminishing returns when we focus on grants with median funding amounts (middle 10%). In a–c, the x-axis denotes grant interdisciplinarity divided into 5-percentile intervals. d) Interdisciplinary papers supported by disciplinary grants (top left) tend to have a similar or higher number of citations than baselines (dashed lines) both from inside and outside of their own fields. Other papers attract more citations than the random baseline, either from their own field (disciplinary papers supported by disciplinary grants; bottom left), outside their own field (interdisciplinary papers supported by interdisciplinary grants; top right), or neither (disciplinary papers supported by interdisciplinary grants; bottom right). In e, we consider sets of the top and bottom 10% interdisciplinary papers based on their references that were supported by multiple grants. We calculate the distance between grants and further divide the groups of publications into sets of highly (dis)similar pairs of (inter)disciplinary grants. We find that high-impact interdisciplinary papers tend to acknowledge the support of closely related disciplinary grants.


###### Downloaded from https://academic.oup.com/pnasnexus/article/5/3/pgag057/8509178 by Korea Inst of Sci & Tech user on 24 March 2026

Finally, as teams are increasingly responsible for producing high-impact advances (7, 40, 42–46), we examine the organizations of collaborative grants and ask whether specific

collaborative formats can substitute for a single disciplinary anchor or are particularly suited for producing high-impact interdisciplinary publications. For instance, highly disciplinary grants

from distant disciplines may foster interdisciplinary advances by combining deep disciplinary expertise across disparate scientific fields. In other words, individual grants may be deeply disciplinary, but combining those from different disciplines could enable interdisciplinary efforts. To investigate this, we consider papers that acknowledged support from multiple grants. For each paper, we compute both the average interdisciplinarity of the supporting grants and the average disciplinary distance between them. We then categorize these papers into four groups based on the interdisciplinarity and distance scores of their supporting grants. These groups represent different collaborative grant formats: proximate disciplinary grants; distant disciplinary grants; proximate interdisciplinary grants; and distant interdisciplinary grants (from left to right in Fig. 4e).

Comparing the impact of papers supported by these four distinct collaborative formats reveals striking patterns. Papers garner the highest impact when they are highly interdisciplinary and supported by multiple disciplinary grants that are proximate in their intellectual space (Fig. 4e, far left). Conversely, the impact of papers decreases when supported by distant disciplinary grants and drops further for publications resulting from collaborations involving distant interdisciplinary grants (Fig. 4e, far right). These patterns are robust after controlling for a range of fundingand author-level factors (see Note S4 and Tables S2 and S3 for multivariate analyses). Overall, our results suggest that while distant disciplinary grants can span broader intellectual terrains, simply mixing “distant” funding sources does not create a successful anchor. Instead, closely related disciplinary grants tend to be most effective in maintaining the “knowledge core” necessary to produce impactful interdisciplinary work. This finding further underscores the significant role of disciplinary grants in fostering high-impact interdisciplinary advances (see Note S5 and Figs. S9–S15 for the robustness of our key results across different funding agencies, time periods, disciplines, and countries).

## Discussion

Our results suggest that the most effective route to interdisciplinary advances is not necessarily through interdisciplinary funding but through the deep structural support of disciplinary grants. While interdisciplinary grants succeed in their intended goal (i.e. producing papers with high interdisciplinarity), they appear to struggle with the “dual evaluative constraint” required for high impact (i.e. the need to satisfy the rigorous standards of a “knowledge core” while simultaneously reaching across fields). This aligns with theories of “innovation by displacement” (47, 48), which suggest that to displace existing paradigms, novel ideas must possess sufficient disciplinary legitimacy. Disciplinary grants appear to provide this legitimacy, allowing researchers to launch broad explorations from a stable platform, thereby garnering deep and broad citations.

Specifically, our results show that the broad and deep impacts of disciplinary grants are not simply a consequence of funding size, reception of ideas within disciplinary boundaries, or collaborative grant formats. Even with comparable funding resources, disciplinary grants tend to be more effective in producing highimpact interdisciplinary advances than their interdisciplinary counterparts and seem especially powerful when paired with other closely related disciplinary grants. This epistemic advantage appears to stem from the tendency of interdisciplinary work, when fueled by disciplinary anchors, to draw attention and garner citations from both its core field and broad external fields. While our analyses are correlational by nature and do not allow causal

interpretations, these results align with the view that “narrow work has broad impact” (17) and further emphasize the advantage of deep disciplinary expertise in the ambit of research (7, 49).

These observations have important implications for science policy. As funding agencies increasingly prioritize interdisciplinary mechanisms to solve complex problems (2, 3, 9–11), they may inadvertently be removing the very structures that enable high-impact solutions. Our analysis shows that “mixing” funding sources from distant disciplines does not substitute for a strong anchor; rather, impact is maximized when grants are disciplinary and intellectually proximate. Amid the broad shifts toward interdisciplinary sciences (1, 17, 18), our findings highlight the enduring challenges of interdisciplinary work, suggesting that the fruits of interdisciplinary programs are not always guaranteed. While interdisciplinary grants appear to produce intended outcomes, i.e. papers with high interdisciplinarity, we find that highly interdisciplinary grants tend to yield fewer total papers and a reduced probability of producing highly impactful papers, despite having larger funding on average.

However, these findings should not be interpreted as a dismissal of interdisciplinary grants. These programs remain essential for nurturing specific types of cross-disciplinary collaborations that might otherwise never form and for addressing problems that sit truly “between” established fields. Rather, our findings reflect the substantial costs and risks of interdisciplinary research, highlighting the need to manage tensions among different disciplinary and professional approaches (for research communities) and integrate deep disciplinary expertise in driving interdisciplinary work (for individual researchers and teams). Challenges may arise from the social friction of managing disparate disciplinary cultures (2, 50–55), the difficulty of developing a common language (51, 53, 56), or structural barriers where disciplinary journals dominate (57–59). It is also possible that interdisciplinary grants are systematically directed toward “harder” or more nascent problems that yield fewer publications or slower-emerging impact. Therefore, our results suggest that the design of these programs needs to be reconsidered. To unleash the full potential of interdisciplinary research, funders and policymakers might consider mechanisms that encourage “anchored exploration” rather than enforcing artificial recombination of distant disciplines.

Several limitations of our study suggest avenues for further research. First, this paper focuses on grants’ outcomes in terms of papers and citations. While these are major outputs, funders often also emphasize broader impacts, such as outreach, practical applications, and policy relevance, which are not captured by our publication-based measures (11). Consequently, our findings should be interpreted as reflecting “scientific impact” within the academic community rather than broader “societal impact.” Future work may also integrate diverse forms of interdisciplinary support, including seed grants, training programs, and targeted faculty hiring, to encompass a wider range of outcomes. Second, our data trace grant outcomes through grant acknowledgments in the paper. While this is a common practice in similar studies, some grants may be acknowledged tangentially or inconsistently. One open question is whether one can refine acknowledgment analyses by distinguishing relative contributions or validating acknowledgments through complementary data. Third, our analysis focuses on interdisciplinarity revealed in the thematic content of proposals and papers rather than the disciplinary backgrounds of the researchers. While the two are often correlated, our data do not allow us to determine whether the disciplinary anchor effect stems from a single researcher with deep expertise or a team of specialists working in concert. Finally, while we identify robust

###### Downloaded from https://academic.oup.com/pnasnexus/article/5/3/pgag057/8509178 by Korea Inst of Sci & Tech user on 24 March 2026

associations between funding orientation and the interdisciplinarity and impact of resulting papers, our study is observational. We cannot rule out that unobserved factors—such as the specific “risk appetite” of individual principal investigators (PIs)—drive both the choice of grant and the impact of the paper. Future work could further illuminate the microprocesses of how teams navigate the tension between disciplinary depth and interdisciplinary breadth. Ultimately, rather than viewing our results as a critique of interdisciplinary funding, they should serve as a starting point for richer, multidimensional evaluations of how to best balance disciplinary strength with interdisciplinary aspiration.

## Materials and methods

### Dataset of research grants and articles

We draw upon the Dimensions dataset (36), which tracks scientific publications and the grants that they acknowledge. Our analysis focuses on grants that were awarded after 1985, capturing 350,526 grants and 1,293,934 resulting papers that were published before 2009 (to allow time for citations to accumulate, given that our citation data cutoff is in 2020). To compute interdisciplinarity measures, we only include papers with at least one reference and one citation. Overall, these papers and grants cover 292 fields and 164 funding agencies across 26 countries. We further complement this dataset with abstracts, fields of study labels, and reference and citation information from corresponding papers by merging the Dimensions data with the MAG dataset (37). Note that we provide further details on the extensive coverage and comprehensiveness of our data sources, which surpass those of other widely used databases (38), along with discussions addressing potential concerns in Note S1.

### Fields of study

In defining research fields, we align with the notion of topical coherence as the systematic production of knowledge, particularly as manifested in content (60–62). Similarly, contrary to views that define interdisciplinarity by the disciplinary backgrounds of grant recipients or paper authors, we focus on the thematic content of proposals and publications. This perspective is crucial for understanding the thematic continuity between a grant’s objectives and the resulting research output, highlighting the tangible link between the nature of a grant and the characteristics of the research it supports.

To operationalize this, we utilize the MAG field of study taxonomy. Unlike static, journal-based classifications used in databases like Scopus and Web of Science (WoS), MAG employs a dynamic, six-level hierarchical taxonomy (levels 0 to 5) constructed through a heterogeneous graph learning framework (37, 63). The hierarchy begins with 19 broad top-level disciplines (level 0; e.g. biology, physics, and computer science) and branches into increasingly granular subfields (level 1; e.g. molecular biology, quantum mechanics, and AI) down to specific concepts (level 5). Individual papers are assigned to these fields through a hybrid classification pipeline that combines semantic analysis of the paper’s text (title and abstract) with structural analysis of its citation network. This allows a single publication to be associated with multiple fields across different levels of granularity based on its actual content and intellectual lineage.

Also, given the limitations of journal-based categorizations, especially in fields where journals are not the primary medium of scientific communication (e.g. computer and information sciences), MAG’s content-based classification offers a more

comprehensive scheme with comparable coherence. This approach, grounded in the indexing and classification of publications in MAG, offers a common basis for our analysis.

In this study, we specifically use the level 1 field information from the MAG hierarchy. We associate each publication with one or more of the 292 level 1 fields, which are comparable to the granularity of classifications in other popular bibliographic databases such as WoS. The validity of our approach is demonstrated by the similarity of our results on the longitudinal trends of interdisciplinarity of publications (Fig. 2a) with those reported in Gates et al. (17), which relied on WoS data.

In this study, we specifically use the level 1 field information from the MAG hierarchy. We associate each publication with one or more of the 292 level 1 fields, a granularity comparable to the subject categories in WoS. The validity of this approach is supported by the similarity of our results regarding longitudinal trends in publication interdisciplinarity (Fig. 2a) with those reportedin Gates et al. (17), which relied on WoS data.

### Field representation in a grant (labeled-LDA)

A key empirical challenge in quantifying the interdisciplinarity of grants is systematically assigning grants to the research fields they belong to. Here, we use a new measurement approach using labeled-LDA (64), allowing us to estimate the probability that a given grant is associated with a particular scientific field based on its abstract. Specifically, we train our model on a sample of 572,302 paper abstracts and their one or more field-of-study labels. We obtain this sample through random sampling of 1 million papers from the MAG dataset but exclude papers without level 1 field label or with abstracts under 100 words. The resulting model constructs a one-to-one correspondence between latent topics and labels, enabling us to learn a probability distribution of wordfield associations. We validate our model through manual inspections of these word-field associations as well as out-of-sample classification tasks (see Note S3; Table S1 lists the top 10 words per field by probability and FREquency and EXclusivity score, FREX). Additionally, by applying our methods to papers, we find that the distances between fields computed by the labeled-LDA method and citation patterns (described in the “Distance between fields” section) exhibit a moderate positive correlation (Pearson’s r = 0.451, 95% CI 0.443–0.459, P < 0.001), showing general consistency between our method and the literature (see Note S3 for more contextualization). These validation results also indicate that the used field categories are conceptually coherent and align well with general understandings of fields of study, thereby supporting the validity of MAG’s field categories.

In applying the trained labeled-LDA model to individual grant abstracts, we calculate the probability of a grant being associated with specific scientific fields. In our assessment of grant interdisciplinarity, we renormalize the field probabilities by excluding those with the lowest probability score, deemed irrelevant, to vary the number of pertinent fields (capturing the notion of volume and variety in the defined interdisciplinarity below). The estimation of field probabilities of grants is analogous to the vector of probabilities that a publication is associated with research fields as described below (see the “Field representation in a paper” section). Note that we replicate the main results without the renormalization process. Furthermore, our approach is not confined to a mere classification task. It is highly adept at estimating document-label “relevance” in probabilities across multiple predefined labels, which is particularly useful when a coherent labeling scheme is absent in one system (i.e. “grants”) but can be

###### Downloaded from https://academic.oup.com/pnasnexus/article/5/3/pgag057/8509178 by Korea Inst of Sci & Tech user on 24 March 2026

extrapolated from another (i.e. “papers”). This capability enables us to analyze both research grants and publications under a unified field classification scheme (see Note S3 for more details).

### Field representation in a paper

Following previous research (17, 18), we use a paper’s references to estimate interdisciplinary inspiration and its citations to estimate the interdisciplinary impact of a paper. We first represent each publication by a vector over 292 scientific fields, p. By considering all references of a paper, we compute the paper’s probability to belong to field i (pi) as a fraction of references that are associated with field i. We apply the same process when we consider citations of a paper.

### Distance between fields

As scientific fields vary in their proximity, we compute the distance between fields by estimating the overall knowledge stock within a discipline. In particular, we consider the cumulative reference or citation vectors vi over a set of n papers within the field i, where vi = { p1,i, . .., pn,i}. The distance, dij, is then defined as the cosine distance between fields i (vi) and j (vj),

vi · vj |vi|·|vj|

dij = 1 −

.

Here, fields that exhibit similar proportion distributions across papers (i.e. they tend to co-occur or appear together in the same reference or citation lists) have a small distance dij ≈ 0, while fields that rarely co-occur (indicating disjoint knowledge domains) have a large distance dij ≈ 1. Using an M × N discipline proportion matrix of Pi values (for each row, i.e. paper,

􏽐

i pi = 1), we compute the cosine distances between all field pairs. Note that the distances between fields that were determined from references and citations are highly similar (Pearson’s r = 0.978, 95% CI 0.978–0.978, P < 0.001), indicating the robustness of this approach.

discipline), whereas an RS score of 1 corresponds to the highest level of interdisciplinarity.

To provide more comprehensive understanding, in Note S2, we discuss discrepancies in various measurement approaches of interdisciplinarity and potential confounding factors related to our interdisciplinary measure (e.g. the number of fields associated with a paper, which has also been increasing over time; Fig. S8).

### Ethics statement

As part of the model validation described in Note S3, we conducted a manual validation of field representations learned by labeled-LDA with crowdworkers recruited through Amazon Mechanical Turk. The Institutional Review Board of New York University Abu Dhabi reviewed this activity and determined that it does not constitute Human Subjects Research. The task involved structured annotation in which workers applied predefined rating scales to evaluate word-field relevance (see Figs. S16 and S17 for the survey instructions and an example question). No demographic information, personal identifiers, or data reflecting participants’ beliefs, opinions, or other individual characteristics were collected, and the activity was strictly limited to a human intelligence task. Informed consent was obtained from all participants prior to the start of the task.

## Acknowledgments

This work uses data sourced from Dimensions.ai through researcher access plans. The major part of this research is carried out during M.P.’s research fellowship at the Center for Science of Science and Innovation at Northwestern University.

## Supplementary Material

Supplementary material is available at PNAS Nexus online.

### Grant and paper interdisciplinarity (RS diversity)

Our definition of interdisciplinarity emphasizes “diversity” and “coherence,” reflecting the integration of knowledge from multiple research fields and the intensity of relations between these knowledge bodies (62). Numerous metrics, including network and entropy measures, have been proposed to assess interdisciplinarity, possibly yielding inconsistent results (62, 65, 66). However, consensus among scholars stipulates that simply counting the number of disciplines that occur in references and citations is inadequate for properly quantifying interdisciplinarity. A more comprehensive approach considers not only the count but also the relative proportion of each discipline (capturing entropy) and the distance between disciplines (reflecting the intrinsic dissimilarity between disciplines) (17, 21, 66, 67). For example, a paper primarily referencing computer science and information science is less diverse than one that equally draws from both computer science and economics. Consequently, RS diversity has emerged as a common measure to quantify interdisciplinary research (17, 18, 21, 24, 39, 66). The RS index of a grant or a paper is defined as

􏽘

RS(p) = 2 ×

pipjdij,

i≠j

where pi (pj) is the probability that the underlying grant (or paper) is associated with discipline i (j), while dij is the distance between discipline i and j. An RS score of 0 reflects a lack of interdisciplinarity (i.e. all references, citations, or grants are from the same

## Funding

D.W. was supported by the National Science Foundationgrant TF-2404035. S.W. was supported by the National Science Foundation grants 2123635 and 2210023. M.P. was partially supported by the NYUAD Center for Interacting Urban Networks(CITIES) and the Center for Interdisciplinary Data Science and Artificial Intelligence(CIDSAI), funded by Tamkeen under NYUAD Research Institute awards CG001 and CG016, respectively.

## Author Contributions

Minsu Park (Conceptualization, Funding acquisition, Investigation, Methodology, Resources, Validation, Visualization, Writing—original draft, Writing—review & editing), Suman Kalyan Maity (Validation, Visualization), Stefan Wuchty (Conceptualization, Funding acquisition, Project administration, Supervision, Writing—original draft, Writing—review & editing), and Dashun Wang (Conceptualization, Data curation, Funding acquisition, Project administration, Resources, Supervision, Writing—original draft, Writing—review & editing)

## Preprints

This manuscript was posted on a preprint at https://arxiv.org/abs/ 2303.14732.

###### Downloaded from https://academic.oup.com/pnasnexus/article/5/3/pgag057/8509178 by Korea Inst of Sci & Tech user on 24 March 2026

## Data Availability

The aggregated data and code necessary to reproduce the main figures are available in the Open Science Framework (OSF) repository: https://osf.io/fya39/. The raw data were obtained from Dimensions and Microsoft Academic Graph (MAG). While the full Dimensions dataset is proprietary and available via Dimensions AI (https://www.dimensions.ai), a comparable openaccess subset focusing on NSF and NIH grants is available through SciSciNet (https://www.nature.com/articles/s41597-023-02198-9). The MAG dataset remains publicly accessible via various sources, including Zenodo (e.g. https://zenodo.org/records/2628216).

## References

- 1 Van Noorden R. 2015. Interdisciplinary research by the numbers. Nature. 525:306–307.
- 2 Bromham L, Dinnage R, Hua X. 2016. Interdisciplinary research has consistently lower funding success. Nature. 534:684–687.
- 3 Rylance R. 2015. Grant giving: global funders to focus on interdisciplinarity. Nature. 525:313–315.
- 4 Ledford H. 2015. How to solve the world’s biggest problems. Nature. 525:308–311.
- 5 Institute of Medicine of the National Academies National Academy of Sciences, National Academy of Engineering. Facilitating interdisciplinary research. The National Academies Press, Washington, DC, 2005.
- 6 Bloom N, Jones CI, van Reenen J, Webb M. 2020. Are ideas getting harder to find? Am Econ Rev. 110:1104–1144.
- 7 Jones BF. 2009. The burden of knowledge and the “death of the renaissance man”: is innovation getting harder? Rev Econ Stud. 76: 283–317. https://doi.org/10.1111/j.1467-937X.2008.00531.x
- 8 Teodoridis F. 2018. Understanding team knowledge production: the interrelated roles of technology and expertise. Manag Sci. 64:3625–3648.
- 9 Leahey E, Beckman CM, Stanko TL. 2017. Prominent but less productive: the impact of interdisciplinarity on scientists’ research. Adm Sci Q. 62:105–139.
- 10 Lyall C, Bruce A, Marsden W, Meagher L. 2013. The role of funding agencies in creating interdisciplinary knowledge. Sci Public Policy. 40:62–71.
- 11 Jacobs JA, Frickel S. 2009. Interdisciplinarity: a critical assessment. Annu Rev Sociol. 35:43–65.
- 12 Rhoten D, Parker A. 2004. Risks and rewards of an interdiciplinary research path. Science. 306:2046.
- 13 Leahey E, Barringer SN. 2020. Universities’ commitment to interdisciplinary research: to what end? Res Policy. 49:103910.
- 14 Leahey E. 2018. The perks and perils of interdisciplinary research. Eur Rev. 26:S55–S67.
- 15 Collins R. The sociology of philosophies. Harvard University Press, 1998.
- 16 Cole S. 1983. The hierarchy of the sciences? Am J Sociol. 89: 111–139.
- 17 Gates AJ, Ke Q, Varol O, Barabási AL. 2019. Nature’s reach: narrow work has broad impact. Nature. 575:32–34.
- 18 Porter AL, Rafols I. 2009. Is science becoming more interdisciplinary? Measuring and mapping six research fields over time. Scientometrics. 81:719–745.
- 19 Chen S, Arsenault C, Larivière V. 2015. Are top-cited papers more interdisciplinary? J Informetr. 9:1034–1046.
- 20 Okamura K. 2019. Interdisciplinarity revisited: evidence for research impact and dynamism. Palgrave Commun. 5:141.


- 21 Wang J, Thijs B, Glänzel W. 2015. Interdisciplinarity and impact: distinct effects of variety, balance, and disparity. PLoS One. 10: e0127298.
- 22 Yegros-Yegros A, Rafols I, D’Este P. 2015. Does interdisciplinary research lead to higher citation impact? The different effect of proximal and distal interdisciplinarity. PLoS One. 10:e0135095.
- 23 Porter AL, Roessner JD, Cohen AS, Perreault M. 2006. Interdisciplinary research: meaning, metrics and nurture. Res Eval. 15:187–195.
- 24 Wagner CS, et al. 2011. Approaches to understanding and measuring interdisciplinary scientific research (IDR): a review of the literature. J Informetr. 5:14–26.
- 25 Xiang S, Romero DM, Teplitskiy M. 2025. Evaluating interdisciplinary research: disparate outcomes for topic and knowledge base. Proc Natl Acad Sci U S A. 122:e2409752122.
- 26 Fortin JM, Currie DJ. 2013. Big science vs. little science: how scientific impact scales with funding. PLoS One. 8:e65263.
- 27 Jacob BA, Lefgren L. 2011. The impact of research grant funding on scientific productivity. J Public Econ. 95:1168–1177.
- 28 Rigby J. 2013. Looking for the impact of peer review: does count of funding acknowledgements really predict research impact? Scientometrics. 94:57–73.
- 29 Tohalino JAV, Amancio DR. 2022. On predicting research grants productivity via machine learning. J Informetr. 16:101260.
- 30 Yan E, Wu C, Song M. 2018. The funding factor: a crossdisciplinary examination of the association between research funding and citation impact. Scientometrics. 115:369–384.
- 31 Jang H. 2022. Predicting funded research project performance based on machine learning. Res Eval. 31:257–270.
- 32 Li D, Azoulay P, Sampat BN. 2017. The applied value of public investments in biomedical research. Science. 356:78–81.
- 33 Leydesdorff L, Wagner C. 2009. Macro-level indicators of the relations between research funding and research output. J Informetr. 3:353–362.
- 34 Wang J, Shapira P. 2011. Funding acknowledgement analysis: an enhanced tool to investigate research sponsorship impacts: the case of nanotechnology. Scientometrics. 87:563–586.
- 35 de Solla Price DJ. Little science, big science. Columbia University Press, 1963.
- 36 Herzog C, Hook D, Konkiel S. 2020. Dimensions: bringing down barriers between scientometricians and data. Quant Sci Stud. 1: 387–395.
- 37 Wang K, et al. 2020. Microsoft academic graph: when experts are not enough. Quant Sci Stud. 1:396–413.
- 38 Visser M, van Eck NJ, Waltman L. 2021. Large-scale comparison of bibliographic data sources: Scopus, Web of Science, Dimensions, Crossref, and Microsoft Academic. Quant Sci Stud. 2:20–41.
- 39 Stirling A. 2007. A general framework for analysing diversity in science, technology and society. J R Soc Interface. 4:707–719.
- 40 Wuchty S, Jones BF, Uzzi B. 2007. The increasing dominance of teams in production of knowledge. Science. 316:1036–1039.
- 41 Ebadi A, Schiffauerova A. 2015. How to receive more funding for your research? Get connected to the right people. PLoS One. 10: e0133061. https://doi.org/10.1371/journal.pone.0133061
- 42 Stvilia B, et al. 2011. Composition of scientific teams and publication productivity at a national science lab. J Am Soc Inf Sci Technol. 62:270–283.
- 43 Jones BF, Wuchty S, Uzzi B. 2008. Multi-university research teams: shifting impact, geography, and stratification in science. Science. 322:1259–1262.


###### Downloaded from https://academic.oup.com/pnasnexus/article/5/3/pgag057/8509178 by Korea Inst of Sci & Tech user on 24 March 2026

- 44 Haeussler C, Sauermann H. 2020. Division of labor in collaborative knowledge production: the role of team size and interdisciplinarity. Res Policy. 49:103987.
- 45 Wu L, Wang D, Evans JA. 2019. Large teams develop and small teams disrupt science and technology. Nature. 566:378–382.
- 46 Uzzi B, Mukherjee S, Stringer M, Jones B. 2013. Atypical combinations and scientific impact. Science. 342:468–472.
- 47 Li L, Lin Y, Wu L. 20 November 2025. Innovation by displacement. arXiv 03723. https://doi.org/10.48550/arXiv.2512.03723, preprint: not peer reviewed.
- 48 Kuhn TS. The structure of scientific revolutions. University of Chicago Press, 1962.
- 49 Hill R, et al. 2025. The pivot penalty in research. Nature. 642: 999–1006. https://doi.org/10.1038/s41586-025-09048-1
- 50 Kraut R, Galegher J, Egido C. Relationships and tasks in scientific research collaborations. In: Proceedings of the ACM Conference on Computer Supported Cooperative Work, CSCW; 1986 December 3–5; Austin, TX. Association for Computing Machinery; 1986. p. 229–245.
- 51 Hara N, Solomon P, Kim SL, Sonnenwald DH. 2003. An emerging view of scientific collaboration: scientists’ perspectives on collaboration and factors that impact collaboration. J Am Soc Inf Sci Technol. 54:952–965.
- 52 Cummings JN, Kiesler S. 2005. Collaborative research across disciplinary and organizational boundaries. Soc Stud Sci. 35:703–722.
- 53 Jeffrey P. 2003. Smoothing the waters: observations on the process of cross-disciplinary research collaboration. Soc Stud Sci. 33:539–562.
- 54 Laudel G. 2006. Conclave in the Tower of Babel: how peers review interdisciplinary research proposals. Res Eval. 15:57–68.
- 55 Goring SJ, et al. 2014. Improving the culture of interdisciplinary collaboration in ecology by expanding measures of success. Front Ecol Environ. 12:39–47.


- 56 Bracken LJ, Oughton EA. 2006. “What do you mean?” The importance of language in developing interdisciplinary research. Trans Inst Br Geogr. 31:371–382.
- 57 Laursen BK, Motzer N, Anderson KJ. 2022. Pathways for assessing interdisciplinarity: a systematic review. Res Eval. 31:326–343.
- 58 Committee on Facilitating Interdisciplinary Research, National Academy of Sciences, and National Academy of Engineering. Facilitating interdisciplinary research. National Academies Press, 2004.
- 59 Vladova G, Haase J, Friesike S. 2025. Why, with whom, and how to conduct interdisciplinary research? A review from a researcher’s perspective. Sci Public Policy. 52:165–180.
- 60 Abbott A. Chaos of disciplines. University of Chicago Press, 2001.
- 61 Sugimoto CR, Weingart S. 2015. The kaleidoscope of disciplinarity. J Doc. 71:775–794.
- 62 Wang Q, Schneider JW. 2020. Consistency and validity of interdisciplinarity measures. Quant Sci Stud. 1:239–263.
- 63 Wang K, et al. 2019. A review of Microsoft academic services for science of science studies. Front Big Data. 2:45.
- 64 Ramage D, Hall D, Nallapati R, Manning CD. Labeled LDA: a supervised topic model for credit attribution in multi-labeled corpora. In: Proceedings of the Conference on Empirical Methods in Natural Language Processing; 2009 August 6–7; Singapore. Association for Computational Linguistics; 2009, p. 248–256.
- 65 Leydesdorff L, Rafols I. 2011. Indicators of the interdisciplinarity of journals: diversity, centrality, and citations. J Informetr. 5:87–100.
- 66 Qun Z, Menghui Y. 2023. An efficient entropy of sum approach for measuring diversity and interdisciplinarity. J Informetr. 17: 101425.
- 67 Larivière V, Haustein S, Börner K. 2015. Long-distance interdisciplinarity leads to higher scientific impact. PLoS One. 10:e0122565.


###### Downloaded from https://academic.oup.com/pnasnexus/article/5/3/pgag057/8509178 by Korea Inst of Sci & Tech user on 24 March 2026

