# arXiv:2603.20988v1[cs.AI]22 Mar 2026

## Can we automatize scientific discovery in the cognitive sciences?

### Akshay K. Jagadish1, Milena Rmus2, Kristin Witte2,3, Marvin Mathony2, Marcel Binz2, and Eric Schulz2,*

1Princeton AI Lab, Princeton University, New Jersey, USA 2Institute for Human-Centered AI, Helmholtz Munich, Neuherberg, Germany 3Ludwig-Maximilians-University, Munich, 80539, Germany

*eric.schulz@helmholtz-munich.de

### ABSTRACT

The cognitive sciences aim to understand intelligence by formalizing underlying operations as computational models. Traditionally, this follows a cycle of discovery where researchers develop paradigms, collect data, and test predefined model classes. However, this manual pipeline is fundamentally constrained by the slow pace of human intervention and a search space limited by researchers’ background and intuition. Here, we propose a paradigm shift toward a fully automated, in silico science of the mind that implements every stage of the discovery cycle using Large Language Models (LLMs). In this framework, experimental paradigms exploring conceptually meaningful task structures are directly sampled from an LLM. High-fidelity behavioral data are then simulated using foundation models of cognition. The tedious step of handcrafting cognitive models is replaced by LLM-based program synthesis, which performs a high-throughput search over a vast landscape of algorithmic hypotheses. Finally, the discovery loop is closed by optimizing for “interestingness”, a metric of conceptual yield evaluated by an LLM-critic. By enabling a fast and scalable approach to theory development, this automated loop functions as a high-throughput in-silico discovery engine, surfacing informative experiments and mechanisms for subsequent validation in real human populations.

### Introduction

The cognitive sciences aim to understand intelligence using computational models1. These models formally ground theories about cognitive processes by specifying interpretable operations and dynamics underlying human reasoning, learning, and decision-making2. The standard model of discovery in the cognitive sciences typically follows a virtuous cycle of four stages3. First, researchers develop a paradigm to test a particular feature of human cognition. Second, a sufficient volume of data is collected from human participants. Third, a predefined class of models is handcrafted and tested against the collected data, which corresponds to targeted hypothesis testing of the involved cognitive processes. Finally, the results of the experiment are reviewed by the scientific community, who then innovate on the paradigm, model class, and model comparisons involved.

While this process has led to general progress in our understanding of cognition, it remains constrained by several structural disadvantages. The primary constraint is the inherent slowness of a cycle that relies on human involvement at every step, where the time elapsed between initial hypothesis and final publication can span years and thus decouple the pace of theory development from the velocity of data acquisition. Furthermore, this manual pipeline restricts the space of hypothesis that gets explored, which is often restricted to familiar experimental designs and model classes rather than the vast landscape of all possible paradigms and algorithmic solutions. This reliance on researcher-driven designs introduces subtle biases and limits the scalability of experimentation and theory development.

These limitations raise the question: can we remove the bottlenecks imposed by human intervention and genuinely scale up scientific discovery in the cognitive sciences?4,5 We argue that we should seriously consider accelerating the discovery process by automating the steps involved in the process6. We are currently at a critical inflection point where models capable of automating each step of the standard discovery cycle are becoming available7. In the following sections, we examine how the four constituent stages of this cycle, i.e., proposing experiments, generating data, synthesizing models, and closing the loop through iterative refinement, can be implemented in silico. By enabling a new approach that is remarkably fast, scalable, and widely applicable, an automated science of the mind is no longer a distant fiction, but an imminent reality.

### Proposing experiments

Automated discovery begins by defining the space of possible experiments. If machine algorithms are to generate new paradigms rather than merely optimize existing ones, a formal language for describing experimental structures and how their constituent

#### Experimentalist proposes design and participant set-up

Cognitive foundation model produces behavioral data for proposed set-up

###### Grammar:

Meta-data: Age Sex Education Diagnosis Questionnaires Health status Genetic risk Life history …

![image 1](Jagadish et al._2026_Can we automatize scientific discovery in the cognitive sciences_images/imageFile1.png)

![image 2](Jagadish et al._2026_Can we automatize scientific discovery in the cognitive sciences_images/imageFile2.png)

![image 3](Jagadish et al._2026_Can we automatize scientific discovery in the cognitive sciences_images/imageFile3.png)

Modeller finds best fitting model for the generated behavioral data

#### Critic reports on the findings

![image 4](Jagadish et al._2026_Can we automatize scientific discovery in the cognitive sciences_images/imageFile4.png)

![image 5](Jagadish et al._2026_Can we automatize scientific discovery in the cognitive sciences_images/imageFile5.png)

![image 6](Jagadish et al._2026_Can we automatize scientific discovery in the cognitive sciences_images/imageFile6.png)

![image 7](Jagadish et al._2026_Can we automatize scientific discovery in the cognitive sciences_images/imageFile7.png)

