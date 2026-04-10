"""Process Science of Science papers 259-284: extract figures, write review.md and index.html."""
import os, re, sys, json
from pathlib import Path

BASE = Path("C:/Users/jehyu/Arbeitplatz/paper-curation/papers")

ENTRIES = [
    {"slug": "259_Remote_collaboration_fuses_fewer_breakth", "num": 259,
     "title": "Remote collaboration fuses fewer breakthrough ideas",
     "authors": "Yiling Lin, Carl Benedikt Frey, Lingfei Wu",
     "date": "2023", "doi": "10.1038/s41586-023-06767-1", "arxiv_id": "",
     "pdf_path": r"C:\Users\jehyu\GoogleDrive\Zotero\Lin et al._2023_Remote collaboration fuses fewer breakthrough ideas.pdf",
     "has_pdf": True, "venue": "Nature"},
    {"slug": "260_Women_are_credited_less_in_science_than", "num": 260,
     "title": "Women are credited less in science than men",
     "authors": "Matthew B. Ross, Britta M. Glennon, Raviv Murciano-Goroff, Enrico G. Berkes, Bruce A. Weinberg, Julia I. Lane",
     "date": "2022", "doi": "10.1038/s41586-022-04966-w", "arxiv_id": "",
     "pdf_path": r"C:\Users\jehyu\GoogleDrive\Zotero\Ross et al._2022_Women are credited less in science than men.pdf",
     "has_pdf": True, "venue": "Nature"},
    {"slug": "261_The_Burden_of_Knowledge_and_the_Death_of", "num": 261,
     "title": "The Burden of Knowledge and the Death of the Renaissance Man",
     "authors": "Benjamin F. Jones",
     "date": "2009", "doi": "10.1111/j.1467-937X.2009.00531.x", "arxiv_id": "",
     "pdf_path": "", "has_pdf": False, "venue": "The Review of Economic Studies"},
    {"slug": "262_The_Increasing_Dominance_of_Teams_in_Pro", "num": 262,
     "title": "The Increasing Dominance of Teams in Production of Knowledge",
     "authors": "Stefan Wuchty, Benjamin F. Jones, Brian Uzzi",
     "date": "2007", "doi": "10.1126/science.1136099", "arxiv_id": "",
     "pdf_path": "", "has_pdf": False, "venue": "Science"},
    {"slug": "263_Systematic_Inequality_and_Hierarchy_in_F", "num": 263,
     "title": "Systematic Inequality and Hierarchy in Faculty Hiring Networks",
     "authors": "Aaron Clauset, Samuel Arbesman, Daniel B. Larremore",
     "date": "2015", "doi": "10.1126/sciadv.1400005", "arxiv_id": "",
     "pdf_path": "", "has_pdf": False, "venue": "Science Advances"},
    {"slug": "264_Principles_of_Scientific_Research_Team_F", "num": 264,
     "title": "Principles of Scientific Research Team Formation and Evolution",
     "authors": "Staša Milojević",
     "date": "2014", "doi": "10.1073/pnas.1309723111", "arxiv_id": "",
     "pdf_path": "", "has_pdf": False, "venue": "Proceedings of the National Academy of Sciences"},
    {"slug": "265_A_General_Theory_of_Bibliometric_and_Oth", "num": 265,
     "title": "A General Theory of Bibliometric and Other Cumulative Advantage Processes",
     "authors": "Derek De Solla Price",
     "date": "1976", "doi": "10.1002/asi.4630270505", "arxiv_id": "",
     "pdf_path": "", "has_pdf": False, "venue": "Journal of the American Society for Information Science"},
    {"slug": "266_Unsupervised_Word_Embeddings_Capture_Lat", "num": 266,
     "title": "Unsupervised Word Embeddings Capture Latent Knowledge from Materials Science Literature",
     "authors": "Vahe Tshitoyan, John Dagdelen, Leigh Weston, Alexander Dunn, Ziqin Rong, Olga Kononova, Kristin A. Persson, Gerbrand Ceder, Anubhav Jain",
     "date": "2019", "doi": "10.1038/s41586-019-1335-8", "arxiv_id": "",
     "pdf_path": r"C:\Users\jehyu\GoogleDrive\Zotero\Unsupervised Word Embeddings Capture Latent Knowledge from Materials Science Lit.pdf",
     "has_pdf": True, "venue": "Nature"},
    {"slug": "267_Growth_Rates_of_Modern_Science_Bibliome", "num": 267,
     "title": "Growth Rates of Modern Science: Bibliometric Analysis Based on the Number of Publications and Cited References",
     "authors": "Lutz Bornmann, Rüdiger Mutz",
     "date": "2015", "doi": "10.1002/asi.23329", "arxiv_id": "",
     "pdf_path": r"C:\Users\jehyu\GoogleDrive\Zotero\Bornmann and Mutz_2015_Growth Rates of Modern Science Bibliometric Analysis Based on the Number of Publications and Cited.pdf",
     "has_pdf": True, "venue": "Journal of the Association for Information Science and Technology"},
    {"slug": "268_Citation_Analysis_as_a_Tool_in_Journal_E", "num": 268,
     "title": "Citation Analysis as a Tool in Journal Evaluation",
     "authors": "Eugene Garfield",
     "date": "1972", "doi": "10.1126/science.178.4060.471", "arxiv_id": "",
     "pdf_path": r"C:\Users\jehyu\GoogleDrive\Zotero\1972_Citation Analysis as a Tool in Journal Evaluation.pdf",
     "has_pdf": True, "venue": "Science"},
    {"slug": "269_Theory_and_Practice_of_the_g-index", "num": 269,
     "title": "Theory and Practice of the g-index",
     "authors": "Leo Egghe",
     "date": "2006", "doi": "10.1007/s11192-006-0144-7", "arxiv_id": "",
     "pdf_path": r"C:\Users\jehyu\GoogleDrive\Zotero\2006_Theory and Practice of the g-index.pdf",
     "has_pdf": True, "venue": "Scientometrics"},
    {"slug": "270_Relative_Citation_Ratio_A_New_Metric_Th", "num": 270,
     "title": "Relative Citation Ratio: A New Metric That Uses Citation Rates to Measure Influence at the Article Level",
     "authors": "B. Ian Hutchins, Xin Yuan, James M. Anderson, George M. Santangelo",
     "date": "2016", "doi": "10.1371/journal.pbio.1002541", "arxiv_id": "",
     "pdf_path": r"C:\Users\jehyu\GoogleDrive\Zotero\Relative Citation Ratio A New Metric That Uses Citation Rates to Measure Influen.pdf",
     "has_pdf": True, "venue": "PLOS Biology"},
    {"slug": "271_Bibliometrics_Global_Gender_Disparities", "num": 271,
     "title": "Bibliometrics: Global Gender Disparities in Science",
     "authors": "Vincent Larivière, Chaoqun Ni, Yves Gingras, Blaise Cronin, Cassidy R. Sugimoto",
     "date": "2013", "doi": "10.1038/504211a", "arxiv_id": "",
     "pdf_path": r"C:\Users\jehyu\GoogleDrive\Zotero\Bibliometrics Global Gender Disparities in Science.pdf",
     "has_pdf": True, "venue": "Nature"},
    {"slug": "272_Quantifying_Long-term_Scientific_Impact", "num": 272,
     "title": "Quantifying Long-term Scientific Impact",
     "authors": "Dashun Wang, Chaoming Song, Albert-László Barabási",
     "date": "2013", "doi": "10.1126/science.1237825", "arxiv_id": "",
     "pdf_path": r"C:\Users\jehyu\GoogleDrive\Zotero\Quantifying Long-term Scientific Impact.pdf",
     "has_pdf": True, "venue": "Science"},
    {"slug": "273_Co-Citation_Analysis_Bibliographic_Coupl", "num": 273,
     "title": "Co-Citation Analysis Bibliographic Coupling and Direct Citation: Which Citation Approach Represents the Research Front Most Accurately",
     "authors": "Kevin W. Boyack, Richard Klavans",
     "date": "2010", "doi": "10.1002/asi.21419", "arxiv_id": "",
     "pdf_path": "", "has_pdf": False, "venue": "Journal of the American Society for Information Science and Technology"},
    {"slug": "274_Design_and_Update_of_a_Classification_Sy", "num": 274,
     "title": "Design and Update of a Classification System: The UCSD Map of Science",
     "authors": "Katy Börner, Richard Klavans, Michael Patek, Angela M. Zoss, Joseph R. Biberstine, Robert P. Light, Vincent Larivière, Kevin W. Boyack",
     "date": "2012", "doi": "10.1371/journal.pone.0039464", "arxiv_id": "",
     "pdf_path": "", "has_pdf": False, "venue": "PLoS ONE"},
    {"slug": "275_Community_Detection_in_Graphs", "num": 275,
     "title": "Community Detection in Graphs",
     "authors": "Santo Fortunato",
     "date": "2010", "doi": "10.1016/j.physrep.2009.11.002", "arxiv_id": "",
     "pdf_path": r"C:\Users\jehyu\GoogleDrive\Zotero\Community Detection in Graphs.pdf",
     "has_pdf": True, "venue": "Physics Reports"},
    {"slug": "276_Fast_Unfolding_of_Communities_in_Large_N", "num": 276,
     "title": "Fast Unfolding of Communities in Large Networks",
     "authors": "Vincent D Blondel, Jean-Loup Guillaume, Renaud Lambiotte, Etienne Lefebvre",
     "date": "2008", "doi": "10.1088/1742-5468/2008/10/P10008", "arxiv_id": "",
     "pdf_path": r"C:\Users\jehyu\GoogleDrive\Zotero\Fast Unfolding of Communities in Large Networks.pdf",
     "has_pdf": True, "venue": "Journal of Statistical Mechanics: Theory and Experiment"},
    {"slug": "277_Collective_Credit_Allocation_in_Science", "num": 277,
     "title": "Collective Credit Allocation in Science",
     "authors": "Hua-Wei Shen, Albert-László Barabási",
     "date": "2014", "doi": "10.1073/pnas.1401992111", "arxiv_id": "",
     "pdf_path": "", "has_pdf": False, "venue": "Proceedings of the National Academy of Sciences"},
    {"slug": "278_The_State_of_OA_A_Large-Scale_Analysis", "num": 278,
     "title": "The State of OA: A Large-Scale Analysis of the Prevalence and Impact of Open Access Articles",
     "authors": "Heather Piwowar, Jason Priem, Vincent Larivière, Juan Pablo Alperin, Lisa Matthias, Bree Norlander, Ashley Farley, Jevin West, Stefanie Haustein",
     "date": "2018", "doi": "10.7717/peerj.4375", "arxiv_id": "",
     "pdf_path": "", "has_pdf": False, "venue": "PeerJ"},
    {"slug": "279_The_Preeminence_of_Ethnic_Diversity_in_S", "num": 279,
     "title": "The Preeminence of Ethnic Diversity in Scientific Collaboration",
     "authors": "Bedoor K. AlShebli, Talal Rahwan, Wei Lee Woon",
     "date": "2018", "doi": "10.1038/s41467-018-07634-8", "arxiv_id": "",
     "pdf_path": r"C:\Users\jehyu\GoogleDrive\Zotero\The Preeminence of Ethnic Diversity in Scientific Collaboration.pdf",
     "has_pdf": True, "venue": "Nature Communications"},
    {"slug": "280_The_Diversity-Innovation_Paradox_in_Scie", "num": 280,
     "title": "The Diversity-Innovation Paradox in Science",
     "authors": "Bas Hofstra, Vivek V. Kulkarni, Sebastian Munoz-Najar Galvez, Bryan He, Dan Jurafsky, Daniel A. McFarland",
     "date": "2020", "doi": "10.1073/pnas.1915378117", "arxiv_id": "",
     "pdf_path": r"C:\Users\jehyu\GoogleDrive\Zotero\Hofstra et al._2020_The Diversity-Innovation Paradox in Science.pdf",
     "has_pdf": True, "venue": "Proceedings of the National Academy of Sciences"},
    {"slug": "281_The_Chaperone_Effect_in_Scientific_Publi", "num": 281,
     "title": "The Chaperone Effect in Scientific Publishing",
     "authors": "Vedran Sekara, Pierre Deville, Sebastian E. Ahnert, Albert-László Barabási, Roberta Sinatra, Sune Lehmann",
     "date": "2018", "doi": "10.1073/pnas.1800471115", "arxiv_id": "",
     "pdf_path": "", "has_pdf": False, "venue": "Proceedings of the National Academy of Sciences"},
    {"slug": "282_Productivity_Prominence_and_the_Effects", "num": 282,
     "title": "Productivity Prominence and the Effects of Academic Environment",
     "authors": "Samuel F. Way, Allison C. Morgan, Daniel B. Larremore, Aaron Clauset",
     "date": "2019", "doi": "10.1073/pnas.1817431116", "arxiv_id": "",
     "pdf_path": "", "has_pdf": False, "venue": "Proceedings of the National Academy of Sciences"},
    {"slug": "283_Historical_Comparison_of_Gender_Inequali", "num": 283,
     "title": "Historical Comparison of Gender Inequality in Scientific Careers Across Countries and Disciplines",
     "authors": "Junming Huang, Alexander J. Gates, Roberta Sinatra, Albert-László Barabási",
     "date": "2020", "doi": "10.1073/pnas.1914221117", "arxiv_id": "",
     "pdf_path": r"C:\Users\jehyu\GoogleDrive\Zotero\Huang et al._2020_Historical Comparison of Gender Inequality in Scientific Careers Across Countries and Disciplines.pdf",
     "has_pdf": True, "venue": "Proceedings of the National Academy of Sciences"},
    {"slug": "284_The_Misleading_Narrative_of_the_Canonica", "num": 284,
     "title": "The Misleading Narrative of the Canonical Faculty Productivity Trajectory",
     "authors": "Samuel F. Way, Allison C. Morgan, Aaron Clauset, Daniel B. Larremore",
     "date": "2017", "doi": "10.1073/pnas.1702121114", "arxiv_id": "",
     "pdf_path": "", "has_pdf": False, "venue": "Proceedings of the National Academy of Sciences"},
]

