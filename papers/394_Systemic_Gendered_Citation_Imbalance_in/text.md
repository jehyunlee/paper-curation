# arXiv:2603.23273v1[cs.DL]24 Mar 2026

## Systemic Gendered Citation Imbalance in Computer Science: Evidence from Conferences and Journals

Kazuki Nakajima1, Yuya Sasaki2, Sohei Tokuno3, and George Fletcher4 1Tokyo Metropolitan University 2The University of Osaka 3Nara Institute of Science and Technology 4Eindhoven University of Technology

Abstract

Gender imbalance persists across science, technology, engineering, and mathematics (STEM) fields, including computer science, where it appears in researcher demographics, productivity, recognition, hiring, and career progression. Given computer science’s rapid expansion and global influence, addressing this imbalance is essential for broadening participation and fueling innovation. Although journal-oriented disciplines exhibit consistent gender imbalances in citation practices, it remains unclear whether similar patterns arise in the conference-centric culture of computer science. Here, we systematically investigate gender imbalance in citations of conference and journal papers in computer science. We find that papers for which a woman is listed as either first or last author receive fewer citations than expected, partly because of homophilic citation tendencies (i.e., authors tend to cite papers that share specific attributes). This imbalance is especially pronounced for conference papers–particularly those published at top-tier venues–relative to journals. Moreover, we find that the prominence of the first or last author and the structure of their local co-authorship networks are potential drivers of these imbalances. By exploring how conference-centric publishing practices can amplify systemic imbalances in computer science, our study offers insights that may inform efforts to foster more equitable representation in academia.

Keywords: Science of science, gender imbalance, citation practice, citation networks

#### 1 Introduction

Gender imbalance remains a pervasive issue across academia worldwide. Although the proportion of female authors has been steadily increasing, women remain underrepresented in senior authorship positions and leadership roles across multiple disciplines and regions, compared to the gender ratio at undergraduate and graduate levels [44, 31, 85]. In addition, systemic disparities persist in research productivity [104, 97, 33, 1], academic awardees [49, 51], faculty hiring [57, 77], access to funding [6, 103], and citations received by authors [35], all of which collectively disadvantage female researchers throughout their careers. Observed across various disciplines, these imbalances reflect a broader pattern of inequity embedded within the academic ecosystem. Addressing such systemic imbalances is essential for achieving equity and sustainability in academia and promoting greater scientific diversity and innovation [88, 83].

Citations form the basis for many measurements and indicators in “science of science” studies, informing assessments of the impact of publications, researchers, institutions, and countries, and key

decisions in academic evaluation [22, 54]. While citations offer valuable insights into the structure and development of scientific knowledge, citation statistics are often shaped by a range of social, structural, and epistemic factors that introduce systematic imbalances. For example, average citation counts vary substantially across disciplines [70], and many journals receive a disproportionate share of their citations from a small set of publication venues [41]. Similarly, research-active countries tend to receive more citations than expected given the subject areas in which they publish [28]. In the context of gender, recent studies have identified consistent under-citation of women-authored papers, partly due to homophily, skewed citation practices, and self-citation patterns favoring male authors [39, 18, 86]. Such imbalances distort the production and flow of scientific knowledge and undermine the neutrality of citations as indicators of scholarly value.

Computer science stands out globally for its vast and expanding student and researcher population, extensive research output, and significant investment. First, the pipeline of human resources in science, technology, engineering, and mathematics (STEM)–including computer science–is immense and growing. In 2020 alone, China awarded 3.6 million new STEM degrees, India 2.6 million, and the United States 820,000, with countries such as Brazil and Mexico outpacing Iran and Japan [62]. This growth is often driven by computer science programs; for example, North African nations like Tunisia and Algeria report high STEM graduation rates owing to robust computing and engineering curricula [7]. The computer science community has grown in tandem with enrollment, and in the European Union, the information and communication technology sector accounts for 20% to 50% of total research and development personnel [20]. Second, computer science publications represent a substantial share of global research output–roughly one-tenth [89]–and increased by 21% from 2015 to 2019, with subfields such as artificial intelligence and robotics experiencing especially rapid growth [75]. Third, public investment in computer science research and education has reached unprecedented levels worldwide, as governments prioritize digital innovation and expand funding for computing and artificial intelligence [75]. For instance, the National Science Foundation in the United States allocated approximately one billion dollars to its Computer and Information Science and Engineering Directorate for fiscal year 2024 [90]. These indicators highlight the discipline’s exceptional scale, growth, and influence, making it imperative to examine whether its expansion is accompanied by equitable representation.

Gender imbalance affects many aspects of computer science, including authorship, productivity, recognition, research careers, and academic positions. Estimates suggest that women account for only 15–30% of computer science authors worldwide [31, 24], with progress increasing at a slow pace [14]. Moreover, the extent of imbalance varies across subfields [24, 67], and female authors face additional disadvantages–such as shorter career lengths–resulting in fewer publications and citations relative to their male counterparts [36, 33, 48]. This imbalance grows more pronounced at advanced career stages, as seen in the United States, where women comprise only 15% of tenure-track faculty in computer science [13, 102]. The underrepresentation of women in senior positions may stem from differential retention and advancement rates, with many leaving academia before attaining these ranks [82, 48]. Given the discipline’s rapid expansion and global influence, addressing gender inequity through sustained, data-driven investigation is essential and urgent to ensure that the future of computer science is equitable, inclusive, and reflective of its full talent pool.

Research practices–such as authorship, publication venues, and citation behavior–and their links to gender imbalance vary significantly across disciplines. Recent studies of gendered citation imbalance (i.e., citation imbalance regarding authors’ gender) have focused on journal papers within single disciplines, including astronomy [8], communications [101], dentistry [55], economics [17], environmental studies [61], international relations [50], medicine [11], neuroscience [18], physics [86], and plant science [66]. However, the extent of such imbalances in computer science remains largely unknown. Findings from other disciplines cannot be generalized to computer science, given its

unique publishing culture. Unlike in most disciplines where journals dominate, computer scientists often present their work at conferences, which involve short peer-review cycles on fixed schedules to expedite dissemination [98, 21]. Furthermore, conferences and journals are ranked based on citation metrics, with top-ranked venues considered especially prestigious [26, 95, 99, 47]. The rapid growth of top-tier conferences has stretched organizing committees beyond capacity, fueling concerns about the thoroughness of peer reviews [98, 21, 80]. This starkly different publication culture highlights the need to examine how conference-centric practices influence gendered citation patterns.

In this study, we systematically analyze a unique citation network of computer science papers written by authors with assigned binary genders. We characterize gendered citation patterns as the difference between observed citation behavior and that expected under reference models that account for key structural properties of the network. This work significantly extends our previous study, which focused exclusively on citations between conference papers in computer science [59], by incorporating journal publications into our dataset and addressing the following new research questions: (i) What are the patterns of gender imbalance in citations of both conference and journal papers within computer science? (ii) How does gender imbalance in citations differ between conferences and journals? (iii) What characteristics of citing papers are associated with gendered citation behavior?

#### 2 Methods

##### 2.1 Construction of a new dataset

We constructed a unique dataset of 394,432 papers published in computer science conferences and journals, along with 752,742 citations. By integrating publication data from two open databases, we enriched each paper’s metadata with bibliographic details, authors’ binary genders, authorship information, citations, publication venues, and research topics and subfields. We also identified venue ranks for conferences and journals using external ranking databases. Because investigating gendered citation behavior requires accounting not only for the gender of authors but also for various author- and paper-level characteristics that may influence citation patterns, this enriched dataset enables a more comprehensive analysis of gendered citation imbalance in computer science than in our previous work [59]. We describe the dataset construction process below.

###### 2.1.1 DBLP

The DBLP Computer Science Bibliography (originally an acronym for “DataBase systems and Logic Programming”, subsequently referred to as DBLP) indexes publications in computer science, encompassing both conferences and journals [93, 45]. DBLP has served as a primary bibliographic resource for computer science and has been widely used for bibliometric analyses on the research landscape of the discipline (e.g., Refs. [68, 71, 81, 9, 38, 72, 59]). We used its July 1, 2024 snapshot, which included 7,034,299 papers published in 13,007 conferences and 2,031 journals between 1950 and 2024. Each paper provides its title, publication year, authors’ IDs, authorship order, and the name of the associated conference or journal. DBLP employs a proprietary algorithm to assign unique IDs to authors, identifying 3,609,641 authors. Previous evaluation showed that DBLP’s author name disambiguation performance is highly competitive, possibly due to its hybrid approach combining algorithmic disambiguation and manual error correction [37]. Each ID consists of the author’s full name, optionally followed by a four-digit number if multiple authors share the same name [92]. We applied this rule to recover each author’s full name from their assigned ID. While DBLP offers precise and well-disambiguated venue information, it lacks the broader bibliographic

coverage and topic classifications.

###### 2.1.2 OpenAlex

OpenAlex provides hundreds of millions of publication records with extensive metadata across multiple disciplines [69]. We used its September 27, 2024 snapshot, which contained 155,449,238 papers published between 1950 and 2024. For each paper v, we extracted its title, publication date, primary research topic and subfield, authors’ names and affiliations, authorship order, and the list of papers cited by v. While every paper lists at least one author, some lack affiliation information for certain authors. Each paper is classified under one of 4,516 research topics, which are more granular than the 252 subfields to which they belong [63]. Although OpenAlex provides comprehensive cross-disciplinary coverage of publication and citation data [16], we found that many conference and journal names for computer science publications were either missing or not properly disambiguated.

###### 2.1.3 Matching papers between OpenAlex and DBLP

To reconcile the limitations of both databases, we matched each DBLP paper with its corresponding paper in OpenAlex using three criteria: (i) identical publication year, (ii) matching order of authors’ last names, and (iii) a title discrepancy of no more than 25%, measured by the Levenshtein distance normalized by the longer title. These criteria have been previously applied to align multiple publication datasets [33]. The relatively generous 25% threshold for Levenshtein distance accounts for common discrepancies between databases, such as different encodings of mathematical symbols and the inclusion or exclusion of subtitles. We treated the last space-separated word in an author’s full name as their last name [58]. Using this approach, we identified 3,720,575 DBLP papers with unique matches in OpenAlex. For each matched paper v, we supplemented the DBLP record with OpenAlex metadata, including the title, publication date, primary research topic and subfield, authors’ names and affiliations, authorship order, and the list of papers cited by v. Hereafter, we refer to these 3,720,575 enriched papers as D. There are 23,274,023 citations among papers in D.

###### 2.1.4 Conference and journal ranks

We use the following ranking systems to capture the structure of publication prestige in computer science. While some resources use a curated list of top-tier venues (e.g., CSRankings [15]), our analysis requires a multi-tiered classification to examine citation imbalances across a broad spectrum of publication venues.

We use the 2021 CORE conference ranking [91] to determine the ranking of computer science conferences. This system evaluates each conference based on its reputation and a range of metrics (e.g., citation statistics of papers and authors, and acceptance rates)1. We focus on the 768 conference names assigned to four ranks–A∗, A, B, and C–in which A∗ is the highest and C is the lowest.

Similarly, we use the 2021 SCImago Journal Rank (SJR) [76] to rank computer science journals. SCImago draws on Scopus data covering over 34,100 journal titles from more than 5,000 publishers2. We restricted our selection to journals indexed under the ‘Computer Science’ subject area for the year 2021. This filtering process yielded 1,734 journals assigned to quartiles Q1, Q2, Q3, or Q4, with Q1 being the highest and Q4 the lowest. While SCImago database indexes journals across

- 1https://drive.google.com/file/d/1DQixeK53tlq_jh6IspIHroiwu1pmM6-y/edit (accessed April 2024)
- 2https://www.scimagojr.com/aboutus.php (accessed November 2024)


disciplines, previous analysis has shown that SJR correlates strongly with the Journal Impact Factor specifically for computer science journals [78].

Because DBLP frequently abbreviates conference and journal names, many entries do not directly match those in the CORE and SCImago data. Therefore, for each venue appearing in D, the first and second authors (KN and YS) manually assigned a venue rank (A∗, A, B, C, Q1, Q2, Q3, or Q4) or labeled it “N/A” (not applicable). This process yielded 60 A∗-ranked, 130 A-ranked, 286 B-ranked, and 233 C-ranked conferences, as well as 341 Q1-ranked, 301 Q2-ranked, 209 Q3-ranked, and 128 Q4-ranked journals.

###### 2.1.5 Prominence and coauthors of authors

There are 2,430,109 unique author IDs in the papers comprising D. For each author z, we identify all papers listing z as an author (hereafter, z’s papers) and compute two characteristics: (i) prominence, defined as the total number of citations received by z’s papers, and (ii) coauthors, the set of authors who have coauthored at least one paper with z. We calculate these metrics using the entire dataset and treat them as static attributes representing the author’s prominence and co-authorship networks, which is consistent with our use of static rankings of conferences and journals.

###### 2.1.6 Country of affiliation and gender of authors

We assign a country of affiliation to each author based on the affiliations listed in their publications [33, 58]. Specifically, we count the frequency of each country in an author z’s affiliations and assign the most frequent country if it is unique. If no country is uniquely most frequent, we exclude the author from the dataset. We assigned a country of affiliation to 2,059,647 of the 2,430,109 authors in our dataset.

We then assign binary gender to each author using the method developed in Ref. [58], which incorporates the author’s country of affiliation, first publication year, and first name. This method addresses known challenges in name-based gender inference, particularly for East Asian names [58], but is limited to binary classification (see the Discussion Section for further limitations).

To extract first-name candidates from an author’s full name, we follow naming conventions based on their country of affiliation. For authors whose country of affiliation is China, Japan, or South Korea and whose name consists of k space-separated words, denoted by w1,...,wk, we use w1, w1w2, ..., and w1 ···wk−1 as k − 1 candidates of their first name. For example, the first-name candidates for the name “Gil Dong Hong” are “Gil” and “Gil Dong”. For the remaining authors, we assume that the first space-separated word in their name is their sole first-name candidate.