Reports on: Interestingness Novelty Fit to literature Quality Uncertainty …

Figure 1. An automated cycle of scientific discovery in the cognitive sciences. An experimentalist proposes experiments, a cognitive foundation model generates behavioral data. A modeller proposes and tests different computational models. Finally, a critic judges the “interestingness” of the results and parsed that signal back to the experimentalist for further optimization.

components can be combined is required. A natural starting point are generative grammars over experiments8. For instance, a grammar over Markov Decision Processes (MDPs)9 could provide an initial foundation. Because MDPs are formally defined by environmental states, transition dynamics, and reward structures, they can capture a vast class of decision-making tasks used in psychology and neuroscience, ranging from simple multi-armed bandits10 to multi-step planning paradigms11.

Yet, this approach immediately exposes a representational bottleneck: automated discovery is fundamentally constrained by the expressivity of its underlying grammar. Ideally, the task language should be able to express a broad range of existing cognitive experiments while allowing flexible integration of new experiments with previously unexplored factors. Building such a language remains a key scientific challenge. We propose that a promising strategy in the future is to use an LLM itself as an intelligent experiment sampler. In this framework, an LLM directly proposes a set of experiments that are best positioned to elicit a specific type of behavior or test a specific hypothesis, and critically, it can further refine them based on feedback, adding or removing key experimental factors as needed.

### Generating data

Once a task is specified, the cycle proceeds to the generation of synthetic behavioral data. This is achieved using recent iterations of the Centaur model12, a foundation model of human cognition. These models can generate data for any cognitive experiment that can be expressed in language format. For example, MDP-like tasks can be described as a task in which the agent needs to choose between multiple options repeatedly to maximize rewards. Once the agent made a choice, the reward of the chosen option gets generated, the choice and its outcome are appended to the trial history that is then re-submitted as a new prompt to generate the next choice, and so forth13. Unlike traditional cognitive models that require manual parameter tuning, foundation models, like Centaur, can generate de novo data that are often indistinguishable from human behavior. While the ability of these models to generalize to entirely novel experimental structures remains a subject of ongoing debates, current evidence suggests they can (at least to some extent) successfully extrapolate to tasks outside their initial training distribution14.

In recent efforts, we aim to scale the underlying datasets for these models by an order of magnitude and integrate extensive subject-specific metadata. By incorporating demographics (e.g., age, gender, nationality) and questionnaire scores (e.g., psychiatric symptom scales), the data generation process can be conditioned on specific individual differences. This allows the system to simulate not just a generic agent, but a targeted participant profile, for instance, simulating the behavior of a 30-year-old individual with high scores in obsessive-compulsive traits performing a specific planning task. By parsing both the

proposed experiment and these subject-specific features into the generative engine, we can produce high-fidelity behavioral data that reflects the high-dimensional complexity of real-world populations. This data can the be submitted to the next step of the cycle: model synthesis.

### Synthesizing models

The third stage of the discovery cycle, i.e. model synthesis and comparison, is traditionally labor-intensive. In the standard paradigm, researchers must manually specify a small set of candidate models, derive their likelihood functions, and fit them to empirical data using computationally demanding optimization routines. This process is not only slow but also inherently biased toward a narrow set of “cognitively plausible” functions that humans are familiar with and are capable of formalizing and testing. To automate this stage, we must shift from carefully handcrafting to synthesizing models at scale, where the search space encompasses a vast landscape of algorithmic hypotheses.

Recent advances have demonstrated that LLMs can act as creative agents in this symbolic space15. For instance, Rmus and Jagadish et al.16 leveraged LLMs’ abilities to generate hypotheses about cognitive processes, developing a novel pipeline for Guided generation of Computational Cognitive Models (GeCCo) that can synthesize cognitive models as Python functions, and iteratively refine them based on feedback on their predictive performance. Through this iterative feedback loop, the system uses these performance signals to refine its code, exploring the algorithmic space to arrive at the best-fitting model while maintaining a record of all intermediate hypotheses.

Other approaches to automated model discovery rely on evolutionary algorithms17, which use mutation and crossover operators to evolve complex architectures from simpler building blocks, or on hybrid systems that couple evolutionary search with LLM-based program synthesis. One example is FunSearch18, which iteratively samples code variants for a target function, executes them to obtain an objective score, and retains the best programs as seeds for further search. While such methods can be computationally expensive, they offer a path toward discovering mechanisms that human intuition might overlook, transforming model synthesis into an objective, high-throughput search over cognitive programs19.

### Closing the loop