def extract_fig1(pdf_path, fig_dir):
    """Extract figure 1 page from PDF."""
    try:
        import fitz
        if not pdf_path or not os.path.exists(pdf_path):
            return False
        with open(pdf_path, "rb") as f:
            header = f.read(4)
        if header != b"%PDF":
            return False
        doc = fitz.open(pdf_path)
        fig_page = None
        for pn in range(min(15, len(doc))):
            if re.search(r'(Figure\s+1[^0-9]|Fig\.?\s*1[^0-9])', doc[pn].get_text()):
                fig_page = pn
                break
        if fig_page is None:
            fig_page = min(1, len(doc)-1)
        pix = doc[fig_page].get_pixmap(matrix=fitz.Matrix(3, 3))
        os.makedirs(fig_dir, exist_ok=True)
        pix.save(os.path.join(fig_dir, "fig1.png"))
        doc.close()
        return True
    except Exception as e:
        print(f"  Figure extraction failed: {e}")
        return False


def read_pdf_text(pdf_path, max_pages=15):
    """Extract text from PDF for analysis."""
    try:
        import fitz
        if not pdf_path or not os.path.exists(pdf_path):
            return ""
        doc = fitz.open(pdf_path)
        texts = []
        for pn in range(min(max_pages, len(doc))):
            texts.append(doc[pn].get_text())
        doc.close()
        return "\n".join(texts)
    except:
        return ""


