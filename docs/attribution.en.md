# Attribution — who worked where

![Author-to-institution pipeline](../attribution_workflow.png)

> 🐱 **Ten cats try in order, and the librarian cat checks every one of them.**

Answering "the 20 most active institutions in AI4S and their leading
researchers" from a corpus needs two things. Which institutions a paper
carries is easy to count; tying an *author* to one of them means reading the
superscripts in the byline. Without the second, a per-institution researcher
list fills up with people who were never there.

The full account, with the measurements behind each decision, is in the
[Korean document](attribution.md); this page carries the part that used to sit
in the README.

## When to use the LLM — three arrangements, one set of papers

An LLM reading a rendered first page handles superscripts, symbols and footnote
placement in one go, which raises the question of whether the eight PDF parsers
earn their keep. All three arrangements were run over the **same 300 random
ai4s papers** (`pipeline/experiment_ladder_order.py --sample 300`, fixed seed),
and each one is billed only for the pages it would actually request.

| | **①** Reader last only | **②** Reader first | **③** Now — last, plus top-up below 80% |
|---|---:|---:|---:|
| Papers resolved | 239 | 239 | 239 |
| **Author-institution links** | 1,024 | 1,165 | **1,177** |
| Pages the reader read | 23 (8%) | 300 (100%) | 174 (58%) |
| Time | **2.3 min** | 28.8 min | 16.5 min |
| Cost | **$0.22** | $2.84 | $1.62 |
| Per 1,000 papers | **$0.73** | $9.47 | $5.40 |

**All three resolve the same papers.** Not one paper was resolved by the parsers
and missed by the reader, nor the reverse (`only_parsers: 0, only_reader: 0`).
The 61 that all three failed have no institution rows or no authors at all, so
no reader can reach them. **Order does not change reach.**

What changes is **depth**. Across the 103 papers where ① and ② disagree,
checking the extra links against the page gives **189 supported for the reader
against 79 for the parsers** — and, in the other direction, **14 links no page
supports for the reader against 1 for the parsers**. It reads deeper and it also
invents more.

**③ yields more links than ②** (1,177 vs 1,165). ② *replaces* the parser output
with the reader's, while ③ reads only the thin papers and *adds* to what the
parsers found. The two readers catch different authors often enough that the
union is wider than either alone — at **57%** of ②'s cost and time.

So ③ is what runs: the page is reread only where the parsers mapped **fewer than
80% of the authors** (`--augment`), which is usually a large collaboration whose
byline wraps over ten lines and where a parser read only the first.

### Applied to the whole 4,196-paper corpus

| | Before (①) | **After (③)** |
|---|---:|---:|
| Papers resolved | 3,628 (86.5%) | 3,628 (**86.5%**) |
| Author-institution links | 24,449 | **26,212** (+1,763) |
| Authors with an institution | 14,530 | **15,280** (+750) |
| **Papers where every author is placed** | 1,883 (44.9%) | **2,222 (53.0%)** |
| Papers the reader read | 54 | 689 |
| Added time / cost | — | 112 min · **$10.53** (once) |

> A later fix restored institution extraction for papers with no publisher
> deposit, so the corpus now stands at **3,706 papers resolved (88.3%) and
> 26,905 links**. See [attribution](docs/attribution.md).

**Papers resolved did not move, and that is the point.** Topping up does not
reach new papers; it finishes reading papers already resolved. What grows is
author coverage, which is what the per-institution researcher rankings rest on.

```bash
python pipeline/extract_byline_llm.py --augment --execute     # partly-mapped papers
python pipeline/experiment_ladder_order.py --sample 300       # re-check all three
```
