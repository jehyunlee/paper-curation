CAN AI REVIEW THE 
SCIENTIFIC LITERATURE?
Artificial intelligence could help to make sense of the world’s 
science — but it comes with risks. By Helen Pearson
ILLUSTRATION: PIOTR KOWALCZYK
276  |  Nature  |  Vol 635  |  14 November 2024
Feature

W
hen Sam Rodriques was 
a neurobiology graduate 
student, he was struck by a 
fundamental limitation of sci-
ence. Even if researchers had 
already produced all the infor-
mation needed to understand 
a human cell or a brain, “I’m not 
sure we would know it”, he says, “because no 
human has the ability to understand or read all 
the literature and get a comprehensive view.”
Five years later, Rodriques says he is closer 
to solving that problem using artificial intel-
ligence (AI). In September, he and his team 
at the US start-up FutureHouse announced 
that an AI-based system they had built could, 
within minutes, produce syntheses of sci-
entific knowledge that were more accurate 
than Wikipedia pages1. The team promptly 
generated Wikipedia-style entries on around 
17,000 human genes, most of which previously 
lacked a detailed page.
Rodriques is not the only one turning to 
AI to help synthesize science. For decades, 
scholars have been trying to accelerate the 
onerous task of compiling bodies of research 
into reviews. “They’re too long, they’re incred-
ibly intensive and they’re often out of date by 
the time they’re written,” says Iain Marshall, 
who studies research synthesis at King’s 
College London. The explosion of interest 
in large language models (LLMs), the gener-
ative-AI programs that underlie tools such as 
ChatGPT, is prompting fresh excitement about 
automating the task. 
Some of the newer AI-powered science 
search engines can already help people to 
produce narrative literature reviews — a 
written tour of studies — by finding, sorting 
and summarizing publications. But they 
can’t yet produce a high-quality review by 
themselves. The toughest challenge of all is 
the ‘gold-standard’ systematic review, which 
involves stringent procedures to search and 
assess papers, and often a meta-analysis to 
synthesize the results. Most researchers agree 
that these are a long way from being fully auto-
mated. “I’m sure we’ll eventually get there,” 
says Paul Glasziou, a specialist in evidence and 
systematic reviews at Bond University in Gold 
Coast, Australia. “I just can’t tell you whether 
that’s 10 years away or 100 years away.” 
At the same time, however, researchers 
fear that AI tools could lead to more sloppy, 
inaccurate or misleading reviews polluting the 
literature. “The worry is that all the decades of 
research on how to do good evidence synthesis 
starts to be undermined,” says James Thomas, 
who studies evidence synthesis at University 
College London. 
Computer-assisted reviews
Computer software has been helping 
researchers to search and parse the research 
literature for decades. Well before LLMs 
emerged, scientists were using machine-learn-
ing and other algorithms to help to identify 
particular studies or to quickly pull findings 
out of papers. But the advent of systems such 
as ChatGPT has triggered a frenzy of interest in 
speeding up this process by combining LLMs 
with other software. 
It would be terribly naive to ask ChatGPT 
— or any other AI chatbot — to simply write 
an academic literature review from scratch, 
researchers say. These LLMs generate text by 
training on enormous amounts of writing, 
but most commercial AI firms do not reveal 
what data the models were trained on. If 
asked to review research on a topic, an LLM 
such as ChatGPT is likely to draw on credible 
academic research, inaccurate blogs and who 
knows what other information, says Marshall. 
“There’ll be no weighing up of what the most 
pertinent, high-quality literature is,” he says. 
And because LLMs work by repeatedly gener-
ating statistically plausible words in response 
to a query, they produce different answers to 
the same question and ‘hallucinate’ errors — 
including, notoriously, non-existent academic 
references. “None of the processes which are 
regarded as good practice in research synthe-
sis take place,” Marshall says. 
A more sophisticated process involves 
uploading a corpus of pre-selected papers to 
an LLM, and asking it to extract insights from 
them, basing its answer only on those studies. 
This ‘retrieval-augmented generation’ seems 
to cut down on hallucinations, although it does 
not prevent them. The process can also be set 
up so that the LLM will reference the sources 
it drew its information from. 
This is the basis for specialized, AI-powered 
science search engines such as Consensus and 
Elicit. Most companies do not reveal exact 
details of how their systems work. But they 
typically turn a user’s question into a comput-
erized search across academic databases such 
as Semantic Scholar and PubMed, returning 
the most relevant results.
An LLM then summarizes each of these 
studies and synthesizes them into an answer 
that cites its sources; the user is given various 
options to filter the work they want to include. 
“They are search engines first and foremost,” 
says Aaron Tay, who heads data services at 
Singapore Management University and blogs 
about AI tools. “At the very least, what they cite 
is definitely real.” 
These tools “can certainly make your review 
and writing processes efficient”, says Mushtaq 
Bilal, a postdoctoral researcher at the Uni-
versity of Southern Denmark in Odense, who 
trains academics in AI tools and has designed 
his own, called Research Kick. Another AI 
system called Scite, for example, can quickly 
generate a detailed breakdown of papers that 
support or refute a claim. Elicit and other sys-
tems can also extract insights from different 
sections of papers — the methods, conclusions 
and so on. There’s “a huge amount of labour 
that you can outsource”, Bilal says. 
But most AI science search engines cannot 
produce an accurate literature review auton-
omously, Bilal says. Their output is more “at 
the level of an undergraduate student who 
pulls an all-nighter and comes up with the 
main points of a few papers”. It is better for 
researchers to use the tools to optimize parts 
of the review process, he says. James Brady, 
head of engineering at Elicit, says that its users 
are augmenting steps of reviewing “to great 
effect”. 
Another limitation of some tools, including 
Elicit, is that they can only search open-access 
papers and abstracts, rather than the full 
text of articles. (Elicit, in Oakland, California, 
searches about 125 million papers; Consen-
sus, in Boston, Massachusetts, looks at more 
than 200 million.) Bilal notes that much of the 
research literature is paywalled and it’s compu-
tationally intensive to search a lot of full text. 
“Running an AI app through the whole text of 
millions of articles will take a lot of time, and it 
will become prohibitively expensive,” he says. 
Full-text search
For Rodriques, money was in plentiful supply, 
because FutureHouse, a non-profit organiza-
tion in San Francisco, California, is backed by 
former Google chief executive Eric Schmidt and 
other funders. Founded in 2023, FutureHouse 
aims to automate research tasks using AI. 
This September, Rodriques and his team 
revealed PaperQA2, FutureHouse’s open-
source, prototype AI system 1. When it is given 
a query, PaperQA2 searches several academic 
databases for relevant papers and tries to 
access the full text of both open-access and 
paywalled content. (Rodriques says the team 
has access to many paywalled papers through 
its members’ academic affiliations.) The sys-
tem then identifies and summarizes the most 
relevant elements. In part because PaperQA2 
digests the full text of papers, running it is 
expensive, he says. 
The FutureHouse team tested the system by 
using it to generate Wikipedia-style articles 
on individual human genes. They then gave 
THOSE ARE IMPORTANT 
LITTLE TOOLS IN 
SHAVING DOWN THE 
TIME OF DOING A 
SYSTEMATIC REVIEW.”
Nature  |  Vol 635  |  14 November 2024  |  277