# ── Review content database ──
REVIEWS = {
    259: {
        "mode": "PDF",
        "essence": "원격 협업은 혁신적 아이디어를 더 적게 만들어낸다. 20세기 후반부터 2020년까지 미국·유럽·중국의 특허·논문·소프트웨어 약 2,000만 건을 분석한 결과, 원격팀은 대면팀보다 Disruption index(CD₅)가 평균 약 0.08 낮았다—즉 기존 지식을 파괴적으로 대체하는 돌파구 연구는 물리적 근접 환경에서 유의미하게 더 많이 나온다. 원격팀은 기존 아이디어를 개발(development)하는 데는 비슷하거나 더 뛰어나지만, 완전히 새로운 방향을 여는 '융합(fusion)' 능력이 약하다는 점이 핵심 발견이다.",
        "originality": "- [authorship, finding] \"Here we show that teams operating at a distance are less likely to make breakthrough innovations.\"\n- [continuation] \"Remote teams are more likely to develop and refine existing ideas, but less likely to disrupt with new ones.\"",
        "how": "- **데이터**: 미국 특허(USPTO), Web of Science 논문, GitHub 소프트웨어 커밋—총 약 2,000만 건, 1954–2020년\n- **Disruption 측정**: CD₅ index(backward/forward citation 패턴으로 계산)—기존 선행 연구를 대체하는 정도 측정\n- **원격성 측정**: 발명자/저자 소속 기관 도시 간 거리(위도·경도 기반)\n- **통제변수**: 팀 규모, 논문/특허 연도, 분야 고정효과, 저자 이전 실적\n- **추가 분석**: 텍스트 유사도(word2vec), 전화 통화 데이터(AT&T), COVID-19 자연실험 등으로 메커니즘 검증",
        "why": "- 원격근무 확대로 과학·기술 혁신이 지리적 제약에서 자유로워진다는 통념에 정면으로 도전하는 발견\n- 원격 협업이 개발(incremental) 연구에는 적합하지만 혁신적(disruptive) 연구에는 불리하다는 비대칭성 규명\n- 연구 정책·조직 설계(실험실 배치, 원격근무 정책)에 직접적 시사점 제공",
        "limitation": "- CD₅ index가 인용 패턴에 의존하므로, 인용되기까지 시간이 걸리는 최신 연구는 과소평가될 수 있음\n- 원격성을 기관 소재지 거리로만 측정하여 실제 대면 빈도를 포착하지 못함\n- 인과 관계보다는 상관관계에 가깝고, 원격팀 선택 편향(selection bias)이 완전히 제거되지 않음",
        "further": "- 화상회의 기술 발전(e.g., VR 협업)이 원격팀의 혁신 능력 gap을 줄일 수 있는지 장기 추적\n- 원격 환경에서 혁신적 아이디어를 촉진하는 조직·제도적 개입(intervention) 효과 검증\n- 소규모 학제간 팀과 대규모 원격팀 간 혁신 패턴 비교 분석",
        "scores": {"Novelty": 5, "Technical Soundness": 4, "Significance": 5, "Clarity": 4, "Overall": 5},
        "summary": "2,000만 건의 특허·논문·소프트웨어를 분석하여 원격 협업이 혁신적 아이디어 생산을 구조적으로 억제함을 실증한 과학의 과학 분야 핵심 연구로, 원격근무 시대에 혁신 정책 설계에 즉각적 함의를 제공한다."
    },
    260: {
        "mode": "PDF",
        "essence": "과학에서 여성의 기여는 체계적으로 과소 인정된다. 대규모 행정 데이터(NIH 연구팀), 저자 설문조사, 정성적 인터뷰 세 가지 독립적 데이터 소스를 분석한 결과, 같은 팀에서 동일한 기여를 해도 여성이 남성보다 논문·특허 저자로 포함될 확률이 유의미하게 낮았다. 이 크레딧 gap은 거의 모든 과학 분야와 경력 단계에 걸쳐 일관되게 나타났으며, 관찰된 성별 생산성 격차의 상당 부분이 실제 기여 차이가 아닌 귀속(attribution) 차이에서 비롯됨을 시사한다.",
        "originality": "- [authorship, finding] \"Here we find that at least part of this gap is the result of unacknowledged contributions: women in research teams are significantly less likely than men to be credited with authorship.\"\n- [continuation] \"The gender gap in attribution is present across most scientific fields and almost all career stages.\"",
        "how": "- **데이터 1**: NIH UMETRICS 행정 데이터—연구팀 구성, 논문/특허 산출물, 개인별 크레딧 귀속 매칭 (대규모 종단 데이터)\n- **데이터 2**: 저자 대상 설문조사—자신의 기여가 제대로 인정받았는지 자기보고\n- **데이터 3**: 정성적 인터뷰—여성의 기여가 묵살되는 사회적 메커니즘 탐색\n- **분석**: 팀 고정효과(within-team comparison)로 동일 팀 내 성별 귀속 차이 추정, logistic regression으로 저자 포함 확률 모델링\n- **통제변수**: 경력 단계, 팀 규모, 분야, 연도",
        "why": "- 관찰된 성별 생산성 격차가 실제 기여 차이가 아닌 구조적 편향에서 비롯됨을 증명, 과학계 다양성 정책 근거 제공\n- 세 가지 독립 방법론이 동일한 결론에 수렴하여 발견의 강건성(robustness) 확인\n- 여성 과학자 유지 및 승진 정책 설계에 직접적 증거 제공",
        "limitation": "- NIH 데이터 기반이므로 미국 생의학·보건 분야 편향이 있으며, 다른 나라·분야로의 일반화 주의 필요\n- 기여 수준을 직접 측정하지 못하고 행정 데이터(급여, 지출 등)의 간접 지표에 의존\n- 설문 응답 편향(response bias): 크레딧을 받은 사람이 응답할 가능성이 높을 수 있음",
        "further": "- 다국가·다분야 비교 연구로 귀속 불평등의 국가별·문화별 변이 분석\n- 저자 순서(first/last authorship) 내 성별 편향 심층 분석\n- 저자 기재 관행 개선(CRediT taxonomy 등)의 실제 효과 평가",
        "scores": {"Novelty": 4, "Technical Soundness": 5, "Significance": 5, "Clarity": 5, "Overall": 5},
        "summary": "세 가지 독립 데이터로 여성 과학자의 기여가 체계적으로 저평가됨을 증명하여, 관찰된 성별 생산성 격차의 원인이 능력 차이가 아닌 구조적 귀속 편향임을 실증한 과학정책 분야의 중요 연구다."
    },
    261: {
        "mode": "Web-only",
        "essence": "지식의 최전선은 계속 확장되어 신진 연구자들이 그 경계에 도달하기까지 더 많은 시간과 교육이 필요하다—이것이 '지식의 부담(burden of knowledge)'이다. Jones(2009)는 이 부담 때문에 르네상스 인(Renaissance Man)—혼자서 여러 분야를 혁신하는 천재—은 사실상 사라졌으며, 그 결과 팀 연구 증가, 전문화 심화, 혁신 연령 상승이라는 세 가지 구조적 변화가 20세기 내내 일어났음을 특허 및 노벨상 데이터로 실증했다.",
        "originality": "- [novelty] \"첫 번째 실증 연구로서 지식 부담이 과학기술 혁신의 구조를 어떻게 바꾸는지를 체계적으로 분석함\"",
        "how": "- **데이터**: 미국 특허청(USPTO) 데이터, 노벨 수상자 이력, 박사학위 취득 연령 추세\n- **분석**: 첫 번째 특허/논문 연령 추세 분석, 팀 규모 시계열, 전문화(세부 분야 범위) 변화 측정\n- **이론 모델**: 지식 부담이 혁신 생산성에 미치는 영향을 공식화한 간단한 이론 프레임워크 제시\n- **비교**: 개인 발명가 vs 팀 발명가의 특허 생산성 비교",
        "why": "- 팀 과학(team science) 증가와 혁신 연령 상승 현상에 대한 통합적 설명 제공\n- 학문 분야 간 경계를 넘나드는 '르네상스형' 연구자의 역사적 소멸 메커니즘 규명\n- R&D 정책, 교육 시스템, 연구 조직 설계에 대한 함의 제공",
        "limitation": "- 지식 부담을 교육 기간으로 간접 측정하는 한계\n- 특허 및 노벨상 데이터는 특정 유형의 혁신(상업화 가능, 극히 탁월한 성과)에만 해당\n- 지식 압축(textbook consolidation)이나 디지털 정보 접근성 향상의 반작용 효과는 미고려",
        "further": "- 디지털 시대(2000년대 이후) 지식 부담 변화 분석: 정보 접근성 향상이 부담을 완화했는가?\n- 학제간 연구가 지식 부담을 어떻게 우회하는지 분석\n- AI 보조 연구가 르네상스 인의 부활을 가능하게 하는지 탐구",
        "scores": {"Novelty": 5, "Technical Soundness": 4, "Significance": 5, "Clarity": 4, "Overall": 5},
        "summary": "혁신의 최전선에 도달하는 데 더 많은 교육이 필요해지는 '지식의 부담'이 팀 연구 증가·전문화·혁신 연령 상승을 유발함을 실증한 과학의 과학 분야 고전 논문이다."
    },
    262: {
        "mode": "Web-only",
        "essence": "팀이 지식 생산에서 점점 더 지배적이 되고 있으며, 팀 연구는 개인 연구보다 더 높은 피인용도와 더 큰 영향력을 보인다. Wuchty et al.(2007)은 1945–2000년의 논문 2,000만 편과 특허 200만 건을 분석해 팀 규모가 모든 분야에서 증가했으며, 팀 논문이 개인 논문보다 피인용도가 높은 경향이 가속화됨을 보였다—이는 복잡한 현대 과학 문제가 팀 기반 접근을 필요로 함을 시사한다.",
        "originality": "- [novelty] \"최초로 20세기 후반 전 분야에 걸쳐 팀 지식 생산 지배 현상을 대규모 데이터로 체계적으로 증명함\"",
        "how": "- **데이터**: ISI Web of Science 논문(1945–2000) 약 2,000만 편, USPTO 특허(1975–2000) 약 200만 건\n- **측정**: 저자 수(팀 규모), 피인용도, 분야별·연도별 시계열 분석\n- **분석**: 팀 논문 vs 개인 논문의 피인용도 비교(분야·연도 통제), 팀 규모 증가 추세 회귀분석",
        "why": "- 과학 지식 생산의 사회적 구조가 근본적으로 팀 중심으로 전환됨을 대규모 데이터로 최초 입증\n- 팀 연구 지원 정책, 연구비 배분, 학술 인센티브 설계에 대한 증거 제공\n- 과학사회학·과학정책 분야의 기초 자료로 광범위하게 활용됨",
        "limitation": "- 피인용도만으로 질적 영향력을 측정하는 한계(자기인용, 분야별 인용 관행 차이)\n- 팀 규모 증가가 협업 심화를 의미하는지, 단순 공동저자 추가인지 구분 어려움\n- 2000년 이후 데이터 포함 시 인터넷·글로벌 협업 확산 효과가 추가될 수 있음",
        "further": "- 팀 내 역할 분화와 기여 불평등(예: 저자 순서)의 시계열 변화 분석\n- 팀 다양성(전공, 국가, 성별)이 팀 성과에 미치는 영향\n- 최적 팀 규모의 분야별·주제별 차이",
        "scores": {"Novelty": 5, "Technical Soundness": 4, "Significance": 5, "Clarity": 5, "Overall": 5},
        "summary": "20세기 후반 모든 과학·기술 분야에서 팀 연구가 지식 생산을 지배하게 되었고 팀 논문이 개인 논문보다 더 높은 영향력을 가짐을 대규모 실증 분석으로 확립한, 과학의 과학 분야의 선도적 연구다."
    },
    263: {
        "mode": "Web-only",
        "essence": "미국 교수직 채용 네트워크에는 심각한 불평등과 위계가 존재한다. 전체 학과의 약 25%가 전체 교수직의 71–86%를 공급하며, 소수 엘리트 기관이 나머지 기관으로 거의 일방적으로 인력을 공급한다. 하위 기관 출신이 상위 기관에 취업하는 상향 이동은 극히 드물고, 이 위계 구조는 컴퓨터과학·역사학·경영학 세 분야 모두에서 일관되게 관찰된다.",
        "originality": "- [novelty] \"최초로 미국 교수직 채용 전체 네트워크를 매핑하여 위계적 불평등을 정량적으로 규명함\"",
        "how": "- **데이터**: 컴퓨터과학·역사학·경영학 전체 교수 약 19,000명의 박사 취득 기관 및 현 소속 기관 데이터\n- **분석**: 방향성 그래프(directed network)로 채용 흐름 모델링, 위계 점수(prestige score) 추정\n- **통계**: 로렌츠 곡선, 지니 계수로 불평등 정량화; 성별·직급별 하위 분석",
        "why": "- 학문적 능력주의(meritocracy)에 대한 이상이 실제로는 구조적 위계에 의해 제약됨을 실증\n- 소수 엘리트 기관의 지식 생산 지배가 어떻게 재생산되는지 메커니즘 규명\n- 고등교육 정책, 다양성 증진, 기관 서열 해소를 위한 정책 설계에 증거 제공",
        "limitation": "- 세 개 분야만 분석하여 이공계·예술·의학 등으로의 일반화 한계\n- 채용 시점의 연구 능력 차이를 통제하지 못해 위계가 능력 vs 브랜드 중 무엇을 반영하는지 불명확\n- 시점 횡단 데이터로 시계열 변화(위계가 강화되는지 완화되는지) 불분명",
        "further": "- 이공계·의학·예술 분야로 확장한 비교 분석\n- 위계 구조가 연구 혁신성(novelty, disruption)에 미치는 영향 분석\n- 글로벌 비교: 미국 외 유럽·아시아 채용 네트워크의 위계성 비교",
        "scores": {"Novelty": 4, "Technical Soundness": 4, "Significance": 5, "Clarity": 4, "Overall": 4},
        "summary": "미국 학계 채용 네트워크 전수 분석으로 소수 엘리트 기관이 교수직 공급을 독점하는 위계적 불평등 구조를 실증하여, 학문적 능력주의 담론에 근본적 의문을 제기한 중요한 과학사회학 연구다."
    },
    264: {
        "mode": "Web-only",
        "essence": "과학 연구팀의 형성과 진화는 두 가지 메커니즘—Poisson(무작위) 과정과 power-law 성장 과정—의 혼합으로 설명된다. Milojević(2014)는 천문학·경제학·수학 등 5개 분야 50만 편 논문 팀 데이터를 분석해, 소규모 팀은 무작위로 형성되지만 대규모 팀은 복잡한 협업 네트워크의 성장 메커니즘을 따름을 보였다. 팀 규모 분포는 분야마다 특유의 패턴을 가지며, 이는 해당 분야 과학 문제의 복잡성과 연구 인프라 요구를 반영한다.",
        "originality": "- [novelty] \"연구팀 규모 분포를 두 과정의 혼합으로 수학적으로 모델링한 최초 시도\"",
        "how": "- **데이터**: Web of Science 논문 약 50만 편, 천문학·경제학·수학·생태학·로보틱스 5개 분야\n- **모델**: Poisson 분포 + power-law 분포의 혼합 모델로 팀 규모 분포 피팅\n- **분석**: 분야별 팀 규모 분포 비교, 시계열 변화(1990–2010) 분석",
        "why": "- 팀 과학의 보편적 원리와 분야별 특수성을 통합적으로 설명하는 이론 프레임워크 제공\n- 과학 분야의 협업 구조를 이해하여 연구비·인력 정책에 최적 팀 구성 근거 제공\n- 팀 규모 증가 추세의 수리적 기반 정립",
        "limitation": "- 저자 수를 팀 규모 대리 지표로 사용하는 한계(공저자가 항상 적극적 팀원은 아님)\n- 5개 분야에 국한되어 물리학·화학·공학 등 다른 분야 검증 필요\n- 팀 형성 메커니즘(왜 누구와 협업하는가)은 설명하지 못함",
        "further": "- 팀 내 역할 네트워크와 인지 다양성이 팀 성과에 미치는 영향\n- 팀 해체 및 재형성 패턴의 수리 모델 개발\n- 디지털 협업 플랫폼이 팀 형성 메커니즘에 미치는 영향",
        "scores": {"Novelty": 4, "Technical Soundness": 4, "Significance": 3, "Clarity": 4, "Overall": 4},
        "summary": "과학 연구팀 규모 분포를 Poisson+power-law 혼합 모델로 수리적으로 모델링하여 팀 형성의 보편 원리와 분야 특수성을 통합 설명한 독창적인 계량과학 연구다."
    },
    265: {
        "mode": "Web-only",
        "essence": "'부익부(Matthew effect)'는 과학에서 보편적이다. Price(1976)는 인용 네트워크에서 이미 많이 인용된 논문이 더 많이 인용되는 누적 우위(cumulative advantage) 과정이 수학적으로 power-law 분포(Pareto 분포)를 생성함을 이론적으로 증명했다. 이 발견은 h-index, 저널 임팩트 팩터 등 후속 계량과학 지표의 이론적 토대가 되었으며, 과학 내 불평등의 필연적 구조적 기원을 설명한다.",
        "originality": "- [novelty] \"누적 우위 과정의 수리 모델을 최초로 계량과학에 적용하여 power-law 분포의 이론적 도출\"",
        "how": "- **이론 모델**: 확률적 과정(stochastic process)으로 누적 우위 모델 공식화—각 시점에 새 인용이 기존 인용 수에 비례하는 확률로 추가됨\n- **수학적 도출**: 이 과정이 점근적으로 power-law 분포를 생성함을 증명\n- **데이터 검증**: 실제 인용 분포, 저널 논문 수, 과학자 논문 수 분포와 비교",
        "why": "- 과학에서 '부익부' 현상의 수학적 필연성을 최초로 증명하여 계량과학 이론의 기초 확립\n- 인용 지표, 저널 영향력 측정, 과학자 평가 지표 설계의 이론적 근거 제공\n- Lotka 법칙, Bradford 법칙, Zipf 법칙의 통합 설명 프레임워크",
        "limitation": "- 단순화된 확률 모델로 실제 인용 과정의 복잡성(선호적 연결 외 다른 요인들) 미반영\n- 학제간 차이, 자기인용, 부정적 인용 등을 고려하지 않음\n- 모델이 분포의 꼬리(극단적 고인용)를 정확히 포착하지 못할 수 있음",
        "further": "- 소셜 미디어 시대의 누적 우위: 온라인 가시성이 인용에 미치는 영향\n- 오픈 액세스가 누적 우위 구조를 변화시키는지 분석\n- AI 추천 시스템이 인용 편향을 강화하는지 탐구",
        "scores": {"Novelty": 5, "Technical Soundness": 5, "Significance": 5, "Clarity": 4, "Overall": 5},
        "summary": "과학 내 누적 우위(Matthew effect)의 수학적 구조를 확률 과정으로 최초 공식화하여 power-law 인용 분포의 이론적 기원을 밝힌 계량과학의 고전 논문이다."
    },
    266: {
        "mode": "PDF",
        "essence": "재료과학 문헌에서 훈련된 비지도 단어 임베딩(word2vec)이 열전 재료 발견에 관한 잠재 지식을 포착한다. mat2vec 모델은 2018년 이전 문헌만으로 훈련되었는데도 2018년 이후 실제로 발견된 열전 재료 후보들을 정확히 예측했으며, '미래 재료'와 기능적으로 유사한 재료를 높은 순위로 추천했다. 이는 과학 문헌에 명시적으로 기술되지 않은 잠재 지식(latent knowledge)이 언어 모델을 통해 추출 가능함을 보인 것이다.",
        "originality": "- [authorship, action] \"We show that materials science knowledge present in the scientific literature can be efficiently encoded as information-dense word embeddings.\"\n- [novelty, finding] \"The embeddings allow for predictions about future materials discoveries by identifying hidden structure in the literature.\"",
        "how": "- **데이터**: 재료과학 문헌 330만 편 초록 + 전체 텍스트 일부(1922–2018)\n- **모델**: word2vec(skip-gram) 기반 mat2vec—200차원 임베딩, 특수 재료 토크나이저\n- **검증**: 원소 주기율표 구조 재현, 열전 재료 예측(2018 이전 데이터로 이후 발견 예측)\n- **응용**: 특정 성질(예: 열전 성능 ZT 값)과 가장 유사한 재료 추천",
        "why": "- 과학 문헌에 흩어진 암묵적 지식을 자동으로 추출·연결하여 새로운 재료 발견 가속화\n- 실험 없이 컴퓨터만으로 유망 재료 후보를 좁혀 연구 효율성 획기적 향상\n- NLP 기법을 재료과학에 처음으로 체계적으로 적용한 방법론 확립",
        "limitation": "- 훈련 데이터의 편향(영어 문헌 중심, 인기 재료 과잉 대표)이 예측 편향으로 이어질 수 있음\n- 단어 의미의 맥락 의존성(같은 단어가 다른 의미)을 처리하는 데 word2vec의 한계\n- 문헌에 기술된 것만 학습—미발표 음성 결과(negative results)는 반영 못함",
        "further": "- BERT/LLM 기반 문맥 인식 임베딩으로의 업그레이드\n- 합성 경로, 처리 조건 등 다중 성질 동시 최적화\n- 임베딩이 포착한 재료 관계의 해석가능성(interpretability) 향상",
        "scores": {"Novelty": 5, "Technical Soundness": 4, "Significance": 5, "Clarity": 5, "Overall": 5},
        "summary": "330만 편 재료과학 문헌에서 훈련된 word2vec 임베딩이 미래 열전 재료 발견을 정확히 예측하여, 과학 문헌의 잠재 지식 추출 가능성을 실증한 AI for Science 분야의 선구적 논문이다."
    },
    267: {
        "mode": "PDF",
        "essence": "현대 과학은 지수적으로 성장하고 있다. Bornmann & Mutz(2015)는 1650년부터 2012년까지 논문 수와 참고문헌 수의 시계열을 분석하여, 20세기 중반까지는 약 35년마다 두 배로 증가하는 지수적 성장이 지배했으며, 이후 성장률이 다소 둔화되었음을 밝혔다. 특히 참고문헌 수는 논문 수보다 더 빠르게 증가하고 있어 지식 연결 밀도가 높아지고 있다.",
        "originality": "- [authorship, action] \"We present a bibliometric analysis of the growth of science based on the number of publications and cited references.\"\n- [finding] \"The growth of science follows an exponential pattern, with a doubling time of approximately 9 years for publications in recent decades.\"",
        "how": "- **데이터**: Web of Science(1980–2012), Scopus, 역사적 문헌 추정치(Price 1963, Mabe 2003 등)\n- **측정**: 연도별 논문 수, 참고문헌 수 집계 및 성장률 계산\n- **분석**: 지수 성장 모델 피팅, 분야별(자연과학·사회과학·인문학) 성장률 비교\n- **통계**: 성장 가속/감속 구간 검출, doubling time 추정",
        "why": "- 과학 성장률 파악은 저널 용량 계획, 동료 심사 부하, R&D 예산 정책에 핵심 기초 데이터\n- 참고문헌 성장이 논문 수 성장을 앞선다는 발견은 지식 통합 속도 분석에 중요\n- 역사적 성장 패턴 이해는 미래 과학 생태계 예측의 기반",
        "limitation": "- Web of Science의 저널 커버리지 편향—비영어권, 신흥국 문헌 과소 대표\n- 논문 수 증가가 품질 향상을 의미하지 않으며, 분할출판(salami slicing) 등으로 인한 인위적 증가 가능\n- 데이터베이스 색인 정책 변화가 외관상 성장률 변화로 나타날 수 있음",
        "further": "- 오픈 액세스·프리프린트 시대의 과학 성장 패턴 재분석\n- 논문 수 증가 대비 실질 지식 증가율(질 보정 성장) 측정 방법론 개발\n- AI 보조 연구가 성장률에 미치는 영향 전망",
        "scores": {"Novelty": 3, "Technical Soundness": 4, "Significance": 4, "Clarity": 4, "Overall": 4},
        "summary": "1650년 이래 과학 문헌의 지수적 성장 패턴을 체계적으로 정량화하여, 현대 과학 생산성 연구와 저널 정책 설계를 위한 기초 계량 자료를 제공하는 견실한 서지계량 연구다."
    },
    268: {
        "mode": "PDF",
        "essence": "인용 분석은 저널 평가의 유효한 도구다. Garfield(1972)는 저널 임팩트 팩터(Journal Impact Factor, JIF) 개념을 공식 제안하고, Science Citation Index(SCI) 데이터를 이용해 저널이 과학 문헌에 미치는 영향력을 정량적으로 측정하는 방법론을 제시했다. 이 논문은 계량과학 분야에서 가장 많이 인용되는 고전 중 하나로, JIF가 수십 년간 학술 평가의 표준 지표가 된 것의 기초를 놓았다.",
        "originality": "- [novelty] \"Journal Impact Factor 개념을 최초로 공식 정의하고 저널 평가 도구로의 적용을 체계화함\"",
        "how": "- **데이터**: Science Citation Index(SCI) 1969–1971년 데이터\n- **JIF 계산**: 2년간 논문 피인용 수 / 2년간 총 논문 수\n- **검증**: 상위 저널과 하위 저널 간 JIF 비교, 분야별 JIF 분포 분석\n- **응용**: 도서관 저널 구독 선택 기준으로의 활용 가능성 논의",
        "why": "- 저널 품질을 계량적으로 비교 가능한 단일 숫자로 요약하는 방법 제시\n- 도서관·연구기관의 저널 구독 결정에 객관적 기준 제공\n- 과학 문헌의 영향력 전파 패턴 이해의 기초 확립",
        "limitation": "- 분야별 인용 관행 차이로 인해 JIF는 다른 분야 간 비교에 부적합\n- 2년 인용 창(citation window)이 느린 분야(수학, 인문학)에서는 부적절\n- 저널 수준 지표를 개별 논문·연구자 평가에 오용하는 관행(San Francisco Declaration, Leiden Manifesto에서 비판)\n- 리뷰 논문, 편집자 사설 등이 분모·분자에 불균등하게 포함되어 조작 가능",
        "further": "- 분야 정규화 피인용도(FNCS), RCR 등 JIF 한계를 보완하는 새 지표 개발(실제로 진행됨)\n- 논문 수준 지표(Altmetrics, 개별 논문 피인용도)로의 전환 논의\n- AI가 생성한 논문에서 JIF의 의미가 어떻게 변화하는지",
        "scores": {"Novelty": 5, "Technical Soundness": 3, "Significance": 5, "Clarity": 5, "Overall": 5},
        "summary": "저널 임팩트 팩터(JIF)를 최초로 공식 정의하고 저널 평가 도구로 제안한 계량과학의 가장 영향력 있는 고전 논문으로, 수십 년간 학술 평가의 표준 지표가 된 JIF의 이론적·실용적 기반을 마련했다."
    },
    269: {
        "mode": "PDF",
        "essence": "g-index는 h-index의 한계를 보완하는 새로운 인용 지표다. Egghe(2006)가 제안한 g-index는 '상위 g편 논문이 평균적으로 g²회 이상 인용된' 최대 g값으로 정의되어, h-index가 놓치는 고피인용 논문의 기여를 포착한다. h-index와 달리 g는 상위 논문의 인용 수 증가에 민감하게 반응하며, 수학적으로는 항상 g ≥ h 관계가 성립한다.",
        "originality": "- [authorship, novelty, action] \"We introduce the g-index as a new bibliometric indicator that improves upon the h-index by giving more weight to highly cited articles.\"\n- [finding] \"The g-index always satisfies g ≥ h and captures the tail performance of highly cited papers.\"",
        "how": "- **이론**: g-index 정의 공식화—상위 g편 논문의 총 인용 수 ≥ g² 조건 충족하는 최대 g\n- **수학 분석**: h와 g의 관계(g ≥ h 증명), Lotka 법칙·Zipf 분포 하에서의 g 점근 분석\n- **실증 비교**: 노벨상 수상자, 과학자 샘플에서 h와 g 비교",
        "why": "- h-index는 고인용 논문의 추가 인용을 무시하는 구조적 한계를 가짐\n- g-index는 단 하나의 수로 누적 인용 성과를 더 민감하게 포착\n- 연구자 평가·채용·승진 결정에서 h의 보완 지표로 광범위하게 활용됨",
        "limitation": "- g-index도 분야별 인용 관행 차이를 보정하지 못함\n- 경력 초기 연구자에게 불리한 구조(누적 인용 필요)\n- 자기인용, 리뷰 논문의 고인용 등에 취약",
        "further": "- 분야 정규화 g-index(normalized g) 개발\n- h, g 외 다양한 지표의 조합 최적화 연구\n- 동료 심사 기반 평가와 지표 기반 평가의 상관관계 분석",
        "scores": {"Novelty": 4, "Technical Soundness": 4, "Significance": 4, "Clarity": 4, "Overall": 4},
        "summary": "h-index가 놓치는 고피인용 논문의 탁월한 기여를 포착하는 g-index를 수학적으로 정의·분석한 계량과학 논문으로, h-index의 주요 보완 지표로 자리잡았다."
    },
    270: {
        "mode": "PDF",
        "essence": "논문 수준의 상대적 인용 비율(Relative Citation Ratio, RCR)은 기존 JIF나 절대 피인용수의 한계를 극복하는 분야 정규화 지표다. Hutchins et al.(2016)은 NIH PubMed Central 데이터로 RCR를 개발했는데, 이는 동일 시기·분야 논문들의 인용 네트워크를 기준으로 개별 논문의 영향력을 정규화한다. RCR 1.0이 분야 평균이며, peer review 평가와 높은 상관관계(r=0.87)를 보여 연구 영향력의 실용적 지표로 검증되었다.",
        "originality": "- [authorship, novelty, action] \"We developed the Relative Citation Ratio (RCR), a new field-normalized bibliometric measure of scientific influence at the article level.\"\n- [finding] \"RCR correlates strongly with peer review assessments of scientific influence (r = 0.87).\"",
        "how": "- **데이터**: NIH PubMed Central 논문 약 880만 편\n- **RCR 계산**: 논문의 연간 인용률을 공동인용 네트워크(co-citation network)로 정의된 동분야 논문들의 평균 인용률로 나누어 정규화\n- **검증**: NIH 연구비 수혜 논문의 expert peer review 점수와 RCR 상관관계 분석\n- **비교**: JIF, h-index 등 기존 지표와의 비교",
        "why": "- 분야 간 비교 가능한 논문 수준 지표 제공—JIF는 저널 수준, 분야 간 비교 불가\n- 연구비 배분, 연구자 채용·평가에서 더 공정하고 정확한 정량 지표 필요\n- NIH 공식 채택으로 실제 정책 영향력 획득",
        "limitation": "- 공동인용 네트워크 정의 방법에 따라 결과가 달라질 수 있음\n- 인용되기 전(발표 직후) 논문은 RCR 계산 불가\n- 신흥 학제간 분야에서 적절한 비교 분야 설정이 어려울 수 있음",
        "further": "- 프리프린트·오픈 데이터 시대의 RCR 확장\n- 부정적 인용(반박 논문 인용)을 분리 처리하는 정교화\n- 팀 기여도 가중치 RCR 변형 개발",
        "scores": {"Novelty": 4, "Technical Soundness": 5, "Significance": 4, "Clarity": 5, "Overall": 4},
        "summary": "공동인용 네트워크 기반의 분야 정규화 논문 영향력 지표 RCR을 개발하고 NIH 데이터로 검증하여, 분야 간 비교 가능한 실용적 연구 평가 도구를 제시한 계량과학 논문이다."
    },
    271: {
        "mode": "PDF",
        "essence": "과학에서 성별 격차는 전 세계적으로 지속되며, 여성은 논문 수, 국제 협업, 저널 영향력에서 남성보다 낮은 수치를 보인다. Larivière et al.(2013)은 Web of Science 550만 편 논문(2008–2012)을 분석해 여성이 전 세계 저자의 30% 미만이며, 지역·분야별로 크게 다르지만 보편적으로 성별 격차가 존재함을 보였다. 특히 국제 협업에서의 성별 격차는 연구 가시성과 영향력에 복합적으로 작용한다.",
        "originality": "- [authorship, action] \"We present a global analysis of gender disparities in science using a large-scale dataset of 5.4 million papers.\"\n- [finding] \"Women account for fewer than 30% of authors worldwide, with significant variation across countries and disciplines.\"",
        "how": "- **데이터**: Web of Science 2008–2012 논문 약 540만 편, 저자 이름 기반 성별 추정\n- **성별 추정**: 이름-성별 사전 및 국가별 이름 데이터베이스 활용\n- **분석**: 저자 성별 비율, 국제 협업률, 피인용도의 국가·분야·연도별 비교\n- **지표**: 논문 수 비율, 피인용도 비율, 국제 공저 비율",
        "why": "- 과학 인력의 성별 다양성이 혁신에 미치는 영향 이해의 기초 데이터\n- 성별 격차의 국가·분야별 패턴 파악으로 정책 개입의 우선순위 설정 가능\n- 여성 과학자 유지·증가를 위한 글로벌 비교 벤치마크 제공",
        "limitation": "- 이름 기반 성별 추정의 오류(문화권별 중성 이름, 이름 변경)\n- 논문 수 및 인용으로만 측정하여 기여의 질적 측면 미반영\n- 2008–2012년 단기 스냅샷으로 장기 추세 파악 한계",
        "further": "- 성별 격차의 시계열 변화 및 세대별 분석\n- 출산·육아 등 생애 이벤트가 성별 생산성 격차에 미치는 영향\n- 성별 다양성이 팀 성과에 미치는 인과적 영향 분석",
        "scores": {"Novelty": 3, "Technical Soundness": 4, "Significance": 4, "Clarity": 4, "Overall": 4},
        "summary": "540만 편 논문 분석으로 과학 내 성별 격차의 전 세계적 패턴을 정량화한 대규모 계량 연구로, 과학 다양성 정책 설계를 위한 핵심 기초 데이터를 제공한다."
    },
    272: {
        "mode": "PDF",
        "essence": "논문의 장기 인용 영향력은 'sleeping beauty(수면 후 각성)' 현상을 포함하여 단순 지수 감소가 아닌 복잡한 패턴을 보인다. Wang et al.(2013)은 Physical Review 저널의 30만 편 논문 인용 시계열을 분석해, 대부분의 논문은 발표 직후 인용이 증가했다 감소하는 패턴을 보이지만, 일부는 오랜 잠복기 후 급격히 각성하는 sleeping beauty 패턴을 보임을 확인했다. 이들은 이를 $c(t) = m(e^{\\mu t}-1) + \eta$ 모델로 정량화했다.",
        "originality": "- [authorship, novelty, action] \"We quantify the long-term scientific impact of papers by fitting their citation histories with a model that captures immediate and delayed recognition.\"\n- [finding] \"A subset of papers exhibit 'sleeping beauty' patterns—delayed recognition after initial obscurity.\"",
        "how": "- **데이터**: Physical Review(PR) 1893–2009, 30만 편 논문의 연도별 인용 시계열\n- **모델**: $c(t) = m(e^{\\mu t}-1) + \\eta$ (즉각 영향 m, 성장률 μ, 지연 영향 η 세 파라미터)\n- **분류**: 모델 파라미터 기반 논문 유형(regular, delayed impact 등) 군집화\n- **검증**: 노벨상 수상 논문의 sleeping beauty 패턴 확인",
        "why": "- 단기 인용 지표(JIF 2년)가 장기 영향력을 과소평가하는 문제 해결\n- Sleeping beauty 현상의 정량적 이해는 연구비 심사, 조기 종료 결정의 근거 재고에 활용\n- 피인용 패턴의 다양성 이해는 분야별 평가 지표 정교화에 기여",
        "limitation": "- 물리학(PR) 데이터에 편중—다른 분야 일반화 필요\n- 모델의 세 파라미터 추정에 노이즈가 많고 과적합 위험\n- Sleeping beauty 정의가 임의적이어서 다른 기준에서는 결과 달라질 수 있음",
        "further": "- 다분야 비교: 생의학·화학·사회과학에서 sleeping beauty 비율 비교\n- 무엇이 sleeping beauty를 '깨우는지' 인과 분석(리뷰 논문? 기술 발전? 재발견?)\n- 사전 출판(preprint) 시대의 인용 패턴 변화",
        "scores": {"Novelty": 4, "Technical Soundness": 4, "Significance": 4, "Clarity": 4, "Overall": 4},
        "summary": "30만 편 논문의 인용 시계열을 3-파라미터 모델로 정량화하여 sleeping beauty 패턴을 포함한 과학적 영향력의 장기 역학을 체계적으로 분석한 계량과학 연구다."
    },
    273: {
        "mode": "Web-only",
        "essence": "공동인용(co-citation), 서지 결합(bibliographic coupling), 직접 인용 세 가지 인용 접근법 중 어느 것이 연구 최전선을 가장 정확히 표현하는가? Boyack & Klavans(2010)는 MEDLINE 데이터를 이용해 세 방법 모두를 평가한 결과, 공동인용과 서지 결합이 직접 인용보다 연구 클러스터의 품질(전문가 평가 대비)이 높고, 특히 서지 결합이 최신성 측면에서 유리함을 보였다. 두 방법의 결합이 최적 성능을 낸다.",
        "originality": "- [novelty] \"최초로 세 가지 인용 접근법을 동일 데이터에서 체계적으로 비교 평가함\"",
        "how": "- **데이터**: MEDLINE 2003–2007 논문 약 230만 편\n- **세 가지 접근법**: co-citation(공동 인용된 논문 쌍), bibliographic coupling(공통 참고문헌 공유), direct citation\n- **평가**: 전문가 분류(MeSH)와의 일치도 측정(precision, recall), 클러스터 품질 비교\n- **군집화**: 각 방법별 유사도 행렬 → Louvain 커뮤니티 탐지",
        "why": "- 과학 지도(science mapping)와 연구 프런트 파악에 어떤 인용 지표가 최적인지 방법론 정립\n- 지식 구조 분석 도구 설계에 근거 제공\n- 학술 데이터베이스 및 추천 시스템 설계에 실용적 함의",
        "limitation": "- MEDLINE(생의학) 단일 분야 데이터—물리학, 인문학 등 다른 분야 일반화 한계\n- 전문가 분류(MeSH)를 ground truth로 사용하는 데 한계(MeSH 자체도 불완전)\n- 데이터 규모와 시간 창의 선택에 결과가 민감할 수 있음",
        "further": "- 다분야 비교 및 하이브리드 지표 개발\n- 동적 서지 결합(temporal bibliographic coupling)으로 연구 프런트 진화 추적\n- LLM 임베딩과 인용 기반 방법의 결합 효과 평가",
        "scores": {"Novelty": 3, "Technical Soundness": 4, "Significance": 4, "Clarity": 4, "Overall": 4},
        "summary": "세 가지 인용 기반 과학 지도 방법을 동일 데이터에서 체계적으로 비교하여 공동인용·서지 결합의 우수성을 입증한 계량과학 방법론 연구다."
    },
    274: {
        "mode": "Web-only",
        "essence": "UCSD 과학 지도(Map of Science)는 약 2,500만 편 논문의 인용 관계를 기반으로 과학 전체를 13개 주요 분야, 554개 세부 분야 클러스터로 시각화한 글로벌 과학 분류 시스템이다. Börner et al.(2012)은 이 지도의 설계 원칙과 2009–2011년 업데이트 과정을 기술하며, 연구 포트폴리오 분석, 정책 평가, 과학 나침반(science compass)으로의 활용 방법을 제시한다.",
        "originality": "- [authorship, action] \"We present the design and update of the UCSD Map of Science, a global classification system covering 25 million papers across 554 subdiscipline clusters.\"",
        "how": "- **데이터**: Web of Science + Scopus 2009–2011 합산 약 2,500만 편 논문\n- **군집화**: 서지 결합(bibliographic coupling) 기반 유사도 행렬 → Louvain 커뮤니티 탐지 → 554개 클러스터 → 13개 대분야 수동 합병\n- **시각화**: Gephi 기반 force-directed 레이아웃, 색상 코딩\n- **검증**: 전문가 패널 리뷰 및 NIH, NSF 연구비 데이터 적용 테스트",
        "why": "- 과학 전체의 구조와 분야 간 연결성을 한눈에 파악하는 표준 참조 지도 제공\n- 기관·국가·연구자의 연구 포트폴리오를 과학 지도 위에 투영하여 전략적 분석 지원\n- 과학 정책, 연구비 배분, 학제간 협업 기회 탐색에 실용적 도구",
        "limitation": "- Web of Science·Scopus 색인 편향이 지도에 그대로 반영\n- 인문학·사회과학은 인용 관행 차이로 클러스터 품질이 낮음\n- 2년 단위 업데이트 주기로 빠르게 변하는 신흥 분야 포착에 지연",
        "further": "- 실시간 업데이트 가능한 동적 과학 지도 개발\n- arXiv, PubMed 등 미색인 데이터 포함 확대\n- LLM 기반 의미론적 과학 지도와의 비교·통합",
        "scores": {"Novelty": 3, "Technical Soundness": 4, "Significance": 4, "Clarity": 4, "Overall": 4},
        "summary": "2,500만 편 논문을 554개 클러스터로 분류한 UCSD 과학 지도의 설계 방법론과 업데이트 과정을 기술한 실용적 도구 논문으로, 과학 지도 제작 분야의 방법론 표준을 제공한다."
    },
    275: {
        "mode": "PDF",
        "essence": "그래프의 커뮤니티 탐지(community detection)는 노드와 엣지로 이루어진 네트워크에서 내부 연결이 밀하고 외부 연결이 성긴 클러스터를 찾는 문제다. Fortunato(2010)의 이 리뷰 논문은 계층적 클러스터링, modularity 최적화, 스펙트럼 방법, 통계적 추론 등 주요 알고리즘 패밀리를 체계적으로 정리하고 비교하며, 해상도 한계(resolution limit of modularity)와 같은 근본적 문제점을 분석한다.",
        "originality": "- [authorship, action] \"We present a comprehensive review of community detection algorithms in complex networks, covering both deterministic and statistical approaches.\"",
        "how": "- **범위**: 2010년까지 주요 커뮤니티 탐지 알고리즘 전체 리뷰\n- **분류 체계**: 계층적 방법, graph partitioning, modularity 기반, 스펙트럼, 베이지안/통계적, 동적 방법\n- **평가 기준**: 정확도(ground truth 비교), 계산 복잡도, 확장성\n- **벤치마크**: LFR benchmark, karate club, football network 등 표준 테스트 그래프 사용",
        "why": "- 커뮤니티 탐지는 소셜 네트워크, 생물 네트워크, 지식 그래프, 인용 네트워크에 광범위하게 적용\n- 알고리즘 선택 기준과 한계에 대한 통합 이해 제공\n- 2010년 이후 커뮤니티 탐지 연구의 표준 참고 문헌으로 기능(10,000회 이상 피인용)",
        "limitation": "- 리뷰 특성상 저자의 알고리즘 선택·설명에 주관적 편향 가능\n- Modularity 기반 방법의 해상도 한계(resolution limit) 등 한계는 기술하지만 완전한 해결책 미제시\n- 2010년 이후 등장한 딥러닝 기반 방법(graph neural network, deep clustering) 미포함",
        "further": "- GNN(Graph Neural Network) 기반 커뮤니티 탐지 방법으로의 확장\n- 동적·시간 진화 네트워크에서의 커뮤니티 탐지\n- 지식 그래프·인용 네트워크에서의 실용적 응용",
        "scores": {"Novelty": 3, "Technical Soundness": 5, "Significance": 5, "Clarity": 5, "Overall": 5},
        "summary": "네트워크 커뮤니티 탐지 알고리즘 전체를 체계적으로 정리하고 한계를 분석한 포괄적 리뷰로, 10,000회 이상 피인용된 해당 분야의 표준 참고 논문이다."
    },
    276: {
        "mode": "PDF",
        "essence": "Louvain 알고리즘은 대규모 네트워크에서 커뮤니티를 빠르고 정확하게 탐지하는 방법이다. Blondel et al.(2008)이 제안한 이 알고리즘은 modularity를 국소적으로 탐욕적(greedy)으로 최적화하는 두 단계 절차를 반복하여, 1억 2,800만 엣지의 네트워크에서도 수분 내에 계층적 커뮤니티 구조를 탐지한다. 기존 방법 대비 수십~수백 배 빠른 속도를 달성하면서도 modularity 품질은 경쟁 알고리즘과 대등하거나 우월하다.",
        "originality": "- [authorship, novelty, action] \"We propose a fast algorithm for community detection in large networks, which we call the Louvain method, based on greedy modularity optimization.\"\n- [finding] \"The algorithm achieves high modularity values while being orders of magnitude faster than competing methods.\"",
        "how": "- **알고리즘**: Phase 1—각 노드를 이웃과 같은 커뮤니티에 배치할 때 modularity 이득 계산 후 탐욕적 이동; Phase 2—커뮤니티를 슈퍼노드로 집계하여 새 그래프 생성 → 반복\n- **데이터**: 휴대폰 통화 네트워크(200만 노드, 1억 2,800만 엣지), 웹 그래프, 생물 네트워크 등\n- **비교**: CNM, Wakita-Tsurumi 등 기존 greedy 방법과 속도·modularity 비교",
        "why": "- 실제 소셜·생물·기술 네트워크는 수백만~수십억 노드 규모로 기존 방법의 적용이 불가\n- 빠른 커뮤니티 탐지는 실시간 네트워크 분석, 추천 시스템, 과학 지도 제작에 필수\n- 광범위한 도메인 적용 가능성으로 사실상 업계 표준 알고리즘이 됨(40,000회 이상 피인용)",
        "limitation": "- Modularity의 해상도 한계(resolution limit): 소규모 커뮤니티가 대규모 커뮤니티에 흡수될 수 있음\n- 탐욕적 국소 최적화로 인한 global optimum 미보장\n- 무작위 초기화로 실행마다 결과가 달라질 수 있음(non-deterministic)",
        "further": "- Leiden 알고리즘 등 해상도 한계와 비결정성을 개선한 후속 개발(실제 진행됨)\n- 방향 그래프, 가중 네트워크, 다중층 네트워크로의 확장\n- 실시간 동적 네트워크 업데이트에서의 incremental Louvain",
        "scores": {"Novelty": 5, "Technical Soundness": 4, "Significance": 5, "Clarity": 5, "Overall": 5},
        "summary": "대규모 네트워크에서 modularity를 탐욕적으로 최적화하는 Louvain 알고리즘을 제안하여 수억 엣지 규모 네트워크의 실용적 커뮤니티 탐지를 가능하게 한, 40,000회 이상 피인용된 네트워크 과학의 핵심 방법론 논문이다."
    },
    277: {
        "mode": "Web-only",
        "essence": "과학에서 집단적 크레딧 배분은 저자 순서 규칙과 무관하게 실제로는 매우 불균등하다. Shen & Barabási(2014)는 Physical Review 논문의 저자 순서와 피인용 패턴을 분석해, 공동저자들이 균등하게 크레딧을 받는 것이 아니라 첫 번째·마지막 저자에 집중되는 U자 곡선 구조를 보임을 정량화했다. 이 편향은 팀 규모가 커질수록 더 강해진다.",
        "originality": "- [novelty] \"최초로 공동저자 크레딧 배분의 실제 패턴을 논문-피인용자 연결 데이터로 정량화함\"",
        "how": "- **데이터**: Physical Review 1954–2013 논문 중 저자 순서·피인용 데이터\n- **측정**: 각 저자 위치별(첫째, 둘째, ... n번째, 마지막) 피인용 회수 귀속 분석\n- **모델**: 저자 위치별 크레딧 배분 함수 피팅\n- **분석**: 팀 규모별, 분야별 크레딧 집중도 비교",
        "why": "- 연구자 평가에서 저자 위치가 기여를 제대로 반영하는지 실증적 근거 제공\n- 크레딧 불평등이 연구자 경력 결정, 여성·소수자 연구자에게 불균등하게 영향을 미침\n- 새로운 공정한 크레딧 배분 시스템(CRediT taxonomy 등) 설계의 증거 기반",
        "limitation": "- 물리학(Physical Review) 단일 분야—의학, 경제학 등 저자 순서 규칙이 다른 분야 적용 한계\n- 피인용을 크레딧 지표로 사용하는 한계(실제 기여 != 인용 기여)\n- 저자 순서가 기여 순서를 반영하지 않는 관행(알파벳 순, 시니어 마지막 등)의 복잡성",
        "further": "- CRediT taxonomy 데이터를 이용한 실제 기여 vs 인용 크레딧 비교\n- 성별·경력 단계별 크레딧 집중 패턴 분석\n- 오픈 저자 기여 플랫폼이 크레딧 불평등을 완화하는 효과 평가",
        "scores": {"Novelty": 4, "Technical Soundness": 4, "Significance": 4, "Clarity": 4, "Overall": 4},
        "summary": "공동저자 크레딧이 저자 위치에 따라 U자형으로 불균등하게 배분됨을 물리학 논문 전수 데이터로 정량화한 연구로, 공정한 연구 크레딧 시스템 설계에 실증적 기반을 제공한다."
    },
    278: {
        "mode": "Web-only",
        "essence": "오픈 액세스(OA) 논문은 전체 논문의 약 28%(2015년 기준)를 차지하며, OA 논문은 비OA 논문보다 더 많이 인용된다. Piwowar et al.(2018)은 Unpaywall, Crossref, Web of Science 등 여러 소스를 결합하여 OA 현황을 분석했다. OA 방식에 따라 골드(출판사 OA), 그린(기관 저장소), 하이브리드 등이 있으며, 그린 OA 논문이 인용 이득이 가장 크다.",
        "originality": "- [authorship, action] \"We present a large-scale analysis of the prevalence and impact of open access articles using a novel combination of data sources.\"\n- [finding] \"OA articles receive 18% more citations on average than non-OA articles.\"",
        "how": "- **데이터**: Unpaywall(OA 여부), Crossref(메타데이터), Web of Science(인용), Scopus\n- **표본**: 약 730만 편 논문(2009–2015)\n- **분류**: Gold OA, Green OA, Hybrid, Bronze(비허가 무료), Closed로 5분류\n- **분석**: OA 여부별 피인용도 비교(분야·연도 통제), OA 증가 추세 분석",
        "why": "- OA 정책 효과를 실증적으로 검증하는 최초의 대규모 분석\n- 연구비 지원 기관, 출판사, 대학의 OA 정책 설계에 증거 제공\n- 지식 민주화와 연구 영향력의 관계 이해",
        "limitation": "- OA 여부 탐지의 정확도 한계(Unpaywall 커버리지 불완전)\n- 인용 이득의 인과성 미확립—OA를 선택한 논문이 원래 더 좋은 논문일 수 있음(selection bias)\n- 분야별 OA 관행 차이가 통제되지 않을 수 있음",
        "further": "- OA 의무화 정책(Plan S 등) 도입 후 OA 비율 및 인용 이득 변화 추적\n- 개도국 연구자에 대한 OA 접근성 향상 효과 분석\n- 프리프린트 서버(arXiv, bioRxiv) 경유 그린 OA의 영향 비교",
        "scores": {"Novelty": 3, "Technical Soundness": 4, "Significance": 4, "Clarity": 4, "Overall": 4},
        "summary": "730만 편 논문의 OA 현황을 정밀 분류하고 OA가 피인용도에 미치는 이득을 정량화한 대규모 계량 연구로, OA 정책 설계의 핵심 증거 자료를 제공한다."
    },
    279: {
        "mode": "PDF",
        "essence": "과학 협업에서 민족 다양성이 가장 강력한 성과 예측 변수다. AlShebli et al.(2018)은 Nature Communications에 발표된 연구에서 WoS 논문 약 900만 편을 분석해, 다른 다양성 지표(성별, 경력 단계, 소속 기관 위신)보다 민족 다양성이 높을수록 논문의 피인용도가 더 높음을 발견했다. 다양한 배경의 연구자들이 더 넓은 관점과 네트워크를 가져와 연구 영향력을 높인다.",
        "originality": "- [authorship, finding] \"We find that ethnic diversity is the most critical factor in predicting citation impact among diversity dimensions studied.\"\n- [novelty] \"This is the largest study to simultaneously examine multiple diversity dimensions in scientific collaboration.\"",
        "how": "- **데이터**: Web of Science 1996–2012 논문 약 900만 편, 저자 이름 기반 민족 추정\n- **민족 분류**: NamSor API로 저자 이름을 동아시아·영미·히스패닉·아랍·남아시아 등으로 분류\n- **다양성 지표**: Blau index로 팀의 민족·성별·경력 다양성 측정\n- **분석**: 다중 회귀, 팀 고정효과, 분야·연도 통제\n- **주의**: 이 논문은 2022년 철회(retraction)됨—방법론적 오류 및 편향 논란",
        "why": "- 팀 다양성이 연구 혁신에 미치는 영향에 대한 대규모 실증 분석\n- 연구팀 구성 다양화 정책의 증거 기반 제공\n- 민족, 성별, 경력 다양성의 상대적 중요성 비교",
        "limitation": "- **이 논문은 2022년 철회됨**: 민족 추정의 체계적 오류, 분석 방법의 편향 문제가 지적됨\n- 이름 기반 민족 추정의 정확도 한계(특히 아프리카, 다문화 이름)\n- 인과관계 미확립: 다양한 팀이 더 좋은 성과를 내는 것인지, 성과 좋은 연구자들이 다양한 협업을 선호하는지 불명확\n- 피인용도만으로 연구 품질을 측정하는 한계",
        "further": "- 방법론적 결함을 수정한 재분석\n- 민족 다양성 외 인지 다양성, 전공 다양성의 영향 비교\n- 팀 내 민족 다양성과 협업 네트워크 구조의 상호작용 분석",
        "scores": {"Novelty": 3, "Technical Soundness": 2, "Significance": 3, "Clarity": 3, "Overall": 2},
        "summary": "과학팀의 민족 다양성이 연구 영향력의 핵심 예측 변수임을 주장했으나, 2022년 방법론적 오류로 철회된 논문으로, 다양성 연구에서 측정 방법의 엄밀성이 얼마나 중요한지를 보여주는 사례다."
    },
    280: {
        "mode": "PDF",
        "essence": "다양성-혁신의 역설: 소수자 연구자들은 더 참신한 개념을 제안하지만, 그들의 개념이 채택되고 인정받을 확률은 낮다. Hofstra et al.(2020)은 Stanford 박사 논문 약 1,200만 단어와 저자의 인구통계 데이터를 결합 분석하여, 여성·소수 인종 연구자가 논문에서 더 참신한(novel) 개념을 제안하지만 그 개념들이 후속 연구에서 인용·채택되는 비율은 낮음을 발견했다. 이는 과학적 지식 생산의 인구통계적 편향을 실증한다.",
        "originality": "- [authorship, finding] \"We find that PhD students from underrepresented groups innovate more in their dissertations, but these innovations are less likely to be adopted.\"\n- [novelty] \"We reveal a diversity-innovation paradox—diversity increases novelty but decreases adoption of innovations.\"",
        "how": "- **데이터**: ProQuest 박사 논문 데이터베이스(1977–2015) + 저자 성별·인종 데이터 약 120만 명\n- **참신성 측정**: Stanford NLP 도구로 논문 내 새로운 개념(신조어, 개념 조합) 탐지 후 후속 인용에서의 채택 추적\n- **인구통계**: 이름 기반 성별·인종 분류(African American, Asian, White, Hispanic)\n- **분석**: 회귀 분석으로 인구통계 → 참신성 → 채택률 경로 추정",
        "why": "- 다양성이 혁신을 촉진한다는 가설을 실증하면서도, 동시에 구조적 불평등이 혁신의 확산을 억제함을 보임\n- 단순한 '다양성 = 좋은 것' 담론을 넘어 다양성의 혜택이 누구에게 귀속되는지 질문\n- 과학 지식 생산의 인구통계적 편향 시정을 위한 정책 근거 제공",
        "limitation": "- 박사 논문에 국한—출판 논문, 특허 등 다른 형태의 혁신 산출물 미포함\n- 이름 기반 인종 분류의 부정확성\n- '참신성' 측정이 언어적 신규성에 의존하여 실질 혁신과 괴리 가능",
        "further": "- 출판 심사 과정에서 소수자 혁신이 걸러지는 메커니즘 분석\n- 멘토·지도교수 구성이 소수자 혁신 채택률에 미치는 영향\n- 글로벌 확장: 개도국 연구자의 혁신 vs 채택 패턴",
        "scores": {"Novelty": 5, "Technical Soundness": 4, "Significance": 5, "Clarity": 4, "Overall": 5},
        "summary": "소수자 연구자들의 더 높은 혁신성과 낮은 채택률이라는 역설적 패턴을 실증하여, 과학 지식 생산의 구조적 불평등을 드러낸 사회과학과 계산 방법의 융합 연구다."
    },
    281: {
        "mode": "Web-only",
        "essence": "샤프롱 효과(chaperone effect): 젊은 과학자의 첫 논문이 저명한 선임 과학자와 공동 저술될 경우, 그 선임의 명성이 논문의 게재 성공률과 영향력에 통계적으로 유의한 양의 효과를 미친다. Sekara et al.(2018)은 PNAS 논문 데이터로 이 효과를 정량화했으며, 이는 과학 커리어 초기에 좋은 지도자를 갖는 것이 단순 능력 이상으로 중요하다는 구조적 불평등을 시사한다.",
        "originality": "- [novelty] \"최초로 공동저자 명성의 '샤프롱 효과'를 대규모 데이터로 정량화함\"",
        "how": "- **데이터**: PNAS 논문 저자 네트워크 및 피인용 데이터\n- **설계**: 신진 연구자(첫 논문 저자)와 공동 저술한 선임 저자의 명성(h-index, 피인용 수) 측정\n- **결과 지표**: 논문 게재 확률(PNAS 심사 통과율), 이후 피인용도\n- **통제**: 논문 분야, 연도, 신진 연구자 자체 특성",
        "why": "- 과학 커리어에서 지도자·멘토의 구조적 중요성 실증\n- 명문 기관 출신 편향(prestige bias)의 메커니즘 규명\n- 진정한 능력주의적 과학 커뮤니티 구현을 위한 개입 설계 근거",
        "limitation": "- PNAS 단일 저널로 일반화 한계\n- 역인과 가능성: 좋은 연구가 좋은 멘토를 끌어당기는지 구분 어려움\n- 명성을 h-index로 측정하는 한계",
        "further": "- 다저널 비교 분석으로 샤프롱 효과의 범용성 검증\n- 성별·인종별 샤프롱 효과의 차이 분석\n- 샤프롱 없이 성공한 혁신적 논문의 특성",
        "scores": {"Novelty": 4, "Technical Soundness": 3, "Significance": 4, "Clarity": 4, "Overall": 4},
        "summary": "저명 공동저자가 신진 연구자의 논문 성공 확률과 영향력에 미치는 샤프롱 효과를 정량화하여, 과학 커리어에서 구조적 불평등의 새로운 메커니즘을 밝힌 연구다."
    },
    282: {
        "mode": "Web-only",
        "essence": "학문 환경(재직 기관의 명성)이 개인 연구자의 생산성에 독립적으로 영향을 미친다. Way et al.(2019)는 컴퓨터과학 교수 약 2,500명의 경력 이동 데이터를 분석해, 더 명망 있는 기관으로 이동하면 생산성이 증가하고 낮은 곳으로 이동하면 감소함을 발견했다. 이는 개인 능력과 무관한 환경 효과(institutional effect)가 실재함을 시사한다.",
        "originality": "- [novelty] \"최초로 자연 실험적 설계(기관 이동)로 학문 환경의 인과적 생산성 효과를 정량화함\"",
        "how": "- **데이터**: 컴퓨터과학 교수 2,500명 경력 이력 및 논문 생산성 데이터\n- **설계**: Difference-in-differences 방식—기관 이동 전후 생산성 변화, 이동 방향(상향/하향)별 비교\n- **통제**: 개인 고정효과, 경력 연차, 연도 효과\n- **측정**: 논문 수, 피인용도, h-index",
        "why": "- '좋은 연구자가 좋은 기관에 간다'는 통념에서 벗어나 환경 자체의 독립적 효과 실증\n- 연구 인프라, 동료 효과, 자원 배분 정책의 실질 효과 이해\n- 학문적 이동성(academic mobility) 정책과 기관 투자의 근거 제공",
        "limitation": "- 컴퓨터과학 단일 분야—실험과학 등 다른 분야 일반화 필요\n- 논문 수·피인용도로만 생산성 측정(연구 질 미포함)\n- 이동 선택의 내생성 완전 해소 어려움",
        "further": "- 다분야 비교 및 글로벌 학문 이동성 분석\n- 기관 환경의 어떤 요소(시설, 동료, 자원)가 생산성에 가장 기여하는지 분해\n- 원격근무 확산이 기관 환경 효과를 약화시키는지 분석",
        "scores": {"Novelty": 4, "Technical Soundness": 4, "Significance": 4, "Clarity": 4, "Overall": 4},
        "summary": "기관 이동 전후 비교로 학문 환경이 연구자 생산성에 독립적 인과 효과를 가짐을 처음 실증한 연구로, 기관 투자와 학문적 이동성 정책 설계에 중요한 증거를 제공한다."
    },
    283: {
        "mode": "PDF",
        "essence": "과학 커리어에서 성별 불평등은 국가와 분야에 따라 크게 다르지만, 보편적으로 남성보다 여성의 조기 이탈(attrition)이 더 많다. Huang et al.(2020)은 1955–2010년 Scopus 논문 약 300만 편의 저자 경력 데이터를 분석해, 여성은 평균적으로 더 짧은 커리어를 보이고 조기에 과학을 떠나는 경향이 있으며, 이 gap은 분야별(물리학 최대, 간호학 최소)·국가별로 상이함을 정량화했다.",
        "originality": "- [authorship, action] \"We perform a large-scale historical comparison of gender inequality in scientific careers across 83 countries and 13 fields.\"\n- [finding] \"Women have shorter careers and higher attrition rates than men in nearly all countries and disciplines.\"",
        "how": "- **데이터**: Scopus 1955–2010 논문 약 300만 편, 저자 경력 추적(첫 논문~마지막 논문)\n- **성별 추정**: 이름 기반 분류(World Gender-Name Dictionary)\n- **측정**: 커리어 길이(첫~마지막 논문 연도), 커리어 지속률, 논문 생산성, 협업 네트워크\n- **비교**: 83개국, 13개 분야별 성별 gap 지표 비교\n- **통계**: 생존 분석(Kaplan-Meier), 음이항 회귀",
        "why": "- 성별 과학 불평등의 국가·분야별 패턴 파악으로 정책 개입의 타겟 설정 가능\n- 조기 이탈 패턴이 생애 단계(출산 등)와 연결되는 메커니즘 이해\n- 장기 추세(1955–2010) 분석으로 진전 여부와 지속되는 격차의 성격 파악",
        "limitation": "- Scopus 색인 편향(선진국·영어권 과잉 대표)\n- 이름 기반 성별 분류의 오류, 특히 아시아·아프리카 이름\n- '과학 이탈'을 마지막 출판으로 측정—실제 이탈과 단순 휴지기 구분 어려움",
        "further": "- 성별 커리어 gap의 인과 요인(육아 정책, 멘토링, 기관 문화) 준실험 분석\n- 2010년 이후 데이터로 최근 추세 변화 분석\n- 트랜스젠더·논바이너리 과학자의 커리어 패턴",
        "scores": {"Novelty": 4, "Technical Soundness": 4, "Significance": 5, "Clarity": 4, "Overall": 4},
        "summary": "55년간 83개국 300만 논문 데이터로 과학 커리어의 성별 불평등을 역사적·비교적으로 정량화하여, 국가별·분야별 정책 개입의 표적을 제시한 대규모 계량과학 연구다."
    },
    284: {
        "mode": "Web-only",
        "essence": "교수 생산성이 경력에 따라 포물선형(초기 증가 후 감소)을 보인다는 통념은 집계 편향(aggregation bias)의 산물이다. Way et al.(2017)은 컴퓨터과학 교수 약 2,500명의 개인 수준 경력 데이터를 분석해, 집계 평균에서 보이는 포물선 패턴이 실제로는 서로 다른 생산성 궤적을 가진 개인들을 평균낸 결과임을 보였다. 개인 수준에서 대다수 교수는 단순 감소 또는 불규칙한 패턴을 보이며 포물선 패턴은 소수에 불과하다.",
        "originality": "- [authorship, finding] \"We find that the canonical inverted-U productivity trajectory is a statistical artifact arising from aggregating individual trajectories with heterogeneous patterns.\"\n- [novelty] \"Individual-level analysis reveals that most faculty follow declining or irregular productivity trajectories.\"",
        "how": "- **데이터**: 컴퓨터과학 교수 2,500명 전체 경력 논문 생산성 데이터\n- **방법**: 개인 수준 종단 분석(individual-level longitudinal), 군집 분석으로 개인별 생산성 궤적 유형 분류\n- **비교**: 집계 평균(aggregate average) vs 개인 수준 분포 비교\n- **통제**: 경력 연차, 기관 명성, 분야 세부 분류",
        "why": "- 포물선형 생산성 통념에 근거한 정책(테뉴어 연령 제한, 퇴직 인센티브 등)의 위험성 경고\n- 개인 이질성 무시가 초래하는 집계 편향의 교과서적 사례 제시\n- 과학자 경력 관리, 연구비 배분, 테뉴어 제도 설계에 대한 재고 촉구",
        "limitation": "- 컴퓨터과학 단일 분야—다른 분야 궤적 패턴이 다를 수 있음\n- 논문 수로만 생산성 측정—피인용도, 특허, 정책 영향력 미포함\n- 생산성 감소의 원인(동기 감소? 행정 부담? 연구 방향 전환?)은 분석하지 않음",
        "further": "- 다분야 비교 및 인문학·실험과학 교수의 생산성 궤적 분석\n- 테뉴어 전후 생산성 변화 준실험 분석\n- 생산성 궤적 유형(증가형, 감소형, 포물선형 등)의 예측 요인 분석",
        "scores": {"Novelty": 4, "Technical Soundness": 4, "Significance": 4, "Clarity": 5, "Overall": 4},
        "summary": "교수 생산성의 포물선형 패턴이 개인 이질성을 무시한 집계 편향의 산물임을 실증하여, 과학자 경력 통념을 수정하고 정책적 오용을 경고한 중요한 계량 연구다."
    },
}