We provide the first-name candidates of an author and their country of affiliation to the Gender API3, which was used in previous studies on gender imbalance [18, 86]. The API returns one of three labels (“female,” “male,” or “unknown”) along with an accuracy score and sample size for each inputted first-name candidate.

We apply thresholds to both the accuracy score and sample size to exclude low-confidence results. If multiple first-name candidates exist for an author, we compare the highest femaleclassified accuracy with the highest male-classified one. We assign “female” or “male” according to which score is higher; if they are equal, no gender is assigned. Thresholds were set based on country of affiliation and first publication year to ensure at least 90% classification accuracy on validation sets with ground-truth gender labels [58]. Setting different thresholds based on country of affiliation is intended to address potential country imbalances in the gender assignment process,

3https://gender-api.com/en/ (accessed April 2024)

as the precision of name-based gender inference can depend on a name’s country of origin [74]. We use the same threshold values as in Ref. [58] (see Supplementary Section S3 in Ref. [58]).

In total, we assigned both country of affiliation and gender to 1,257,016 of the 2,430,109 authors in our dataset.

###### 2.1.7 Country of affiliation and gender category of papers

We assign each paper’s country of affiliation and gender category following Ref. [58]. Specifically, we focus on 1,399,106 papers in D that satisfy one of two criteria: (i) a single author with an assigned country and gender, or (ii) the first and last authors sharing the same country of affiliation, each with an assigned gender. We then assign each paper the country of affiliation of its single author or its first and last authors. We also classify each paper into one of four gender categories (“MM,” “MW,” “WM,” “WW”) based on the genders of the first and last authors [18, 86]. Specifically, the first letter (M or W) indicates whether the first author is a man or a woman, while the second letter denotes the gender of the last author. We categorized sole-authored papers by men or women as MM or WW, respectively. We assume that the first and last authors play primary roles in the research and writing of computer science papers, which aligns with common practices in many subfields, although alphabetical ordering is used in some subfields [79].

###### 2.1.8 Citations

We focus on the 672,082 papers in D, each assigned a country of affiliation, a gender category (MM, MW, WM, or WW), and a venue rank (A∗, A, B, C, Q1, Q2, Q3, or Q4), and the citations occurring exclusively among these papers. Given an observed citation from paper u to paper v, we say u “made” the citation and v “received” it. We remove any citation if: (i) v’s publication date is ten years older than u’s [18, 58], (ii) u and v share at least one author (self-citation) [58], (iii) the coauthors of u’s first or last author overlap with v’s authors, or (iv) u’s publication year is before 1990 (due to the small number of WW papers before 1980). Regarding criterion (i), we followed Refs. [18, 58]; this ten-year citation window reflects contemporary citation behavior and prevents our analysis from aggregating across disparate eras with substantially different author demographics. We then discard papers that neither make nor receive any citations, leaving a final set of 394,432 papers and 752,742 citations. Table 1 summarizes the statistics of our data, comparing the initial matched dataset (D) with the final dataset. Note that authors’ gender and venue ranks are not assigned in the initial matched dataset D. We provide additional information on our dataset in Supplementary Section S1.

##### 2.2 Reference models for citation networks

Reference models randomize the citations made by each paper while preserving certain structural properties of the original network. Dworkin et al. introduced the random-draws model as a reference model [18], but it preserves only the number of citations made by each paper, which limits its ability to capture how other network properties contribute to gender imbalance in citations. To address this gap, we propose a family of reference models that preserve the number of citations made by each paper and up to two additional properties [58]: homophily in citations [12, 106] and heterogeneity in the number of citations received per paper [19, 106]. Table 2 outlines the properties each model preserves. In the following, we denote by V = {v1,...,vN} the set of all the papers, E the set of citations in the network, and M = |E| the number of citations, where N is the number of papers.

Table 1: Basic statistics of the initial matched dataset (D) and the final dataset.

###### Initial Matched Dataset

Meaning Count Papers 3,720,575 Citations 23,274,023 Authors 2,430,109 Conferences 10,735 Journals 2,004 Countries of affiliation 214 Research subfields 243 Research topics 4,351 Final Dataset

Meaning Count Papers 394,432 Citations 752,742 Gender-assigned authors 285,406 Conferences 631 Journals 955 Countries of affiliation 140 Research subfields 238 Research topics 2,900 MM papers 298,063 (75.6%) MW papers 30,970 (7.8%) WM papers 43,727 (11.1%) WW papers 21,672 (5.5%) Female authors 54,229 (19.0%) Male authors 231,177 (81.0%) A∗-ranked conferences 60

- A-ranked conferences 124

- B-ranked conferences 254

- C-ranked conferences 193


- Q1-ranked journals 338

- Q2-ranked journals 294

- Q3-ranked journals 203

- Q4-ranked journals 120


Table 2: Properties to be preserved in each reference model.

|Model|Properties to be preserved|
|---|---|
|Random-draws<br><br>|• Number of citations made by each paper|
|Homophilic-draws|• Number of citations made by each paper<br>• Homophily in citation patterns<br><br><br>|
|Preferential-draws|• Number of citations made by each paper<br><br>• Homophily in citation patterns<br><br>• Heterogeneity in the number of citations received per paper<br><br><br>|


- 2.2.1 Random-draws model We first describe the random-draws model [18]. Let V RD(i) denote the set of papers that paper vi ∈ V could potentially cite under this model. Following our citation criteria, V RD(i) comprises papers that (i) are at most ten years older than vi, (ii) do not share any author with vi, and (iii) do not share any author with the coauthors of vi’s first or last author. For each citation (vi,vj) ∈ E, we randomly draw vj′ ∈ V RD(i) with uniform probability and replace (vi,vj) by (vi,vj′) with replacement. The random-draws model preserves the number of citations made by each paper in the original network.

- 2.2.2 Homophilic-draws model

We extend the random-draws model to preserve homophily in citations, referring to this model as the homophilic-draws model. Let S represent a set of paper characteristics (beyond gender category) potentially relevant for homophily in citations. In this study, we focus on (i) country of affiliation, (ii) primary research topic, and (iii) venue rank. Note that S is not limited to these attributes and may vary across disciplines.

For each citation (vi,vj) ∈ E, let V HD(i,j,S) be the subset of V RD(i) (from the random-draws model) consisting of papers that share all attributes in S with vj. Note that V HD(i,j,S) includes vj. In our analyses, V HD(i,j,S) contains papers matching vj in country of affiliation, research topic, and venue rank. We replace each citation (vi,vj) by (vi,vj′) with replacement, where vj′ is uniformly drawn from V HD(i,j,S). The homophilic-draws model preserves the number of citations made by each paper and the number of citations between pairs of countries of affiliation, topics, and venue ranks.

- 2.2.3 Preferential-draws model


We further extend the homophilic-draws model to preserve, approximately, the heterogeneity in citations received per paper. We refer to this as the preferential-draws model, which randomizes the citations made by each paper while respecting the characteristics in S and preferential attachment dynamics.

First, we sort the papers by publication date in ascending order, denoted {vx1,...,vxN}, where

- vx1 is the oldest and vxN is the newest. Let ci,l,PD be the number of citations received by paper
- vi from papers vx1,...,vxl in the model. We initialize ci,l,PD = 0 for all i and l. For each citation (vxl,vj) ∈ E, we define


V PD(xl,j,S) = vj′ ∈ V HD(xl,j,S) ⌊ln(cj′,l−1,PD + 1)⌋ = ⌊ln(cj,l−1,PD + 1)⌋ ,

where ⌊x⌋ is the floor function. Thus, V PD(xl,j,S) contains papers in V HD(xl,j,S) that have received roughly the same number of citations as vj from {vx1,...,vxl−1}. We use the natural logarithm to group papers into bins corresponding to a logarithmic scale of the number of citations received. This log-binning accounts for a heavy-tailed distribution of the number of citations received by a paper and prevents the candidate pool (i.e., V PD(xl,j,S)) from becoming too sparse while approximately preserving the number of citations received by the paper being replaced.

We then sequentially randomize the citations made by vxl from l = 2 to N. For each citation (vxl,vj) ∈ E, we randomly select vj′ from V PD(xl,j,S) with uniform probability, replacing (vxl,vj) by (vxl,vj′) with replacement. Note that vx1 makes no citations, as it is the oldest paper. This sequential process allows the citation count (i.e., cj,l−1,PD) to update dynamically and approximates the preferential attachment dynamics, where papers that accumulate citations early in the process become more likely to be cited by subsequent papers.

Like the homophilic-draws model, this preferential-draws model preserves the number of citations made by each paper and homophily in citations with respect to the country of affiliation, research topic, and venue rank. In addition, it approximately preserves the original distribution of the number of citations received per paper. See Supplementary Section S2 for a pseudocode of the preferential-draws model. See Appendix A for a comparison of structural properties among the three reference models.

##### 2.3 Characterizing gender imbalance in citations

A standard practice in network analysis is to compare the original network with randomized instances generated by reference models in terms of structure and dynamics [60, 53, 65, 23]. We characterize gender imbalance in citations by the difference in citation patterns regarding authors’ gender between the original network and reference models. Consider two subsets of papers, denoted by Vfrom and Vto. We measure the extent to which the papers in Vfrom over- or under-cite the papers in Vto and in a given gender category g ∈ {MM,MW,WM,WW} [18, 86]. We first count the citations made by the papers in Vfrom to those in Vto and in g in the original network, which we denote by ng,obs. Then, we independently generate 100 randomized networks using the reference model. We denote by µg,rand and σg,rand the mean and standard deviation of the number of citations made by the papers in Vfrom to those in Vto and in g across the 100 randomized instances. We define the over/under-citation made by the papers in Vfrom to those in Vto as (ng,obs −µg,rand)/µg,rand [18, 86].

To test the statistical significance of the over/under-citation, we calculate the Z score defined

by (ng,obs − µg,rand)/σg,rand. We say that the papers in Vfrom significantly over-cite those in Vto if the Z score is larger than 3.09 (i.e., p value is lower than 0.001). Similarly, we say that the papers

in Vfrom significantly under-cite those in Vto if the Z score is lower than −3.09 (i.e., p value is lower than 0.001).

##### 2.4 Matched-pair analysis of gender imbalance in citations

To examine which types of papers contribute to gender imbalance in citations, we compare over/undercitation patterns while controlling for key paper-level characteristics [18, 86]. We adopt a matchedpair analysis, as used in previous studies on gender imbalance [33, 46], to identify which characteristics of papers that made citations are associated with stronger gender imbalance in their citation behavior.

Let M and M′ be two disjoint subsets of papers. We generate a set of matched pairs as follows. For each paper u ∈ M, we randomly select (without replacement) a paper v ∈ M′ that matches u on the following characteristics: (i) publication year, (ii) country of affiliation, (iii) primary

Table 3: Number of matched paper pairs used in the analysis. Each row shows a pair of paper subsets M and M′, and the number of matched pairs generated between them.

|M|M′<br><br>|Matched pairs|
|---|---|---|
|WW papers|MM papers<br><br>|10,985|
|MM (conference) MM (with prominent authors) MM (top half of MAor)|MM (journal)<br><br>MM (without prominent authors)<br><br>MM (bottom half of MAor)|49,860<br><br>29,290<br><br>50,124<br>|
|WW (conference) WW (with prominent authors) WW (top half of MAor)|WW (journal)<br><br>WW (without prominent authors)<br><br>WW (bottom half of MAor)<br><br>|1,215 741 1,166|


research subfield, and (iv) number of citations made by paper. We repeat this process 100 times to generate 100 independent sets, denoted by {(M,M′i)}100i=1, where M′i ⊆ M′ for i = 1,...,100. We compute ∆M,g, the over/under-citation made by papers in M to papers in a gender category g ∈ {MM,MW,WM,WW}. Similarly, for each i = 1,...,100, we compute ∆M′

i,g, the over/undercitation made by papers in M′i to papers in g. Let ∆¯M′,g and sM′,g denote the mean and standard deviation, respectively, of these 100 values. The test statistic is defined as

∆¯M′,g − ∆M,g sM′,g/√100

t =

(1)

We test the null hypothesis that ∆M,g = ∆¯M′,g, against the alternative that they differ. If the resulting p-value is below 0.001, we reject the null hypothesis in favor of the alternative.

We first test whether the gender of citing authors is associated with citation imbalance using matched MM–WW paper pairs. Next, we examine three additional characteristics of citing papers:

- (i) venue type (conference versus journal), (ii) involvement of “prominent” authors, and (iii) local coauthorship network. For the characteristic (ii), we define prominent authors as the top 1% of each gender by author prominence. For the characteristic (iii), we use the man-author over-


representation (MAor), defined as the proportion of male coauthors of the first or last author of a paper u, minus the overall proportion of male authors in the dataset [18]. See Section 2.1.5 for the definitions of authors’ prominence and coauthors. For each characteristic, we split the MM papers into two disjoint sets–specifically, MM conference versus journal papers; MM papers with a prominent first or last author versus those with neither; and MM papers in the top versus bottom half of MAor. We then generate matched pairs between the two sets. For WW papers, we apply the same procedure as for MM papers. Table 3 reports the number of matched paper pairs used in our analysis, including MM–WW comparisons and within-group comparisons based on venue type, involvement of prominent authors, and local coauthorship network.

#### 3 Results

##### 3.1 Quantifying gendered citation imbalance in computer science

We constructed a citation network comprising 394,432 papers published in computer science conferences and journals, along with 752,742 citations between them. We classified each paper into

(a) (b)

| |85%<br><br>4% 4% 7%<br><br>67%<br><br>10%<br><br>16%<br><br>7%<br><br>MM<br><br>MW WM WW| | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


| | |
|---|---|
| | |


| | | |
|---|---|---|
| | | |


- Figure 1: Time-varying demographics of published papers by gender category in computer science.