The final—and conceptually hardest—step is to close the loop: deciding how the outcome of one iteration should shape the next experiment, participant profiles and model search. In a fully autonomous pipeline, this requires specifying an objective for the process of scientific discovery itself. Classical strategies from optimal experimental design and active learning may offer a principled starting point: we can propose tasks that maximize expected information gain, reduce posterior uncertainty over models, or target regions of the task grammar where candidate explanations disagree most strongly. Yet these criteria are myopic. They reward discriminability even when the resulting distinctions are scientifically unilluminating, and they often steer the system toward edge cases that are statistically informative but theoretically dull.

To move beyond this, the loop must optimize not only informativeness, but also interestingness. Building on recent work on open-ended discovery and self-improving search20, we can introduce a critic model that evaluates the outcome of each cycle and proposes what to do at the beginning of the next cycle, following an LLM-as-judge framework. In concrete terms, the critic scores a discovery tuple—the proposed experiment, the simulated participant profile(s), the generated data, and the space of models that best explains it—along dimensions such as novelty relative to the system’s prior discoveries, compressibility or simplicity of the best explanation, the presence of qualitative signatures, and the extent to which the results suggest a transferable principle rather than a task-specific hack.

Closing the cycle, experiment generation is guided by an interestingness signal that rewards discoveries with high conceptual yield. The system can then iteratively bias its proposals toward configurations that produce sharp theoretical contrasts, uncover new behavioral phenomena, or force the invention of new explanatory primitives21. Importantly, this does not eliminate the scientist. Instead, it acts as a high-throughput search in the hypothesis space: humans define the problem, the expressiveness of the task language, the structure of the output model family, evaluation principles, the shape of the expected theory, and other constraints, while the automated loop surfaces a small set of unusually informative experiments and mechanisms. The highest-scoring discoveries can then be validated in vivo with human participants, keeping the process anchored to biological cognition while dramatically scaling up and accelerating the search for theory.

### Discussion

Jorge Luis Borges imagined the Library of Babel: an infinite archive containing every possible book, masterpieces and proofs alongside endless gibberish. An automated science of the mind risks building the cognitive analogue of that library: a vast enumerative engine that generates every possible task, every possible dataset, every possible model, most of it worthless. The goal here, however, is not to flood cognitive science with an ocean of synthetic “books”. It is to surface the rare volumes that

matter: experiments that carve nature at its joints, models that compress behavior into explanatory principles, and predictions that survive contact with actual data. If automation succeeds, it should not remove the scientist from discovery, but rather act as an amplifier of our ability to search, to falsify, and to learn.

This paper has outlined an end-to-end vision for such a system: an engine that proposes experiments, generates behavioral data in silico, discovers mechanistic models at scale, and closes the loop by steering search toward high-value discoveries. The promise is apparent, and so are the failure modes. A credible discussion must therefore be blunt about what can go wrong—because the central risk is not merely technical failure, but epistemic failure: producing persuasive-looking results that are scientifically hollow.

The proposed cycle is only as strong as its weakest step. First, automated experimental design is bounded by the expressibility and interpretability of the task language. A task grammar determines what experiments can be proposed, and much of scientific innovation comes from stepping outside the currently explored space: inventing new paradigms, new measurements, or new representational framings. No search procedure can discover what the representation forbids. This makes the experiment grammar itself a central scientific object: it must be able to cover multiple cognitive task domains, from sequential decision-making, memory, and categorization to reasoning, and social cognition, and it should be pressure-tested by systematically probing where it fails.

Second, synthetic data generation is not guaranteed to be a faithful substitute for humans. Behavioral foundation models may rely on shortcuts, drift toward “average” subjects, or fail under genuine distribution shift. Even plausible-looking behavior can be produced for the wrong reasons, yielding an illusion of mechanistic clarity. A pragmatic stance is to treat such models as accelerators for hypothesis generation rather than as ground truth: they should be continuously calibrated against benchmark effects, challenged with adversarial tasks designed to expose heuristics, and, where appropriate, complemented or replaced by smaller, local simulators tuned to specific task families.

Third, model discovery over programs is not smooth optimization. Instead, the optimization space is rugged: tiny edits to the code can break a model, distinct mechanisms can be behaviorally indistinguishable, and LLM-guided search can inherit strong priors and stylistic biases from their training data. There is no guarantee of finding a globally best mechanism, and evaluation metrics can be gamed unless carefully designed. Nevertheless, it is undeniable that this approach can explore far more candidates than was previously possible, and early results suggest that it can discover genuinely new mechanistic descriptions rather than simply rephrasing familiar ones under the right conditions.

Finally, closing the loop with an “interestingness” signal is both enticing and dangerous. A critic could reward theatrical novelty, drift toward idiosyncratic edge cases, or be gamed by policies that learn to manufacture superficial weirdness. Interestingness should therefore not be a single scalar oracle. A safer design is multi-objective: combine novelty with robustness, parsimony, generalization across tasks and populations, and, crucially, unification, i.e., explaining multiple phenomena with shared mechanisms.