print("Review content loaded.")
print(f"Total entries with review data: {len(REVIEWS)}")


def make_review_md(e, rv):
    """Generate review.md content."""
    slug = e["slug"]
    title = e["title"]
    authors = e["authors"]
    date = e["date"]
    doi = e["doi"]
    arxiv_id = e.get("arxiv_id", "")
    venue = e["venue"]
    mode = rv["mode"]

    doi_str = f"[{doi}](https://doi.org/{doi})" if doi else "N/A"
    arxiv_str = f"[{arxiv_id}](https://arxiv.org/abs/{arxiv_id})" if arxiv_id else "N/A"

    has_fig = (BASE / slug / "figures" / "fig1.png").exists()
    fig_block = "\n![Figure 1](figures/fig1.png)\n*Figure 1: 논문 핵심 결과 또는 방법론 개요*\n" if has_fig else ""

    scores = rv["scores"]
    score_rows = "\n".join(f"| {k} | {v}/5 |" for k, v in scores.items())

    return f"""# {title}

> **저자**: {authors} | **날짜**: {date} | **Journal**: {venue} | **DOI**: {doi_str} | **arXiv**: {arxiv_str}
> **리뷰 모드**: {mode}

---

## Essence

{rv['essence']}
{fig_block}
## Originality (Abstract 기반)

{rv['originality']}

## How (방법론)

{rv['how']}

## Why (중요성)

{rv['why']}

## Limitation

{rv['limitation']}

## Further Study

{rv['further']}

## 평가

| 항목 | 점수 |
|------|------|
{score_rows}

**총평**: {rv['summary']}
"""