- (a) Proportions of papers by gender category over time. (b) Proportions of papers in gender categories MW, WM, or WW across 11 subfields of computer science over time.


one of four gender categories–MM, MW, WM, or WW–based on the genders of its first and last authors. Here, the first letter (M or W) denotes the gender of the first author, and the second letter that of the last author. Sole-authored papers by men or women are categorized as MM or WW, respectively. Our dataset includes 298,063 MM papers (75.6%), 30,970 MW papers (7.8%), 43,727 WM papers (11.1%), and 21,672 WW papers (5.5%). Between 1990 and 2023, the share of papers with women as the first and/or last authors increased from 15% to 33% (Fig. 1(a)). Although the pace of increase varies across subfields, the overall trend is upward (Fig. 1(b)).

We now quantify gendered citation imbalance in computer science. We first count the number of citations made by a subset of papers to papers in each gender category. Then, we compare the obtained citation counts with the expected numbers derived from a reference model that randomizes citations while preserving certain properties of the original network. We define the “over/undercitation” as (observed − expected)/expected, which captures how much the observed citation count exceeds (or falls short of) the expected value (see Methods). This approach adopts a standard practice for characterizing subgraphs or patterns appearing in empirical networks and will reveal aspects of citation imbalance not immediately explained by common network properties [96, 65, 23, 41].

We begin with the random-draws model [18], which preserves the number of citations made by each paper, as the reference model. Under this model, we found that all papers in our dataset significantly over-cite MM papers and under-cite WM and WW papers (see Fig. 2(a)). We further categorize citations made by papers by gender category [18, 86]; unless we state otherwise, we focus on citations made by MM and WW papers to distinguish how papers authored by men and by women differ in their citation practices. MM papers significantly over-cite MM papers and undercite MW, WM, and WW papers (see Fig. 2(b)). In contrast, WW papers significantly under-cite MM papers and over-cite MW, WM, and WW papers (see Fig. 2(c)). These results are consistent with previous studies on gender imbalance in citations among journal papers in neuroscience and physics [18, 86].

Citation networks exhibit two common properties [106]: homophily in citations–where papers tend to cite others with similar characteristics–and heterogeneity in the number of citations re-

(b) (c)

(a)

| |From MM (Random-draws)| | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| |From All (Random-draws) More<br><br>cited| | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| |Less cited| | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| |From WW (Random-draws)| | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


(e) (f)

(d)

| |From MM (Homophilic-draws)| | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| |From All (Homophilic-draws)| | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| |From WW (Homophilic-draws)| | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


(h) (i)

(g)

| |From MM (Preferential-draws)| | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| |From All (Preferential-draws)| | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| |From WW (Preferential-draws)| | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


- Figure 2: Gender imbalance in citations made by papers in computer science. Panels (a), (d), and (g) show results for all papers; (b), (e), and (h) for MM papers; and (c), (f), and (i) for WW papers. We used the random-draws model in (a)–(c), the homophilic-draws model in (d)–(f), and the preferential-draws model in (g)–(i). See Supplementary Tables S6–S8 for the statistical significance of the over/under-citation under these three reference models.


ceived per paper–where most papers receive few citations while a small fraction accumulate many. Because these properties often drive structural and dynamical behaviors in citation networks [106], we hypothesize that they contribute to gendered citation imbalance. To test this hypothesis, we extend the random-draws model, which preserves only the number of citations made by each paper but destroys both homophily and citation heterogeneity, to a family of reference models. The homophilic-draws model preserves homophily with respect to (i) country of affiliation [28, 58], (ii) research subfield and topic [87], and (iii) venue rank [95, 47], while the preferential-draws model additionally preserves heterogeneity in the number of citations received per paper. Comparing these models allows us to examine the respective impacts of these two properties on gendered citation imbalance.

Homophily in citations contributes to the over/under-citation made by all papers. Indeed, the over/under-citation received by WW papers decreases from −10.1% in the random-draws model (see Fig. 2(a)) to −6.3% in the homophilic-draws model (see Fig. 2(d)). We observe a similar trend for

(a)

| | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |


- (b) (c)


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


- Figure 3: Gendered citation imbalance across subfields and topics in computer science. (a) Gender imbalance in citations made by all papers to MM and WW papers in each subfield of computer science. See Supplementary Table S9 for the statistical significance of the over/under-citation. (b) Proportion of WW papers in a subfield versus the over/under-citation made by all papers to these papers. (c) Proportion of WW papers in a topic versus the over/under-citation made by all papers to these papers.


(a)

| |From Any| | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


(b) (c)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| |From MM| | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| |From WW| | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


- Figure 4: Temporal trends of gender imbalance in citations made by papers in computer science. (a): All papers. (b): MM papers. (c): WW papers. See Supplementary Figure S3 for the statistical significance of the over/under-citation over time


.

the over/under-citation made by MM papers (see Figs. 2(b) and 2(e)); furthermore, the over/undercitation made by WW papers is largely explained by homophily in citations (see Figs. 2(c) and 2(f)). This indicates that the gendered citation pattern made by WW papers may largely be attributable to structural factors, such as the concentration of female researchers in certain combinations of topic, country, and venue. By contrast, the heterogeneity in the number of citations received per paper has little impact. In fact, the over/under-citation made by all papers is quantitatively comparable between the homophilic-draws and preferential-draws models (see Figs. 2(d) and 2(g)). We observe similar trends for the over/under-citation made by MM papers (see Figs. 2(e) and 2(h)) and by WW papers (see Figs. 2(f) and 2(i)).

To summarize, a persistent gendered citation imbalance remains in computer science, even after accounting for both homophily in citations and heterogeneity in the number of citations received per paper. Homophily in citations is strongly associated with this imbalance, while the latter has a minor impact. Our findings suggest that (i) addressing excessive homophily in citing practices, including over-citations among researchers from the same country of affiliation [2], is crucial, and

- (ii) simply focusing on highly-cited papers is unlikely to eliminate the imbalance. Unless we state otherwise, we employ the preferential-draws model in the subsequent analysis.


This model quantifies gender imbalance in citations that is not immediately explained by the number of citations made by each paper, homophily in citations, or heterogeneity in the number of citations received per paper. While we exclude self-citations here, the gender imbalance is more pronounced when we include (see Supplementary Section S4 for details), which is largely consistent with previous results on gendered self-citation behaviors [39, 18, 86]. Moreover, while we excluded isolated papers (i.e., those that neither make nor receive any citations) from our analyses, a sensitivity analysis confirmed that our main findings on over/under-citation patterns remain qualitatively unchanged (see Supplementary Section S5 for details).

Because the extent of gender imbalance may vary across computer science subfields [24, 67], we analyze the 11 subfields of computer science classified in OpenAlex. We compute the over/undercitation made by all papers to MM and WW papers in each subfield and compare these values across subfields. As expected, the degree of gendered citation imbalance varies among them (Fig. 3(a)). These variations may be associated with gender differences in research focus; recent evidence indicates that women are more represented in applied research areas, yet faculty rated researchers in these areas as less likely to publish, receive tenure, or obtain funding compared to theoretical ones [40]. Such differences in research focus could act as a confounding factor for the observed subfield-level citation imbalance. Figure 3(b) plots the proportion of WW papers in each subfield (horizontal axis) against the over/under-citation made by all papers to those papers (vertical axis). We find a moderate positive correlation between these two measures (Spearman’s rank correlation coefficient = 0.455).

A similar pattern of correlation between the proportion of WW papers and over/under-citation is observed at the topic level. Specifically, we consider the 172 topics within computer science subfields that each contain at least 10 WW papers and have collectively received at least 10 citations to those papers. Figure 3(c) shows the proportion of WW papers in each topic versus the over/under-citation made by all papers to those papers. We observe substantial variation in over/under-citation across research topics and a weaker positive correlation (Spearman’s rank correlation coefficient = 0.202).

Although the proportion of WW papers published each year has steadily increased (see Fig. 1(a)), the over-citation received by MM papers and under-citation received by WW papers exhibit relatively stable trends over time (see Fig. 4(a)). When we categorize papers by gender each year, the temporal trend in over/under-citation made by MM papers closely mirrors that made by all papers (see Fig. 4(b)). WW papers consistently under-cite MM papers and over-cite WW papers, and this pattern has remained similarly stable (see Fig. 4(c)). These findings align with the previous results

for neuroscience and physics disciplines [18, 86] and suggest that citation practices become fixed over the long term and do not easily adapt to a diversifying author population.

##### 3.2 Conferences versus journals

In computer science, international conferences often serve as the primary publication venue, filling a role that journals typically occupy in other disciplines [26, 25, 99]. Their distinctive publishing culture, characterized by short review cycles and other unique features, may shape authors’ citation practices. Indeed, a longstanding debate has compared conferences and journals in this discipline [98, 21, 25, 99, 38]. Here, we examine conferences and journals through the lens of gendered citation imbalance.

We compare the over/under-citation made by all papers to conference versus journal papers in a gender category (MM or WW). MM conference papers are over-cited at twice the rate of MM journal papers, while WW conference papers are under-cited at three times the rate of WW journal papers (Fig. 5(a)). This result suggests that authors citing conference papers may reference a narrower range of researchers, potentially contributing to the observed gendered citation imbalance in computer science. Furthermore, this disparity suggests that the field’s unique publication practices, in which researchers often present their work at international conferences rather than in journals [98, 21], may create a prestige hierarchy among publication venues that intersects with gendered citation imbalance. This observation largely aligns with previous studies on the intersection of gender imbalance and prestige regarding research institutions, research focus, and publication venues [102, 3, 33, 40].

Conferences and journals in computer science are frequently ranked according to citation metrics of the papers they publish [26]. The highest-ranked venues are viewed as especially prestigious [95, 47]. We explore relationships between the venue rank and the extent of gendered citation imbalance. One common conference ranking is the CORE ranking system, which designates the top conferences as A∗, followed by A, B, and C. For journals, we use the SCImago Journal Rank, which classifies the top journals as Q1, followed by Q2, Q3, and Q4. We compute the over/under-citation made by all papers to papers that belong to each venue rank and gender category (MM or WW).

Venue prestige is associated with gendered citation imbalance in computer science, and this association is more pronounced for conferences than for journals (Fig. 5(b)). MM papers are overcited in all conference tiers and in Q1 and Q3 journals, whereas WW papers are under-cited in A∗ and B conferences as well as Q1 and Q3 journals. WW papers in A∗-ranked conferences are under-cited at three times the rate observed in Q1 journals, whereas the over-citation received by MM papers in A∗-ranked conferences is on par with that in Q1 journals.

Gendered citation imbalance is less pronounced, or even reversed, in middle-tier venues (Q2 journals and A-ranked conferences) compared to the top-tier venues (Q1 journals and A∗-ranked conferences) This non-monotonic pattern aligns with previous findings suggesting that prestige bias is often most acute at the top tier of the hierarchy. For instance, authors from top-ranked institutions often benefit disproportionately from their affiliation prestige, whereas those from middle-tier or lower-ranked institutions may experience different evaluation dynamics in peer-review processes [5, 84, 34]. Similarly, our results suggest that the gendered citation imbalance can be amplified in top-tier conferences and journals, potentially due to their greater visibility and competition relative to middle-tier venues.

We examine the variation in over/under-citation received by WW papers across the 120 conferences and 292 journals, each meeting two criteria: (i) publication of at least 10 WW papers and (ii) at least 10 total citations received by those WW papers. In both conference and journal, the proportion of WW papers published in the venue shows almost no correlation with the over/under-

(a)

(b)

| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |


| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |


Conference rank Journal rank

(c) (d)

Conference rank Journal rank

###### Figure 5: Gendered citation imbalance in different publication venues of computer science. (a)Over/under-citation received by MM and WW papers published in conferences and journals. SeeSupplementary Table S10 for the statistical significance of the over/under-citation. (b) Over/under-citation received by MM and WW papers in each venue rank. See Supplementary Table S11 forthe statistical significance of the over/under-citation. (c) Proportion of WW papers in a conferenceversus over/under-citation received by these papers. (d) Proportion of WW papers in a journalversus over/under-citation received by these papers.

citation received by these papers; Spearman’s rank coefficients of 0.092 for conferences (Fig. 5(c)) and 0.026 for journals (Fig. 5(d)).

To summarize, gendered citation imbalance is evident in both conferences and journals within computer science, but it is more pronounced for conference papers, especially those published at top-tier conferences. Furthermore, the variation in the extent of gendered citation imbalance across conferences and journals is largely unexplained by the underlying gender imbalance in presenting authors. This disparity between presenting authors’ gender ratios and actual citation practices may stem from systemic factors, such as conference-dominant culture [98, 21], the involvement of prominent authors [94, 84], and coauthorship networks [52, 38].

##### 3.3 Potential drivers of gendered citation imbalance

Based on these findings, we examine potential drivers of gendered citation imbalance in computer science. To do so, we compare over/under-citation patterns made by papers while controlling for key paper characteristics [18, 86]. We employ a matched-pair analysis, as in previous studies on gender imbalance in research careers [33, 46], to assess whether certain characteristics of papers that made citations are associated with stronger gender imbalance in their citation behavior.

We first hypothesize that an author’s gender influences the gender imbalance in citations made by their papers, as suggested by the patterns shown in Fig. 2. To test this, we conduct a matched-pair analysis that controls for paper characteristics beyond gender category (see Methods). We generate independent sets of matched MM and WW paper pairs–each pair matching in publication year, country of affiliation, subfield, and number of citations made–and then compare the over/undercitation made by MM versus WW papers across these matched sets.

The over/under-citation made by MM papers to papers in each gender category differs significantly from that made by WW papers (Fig. 6(a)). Specifically, MM papers over-cite MM and under-cite MW, WM, and WW, whereas WW papers under-cite MM and over-cite MW, WM, and WW. These findings align with Figs. 2(h) and 2(i), and these gendered citation patterns remained after controlling publication year, country of affiliation, subfield, and number of citations made by the paper.