Despite these risks, the upside of the proposal is large. Automating the loop could increase the throughput of discovery by orders of magnitude, shifting human effort from enumerating possibilities to defining problem representations, the shape of the solutions, constraints, and decisive tests. The most immediate dividends may come from individual differences: conditioning simulated participants on demographics and psychometrics naturally links cognitive modeling with computational psychiatry, enabling mechanistic accounts of heterogeneity rather than an “average mind.” The current proposal can also expand beyond behavior by integrating neuroscience, requiring candidate mechanisms to predict both choices and neural signatures, and beyond text, by incorporating perception to support psychophysics and more ecological paradigms. More broadly, it offers a route to addressing the generalization crisis: by systematically searching for invariances across task variants and populations, we can turn generalization from a post-hoc hope into an explicit selection criterion for theories.

In summary, we appear to be near an inflection point where the required components, i.e. structured experiment representations, behavioral generators, scalable program search, and critic-guided exploration, are simultaneously becoming feasible. The challenge now is epistemic as much as technical: to build systems that produce fewer books and more knowledge, and to develop norms that keep automated discovery tethered to empirical validation. The Library of Babel contains everything; science is the art of finding the few pages worth reading. An automated discovery engine will be worth building if it reliably elevates those pages.

### Acknowledgements

AJ is supported by the Natural and Artificial Mind (NAM) Fellowship, which is generously supported by the Scully Perestsman foundation. ES is funded by the Helmholtz Association, an ERC Starting Grant on "Towards an Artificial Cognitive Science”, and a Wellcome Discovery Award.

### References

- 1. Busemeyer, J. R. & Diederich, A. Cognitive modeling (Sage, 2010).
- 2. Sun, R. The Cambridge Handbook of Computational Psychology (Cambridge University Press, Cambridge, 2008).
- 3. Klahr, D. & Dunbar, K. Dual space search during scientific reasoning. Cogn. Sci. 12, 1–48, DOI: 10.1207/ s15516709cog1201_1 (1988).
- 4. King, R. D. et al. The automation of science. Science 324, 85–89 (2009).
- 5. Lu, C. et al. The ai scientist: Towards fully automated open-ended scientific discovery. arXiv preprint arXiv:2408.06292

(2024).

- 6. Musslick, S. et al. Automating the practice of science: Opportunities, challenges, and implications. Proc. Natl. Acad. Sci. 122, e2401238121 (2025).
- 7. Binz, M. et al. How should the advancement of large language models affect the practice of science? Proc. Natl. Acad. Sci. 122, e2401227121 (2025).
- 8. Musslick, S., Strittmatter, Y. & Dubova, M. Closed-loop scientific discovery in the behavioral sciences. PsyArXiv 10

(2024).

- 9. Miconi, T. Procedural generation of meta-reinforcement learning tasks. arXiv preprint arXiv:2302.05583 (2023).
- 10. Wilson, R. C., Geana, A., White, J. M., Ludvig, E. A. & Cohen, J. D. Humans use directed and random exploration to solve the explore–exploit dilemma. J. experimental psychology: Gen. 143, 2074 (2014).
- 11. Daw, N. D., Gershman, S. J., Seymour, B., Dayan, P. & Dolan, R. J. Model-based influences on humans’ choices and striatal prediction errors. Neuron 69, 1204–1215 (2011).
- 12. Binz, M. et al. A foundation model to predict and capture human cognition. Nature 644, 1002–1009 (2025).
- 13. Binz, M. & Schulz, E. Using cognitive psychology to understand gpt-3. Proc. Natl. Acad. Sci. 120, e2218523120 (2023).
- 14. Binz, M. & Schulz, E. Turning large language models into cognitive models. arXiv preprint arXiv:2306.03917 (2023).
- 15. Austin, J. et al. Program synthesis with large language models. arXiv preprint arXiv:2108.07732 (2021).
- 16. Rmus, M., Jagadish, A. K., Mathony, M., Ludwig, T. & Schulz, E. Generating computational cognitive models using large language models. In The Thirty-ninth Annual Conference on Neural Information Processing Systems.
- 17. Novikov, A. et al. Alphaevolve: A coding agent for scientific and algorithmic discovery. arXiv preprint arXiv:2506.13131

(2025).

- 18. Romera-Paredes, B. et al. Mathematical discoveries from program search with large language models. Nature 625, 468–475 (2024).
- 19. Castro, P. S. et al. Discovering symbolic cognitive models from human and animal behavior. In International Conference on Machine Learning, 6849–6890 (PMLR, 2025).
- 20. Zhang, J., Lehman, J., Stanley, K. & Clune, J. Omni: Open-endedness via models of human notions of interestingness. In The Twelfth International Conference on Learning Representations.
- 21. Yamada, Y. et al. The ai scientist-v2: Workshop-level automated scientific discovery via agentic tree search. arXiv preprint arXiv:2504.08066 (2025).