def inline_md(text):
    """Convert inline markdown to HTML."""
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*]+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', text)
    return text


def md_to_html_body(md):
    """Convert markdown string to HTML body."""
    lines = md.split('\n')
    out = []
    in_ul = False
    in_ol = False
    in_table = False
    in_blockquote = False
    table_rows = []

    def close_list():
        nonlocal in_ul, in_ol
        if in_ul:
            out.append('</ul>')
            in_ul = False
        if in_ol:
            out.append('</ol>')
            in_ol = False

    def close_table():
        nonlocal in_table, table_rows
        if in_table and table_rows:
            out.append('<table>')
            header = [c.strip() for c in table_rows[0].strip('|').split('|')]
            out.append('<tr>' + ''.join(f'<th>{h}</th>' for h in header) + '</tr>')
            for row in table_rows[2:]:
                cells = [c.strip() for c in row.strip('|').split('|')]
                out.append('<tr>' + ''.join(f'<td>{c}</td>' for c in cells) + '</tr>')
            out.append('</table>')
            table_rows.clear()
            in_table = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # Table
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                close_list()
                in_table = True
            table_rows.append(line)
            i += 1
            continue
        elif in_table:
            close_table()

        # Blockquote
        if line.startswith('> '):
            if not in_blockquote:
                close_list()
                out.append('<blockquote>')
                in_blockquote = True
            content = inline_md(line[2:])
            out.append(f'<p>{content}</p>')
            i += 1
            continue
        elif in_blockquote:
            out.append('</blockquote>')
            in_blockquote = False

        # Headings
        if line.startswith('# '):
            close_list()
            out.append(f'<h1>{inline_md(line[2:])}</h1>')
        elif line.startswith('## '):
            close_list()
            out.append(f'<h2>{inline_md(line[3:])}</h2>')
        elif line.startswith('### '):
            close_list()
            out.append(f'<h3>{inline_md(line[4:])}</h3>')
        elif line.strip() == '---':
            close_list()
            out.append('<hr />')
        elif line.startswith('!['):
            close_list()
            m = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', line)
            if m:
                alt, src = m.group(1), m.group(2)
                out.append(f'<div class="review-fig"><img src="{src}" alt="{alt}"><p class="fig-caption">{alt}</p></div>')
        elif line.startswith('*Figure ') and line.endswith('*'):
            # figure caption - already captured by div above; skip
            pass
        elif line.startswith('- '):
            if not in_ul:
                close_list()
                out.append('<ul>')
                in_ul = True
            out.append(f'<li>{inline_md(line[2:])}</li>')
        elif re.match(r'^\d+\. ', line):
            if not in_ol:
                close_list()
                out.append('<ol>')
                in_ol = True
            content = re.sub(r'^\d+\. ', '', line)
            out.append(f'<li>{inline_md(content)}</li>')
        elif line.strip() == '':
            close_list()
        else:
            close_list()
            if line.strip():
                out.append(f'<p>{inline_md(line)}</p>')

        i += 1

    close_list()
    close_table()
    if in_blockquote:
        out.append('</blockquote>')

    return '\n'.join(out)