several hundred AI-written statements from 
these articles, along with statements from 
real (human-written) Wikipedia articles on 
the same topic, to a blinded panel of PhD and 
postdoctoral biologists. The panel found that 
human-authored articles contained twice as 
many ‘reasoning errors’ — in which a written 
claim is not properly supported by the citation 
— than did ones written by the AI tool. Because 
the tool outperforms people in this way, the 
team titled its paper ‘Language agents achieve 
superhuman synthesis of scientific knowledge’. 
Tay says that PaperQA2 and another tool 
called Undermind take longer than conven-
tional search engines to return results — 
minutes rather than seconds — because they 
conduct more-sophisticated searches, using 
the results of the initial search to track down 
other citations and key phrases, for example. 
“That all adds up to being very computation-
ally expensive and slow, but gives a substan-
tially higher quality search,” he says.
Systematic challenge
Narrative summaries of the literature are hard 
enough to produce, but systematic reviews 
are even worse. They can take people many 
months or even years to complete2. 
A systematic review involves at least 
25 careful steps, according to a breakdown 
from Glasziou’s team. After combing through 
the literature, a researcher must filter their 
longlist to find the most pertinent papers, 
then extract data, screen studies for poten-
tial bias and synthesize the results. (Many of 
these steps are done in duplicate by another 
researcher to check for inconsistencies.) 
This laborious method — which is supposed 
to be rigorous, transparent and reproducible 
— is considered worthwhile in medicine, for 
instance, because clinicians use the results 
to guide important decisions about treating 
patients.
In 2019, before ChatGPT came along, 
Glasziou and his colleagues set out to achieve a 
world record in science: a systematic review in 
two weeks. He and others, including Marshall 
and Thomas, had already developed computer 
tools to reduce the time involved. The menu 
of software available by that time included 
RobotSearch, a machine-learning model 
trained to quickly identify randomized trials 
from a collection of studies. RobotReviewer, 
another AI system, helps to assess whether a 
study is at risk of bias because it was not ade-
quately blinded, for instance. “All of those are 
important little tools in shaving down the time 
of doing a systematic review,” Glasziou says. 
The clock started at 9:30 a.m. on Monday 
21 January 2019. The team cruised across the 
line at lunchtime on Friday 1 February, after 
a total of nine working days3. “I was excited,” 
says epidemiologist Anna Mae Scott at the Uni-
versity of Oxford, UK, who led the study while 
at Bond University; everyone celebrated with 
cake. Since then, the team has pared its record 
down to five days. 
Could the process get faster? Other 
researchers have been working to automate 
aspects of systematic reviews, too. In 2015, 
Glasziou founded the International Collab-
oration for the Automation of Systematic 
Reviews, a niche community that, fittingly, has 
produced several systematic reviews about 
tools for automating systematic reviews4. But 
even so, “not very many [tools] have seen wide-
spread acceptance”, says Marshall. “It’s just a 
question of how mature the technology is.” 
Elicit is one company that says its tool helps 
researchers with systematic reviews, not 
just narrative ones. The firm does not offer 
systematic reviews at the push of a button, says 
Brady, but its system does automate some of 
the steps — including screening papers and 
extracting data and insights. Brady says that 
most researchers who use it for systematic 
reviews have uploaded relevant papers they 
find using other search techniques. 
Systematic-review aficionados worry that AI 
tools are at risk of failing to meet two essential 
criteria of the studies: transparency and repro-
ducibility. “If I can’t see the methods used, 
then it is not a systematic review, it is simply 
a review article,” says Justin Clark, who builds 
review automation tools as part of Glasziou’s 
team. Brady says that the papers that review-
ers upload to Elicit “are an excellent, transpar-
ent record” of their starting literature. As for 
reproducibility: “We don’t guarantee that our 
results are always going to be identical across 
repeats of the same steps, but we aim to make it 
so — within reason,” he says, adding that trans-
parency and reproducibility will be important 
as the firm improves its system.
Specialists in reviewing say they would like 
to see more published evaluations of the accu-
racy and reproducibility of AI systems that 
have been designed to help produce literature 
reviews. “Building cool tools and trying stuff 
out is really good fun,” says Clark. “Doing a 
hardcore evaluative study is a lot of hard work.”
Earlier this year, Clark led a systematic review 
of studies that had used generative AI tools to 
help with systematic reviewing. He and his team 
found only 15 published studies in which the 
AI’s performance had been adequately com-
pared with that of a person. The results, which 
have not yet been published or peer reviewed, 
suggest that these AI systems can extract some 
data from uploaded studies and assess the risk 
of bias of clinical trials. “It seems to do OK with 
reading and assessing papers,” Clark says, “but 
it did very badly at all these other tasks”, includ-
ing designing and conducting a thorough liter-
ature search. (Existing computer software can 
already do the final step of synthesizing data 
using a meta-analysis.) 
Glasziou and his team are still trying to 
shave time off their reviewing record through 
improved tools, which are available on a web-
site they call the Evidence Review Accelerator. 
“It won’t be one big thing. It’s that every year 
you’ll get faster and faster,” Glasziou predicts. 
In 2022, for instance, the group released a com-
puterized tool called Methods Wizard, which 
asks users a series of questions about their 
methods and then writes a protocol for them 
without using AI. 
Rushed reviews?
Automating the synthesis of information also 
comes with risks. Researchers have known 
for years that many systematic reviews are 
redundant or of poor quality5, and AI could 
make these problems worse. Authors might 
knowingly or unknowingly use AI tools to race 
through a review that does not follow rigorous 
procedures, or which includes poor-quality 
work, and get a misleading result.
By contrast, says Glasziou, AI could also 
encourage researchers to do a quick check 
of previously published literature when they 
wouldn’t have bothered before. “AI may raise 
their game,” he says. And Brady says that, in 
future, AI tools could help to flag and filter out 
poor-quality papers by looking for telltale signs 
such as P-hacking, a form of data manipulation. 
Glasziou sees the situation as a balance of 
two forces: AI tools could help scientists to 
produce high-quality reviews, but might also 
fuel the rapid generation of substandard ones. 
“I don’t know what the net impact is going to be 
on the published literature,” he says.
Some people argue that the ability to synthe-
size and make sense of the world’s knowledge 
should not lie solely in the hands of opaque, 
profit-making companies. Clark wants to see 
non-profit groups build and carefully test AI 
tools. He and other researchers welcomed the 
announcement from two UK funders last month 
that they are investing more than US$70 million 
in evidence-synthesis systems. “We just want to 
be cautious and careful,” Clark says. “We want to 
make sure that the answers that [technology] is 
helping to provide to us are correct.” 
Helen Pearson is a senior editor at Nature. 
1.	 Skarlinski, M. D. et al. Preprint at arXiv https://doi.
org/10.48550/arXiv.2409.13740 (2024).
2.	 Borah, R., Brown, A. W., Capers, P. L. & Kaiser, K. A. BMJ 
Open 7, e012545 (2017). 
3.	 Clark, J. et al. J. Clin. Epidemiol. 121, 81–90 (2020).
4.	 Blaizot, A. et al. Res. Synth. Methods 13, 353–362 (2022). 
5.	 Ioannidis, J. P. A. Milbank Q. 94, 485–514 (2016). 
BUILDING COOL TOOLS 
AND TRYING STUFF OUT 
IS REALLY GOOD FUN.”
278  |  Nature  |  Vol 635  |  14 November 2024
Feature