We next examine how specific characteristics of MM and WW papers contribute to gender imbalance in citations made by these papers. We focus on three characteristics: (i) venue type (conference or journal), (ii) involvement of “prominent” authors (those with highly cited papers), and (iii) local coauthorship network. Using a matched-pair analysis again, we test whether each characteristic influences gender imbalance (see Methods). First, we split the MM (or WW) papers into two disjoint sets based on a given characteristic; for instance, MM conference papers versus MM journal papers in the case of venue type. Second, we generate independent sets of matched MM (or WW) pairs, controlling for publication year, country of affiliation, subfield, and the number of citations made by the paper. Finally, we compute the over-/under-citation made by MM papers (or WW papers) across the matched sets to assess the association of that characteristic with gendered citation imbalance.

We identified several associations between these three characteristics and the gender imbalance in citations by MM and WW papers. First, the absolute magnitude of over/under-citation made by MM conference papers exceeds that of MM journal papers (Fig. 6(b)). While the under-citation to MM papers remains comparable between WW conference papers and WW journal papers, the overcitation to WW papers is larger in WW conference papers than in WW journal papers (Fig. 6(b)). Second, the involvement of prominent authors exhibits qualitatively different effects for MM and WW papers (Fig. 6(c)): the absolute magnitude of the over/under-citation made by MM papers is greater when prominent authors are involved, whereas that made by WW papers is smaller.

(a) (b)

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
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
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


(c) (d)

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


- Figure 6: Matched pair analysis on potential drivers of gender imbalance in citations made by papers. (a) Authors’ gender. (b) Venue type. (c) Involvement of prominent authors. (d) Local coauthorship network. See Supplementary Tables S14–S17 for the statistical significance of the over/under-citation shown in panels (a), (b), (c), and (d).


This suggests that while the author’s prominence amplifies male homophily, it diminishes female homophily. This result may indicate that prominent female authors could adopt the dominant, malecentric citation norms. While this hypothesis warrants further careful investigation, it suggests the complex interplay between author prominence and citation behavior. Finally, the local coauthorship network of the first and last authors is linked to the over/under-citation made by their papers (Fig. 6(d)), which is consistent with the previous result in neuroscience [18]. In particular, MM papers whose male authors have a high proportion of male coauthors (i.e., top half of the MAor range) display a greater absolute magnitude of over/under-citation than those whose male authors have fewer male coauthors (i.e., bottom half of the MAor range). WW papers with higher male representation in their coauthorship networks (i.e., top half of the MAor range) exhibit stronger over-citation of WW papers. This result may indicate that women in male-dominated coauthorship networks could be more acutely aware of the gendered citation imbalance and have citation norms intended to address it.

#### 4 Discussion

In this study, we investigated the extent of gendered citation imbalance in computer science. We found that papers with women as the first or last authors receive fewer citations across various subfields, topics, and venues in computer science. Previous studies analyzed gender imbalance in researcher demographics, productivity, research careers, and collaboration patterns in computer science [102, 36, 33, 43, 56, 48, 31, 100, 29]. Our study extends previous findings on the gender imbalance in computer science in terms of citation practices. Our results indicate citation practices in the unique conference-oriented culture of computer science may reinforce the gendered citation imbalance.

We found that conference papers in computer science are more prone to gendered citation imbalances–both in making and receiving citations–than journal papers. Several factors may contribute to this disparity. One is the highly compressed peer-review cycle at computer science conferences, often restricted to a few weeks. While these short turnaround times expedite decisions and knowledge dissemination, they raise concerns about review depth and quality. Vardi highlighted the “extreme time and workload pressures” experienced by conference program committees [98]. Fortnow argued that deadline-driven conference culture can lead to arbitrary decisions and prioritize speed over thorough vetting [98, 21]. These abbreviated timelines and rushed evaluations may inadvertently foster selective citation practices that exacerbate gendered citation imbalance, although further quantitative investigation is needed to determine the precise extent of this effect.

Our findings indicate that gendered citation imbalance is particularly pronounced in top-tier conference papers in computer science. In addition to conventional fixed schedules and brief peerreview periods, the rapid expansion of these conferences has surpassed the capacity of program committees, significantly increasing reviewers’ workloads [98, 21]. As early as 2009, Birman and Schneider reported that top-tier computer systems conferences were overwhelmed by submissions, leading to overworked reviewers and potentially cursory paper evaluations [4]. In 2019, an expert panel from the flagship conference on Computer and Communications Security (the so-called CCS conference) reported a surge to 3,039 submissions across four top-tier computer security conferences in 2020, raising concerns about the ability of reviewers to adequately assess such a large volume of manuscripts [80]. In response, several top-tier conferences have begun offering rebuttal opportunities to authors [32]. Future studies should examine how these peer-review dynamics at top-tier conferences shape citation practices, ensuring fair scholarly recognition in computer science.

Computer science conferences have traditionally enforced strict page limits to standardize sub-

missions and facilitate brief review cycles [30]. While these limits remain common, many prestigious conferences now allow longer, more content-rich papers. For instance, the flagship conference in human-computer interaction (the so-called CHI conference) lifted formal page limits in 2016, spurring increases in both paper length and references [64]. Similarly, Geiger’s analysis of another top-tier conference showed that once page limits were removed, average paper length rose, reflecting community norms favoring more thorough reporting [27]. These shifts try to balance efficiency for short review periods, physical constraints on conference proceedings, and the goal of more comprehensive research reporting. Although evolving page-limit policies appear to boost reference counts, it remains unclear how this trend will influence gendered citation imbalance in computer science.

The pronounced difference between conferences and journals in terms of gendered citation imbalance may also be partially driven by “topic proximity” in citation practices. Recent work in physics has shown that gendered citation imbalance is often amplified when authors cite work they are less familiar with (i.e., low topic proximity) [86]. A possible hypothesis in computer science is that the constraints of conference publications (e.g., tight deadlines and page limits) may lead authors to prioritize highly visible or cited papers when referencing work outside their immediate expertise. Because computer science has historically been male-dominated, as we showed, this tendency could amplify gendered citation imbalances relative to journal papers, where authors may have more resources to conduct comprehensive literature searches. Future work could investigate this possible association by measuring topic proximity using paper classifications or text embeddings.

Previous studies deployed reference models to characterize citation behaviors. Uzzi et al. investigated atypical combinations of citations associated with the impact of a paper by randomizing citations using a Monte Carlo algorithm [96]. Kojaku et al. examined anomalous citation patterns across journals using a reference model that accounts for scientific communities and journal size [41]. These reference models are not intended to quantify imbalances in citations received by papers because they preserve the number of citations received by each paper in the original network. Dworkin et al. introduced a reference model for quantifying the gender imbalance in citations received by papers [18]. The model is not designed to investigate the associations between network properties and gendered citation imbalance because it preserves only the number of citations made by each paper in the original network. To address these limitations, we developed a family of reference models that preserve the number of citations made by each paper, along with two network properties: homophily in citations and heterogeneity in the number of citations received per paper.

Using reference models for citation networks, we found that homophily in citations strongly contributes to gendered citation imbalance. Previous studies have also focused on homophily in citations regarding authors’ gender [87, 107]. Tekles et al. reported that in biological and medical fields, gendered citation patterns are largely driven by homophily regarding the research topic [87]. Zhou et al. found that author’s gender homophily partially explains citation behavior in life sciences [107]. By controlling for homophily in citations regarding country of affiliation, research topic, and venue rank, we identified its contribution to the gendered citation imbalance. Together with these previous studies, our findings highlight the significance of controlling for citation homophily when analyzing gendered citation patterns.

By conducting a matched-pair analysis controlling for key paper-level characteristics, we found that the prominence of the first or last author and their local coauthorship network contribute to gender imbalance in citations made by papers. This observation aligns with previous findings that these factors partially shape researchers’ practices. Indeed, at top computer science conferences, manuscripts with prominent authors had higher scores than those without in peer reviews where the reviewers know the authors’ names [94, 84]. Similarly, local coauthorship network influences gender-based citation patterns of neuroscience and physics researchers [18, 86]. Using Yates’s chisquared test [1], we found that these characteristics are not independent (see Supplementary Section

S7). The interaction between these factors may amplify gendered citation imbalance, warranting systematic investigation into their combined effects.

Our study has several limitations. First, the gender assignment method we employed underperformed for Chinese-name benchmark data [58]. As a result, we failed to assign gender categories to many papers written by Chinese authors. Given the rapid increase in China’s contribution to computer science research [28], future work should examine gendered citation imbalances in papers authored by Chinese researchers. Second, although we assumed that the first and last authors played leading roles in each paper, this assumption may not always hold. Indeed, gender imbalance can emerge in how credit is assigned among multiple authors [73], and some computer science subfields adopt alphabetical ordering by surname [79]. Further work is needed to implement gender-aware approaches to author credit and assess gendered citation imbalance in these subfields. Third, additional citation imbalances may exist regarding the author’s country of affiliation [28], nationality [58], and race [42]. Although we focused on citation imbalance regarding the author’s gender, our quantitative framework is not restricted to that context. For instance, citation imbalances likely exist between research-intensive and other countries [28], which could be analyzed using reference models controlling for network properties and paper characteristics other than country of affiliation. Systematic investigations into citation imbalances across various aspects of authors’ identities are an important direction for future research. Fourth, we acknowledge that computer science is becoming increasingly interdisciplinary [10]. This trend makes it challenging to exhaustively define the field’s research landscape, and our analysis might omit certain relevant publications, conferences, or journals in interdisciplinary areas where computer science plays a primary role. Fifth, our analysis treats venue rank, author prominence, and co-authorship networks as static attributes, although they are time-varying. A longitudinal analysis incorporating these time-varying attributes warrants further investigation into how the evolution of an author’s or venue’s prestige over time may influence citation practices.

Despite these limitations, our study provides a systematic and large-scale analysis of gendered citation imbalance in computer science, encompassing both conferences and journals. Our findings are expected to provide actionable insights to inform ongoing efforts toward fostering a more equitable, inclusive, and sustainable academic environment.

#### Appendix A Comparison of reference models

We compare structural properties of the original network with those of randomized networks generated by our three reference models. First, all models exactly preserve the distribution of citations made by each paper (Fig. 7(a)). Second, the random-draws model destroys homophilic citation patterns (in conference rank, journal rank, country of affiliation, and research topic), whereas the homophilic-draws and preferential-draws models preserve these patterns (Figs. 7(b)–(f)). Third, the random-draws model poorly preserves the original heterogeneity in the number of citations received per paper, while the homophilic-draws and preferential-draws models approximate it more closely, with the latter being closer (Fig. 7(g)). These outcomes align with our expectations.

#### Acknowledgements

We thank Naoki Masuda (State University of New York at Buffalo) for his feedback. This work was supported by Japan Science and Technology Agency (JST) as part of Adopting Sustainable Partnerships for Innovative Research Ecosystem (ASPIRE), Grant Number JPMJAP2328. KN thanks the financial support by JSPS KAKENHI Grant Number 24K21056. YS thanks the support

(a)

(b)

(c)

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| |Original Random<br><br>Homophilic<br><br>Preferential| | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


(d)

(e)

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |


(f)

(g)

| | | | | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


- Figure 7: Comparison of structural properties between the original network and the reference models. (a) Distribution of the number of citations made by each paper. (b)–(f) Homophilic citation patterns with respect to (b) conference rank, (c) journal rank, (d) affiliation country, (e) subfield, and (f) topic. (g) Distribution of the number of citations received by each paper. ‘Original’ denotes the original network, ‘Random’ the random-draws model, ‘Homophilic’ the homophilic-draws model, and ‘Preferential’ the preferential-draws model. In (d)–(f), we focus on the 52 countries, 67 subfields, and 284 topics that exhibit at least one homophilic citation in both the original network and each reference model. Curves that completely or substantially overlap are indicated by arrows and labels.


by JST Presto Grant Number JPMJPR21C5.

#### Competing interests

The authors declare that they have no competing interests.

#### Data availability

The OpenAlex snapshot from September 2024 is available at https://docs.openalex.org/download-all-data/

openalex-snapshot. The DBLP snapshot from July 2024 is available at https://blog.dblp. org/tag/snapshot/. The CORE ranking data is available at https://portal.core.edu.au/ conf-ranks/. The SCImago Journal Rank data is available at https://www.scimagojr.com/ journalrank.php?area=1700&year=2021. The Gender API is available for a fee at https:// gender-api.com/. Data from the 3,720,575 papers integrated between OpenAlex and DBLP (see Section 2.1.3) is available at https://doi.org/10.5281/zenodo.16537950.

#### References

- [1] G. Abramo, D. W. Aksnes, and C. A. D’Angelo. Gender differences in research performance within and between countries: Italy vs Norway. Journal of Informetrics, 15:101144, 2021.
- [2] A. Baccini and E. Petrovich. A global exploratory comparison of country self-citations 1996-

2019. PLOS ONE, 18:e0294669, 2023.

- [3] M. H. K. Bendels, R. Mu¨ller, D. Brueggmann, and D. A. Groneberg. Gender disparities in high-quality research revealed by nature index journals. PLOS ONE, 13:1–21, 2018.
- [4] K. Birman and F. B. Schneider. Viewpoint: Program committee overload in systems. Communications of the ACM, 52(5):34–37, 2009.
- [5] R. M. Blank. The effects of double-blind versus single-blind reviewing: Experimental evidence from the american economic review. The American economic review, pages 1041–1067, 1991.
- [6] L. Bornmann, R. Mutz, and H.-D. Daniel. Gender differences in grant peer review: A metaanalysis. Journal of Informetrics, 1:226–238, 2007.
- [7] K. Buchholz. Which countries’ students are getting most involved in stem? Technical report, World Economic Forum, 2023. https://www.weforum.org/stories/2023/ 03/which-countries-students-are-getting-most-involved-in-stem/ [Accessed March 2025].
- [8] N. Caplar, S. Tacchella, and S. Birrer. Quantitative evaluation of gender bias in astronomical publications from citation counts. Nature Astronomy, 1:0141, 2017.
- [9] A. Cavacini. What is the best database for computer science journal articles? Scientometrics, 102:2059–2071, 2015.
- [10] T. Chakraborty. Role of interdisciplinarity in computer sciences: quantification, impact and life trajectory. Scientometrics, 114:1011–1029, 2018.