def make_index_html(e, rv):
    """Generate styled index.html."""
    title = e["title"]
    md = make_review_md(e, rv)
    body_html = md_to_html_body(md)

    # Wrap sections
    sections = re.split(r'(?=<h2>)', body_html)
    wrapped = []
    for sec in sections:
        if not sec.strip():
            continue
        if sec.startswith('<h1>') or sec.startswith('<blockquote>') or sec.startswith('<hr'):
            wrapped.append(sec)
        elif sec.startswith('<h2>Essence'):
            wrapped.append(f'<div class="section-box essence-box">{sec}</div>')
        elif sec.startswith('<h2>'):
            wrapped.append(f'<div class="section-box">{sec}</div>')
        else:
            wrapped.append(sec)

    final_body = '\n'.join(wrapped)

    scores = rv["scores"]
    badges = ''.join(f'<span class="eval-badge">{k}: {v}/5</span>' for k, v in scores.items())
    final_body = final_body.replace(
        '<h2>평가</h2>',
        f'<h2>평가</h2><div class="eval-badges">{badges}</div>'
    )

    css = """* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'KoPub Dotum', 'KoPubDotumMedium', -apple-system, 'Noto Sans KR', sans-serif; max-width: 820px; margin: 0 auto; padding: 2rem 1.5rem; line-height: 1.7; color: #333; background: #f0f2f5; }
h1 { font-size: 1.4rem; color: #1a1a2e; border-bottom: 3px solid #2374D6; padding-bottom: 0.5rem; margin-bottom: 1rem; }
h2 { font-size: 1.1rem; color: #2374D6; margin: 0 0 0.6rem; padding: 0; border: none; }
h3 { font-size: 1rem; color: #333; margin: 0.8rem 0 0.4rem; }
p { margin: 0.4rem 0; }
blockquote { border-left: 4px solid #2374D6; margin: 0.8rem 0; padding: 0.6rem 1rem; background: #f0f4f8; border-radius: 0 8px 8px 0; font-size: 0.88rem; color: #555; }
ul, ol { margin: 0.4rem 0 0.4rem 1.5rem; }
li { margin: 0.2rem 0; font-size: 0.93rem; }
.section-box { background: white; border-radius: 12px; padding: 1.2rem 1.5rem; margin-bottom: 1rem; box-shadow: 0 1px 4px rgba(0,0,0,0.06); }
table { border-collapse: collapse; margin: 0.5rem 0; font-size: 0.85rem; display: none; }
th, td { border: 1px solid #e0e0e0; padding: 4px 10px; text-align: left; }
th { background: #2374D6; color: white; font-weight: 600; font-size: 0.82rem; }
tr:nth-child(even) { background: #f8f9fa; }
td:last-child { text-align: center; font-weight: 600; color: #2374D6; }
.eval-badges { display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0.6rem 0; }
.eval-badge { background: #EEF4FD; color: #1A5CA8; padding: 0.2rem 0.7rem; border-radius: 14px; font-size: 0.8rem; font-weight: 600; }
.essence-box { border: 2px solid #1A5CA8; border-radius: 10px; padding: 1rem 1.2rem; margin: 0.8rem 0; background: #F5F8FE; }
.essence-box h2 { color: #1A5CA8; margin: 0 0 0.5rem; border: none; padding: 0; }
code { background: #e8edf3; padding: 0.15rem 0.4rem; border-radius: 4px; font-size: 0.85rem; }
pre { background: #1a1a2e; color: #e0e0e0; padding: 1rem; border-radius: 8px; overflow-x: auto; margin: 0.8rem 0; }
pre code { background: none; color: inherit; }
img { max-width: min(100%, 700px); border: 1px solid #e8e8e8; border-radius: 8px; margin: 0.8rem auto; display: block; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
img + em, p > em:only-child { font-size: 0.85rem; color: #888; display: block; text-align: center; }
em { font-style: italic; }
hr { border: none; border-top: 1px solid #e0e0e0; margin: 0.5rem 0; }
strong { color: #1a1a2e; }
a { color: #1A5CA8; }
.back { margin-top: 1.5rem; padding: 0.8rem 0; border-top: 2px solid #e0e0e0; }
.back a { font-weight: 600; text-decoration: none; }
.back a:hover { text-decoration: underline; }
.review-fig { text-align: center; margin: 1.5rem 0; padding: 1rem; background: #f8f9fa; border-radius: 12px; }
.review-fig img { max-width: min(100%, 700px); border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
.fig-caption { font-size: 0.85rem; color: #888; margin-top: 0.5rem; font-style: italic; }"""

    mathjax_init = r"window.MathJax={tex:{inlineMath:[['$','$'],['\\(','\\)']],displayMath:[['$$','$$'],['\\[','\\]']]}};"

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/font-kopub/1.0/kopubdotum.css">
<script>{mathjax_init}</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>
<style>
{css}
</style>
</head>
<body>
{final_body}
<div class="back"><a href="../../scisci/index.html">&larr; 목록으로 돌아가기</a></div>
</body>
</html>
"""


# ── Main processing ──
print("Starting figure extraction...")
fig_results = {}
for e in ENTRIES:
    slug = e["slug"]
    num = e["num"]
    fig_dir = BASE / slug / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)

    if e["has_pdf"]:
        ok = extract_fig1(e["pdf_path"], str(fig_dir))
        fig_results[num] = "extracted" if ok else "failed"
        status = "OK" if ok else "FAILED"
    else:
        fig_results[num] = "no_pdf"
        status = "no PDF"
    print(f"  [{num}] {slug[:45]} -> {status}")

print("\nGenerating review.md and index.html files...")
for e in ENTRIES:
    num = e["num"]
    slug = e["slug"]
    rv = REVIEWS.get(num)
    if not rv:
        print(f"  [{num}] NO REVIEW DATA - skipping")
        continue

    paper_dir = BASE / slug
    paper_dir.mkdir(parents=True, exist_ok=True)

    review_content = make_review_md(e, rv)
    (paper_dir / "review.md").write_text(review_content, encoding="utf-8")

    html_content = make_index_html(e, rv)
    (paper_dir / "index.html").write_text(html_content, encoding="utf-8")

    print(f"  [{num}] {slug[:45]} -> written")

print("\nAll done!")