- [11] P. Chatterjee and R. M. Werner. Gender disparity in citations in high-impact journal articles. JAMA Network Open, 4:e2114509–e2114509, 2021.
- [12] V. Ciotti, M. Bonaventura, V. Nicosia, P. Panzarasa, and V. Latora. Homophily and missing links in citation networks. EPJ Data Science, 5:7, 2016.
- [13] A. Clauset, S. Arbesman, and D. B. Larremore. Systematic inequality and hierarchy in faculty hiring networks. Science Advances, 1:e1400005, 2015.
- [14] J. M. Cohoon, S. Nigai, and J. J. Kaye. Gender and computing conference papers. Communications of the ACM, 54:72–80, 2011.
- [15] CSRankings. CSRankings: Computer Science Rankings. Available from https:// csrankings.org/#/index?all&us [Accessed January 2026].
- [16] L. Delgado-Quir´s and J. L. Ortega. Completeness degree of publication metadata in eight free-access scholarly databases. Quantitative Science Studies, pages 1–19, 2024.
- [17] M. L. Dion, J. L. Sumner, and S. M. Mitchell. Gendered citation patterns across political science and social science methodology fields. Political Analysis, 26:312–327, 2018.
- [18] J. D. Dworkin, K. A. Linn, E. G. Teich, P. Zurn, R. T. Shinohara, and D. S. Bassett. The extent and drivers of gender imbalance in neuroscience reference lists. Nature Neuroscience, 23:918–926, 2020.
- [19] Y.-H. Eom and S. Fortunato. Characterizing and modeling citation dynamics. PLOS ONE, 6:1–7, 2011.
- [20] Eurostat. ICT sector – value added, employment and R&D, 2024. https: //ec.europa.eu/eurostat/statistics-explained/index.php?title=ICT_sector_-_ value_added,_employment_and_R%26D [Accessed March 2025].
- [21] L. Fortnow. Viewpoint: Time for computer science to grow up. Communications of the ACM, 52:33–35, 2009.
- [22] S. Fortunato, C. T. Bergstrom, K. B¨rner, J. A. Evans, D. Helbing, S. Milojevi´c, A. M. Petersen, F. Radicchi, R. Sinatra, B. Uzzi, A. Vespignani, L. Waltman, D. Wang, and A.-L. Barab´si. Science of science. Science, 359:eaao0185, 2018.
- [23] B. K. Fosdick, D. B. Larremore, J. Nishimura, and J. Ugander. Configuring random graph models with fixed degree sequences. SIAM Review, 60:315–355, 2018.
- [24] E. Frachtenberg and R. D. Kaner. Underrepresentation of women in computer systems research. PLOS ONE, 17:e0266439, 2022.
- [25] M. Franceschet. The role of conference publications in CS. Communications of the ACM, 53:129–132, 2010.
- [26] J. Freyne, L. Coyle, B. Smyth, and P. Cunningham. Relative status of journal and conference publications in computer science. Communications of the ACM, 53:124–132, 2010.
- [27] R. S. Geiger. The rise and fall of the note: Changing paper lengths in ACM CSCW, 2000–2018. Proceedings of the ACM on Human-Computer Interaction, 3, 2019.


- [28] C. J. Gomez, A. C. Herman, and P. Parigi. Leading countries in global science increasingly receive more citations than other countries doing similar research. Nature Human Behaviour, 6:919–929, 2022.
- [29] A. Hajibabaei, A. Schiffauerova, and A. Ebadi. Gender-specific patterns in the artificial intelligence scientific ecosystem. Journal of Informetrics, 16:101275, 2022.
- [30] J. Y. Halpern and D. C. Parkes. Journals for certification, conferences for rapid dissemination. Communications of the ACM, 54:36–38, 2011.
- [31] L. Holman, D. Stuart-Fox, and C. E. Hauser. The gender gap in science: How long until women are equally represented? PLOS Biology, 16:1–20, 2018.
- [32] J. Huang, W. bin Huang, Y. Bu, Q. Cao, H. Shen, and X. Cheng. What makes a successful rebuttal in computer science conferences?: A perspective on social interaction. Journal of Informetrics, 17:101427, 2023.
- [33] J. Huang, A. J. Gates, R. Sinatra, and A.-L. Barab´si. Historical comparison of gender inequality in scientific careers across countries and disciplines. Proceedings of the National Academy of Sciences of the United States of America, 117:4609–4616, 2020.
- [34] A. E. Hultgren, N. M. Patras, and J. Hicks. Meta-research: Blinding reduces institutional prestige bias during initial review of applications for a young investigator award. eLife, 13:e92339, 2024.
- [35] J. P. A. Ioannidis, K. W. Boyack, T. A. Collins, and J. Baas. Gender imbalances among top-cited scientists across scientific disciplines over time through the analysis of nearly 5.8 million authors. PLOS Biology, 21:e3002385, 2023.
- [36] M. Jadidi, F. Karimi, H. Lietz, and C. Wagner. Gender disparities in science? Dropout, productivity, collaborations and success of male and female computer scientists. Advances in Complex Systems, 21:1750011, 2018.
- [37] J. Kim. Evaluating author name disambiguation for digital libraries: a case of dblp. Scientometrics, 116:1867–1886, 2018.
- [38] J. Kim. Author-based analysis of conference versus journal publication in computer science. Journal of the Association for Information Science and Technology, 70:71–82, 2019.
- [39] M. M. King, C. T. Bergstrom, S. J. Correll, J. Jacquet, and J. D. West. Men set their own cites high: Gender and self-citation across fields and over time. Socius, 3:2378023117738903, 2017.
- [40] S. Kleinberg and J. K. Marsh. Where the women are: Gender imbalance in computing and faculty perceptions of theoretical and applied research. IEEE Access, 13:73520–73529, 2025.
- [41] S. Kojaku, G. Livan, and N. Masuda. Detecting anomalous citation groups in journal networks. Scientific Reports, 11:14524, 2021.
- [42] D. Kozlowski, V. Larivi`ere, C. R. Sugimoto, and T. Monroe-White. Intersectional inequalities in science. Proceedings of the National Academy of Sciences of the United States of America, 119:e2113067119, 2022.


- [43] N. Laberge, K. H. Wapman, A. C. Morgan, S. Zhang, D. B. Larremore, and A. Clauset. Subfield prestige and gender inequality among U.S. computing faculty. Communications of the ACM, 65:46–55, 2022.
- [44] V. Larivi`ere, C. Ni, Y. Gingras, B. Cronin, and C. R. Sugimoto. Bibliometrics: Global gender disparities in science. Nature, 504(7479):211–213, 2013.
- [45] M. Ley. The dblp computer science bibliography: Evolution, research issues, perspectives. In String Processing and Information Retrieval, pages 1–10, 2002.
- [46] W. Li, S. Zhang, Z. Zheng, S. J. Cranmer, and A. Clauset. Untangling the network effects of productivity and prominence among scientists. Nature Communications, 13:4907, 2022.
- [47] X. Li, W. Rong, H. Shi, J. Tang, and Z. Xiong. The impact of conference ranking systems in computer science: A comparative regression analysis. Scientometrics, 116:879–907, 2018.
- [48] H. Lietz, M. Jadidi, D. Kostic, M. Tsvetkova, and C. Wagner. Individual and gender inequality in computer science: A career study of cohorts from 1970 to 2000. Quantitative Science Studies, pages 1–25, 2024.
- [49] A. E. Lincoln, S. Pincus, J. B. Koster, and P. S. Leboy. The Matilda Effect in science: Awards and prizes in the US, 1990s and 2000s. Social Studies of Science, 42:307–320, 2012.
- [50] D. Maliniak, R. Powers, and B. F. Walter. The gender citation gap in international relations. International Organization, 67:889–922, 2013.
- [51] L. I. Meho. The gender gap in highly prestigious international research awards, 2001–2020. Quantitative Science Studies, 2:976–989, 2021.
- [52] G. V. Menezes, N. Ziviani, A. H. Laender, and V. Almeida. A geographical analysis of knowledge production in computer science. In Proceedings of the 18th International Conference on World Wide Web, pages 1041–1050, 2009.
- [53] R. Milo, S. Shen-Orr, S. Itzkovitz, N. Kashtan, D. Chklovskii, and U. Alon. Network motifs: Simple building blocks of complex networks. Science, 298:824–827, 2002.
- [54] S. Milojevi´c. Science of science. Scientometrics, 2025.
- [55] L. B. Moreno, M. C. Franco, S. A. Karam, F. H. van de Sande, and A. F. Montagner. Persistent gender disparity in leading dental publications across 4 decades: An observational study. Journal of Clinical Epidemiology, 171:111386, 2024.
- [56] A. C. Morgan, S. F. Way, M. J. D. Hoefer, D. B. Larremore, M. Galesic, and A. Clauset. The unequal impact of parenthood in academia. Science Advances, 7:eabd1996, 2021.
- [57] C. A. Moss-Racusin, J. F. Dovidio, V. L. Brescoll, M. J. Graham, and J. Handelsman. Science faculty’s subtle gender biases favor male students. Proceedings of the National Academy of Sciences of the United States of America, 109:16474–16479, 2012.
- [58] K. Nakajima, R. Liu, K. Shudo, and N. Masuda. Quantifying gender imbalance in east asian academia: Research career and citation practice. Journal of Informetrics, page 101460, 2023.


- [59] K. Nakajima, Y. Sasaki, S. Tokuno, and G. Fletcher. Quantifying gendered citation imbalance in computer science conferences. In Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, pages 1011–1022, 2024.
- [60] M. E. Newman, S. H. Strogatz, and D. J. Watts. Random graphs with arbitrary degree distributions and their applications. Physical review E, 64:026118, 2001.
- [61] H. O.’Leary, T. Gantzert, A. Mann, E. Z. Mann, N. Bollineni, and M. Nelson. Citation as representation: Gendered academic citation politics persist in environmental studies publications. Journal of Environmental Studies and Sciences, 14:525–537, 2024.
- [62] B. Oliss, C. McFaul, and J. C. Riddick. The global distribution of stem graduates: Which countries lead the way? Technical report, Center for Security and Emerging Technology, 2023. https://cset.georgetown.edu/article/ the-global-distribution-of-stem-graduates-which-countries-lead-the-way/ [Accessed March 2025].
- [63] OpenAlex. OpenAlex: End-to-End Process for Topic Classification, 2024. https: //docs.google.com/document/d/1bDopkhuGieQ4F8gGNj7sEc8WSE8mvLZS/edit#heading= h.5w2tb5fcg77r [Accessed April 2024].
- [64] J. Oppenlaender. Past, present, and future of citation practices in HCI. arXiv preprint arXiv:2405.16526, 2024.
- [65] C. Orsini, M. M. Dankulov, P. Colomer-de Sim´n, A. Jamakovic, P. Mahadevan, A. Vahdat, K. E. Bassler, Z. Toroczkai, M. Bogun˜´, G. Caldarelli, S. Fortunato, and D. Krioukov. Quantifying randomness in real networks. Nature Communications, 6:8627, 2015.
- [66] S. Pandey and T. Burch-Smith. Overcoming citation bias is necessary for true inclusivity in plant science. The Plant Cell, 36:10–13, 2023.
- [67] E. Peltonen. The role of gender in the international conference on pervasive computing and communications. Frontiers in Computer Science, 4:1008552, 2022.
- [68] V. Petricek, I. J. Cox, H. Han, I. G. Councill, and C. L. Giles. A comparison of on-line computer science citation databases. In Research and Advanced Technology for Digital Libraries, pages 438–449, 2005.
- [69] J. Priem, H. Piwowar, and R. Orr. OpenAlex: A fully-open index of scholarly works, authors, venues, institutions, and concepts. arXiv preprint arXiv:2205.01833, 2022.
- [70] F. Radicchi, S. Fortunato, and C. Castellano. Universality of citation distributions: Toward an objective measure of scientific impact. Proceedings of the National Academy of Sciences of the United States of America, 105:17268–17272, 2008.
- [71] F. Reitz and O. Hoffmann. An analysis of the evolving coverage of computer science sub-fields in the dblp digital library. In Research and Advanced Technology for Digital Libraries, pages 216–227, 2010.
- [72] A. Rosenfeld. Is DBLP a good computer science journals database? Computer, 56:101–108, 2023.


- [73] M. B. Ross, B. M. Glennon, R. Murciano-Goroff, E. G. Berkes, B. A. Weinberg, and J. I. Lane. Women are credited less in science than men. Nature, 608:135–145, 2022.
- [74] L. Santamarı´a and H. Mihaljevic´. Comparison and benchmark of name-to-gender inference services. PeerJ Computer Science, 4:e156, 2018.
- [75] S. Schneegans, J. Lewis, and T. Straza. UNESCO science report. The race against time for smarter development. executive summary. Technical report, UNESCO, 2021. https: //unesdoc.unesco.org/ark:/48223/pf0000377250 [Accessed March 2025].
- [76] SCImago. SJR – SCImago Journal & Country Rank [Portal]. Retrieved November 1, 2024, from https://www.scimagojr.com/journalrank.php?area=1700&year=2021.
- [77] J. M. Sheltzer and J. C. Smith. Elite male faculty in the life sciences employ fewer women. Proceedings of the National Academy of Sciences, 111:10107–10112, 2014.
- [78] M.-A. Sicilia, S. S´nchez-Alonso, and E. Garc´ıa-Barriocanal. Comparing impact factors from two different citation databases: The case of computer science. Journal of Informetrics, 5:698–704, 2011.
- [79] J. Solomon. Programmers, professors, and parasites: Credit and co-authorship in computer science. Science and Engineering Ethics, 15:467–489, 2009.
- [80] A. Soneji, F. B. Kokulu, C. Rubio-Medrano, T. Bao, R. Wang, Y. Shoshitaishvili, and A. Doup´e. “Flawed, but like democracy we don’t have a better system”: The experts’ insights on the peer review process of evaluating security papers. In 2022 IEEE Symposium on Security and Privacy (SP), pages 1845–1862, 2022.
- [81] M. Song, G. E. Heo, and S. Y. Kim. Analyzing topic evolution in bioinformatics: investigation of dynamics of the field with conference data in dblp. Scientometrics, 101:397–428, 2014.
- [82] K. Spoon, N. LaBerge, K. H. Wapman, S. Zhang, A. C. Morgan, M. Galesic, B. K. Fosdick, D. B. Larremore, and A. Clauset. Gender and retention patterns among U.S. faculty. Science Advances, 9:eadi2205, 2023.
- [83] C. R. Sugimoto and V. Larivi`ere. Equity for Women in Science. Harvard University Press, Cambridge, MA, 2023.
- [84] M. Sun, J. Barry Danfa, and M. Teplitskiy. Does double-blind peer review reduce bias? evidence from a top computer science conference. Journal of the Association for Information Science and Technology, 73:811–819, 2022.
- [85] R. S´nchez-Jim´enez, P. Guerrero-Castillo, V. P. Guerrero-Bote, G. Halevi, and F. De-MoyaAneg´n. Analysis of the distribution of authorship by gender in scientific output: A global perspective. Journal of Informetrics, 18:101556, 2024.
- [86] E. G. Teich, J. Z. Kim, C. W. Lynn, S. C. Simon, A. A. Klishin, K. P. Szymula, P. Srivastava, L. C. Bassett, P. Zurn, J. D. Dworkin, and D. S. Bassett. Citation inequity and gendered citation practices in contemporary physics. Nature Physics, 18:1161–1170, 2022.
- [87] A. Tekles, K. Auspurg, and L. Bornmann. Same-gender citations do not indicate a substantial gender homophily bias. PLOS ONE, 17:e0274810, 2022.


- [88] A. Llorens et al. Gender bias in academia: A lifetime problem that needs solutions. Neuron, 109:2047–2074, 2021.
- [89] National Science Foundation. Publications output: U.S. trends and international comparisons, 2021. https://ncses.nsf.gov/pubs/nsb20214/ [Accessed March 2025].
- [90] National Science Foundation. Fiscal year 2024 appropriations, 2024. https://www.nsf.gov/ about/budget/fy2024/appropriations [Accessed March 2025].
- [91] The Computing Research and Education Association of Australasia. CORE conference rankings 2021. https://portal.core.edu.au/conf-ranks/ [Accessed April 2024].
- [92] The DBLP team. DBLP computer science bibliography. how to find the key of a person, a publication, or a stream?, 2024. https://dblp.org/faq/How+to+find+the+key+of+a+ person+a+publication+or+a+stream.html [Accessed December 2024].
- [93] The DBLP team. DBLP computer science bibliography. Monthly snapshot release of April 2024., 2024. https://dblp.org/xml/release/dblp-2024-04-01.xml.gz [Accessed April 2024].
- [94] A. Tomkins, M. Zhang, and W. D. Heavlin. Reviewer bias in single- versus double-blind peer review. Proceedings of the National Academy of Sciences, 114:12708–12713, 2017.
- [95] C.-F. Tsai. Citation impact analysis of top ranked computer science journals and their rankings. Journal of Informetrics, 8:318–328, 2014.
- [96] B. Uzzi, S. Mukherjee, M. Stringer, and B. Jones. Atypical combinations and scientific impact. Science, 342:468–472, 2013.
- [97] P. van den Besselaar and U. Sandstr¨m. Gender differences in research performance and its impact on careers: a longitudinal case study. Scientometrics, 106:143–162, 2016.
- [98] M. Y. Vardi. Conferences vs. journals in computing research. Communications of the ACM, 52(5), 2009.
- [99] G. Vrettas and M. Sanderson. Conferences versus journals in computer science. Journal of the Association for Information Science and Technology, 66:2674–2684, 2015.
- [100] L. L. Wang, G. Stanovsky, L. Weihs, and O. Etzioni. Gender trends in computer science authorship. Communications of the ACM, 64:78–84, 2021.
- [101] X. Wang, J. D. Dworkin, D. Zhou, J. Stiso, E. B. Falk, D. S. Bassett, P. Zurn, and D. M. Lydon-Staley. Gendered citation practices in the field of communication. Annals of the International Communication Association, 45:134–153, 2021.
- [102] S. F. Way, D. B. Larremore, and A. Clauset. Gender, productivity, and prestige in computer science faculty hiring networks. In Proceedings of the International Conference on World Wide Web, page 1169–1179, 2016.
- [103] H. O. Witteman, M. Hendricks, S. Straus, and C. Tannenbaum. Are gender gaps due to evaluations of the applicant or the science? a natural experiment at a national funding agency. The Lancet, 393:531–540, 2019.


- [104] Y. Xie and K. A. Shauman. Sex differences in research productivity: New evidence about an old puzzle. American Sociological Review, 63:847–870, 1998.
- [105] F. Yates. Contingency tables involving small numbers and the χ2 test. Supplement to the Journal of the Royal Statistical Society, 1:217–235, 1934.
- [106] A. Zeng, Z. Shen, J. Zhou, J. Wu, Y. Fan, Y. Wang, and H. E. Stanley. The science of science: From the perspective of complex systems. Physics Reports, 714-715:1–73, 2017.
- [107] S. Zhou, S. Chai, and R. B. Freeman. Gender homophily: In-group citation preferences and the gender disadvantage. Research Policy, 53:104895, 2024.


Supplementary Information for: Systemic Gendered Citation Imbalance in Computer Science: Evidence from

Conferences and Journals

Kazuki Nakajima, Yuya Sasaki, Sohei Tokuno, and George Fletcher

#### S1 Additional information on our dataset

- S1.1 Flow diagram of the filtering process for papers Figure S1 shows a flow diagram of the filtering process for papers.
- S1.2 Analysis of the representativeness of our final dataset

To check the representativeness of our final dataset, we tracked the proportions of the four gender categories (i.e., “MM”, “MW”, “WM”, and “WW”) through the filtering process for papers. We found that the relative representation of each category remained stable throughout the process:

- • Papers assigned to countries of affiliation and gender categories (N = 1,399,106): MM: 75.2%, MW: 7.4%, WM: 10.7%, WW: 6.6%
- • Papers published in ranked conferences and journals (N = 672,082): MM: 76.0%, MW: 7.3%, WM: 10.5%, WW: 6.1%
- • Final set for our analysis (N = 394,432): MM: 75.6%, MW: 7.8%, WM: 11.1%, WW: 5.5%


We also compare the distribution of venue types and subfields between the initial matched dataset, D, and the final dataset. The proportion of conference papers decreased in the final dataset (from 51.8% to 39.3%), while the proportion of journal papers increased. This shift reflects our quality criterion of including only venues ranked by CORE or SCImago; more unranked conferences than journals were excluded from the initial matched dataset. Regarding subfields, the filtering process increased the relative share of the 11 computer science subfields while reducing the share of other subfields (from 51.9% to 41.6%; see Table S1). This indicates that our filtering concentrated the dataset on the central research areas of the discipline.

- S1.3 Demographic comparison of included and excluded authors


- Table S2 compares the distributions of the country of affiliation between the set of authors assigned a country of affiliation and the set of authors assigned both a country of affiliation and gender. We list individual countries until their cumulative share of authors assigned a country of affiliation reaches 90%, with the remaining countries grouped as “Others”. The most prominent shift is the sharp decrease in the relative share of authors from China. Similar decreases are also observed for authors from Taiwan, South Korea, Malaysia, Singapore, and Thailand. These shifts reflect the higher gender ambiguity associated with names from these regions, which often failed to meet our gender inference accuracy thresholds.


- S1.4 Summary of metadata for papers
- Table S3 summarizes the metadata of the papers included in our dataset.

S1.5 Additional statistics

- Table S4 shows the number of papers across each subfield-gender category combination. Table S5 shows the number of papers across each venue rank-gender category combination. Figure S2 shows the survival functions of citations made and received by papers in each gender category.


- S2 Pseudocode of the preferential-draws model Algorithm S1 shows a pseudocode of the preferential-draws model. Algorithm S1 Preferential-draws model. Require: Citation network: (V,E) and set of characteristics of the paper: S. Ensure: Randomized network: (V,Erand)

- 1: Sort the papers by publication date in ascending order: vx1,...,vxN.
- 2: Initialize cj,l,PD with zero for any j = 1,...,N for any l = 1,...,N.
- 3: Erand ← an empty list.
- 4: for l = 2,...,N do
- 5: for each citation (vxl,vj) ∈ E do
- 6: Compute the set V HD(xl,j,S).

- 7: V PD(xl,j,S) ← {vj′ | vj′ ∈ V HD(xl,j,S) ∧ ⌊ln(cj′,l−1,PD + 1)⌋ = ⌊ln(cj,l−1,PD + 1)⌋}.

- 8: Draw vj′ uniformly at random from the set V PD(xl,j,S).

- 9: Append citation (vxl,vj′) to Erand.
- 10: for z = l,...,N do
- 11: cj′,z,PD ← cj′,z,PD + 1.
- 12: return (V,Erand)


- S3 Detailed results of the over/under-citation

Tables S6-S8 show the over/under-citations under the random-draws, homophilic-draws, and preferentialdraws models, respectively. Table S9 shows the over/under-citation made by all papers to papers in a given gender category and in a given subfield. Table S10 shows the over/under-citation made by all papers to papers in a given gender category and in a given venue type. Table S11 shows the over/under-citation made by all papers to papers in a given gender category and in a given venue rank. Figure S3 shows the temporal trends of the Z-scores corresponding to the over/under-citation values shown in Fig. 4 of the main text.

- S4 Effects of self-citations on the over/under-citation


We constructed a citation network with self-citations intact, comprising 418,090 papers and 820,258 citations. Recall that a citation is defined as a self-citation if there is any overlap in authorship between the citing paper u and the cited paper v. We then calculated over/under-citations in this network. Table S12 compares these values with those computed from the network in which self-citations were excluded.

#### S5 Effects of isolated papers on the over/under-citation

We constructed a citation network with isolated papers (i.e., papers that neither make nor receive any citations) intact, comprising 542,550 papers and 752,742 citations. We then calculated over/under-citations in this network. Table S13 compares these values with those computed from the network in which isolated papers were excluded.

#### S6 Detailed results of the matching experiments

Tables S14–S17 show the results of the matching experiments with respect to the author’s gender (MM or WW), venue type, involvement of prominent authors, and local coauthorship network, respectively.

#### S7 Relationships between the three characteristics of the paper

We investigate the relationships among our three characteristics: venue type, involvement of prominent authors, and local coauthorship network. Specifically, we use Yates’s chi-squared test [1] for MM and WW papers separately. Fix a gender category g ∈ {MM,WW} and two characteristics, X and Y . Each characteristic is a categorical variable with two possible categories for each paper. We denote by Og,i,j the number of papers in gender category g that fall into category i for X (i = 1,2) and category j for Y (j = 1,2). Let Ng = 2i=1 2j=1 Og,i,j be the total number of papers in category g. We define the test statistic by

2

2

χ2 =

(|Og,i,j − Eg,i,j| − 0.5)2/Eg,i,j, (S2)

i=1

j=1

where

Eg,i,j = Ngpg,iqg,j, (S3)

2

Og,i,j Ng

pg,i =

, (S4)

j=1

2

Og,i,j Ng

qg,j =

. (S5)

i=1

The null hypothesis is that X is independent of Y for the papers in g. If the p value of the test is less than 0.001, we reject the null hypothesis.

Table S18 shows the test statistic and p-value for each combination (g,X,Y ). For MM papers, every pair of characteristics is not independent. For WW papers, every characteristic pair except “venue type versus local coauthorship network” is not independent.

|Initial publication records from DBLP database (July 1, 2024 snapshot) N = 7,034,299| | |
|---|---|---|
| | | |
| | | |


|Excluded because matching with OpenAlex failed. N = 3,313,724|
|---|


|Matched publications with enriched metadata N = 3,720,575| | |
|---|---|---|
| | | |
| | | |


|Excluded because the country of affiliation or gender category for the first or last authors could not be assigned. N = 2,321,469 Note: Excluded 1,173,093 unique authors out of 2,430,109.|
|---|


|Papers assigned to countries of affiliation and gender categories N = 1,399,106| | |
|---|---|---|
| | | |
| | | |


|Excluded venues without recognized rankings N = 727,024|
|---|


|Papers published in ranked conferences and journals N = 672,082| | |
|---|---|---|
| | | |
| | | |


|Excluded because papers met at least one of the following criteria:<br><br>- Self-citations or citations > 10 years old<br>- Publication year before 1990<br>- Papers neither made nor received any citations N = 277,650<br>|
|---|


|Final set for our analysis N = 394,432|
|---|


- Figure S1: Flow diagram of the paper filtering process. The diagram illustrates the step-by-step reduction from the initial publication records in the DBLP database to the final set of papers for our analysis. At each step, the reason and the number of excluded papers are shown. We also note the number of unique authors excluded because their country of affiliation or gender could not be assigned.


#### Supplementary References

[1] F. Yates. Contingency tables involving small numbers and the χ2 test. Supplement to the Journal of the Royal Statistical Society, 1:217–235, 1934.

### (a) (b)

| | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |


| | | | | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | |


- Figure S2: Survival functions of citation counts for each gender category. (a) Number of citations made by a paper, denoted by ki, plus one. (b) Number of citations received by a paper, denoted by ci, plus one.


- Table S1: Comparison of subfield distributions between the initial matched dataset and the final dataset. Subfields not belonging to the ‘Computer Science’ field in OpenAlex are grouped as ‘Others’.


Subfield Initial Set (%) Final Set (%) Artificial Intelligence 12.83 16.50 Computational Theory and Mathematics 3.53 3.86 Computer Graphics and Computer-Aided Design 0.72 1.17 Computer Networks and Communications 9.76 11.63 Computer Science Applications 0.87 1.35 Computer Vision and Pattern Recognition 8.25 9.04 Hardware and Architecture 2.34 3.19 Human-Computer Interaction 1.10 1.71 Information Systems 5.13 6.18 Signal Processing 2.78 2.66 Software 0.78 1.13 Others 51.92 41.59

(a)

From Any

- (b) (c)


From MM From WW

###### Figure S3: Temporal trends of the Z scores of the over/under-citation made by papers in computerscience. (a): All papers. (b): MM papers. (c): WW papers.

- Table S2: Comparison of the distributions of country of affiliation between authors assigned a country (p1) and authors assigned both a country and a gender (p2). Countries are listed individually until the cumulative share of p1 reaches 90%, with the remaining countries grouped as ‘Others’.


Country p1 (%) p2 (%) United States 22.21 26.52 China 16.22 1.77 Germany 5.71 8.07 Japan 4.98 6.00 India 4.25 4.31 United Kingdom 4.22 5.20 South Korea 3.41 2.30 Italy 3.15 4.10 Taiwan 2.95 0.56 Canada 2.86 3.46 France 2.67 3.55 Brazil 2.21 3.19 Australia 1.73 2.04 Netherlands 1.50 1.76 Iran 1.26 1.73 Spain 1.20 1.65 Switzerland 0.96 1.30 Greece 0.84 1.13 Sweden 0.81 1.13 Russia 0.81 0.90 Malaysia 0.79 0.68 Belgium 0.73 0.99 Austria 0.70 1.02 Portugal 0.70 1.02 Finland 0.69 0.88 Singapore 0.68 0.44 Israel 0.66 0.73 Pakistan 0.58 0.79 Thailand 0.49 0.37 Denmark 0.48 0.67 Others 9.55 11.74

Table S3: Summary of paper metadata.

|Attribute<br><br>|Data source|
|---|---|


|Title Publication date Primary research topic Primary research subfield Authors’ names Authors’ affiliations Authors’ IDs Authorship order Papers cited by the paper Venue type (i.e., conference or journal) Venue name Venue rank Country of affiliation Gender category|OpenAlex OpenAlex OpenAlex OpenAlex OpenAlex OpenAlex<br><br>DBLP DBLP OpenAlex<br><br>DBLP DBLP DBLP, CORE, and SCImago<br><br>OpenAlex and DBLP<br><br>OpenAlex, DBLP, Gender API<br><br>|
|---|---|


- Table S4: Number of papers by subfield and gender category.


|Subfield|MM|MW<br><br>|WM<br><br>|WW|
|---|---|---|---|---|


|Artificial Intelligence|49,852 (76.7%)|5,156 (7.9%)<br><br>|6,653 (10.2%)<br><br>|3,413 (5.2%)|
|---|---|---|---|---|
|Computational Theory and Mathematics|12,383 (81.2%)<br><br>|938 (6.2%)<br><br>|1,224 (8.0%)|698 (4.6%)<br><br>|
|Computer Graphics and Computer-Aided Design|4,039 (87.8%)<br><br>|205 (4.5%)|261 (5.7%)<br><br>|92 (2.0%)<br><br>|
|Computer Networks and Communications<br><br>|36,979 (80.5%)|3,102 (6.8%)<br><br>|4,425 (9.7%)<br><br>|1,362 (3.0%)|
|Computer Science Applications<br><br>|3,107 (58.5%)<br><br>|571 (10.8%)<br><br>|866 (16.3%)|764 (14.4%)<br><br>|
|Computer Vision and Pattern Recognition<br><br>|28,040 (78.6%)<br><br>|2,552 (7.2%)<br><br>|3,918 (11.0%)|1,135 (3.2%)<br><br>|
|Hardware and Architecture|10,790 (85.6%)<br><br>|733 (5.8%)<br><br>|851 (6.8%)|227 (1.8%)<br><br>|
|Human-Computer Interaction<br><br>|4,168 (62.0%)<br><br>|730 (10.8%)|1,085 (16.1%)<br><br>|743 (11.1%)|
|Information Systems<br><br>|17,497 (71.7%)<br><br>|2,091 (8.6%)<br><br>|3,081 (12.6%)|1,725 (7.1%)<br><br>|
|Signal Processing|8,266 (78.9%)<br><br>|750 (7.2%)<br><br>|1,136 (10.8%)<br><br>|323 (3.1%)|
|Software<br><br>|3,321 (74.5%)<br><br>|408 (9.2%)<br><br>|461 (10.3%)|265 (6.0%)<br><br>|


###### Table S5: Number of papers by venue rank and gender category.

|Rank|MM<br><br>|MW<br><br>|WM|WW|
|---|---|---|---|---|


|A∗<br><br>|32,325 (79.3%)<br><br>|3,062 (7.5%)|3,692 (9.1%)<br><br>|1,680 (4.1%)|
|---|---|---|---|---|
|A<br><br>|28,020 (75.8%)|3,064 (8.3%)<br><br>|3,851 (10.4%)|2,045 (5.5%)<br><br>|
|B<br><br>|39,782 (76.4%)|4,283 (8.2%)<br><br>|5,943 (11.4%)<br><br>|2,091 (4.0%)|
|C|18,261 (73.1%)<br><br>|2,101 (8.4%)|3,149 (12.6%)<br><br>|1,475 (5.9%)|
|Q1|102,895 (75.9%)<br><br>|10,381 (7.7%)<br><br>|15,173 (11.2%)|7,068 (5.2%)<br><br>|
|Q2<br><br>|49,132 (72.7%)|5,509 (8.2%)<br><br>|8,010 (11.8%)<br><br>|4,962 (7.3%)|
|Q3|23,105 (76.0%)<br><br>|2,134 (7.0%)<br><br>|3,239 (10.7%)<br><br>|1,909 (6.3%)|
|Q4|4,543 (74.5%)<br><br>|436 (7.2%)<br><br>|670 (11.0%)|442 (7.3%)<br><br>|


###### Table S6: Over/under-citation derived from the random-draws model. We present the over/undercitation made by a set of papers (e.g., those in a given gender category or all papers) to another set of papers (also defined by gender category). Here, nobs is the number of citations observed in the original network, while µ and σ are the mean and standard deviation, respectively, of citation counts computed across 100 randomized networks.

|Made by<br><br>|Received by|nobs<br><br>|µ|σ<br><br>|Over/undercitation (%)<br><br>|Z score|p value|
|---|---|---|---|---|---|---|---|


|MM MM MM MM<br><br>|MM MW WM WW|454733 38826 47068 21853<br><br>|438991.5<br><br>40627.3 53171.2 29689.9<br><br>|304.9 179.8 234.7 170.9<br><br>|3.6 −4.4 −11.5 −26.4|51.63 −10.02 −26.01 −45.86<br><br>|< 0.001 < 0.001 < 0.001 < 0.001|
|---|---|---|---|---|---|---|---|
|MW MW MW MW|MM MW WM WW<br><br>|45992 5282 6486 3688<br><br>|47472.8 4594.3 6157.7 3223.2<br><br>|106.1 64.7 72.9 47.2|−3.1 15.0 5.3 14.4<br><br>|−13.96 10.64 4.50 9.85<br><br>|< 0.001 < 0.001 < 0.001 < 0.001|
|WM WM WM WM|MM MW WM WW<br><br>|64414 7692 10244 5586<br><br>|67369.8 6777.6 9189.0 4599.6|131.7 89.4 94.3 65.3<br><br>|−4.4 13.5 11.5 21.4<br><br>|−22.44 10.23 11.19 15.10|< 0.001 < 0.001 < 0.001 < 0.001<br><br>|
|WW WW WW WW<br><br>|MM MW WM WW|27220 3783 5115 4760<br><br>|31674.4 3007.8 4021.0 2174.8<br><br>|86.4 55.2 62.6 41.4<br><br>|−14.1 25.8 27.2 118.9<br><br>|−51.54 14.06 17.48 62.46|< 0.001 < 0.001 < 0.001 < 0.001<br><br>|
|All All All All<br><br>|MM MW WM WW|592359 55583 68913 35887<br><br>|585508.6 55006.9 72539.0 39687.6|357.2 217.8 279.9 202.0<br><br>|1.2 1.0 −5.0 −9.6<br><br>|19.18 2.65 −12.95 −18.82<br><br>|< 0.001 0.004 < 0.001 < 0.001|


###### Table S7: Over/under-citation derived from the homophilic-draws model.

|Made by<br><br>|Received by|nobs|µ<br><br>|σ|Over/undercitation (%)<br><br>|Z score|p value|
|---|---|---|---|---|---|---|---|


|MM MM MM MM<br><br>|MM MW WM WW|454733 38826 47068 21853<br><br>|447203.8<br><br>40175.6 50282.7 24817.9<br><br>|255.1 179.5 195.5 132.2<br><br>|1.7 −3.4 −6.4 −11.9<br><br>|29.51 −7.52 −16.44 −22.43|< 0.001 < 0.001 < 0.001 < 0.001<br><br>|
|---|---|---|---|---|---|---|---|
|MW MW MW MW|MM MW WM WW<br><br>|45992 5282 6486 3688<br><br>|45988.4 5099.5 6662.1 3698.0|87.1 60.2 58.0 49.8<br><br>|0.0 3.6 −2.6 −0.3<br><br>|0.04 3.03 −3.03 −0.20|0.483 0.001 0.001 0.420<br><br>|
|WM WM WM WM|MM MW WM WW<br><br>|64414 7692 10244 5586<br><br>|64612.6 7556.1 10208.7 5558.5<br><br>|101.1 73.0 82.0 59.0|−0.3 1.8 0.3 0.5<br><br>|−1.97 1.86 0.43 0.47<br><br>|0.025 0.031 0.334 0.321<br><br>|
|WW WW WW WW<br><br>|MM MW WM WW|27220 3783 5115 4760<br><br>|28031.5 3661.3 4953.4 4231.7|71.1 43.5 51.9 52.0<br><br>|−2.9 3.3 3.3 12.5<br><br>|−11.41 2.80 3.11 10.16|< 0.001 0.003 < 0.001 < 0.001<br><br>|
|All All All All<br><br>|MM MW WM WW<br><br>|592359 55583 68913 35887|585836.3<br><br>56492.6 72106.9 38306.2<br><br>|324.6 217.7 242.3 170.5<br><br>|1.1 −1.6 −4.4 −6.3|20.10 −4.18<br><br>−13.18<br><br>−14.19<br><br><br>|< 0.001 < 0.001 < 0.001 < 0.001|


###### Table S8: Over/under-citation derived from the preferential-draws model.

|Made by<br><br>|Received by|nobs|µ<br><br>|σ|Over/undercitation (%)<br><br>|Z score|p value|
|---|---|---|---|---|---|---|---|


|MM MM MM MM<br><br>|MM MW WM WW|454733 38826 47068 21853<br><br>|449454.7<br><br>39613.1 48780.3 24631.9<br><br>|341.7 236.0 233.9 169.4<br><br>|1.2<br><br>−2.0<br><br>−3.5 −11.3<br><br><br>|15.45 −3.34 −7.32 −16.40|< 0.001 < 0.001 < 0.001 < 0.001<br><br>|
|---|---|---|---|---|---|---|---|
|MW MW MW MW|MM MW WM WW<br><br>|45992 5282 6486 3688<br><br>|46142.0 5076.2 6506.2 3723.6|86.3 60.2 61.2 48.6<br><br>|−0.3 4.1<br><br>−0.3<br><br>−1.0<br><br><br>|−1.74 3.42 −0.33 −0.73|0.041 < 0.001 0.371 0.232<br><br>|
|WM WM WM WM|MM MW WM WW<br><br>|64414 7692 10244 5586<br><br>|64799.4 7507.8 10029.6 5599.2<br><br>|111.4 69.1 85.6 61.9|−0.6 2.5 2.1 −0.2<br><br>|−3.46 2.67 2.50 −0.21<br><br>|< 0.001 0.004 0.006 0.416<br><br>|
|WW WW WW WW<br><br>|MM MW WM WW|27220 3783 5115 4760<br><br>|27979.6 3644.2 4916.9 4337.2|71.7 51.2 62.0 54.6<br><br>|−2.7 3.8 4.0 9.7<br><br>|−10.60 2.71 3.20 7.74|< 0.001 0.003 < 0.001 < 0.001<br><br>|
|All All All All<br><br>|MM MW WM WW<br><br>|592359 55583 68913 35887|588375.6<br><br>55841.4 70233.1 38291.9<br><br>|427.6 302.3 288.2 217.5<br><br>|0.7<br><br>−0.5<br>−1.9 −6.3<br>|9.32 −0.85 −4.58 −11.06<br><br>|< 0.001 0.196 < 0.001 < 0.001|


###### Table S9: Over/under-citation by all papers to papers by a gender category and subfield.

|Subfield<br><br>|Gender category|nobs|µ|σ<br><br>|Over/undercitation (%)|Z score<br><br>|p value|
|---|---|---|---|---|---|---|---|


|Artificial Intelligence<br><br>|MM WW<br><br>|115843 6324<br><br>|113620.9 7000.1|214.7 125.6<br><br>|2.0 −9.7|10.35 −5.38<br><br>|< 0.001 < 0.001<br><br>|
|---|---|---|---|---|---|---|---|
|Computational Theory and Mathematics|MM WW<br><br>|21814 951<br><br>|21427.3 1077.9|57.6 32.2<br><br>|1.8 −11.8<br><br>|6.71 −3.94<br><br>|< 0.001 < 0.001|
|Computer Graphics and Computer-Aided Design<br><br>|MM WW|11607 158<br><br>|11426.6 223.2|34.7 17.1<br><br>|1.6 −29.2|5.20 −3.80<br><br>|< 0.001 < 0.001|
|Computer Networks and Communications|MM WW<br><br>|79513 2486<br><br>|80036.4 2653.5|145.9 73.6<br><br>|−0.7 −6.3|−3.59 −2.28<br><br>|< 0.001 0.011|
|Computer Science Applications<br><br>|MM WW|5980 1407<br><br>|6195.5 1352.8<br><br>|49.6 37.6<br><br>|−3.5 4.0|−4.35 1.44<br><br>|< 0.001 0.075<br><br>|
|Computer Vision and Pattern Recognition<br><br>|MM WW|69467 1787<br><br>|68487.4 2208.7<br><br>|176.9 72.6<br><br>|1.4 −19.1|5.54 −5.81<br><br>|< 0.001 < 0.001|
|Hardware and Architecture|MM WW<br><br>|24161 517|24200.2 588.2<br><br>|55.3 22.8<br><br>|−0.2 −12.1|−0.71 −3.12<br><br>|0.239 < 0.001|
|Human-Computer Interaction|MM WW<br><br>|9489 1412<br><br>|9235.9 1535.1<br><br>|56.5 47.4|2.7 −8.0<br><br>|4.48 −2.60|< 0.001 0.005<br><br>|
|Information Systems<br><br>|MM WW|39409 3297<br><br>|39386.1 3539.7<br><br>|104.3 61.9<br><br>|0.1 −6.9|0.22 −3.92<br><br>|0.413 < 0.001<br><br>|
|Signal Processing<br><br>|MM WW|14525 376<br><br>|14405.2 422.3<br><br>|55.9 19.5<br><br>|0.8 −11.0|2.14 −2.37<br><br>|0.016 0.009|
|Software|MM WW<br><br>|7318 464|7336.6 677.9<br><br>|48.5 25.0|−0.3 −31.6<br><br>|−0.38 −8.56|0.351 < 0.001<br><br>|


###### Table S10: Over/under-citation by all papers to papers by a gender category and venue type.

|Type<br><br>|Gender category|nobs<br><br>|µ<br><br>|σ<br><br>|Over/undercitation (%)|Z score<br><br>|p value|
|---|---|---|---|---|---|---|---|


|Conference<br><br>|MM WW<br><br>|221681 11520|219533.3<br><br>13012.1|226.9 117.6<br><br>|1.0 −11.5<br><br>|9.47 −12.69<br><br>|< 0.001 < 0.001|
|---|---|---|---|---|---|---|---|
|Journal<br><br>|MM WW|370678 24367<br><br>|368820.3 25325.7<br><br>|316.5 148.2<br><br>|0.5 −3.8|5.87 −6.47<br><br>|< 0.001 < 0.001<br><br>|


###### Table S11: Over/under-citation by all papers to papers by a gender category and subfield.

|Rank<br><br>|Gender category<br><br>|nobs|µ<br><br>|σ<br><br>|Over/undercitation (%)|Z score<br><br>|p value|
|---|---|---|---|---|---|---|---|


|A*<br><br>|MM WW<br><br>|130750 4391<br><br>|129819.0 5360.3|252.5 97.8<br><br>|0.7 −18.1<br><br>|3.69 −9.91<br><br>|< 0.001 < 0.001|
|---|---|---|---|---|---|---|---|
|A<br><br>|MM WW|55092 3667<br><br>|54469.0 3759.5<br><br>|150.5 82.0|1.1 −2.5<br><br>|4.14 −1.13|< 0.001 0.130<br><br>|
|B<br><br>|MM WW<br><br>|37248 1633|36934.5 1814.0<br><br>|82.7 33.8<br><br>|0.8 −10.0|3.79 −5.35<br><br>|< 0.001 < 0.001|
|C<br><br>|MM WW|14350 1163<br><br>|14169.3 1184.6<br><br>|54.6 28.0<br><br>|1.3 −1.8|3.31 −0.77<br><br>|< 0.001 0.220|
|Q1|MM WW<br><br>|257718 16138|256007.4<br><br>17130.2|263.3 153.6<br><br>|0.7 −5.8|6.50 −6.46<br><br>|< 0.001 < 0.001|
|Q2<br><br>|MM WW<br><br>|70613 6768<br><br>|70598.2 6748.6<br><br>|125.3 83.5|0.0 0.3<br><br>|0.12 0.23<br><br>|0.453 0.408|
|Q3<br><br>|MM WW<br><br>|23349 1827<br><br>|23139.9 1993.2|61.1 38.4<br><br>|0.9 −8.3<br><br>|3.42 −4.33|< 0.001 < 0.001<br><br>|
|Q4|MM WW<br><br>|3239 300|3238.2 301.6<br><br>|16.6 9.1|0.0 −0.5<br><br>|0.05 −0.18<br><br>|0.481 0.430|


###### Table S12: Comparison of over/under-citations in networks with and without self-citations.

| | |With self-citations| | |Without self-citations| | |
|---|---|---|---|---|---|---|---|
|Made by<br><br>|Received by|Over/undercitation (%)|Z score<br><br>|p value|Over/undercitation (%)|Z score<br><br>|p value|


|MM MM MM MM<br><br>|MM MW WM WW<br><br>|2.1<br><br>−6.2<br>−7.4 −15.8<br>|33.14 −12.22 −17.19 −22.24<br><br>|< 0.001 < 0.001 < 0.001 < 0.001<br><br>|1.2<br><br>−2.0<br>−3.5 −11.4<br>|14.47 −3.48 −7.03 −17.10<br><br>|< 0.001 < 0.001 < 0.001 < 0.001|
|---|---|---|---|---|---|---|---|
|MW MW MW MW<br><br>|MM MW WM WW|−3.3 24.7 −0.6 2.0<br><br>|−16.06 22.34 −0.58 1.62<br><br>|< 0.001 < 0.001 0.280 0.053<br><br>|−0.3 4.2<br><br>−0.2<br>−1.5<br>|−1.68 3.82<br><br>−0.18<br><br>−1.25<br><br><br>|0.046 < 0.001 0.429 0.105|
|WM WM WM WM<br><br>|MM MW WM WW<br><br>|−3.1 2.7 15.1 2.2|−17.21 2.79 20.71 2.10<br><br>|< 0.001 0.003 < 0.001 0.018|−0.6 2.1 2.2 −0.2<br><br>|−3.18 2.05 2.45 −0.16<br><br>|< 0.001 0.020 0.007 0.438|
|WW WW WW WW<br><br>|MM MW WM WW|−6.4 0.2 1.1 31.1<br><br>|−23.10 0.15 0.90 33.38<br><br>|< 0.001 0.442 0.183 < 0.001|−2.7 3.8 4.2 9.6<br><br>|−11.76 3.14 4.00 8.65|< 0.001 < 0.001 < 0.001 < 0.001<br><br>|
|All All All All|MM MW WM WW<br><br>|0.8<br><br>−1.4<br><br>−2.7 −5.0<br><br><br>|11.50 −2.90 −6.97 −8.51|< 0.001 0.002 < 0.001 < 0.001<br><br>|0.7<br><br>−0.5<br><br>−1.8<br><br><br>−6.4<br><br>|8.90 −1.02 −4.33 −11.12|< 0.001 0.153 < 0.001 < 0.001<br><br>|


###### Table S13: Comparison of over/under-citations in networks with and without isolated papers.

| | |With isolated papers<br><br>| | |Without isolated papers| | |
|---|---|---|---|---|---|---|---|
|Made by|Received by|Over/undercitation (%)<br><br>|Z score|p value<br><br>|Over/undercitation (%)|Z score<br><br>|p value|


|MM MM MM MM<br><br>|MM MW WM WW<br><br>|1.2 −1.4 −3.7 −12.5|15.45 −2.58 −7.57 −18.05<br><br>|< 0.001 0.005 < 0.001 < 0.001<br><br>|1.2<br><br>−2.0<br>−3.5 −11.4<br>|14.47 −3.48 −7.03 −17.10<br><br>|< 0.001 < 0.001 < 0.001 < 0.001|
|---|---|---|---|---|---|---|---|
|MW MW MW MW|MM MW WM WW<br><br>|−0.4 4.8<br><br>−0.0<br><br>−1.9<br>|−1.92 4.05<br><br>−0.02<br><br>−1.35<br><br><br>|0.028 < 0.001 0.493 0.088<br><br>|−0.3 4.2<br><br>−0.2<br>−1.5<br>|−1.68 3.82<br><br>−0.18<br><br>−1.25<br><br><br>|0.046 < 0.001 0.429 0.105|
|WM WM WM WM<br><br>|MM MW WM WW<br><br>|−0.7 3.1 2.5 −0.7|−4.40 3.64 3.35 −0.60<br><br>|< 0.001 < 0.001 < 0.001 0.276|−0.6 2.1 2.2 −0.2<br><br>|−3.18 2.05 2.45 −0.16|< 0.001 0.020 0.007 0.438<br><br>|
|WW WW WW WW|MM MW WM WW<br><br>|−3.1 5.0 4.9 10.3|−10.56 3.48 4.05 8.59<br><br>|< 0.001 < 0.001 < 0.001 < 0.001|−2.7 3.8 4.2 9.6<br><br>|−11.76 3.14 4.00 8.65|< 0.001 < 0.001 < 0.001 < 0.001<br><br>|
|Any Any Any Any<br><br>|MM MW WM WW|0.7 0.2 −1.9 −7.2<br><br>|9.18 0.40 −4.59 −12.13<br><br>|< 0.001 0.343 < 0.001 < 0.001<br><br>|0.7<br><br>−0.5<br>−1.8 −6.4<br>|8.90 −1.02 −4.33 −11.12<br><br>|< 0.001 0.153 < 0.001 < 0.001|


###### Table S14: Comparison of the over/under-citation made by MM papers versus WW papers.

|Received by|Made by MM<br><br>|Made by WW<br><br>|t-statistic|p value|
|---|---|---|---|---|
|MM MW WM WW<br><br>|1.24 ± 0.18<br><br>−1.13 ± 1.33<br><br>−2.40 ± 1.16 −10.69 ± 1.31<br><br><br>|−2.27 5.62 3.82 7.78|194.7 −50.6 −53.6 −141.1<br><br>|< 0.001 < 0.001 < 0.001 < 0.001<br><br>|


###### Table S15: Comparison of the over/under-citation made by conference papers versus journal papersfor MM and WW papers.

|Made by|Received by|Conference<br><br>|Journal|t-statistic<br><br>|p value|
|---|---|---|---|---|---|
|MM<br><br>|MM MW WM WW|1.63 −2.30 −6.06 −18.30<br><br>|1.10 ± 0.04 −3.14 ± 0.35 −3.84 ± 0.33 −9.52 ± 0.45<br><br>|−117.8 −24.1 66.9 194.2<br><br>|< 0.001 < 0.001 < 0.001 < 0.001|
|MM|MM MW WM WW<br><br>|−2.74 2.09 3.03 13.59<br><br>|−2.79 ± 0.29 7.63 ± 1.86 −0.43 ± 1.49 11.68 ± 1.41|−1.6 29.8 −23.2 −13.5<br><br>|0.114 < 0.001 < 0.001 < 0.001|


###### Table S16: Comparison of the over/under-citation made by papers with prominent authors versusthose without for MM and WW papers.

|Made by|Received by<br><br>|With prominent authors|Without prominent authors<br><br>|t-statistic|p value|
|---|---|---|---|---|---|
|MM<br><br>|MM MW WM WW<br><br>|1.56 −3.86 −5.10 −19.17|1.11 ± 0.10 −2.04 ± 0.70 −4.36 ± 0.73 −11.55 ± 0.95<br><br>|−44.2 26.0 10.3 79.9|< 0.001 < 0.001 < 0.001 < 0.001<br><br>|
|WW<br><br>|MM MW WM WW|−2.50 17.96 4.97 −2.77<br><br>|−4.97 ± 0.63 8.61 ± 3.30 7.74 ± 3.30 18.66 ± 3.01<br><br>|−39.4 −28.3 8.4 71.2|< 0.001 < 0.001 < 0.001 < 0.001<br><br>|


###### Table S17: Comparison of the over/under-citation made by papers with high MAor values versusthose with low MAor values for MM and WW papers.

|Made by|Received by<br><br>|Top half of MAor<br><br>|Bottom half of MAor<br><br>|t-statistic|p value|
|---|---|---|---|---|---|
|MM<br><br>|MM MW WM WW|1.11 −0.97 −4.08 −10.87<br><br>|1.66 ± 0.04<br><br>−5.13 ± 0.37<br><br>−6.35 ± 0.34 −15.87 ± 0.47<br><br><br>|122.6 −113.1 −67.3 −106.0|< 0.001 < 0.001 < 0.001 < 0.001<br><br>|
|MM<br><br>|MM MW WM WW|−3.56 5.02 2.56 13.51<br><br>|−1.87 ± 0.42 5.52 ± 2.47 −3.34 ± 1.86 16.10 ± 1.64|40.6 2.0 −31.7 15.7<br><br>|< 0.001 0.044 < 0.001 < 0.001|


###### Table S18: Statistical significance of relationships among the paper’s three categorical variables.

|Gender category|Characteristic X|Characteristic Y<br><br>|χ2-statistic|p value|
|---|---|---|---|---|
|MM|Venue type|Participation of prominent authors<br><br>|4069.5|< 0.001|
| |Venue type|Local coauthorship network<br><br>|568.8<br><br>|< 0.001|
| |Participation of prominent authors<br><br>|Local coauthorship network<br><br>|924.2|< 0.001|
|WW<br><br>|Venue type|Participation of prominent authors<br><br>|270.1|< 0.001|
| |Venue type|Local coauthorship network<br><br>|2.5|0.114|
| |Participation of prominent authors<br><br>|Local coauthorship network<br><br>|320.7<br><br>|< 0.001|


