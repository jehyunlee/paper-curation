# Boltz-1

## Democratizing Biomolecular Interaction Modeling

Jeremy Wohlwend∗12, Gabriele Corso∗12, Saro Passaro∗12, Noah Getz∗12, Mateo Reveiz12, Ken Leidal3, Wojtek Swiderski3, Liam Atkinson4, Tally Portnoi12, Itamar Chinn12, Jacob Silterra12, Tommi Jaakkola12, Regina Barzilay12

Correspondence to {jwohlwend,gcorso,saro00}@csail.mit.edu

Abstract

Understanding biomolecular interactions is fundamental to advancing fields like drug discovery and protein design. In this paper, we introduce Boltz-1, an open-source deep learning model incorporating innovations in model architecture, speed optimization, and data processing achieving AlphaFold3-level accuracy in predicting the 3D structures of biomolecular complexes. Boltz-1 demonstrates a performance on-par with state-of-the-art commercial models on a range of diverse benchmarks, setting a new benchmark for commercially accessible tools in structural biology. Further, we push the boundary of capabilities of these models with Boltz-steering, a new inference time steering technique that is able to fix hallucinations and non-physical predictions from the models. By releasing the training and inference code, model weights, datasets, and benchmarks under the MIT open license, we aim to foster global collaboration, accelerate discoveries, and provide a robust platform for advancing biomolecular modeling.

![image 1](Boltz-1 Democratizing Biomolecular Interaction Modeling_images/imageFile1.png)

![image 2](Boltz-1 Democratizing Biomolecular Interaction Modeling_images/imageFile2.png)

BOLTZ-1 prediction on PDB structure 8SVA TM-score: 0.95

BOLTZ-1 prediction on PDB structure 8IG1 TM-score: 0.95

###### Figure 1: Example predictions of Boltz-1 on targets from the test set.

∗Equal contribution, 1 MIT CSAIL, 2 MIT Jameel Clinic, 3 Genesis Research, a part of Genesis Therapeutics, 4 CHARM Therapeutics

### Contents

- 1 Overview 2
- 2 Data pipeline 3

- 2.1 Data source and processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
- 2.2 Validation and test sets curation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
- 2.3 Dense MSA pairing algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
- 2.4 Unified cropping algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
- 2.5 Robust pocket-conditioning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5


- 3 Modeling 5

- 3.1 Architectural modifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
- 3.2 Training and inference procedures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
- 3.3 Confidence model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
- 3.4 Optimizations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9


- 4 Boltz steering 11

- 4.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
- 4.2 Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
- 4.3 Constraint potentials . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12


- 5 Results 14
- 6 Conclusion 18
- 7 Acknowledgments 18


### 1 Overview

Biomolecular interactions drive almost all biological mechanisms, and our ability to understand these interactions guides the development of new therapeutics and the discovery of disease drivers. In 2020, AlphaFold2 [Jumper et al., 2021] demonstrated that deep learning models can reach experimental accuracy for single-chain protein structure prediction on a large class of protein sequences. However, a critical question about modeling biomolecular complexes in 3D space remained open.

In the past few years, the research community has made significant progress toward solving this pivotal problem. In particular, the use of deep generative models has proven to be effective in modeling the interaction between different biomolecules with DiffDock [Corso et al., 2022] showing significant improvements over traditional molecular docking approaches and, most recently, AlphaFold3 [Abramson et al., 2024] reaching unprecedented accuracy in the prediction of arbitrary biomolecular complexes.

In this manuscript, we present Boltz-1, the first fully commercially accessible open-source model reaching AlphaFold3 reported levels of accuracy. By making the training and inference code, model weights, datasets, and benchmarks freely available under the MIT license, we aim to empower researchers, developers, and organizations around the world to experiment, validate, and innovate with Boltz-1. At a high level, Boltz-1 follows the general framework and architecture presented by Abramson et al. [2024], but it also presents several innovations which include:

- 1. New algorithms to more efficiently and robustly pair MSAs, crop structure at training time, and condition predictions on user-defined binding pockets;


- 2. Changes to the flow of the representations in the architecture and the diffusion training and inference procedures;
- 3. Revision of the confidence model both in terms of architectural components as well as the framing of the task as a fine-tuning of the model’s trunk layers.


In the following sections, we detail these changes as well as benchmark the performance of Boltz-1 with other publicly available models. Our experimental results show that Boltz-1 delivers performance on par with the state-of-the-art commercial models on a wide range of structures and metrics.

Further, we tackle one of the biggest outstanding challenges with machine learning based structure prediction methods, their frequent lack of respect for physical laws observed, for example, in mistakes in properties like internal geometries, chirality, and steric clashes as well as hallucinations like overlapping chains. We propose a new inference time technique, Boltz-steering, which is able to solve almost all these physical issues while maintaining the model accuracy. We refer to the Boltz-1 model with the steering as Boltz-1x.

Given the dynamic nature of this open-source project, this manuscript and its linked GitHub repository1 will be regularly updated with improvements from our core team and the community. We aspire for this project and its associated codebase to serve as a catalyst for advancing our understanding of biomolecular interactions and a driver for the design of novel biomolecules.

### 2 Data pipeline

Boltz-1 operates on proteins represented by their amino acid sequence, ligands represented by their smiles strings (and covalent bonds), and nucleic acids represented by their genomic sequence. This input is then augmented by adding multiple sequence alignment (MSA) and predicted molecular conformations. Unlike AlphaFold3, we do not include input templates, due to their limited impact on the performance of large models.

In this section, we first outline how the structural training data, as well as the MSA and conformer, were obtained and describe the curation of our validation and test sets. Then, we describe three important algorithmic developments applied to data curation and augmentation that we find to be critical:

- 1. A new algorithm to pair MSAs for multimeric protein complexes from taxonomy information (2.3).
- 2. A unified cropping algorithm that combines the spatial and contiguous cropping strategies used in previous work (2.4).
- 3. A robust pocket-conditioning algorithm tailored to common use cases (2.5).


#### 2.1 Data source and processing

PDB structural data For training we use all PDB structures [Berman et al., 2000] released before 2021-09-30 (same training cut-off date as AlphaFold3) and with a resolution of at least 9˚A. We parse the Biological Assembly 1 from these structures from their mmCIF file. For each polymer chain, we use the reference sequence and align it to the residues available in the structure. For ligands, we use the CCD dictionary to create the conformers and to match atoms from the structure. We remove leaving atoms when (1) the ligand is covalently bound and (2) that atom does not appear in the PDB structure. Finally, we follow the same process as AlphaFold3 for data cleaning, which includes the ligand exclusion list, the minimum number of resolved residues, and the removal of clashing chains.

MSA and molecular conformers We construct MSAs for the full PDB data using the colabfold search

tool [Mirdita et al., 2022] (which leverages MMseqs2 [Steinegger and S¨oding, 2017]), using default parameters (versions: uniref30 2302, colabfold envdb 202108). We then assign taxonomy labels to

1https://github.com/jwohlwend/boltz

all UniRef sequences using the taxonomy annotation provided by UniProt [Consortium, 2015]. For the initial molecular conformers that are provided to the model, we pre-compute a single conformer for all CCD codes using the RDKit’s ETKDGv3 [Wang et al., 2022].

Structure prediction training pipeline We train the structure prediction model (see Section 3.2 for details of the confidence model training) for a total of 68k steps with a batch size of 128. During the first 53k iterations, we use a crop size of 384 tokens and 3456 atoms and draw structures equally from the PDB dataset and the OpenFold distillation dataset (approximately 270K structures, using the MSAs they provided) [Ahdritz et al., 2024]. For the last 15k iterations, we only sampled from the PDB structures and had a crop size of 512 tokens and 4608 atoms. As a comparison AlphaFol3 trained a similar architecture for nearly 150k steps with a batch size of 256, which required approximately four times the computing time. We attribute some of this drastic reduction to the various innovations we detail in the remainder of this section and the next.

#### 2.2 Validation and test sets curation

To address the absence of a standardized benchmark for all-atom structures, we are releasing a new PDB split designed to help the community converge on reliable and consistent benchmarks for all-atom structure prediction tasks.

Our training, validation and test splitting strategy largely follows Abramson et al. [2024]. We first cluster the protein sequences in PDB by sequence identity with the command mmseqs easy-cluster ... --min-seq-id 0.4 [Hauser et al., 2016]. Then, we select all structures in PDB satisfying the following filters:

- 1. Initial release date is before 2021-09-30 (exclusive) and 2023-01-13 (inclusive).
- 2. Resolution is below 4.5˚A.
- 3. All the protein sequences of the chains are not present in any training set clusters (i.e. before 2021-09-30).
- 4. Either no small-molecule is present, or at least one of the small-molecules exhibits a Tanimoto similarity of 0.8 or less to any small-molecule in the training set. Here, a small-molecule is defined as any non-polymer entity containing more than one heavy atom and not included in the ligand exclusion list.


This yields 1728 structures, which we further refine through the following steps:

- 1. Retaining all the structures containing RNA or DNA entities. (126 structures)
- 2. Iteratively adding structures containing small-molecules or ions under the condition that all their protein chains belong to new unseen clusters (330 additional structures)
- 3. Iteratively adding multimeric structures under the condition that all the protein chains belong to new unseen clusters. These are further filtered by randomly keeping only 50% of the passing structures. (231 additional structures)
- 4. Iteratively adding monomers under the condition that their chain belongs to a new unseen cluster. These are further randomly filtered out by keeping only 30% of the passing structures. (57 additional structures)


This results in a total of 744 structures. Finally, we retain the structures with at most 1024 residues in the valid protein/RNA/DNA chains, finishing with a total of 553 validation set structures.

The test set is created using the same procedure described above with the following differences: for protein and ligand similarity exclusion we consider all structures released before 2023-01-13 (which include all training and validation sets), we filter to structures released after 2023-01-13 and the final size filter to structures between 100 and 2000 total residues. The resulting final test set size is 593.

#### 2.3 Dense MSA pairing algorithm

Multiple sequence alignments uncover amino acids that co-evolved throughout evolution, and therefore are likely close to each other in physical space. However, extracting such signals for protein-protein interactions poses a greater challenge, as most proteins are sequenced or reported individually. To approximate these pairings, researchers have leveraged the taxonomy information frequently associated with sequences. In Algorithm 3, we present a method for pairing MSAs using taxonomy in a manner that preserves MSA density (a critical factor, as model complexity scales linearly with the number of MSA rows) while balancing the trade-off between the signal derived from paired sequences and the sequence redundancy within each chain.

#### 2.4 Unified cropping algorithm

In order to efficiently train on complexes with variable size, methods like AlphaFold2 and AlphaFold3 crop the structures during training to a fixed maximum number of atoms, residues, or tokens. The most common techniques to perform such crops are (1) contiguous, where tokens are chosen to be consecutive residues in a biomolecular sequence (or entire molecules), and (2) spatial crops, where tokens are chosen purely depending on their distance from a center token. Each of these two has its advantages and provides different training signals to the models, therefore they are often used in combination as done, for example, by Abramson et al. [2024].

We argue, however, that these are two extremes and it is useful to train the model on a more diverse range of cropping strategies. To this end, we define a new cropping algorithm which directly interpolates between spatial and contiguous strategies. The algorithm, formalized in Algorithm 4, revolves around the definition of neighborhoods, that characterize contiguous portions of sequences of a particular length (or entire non-polymer entities) around a specific token. Neighborhoods are incrementally added to the crop depending on the distance of their central token from the chosen center of the crop. If the size of the neighborhoods is chosen to be zero, this strategy translates into spatial cropping, whereas if the size is half of the maximum token budget, this strategy translates into continuous cropping. In our experiments, we find it beneficial to randomly sample the neighborhood size uniformly between zero and 40 tokens for every training sample.

#### 2.5 Robust pocket-conditioning

In many real-world scenarios, researchers have prior knowledge of the protein’s binding pocket. Therefore, it is valuable to enable the model to condition on the pocket information. AlphaFold3 explored pocket-conditioned generation by fine-tuning the model to include an additional token feature for all the pocket-ligand pairs, where the pocket is defined as any residue with heavy atoms within 6˚A of the ligand. While effective, this design has some limitations. It requires maintaining two models, one with and one without pocket conditioning, and it assumes the specification of all residues within 6˚A. This assumption may not align with realistic scenarios, where users might only know key residues, and the full set of interacting residues is highly dependent on the ligand pose, which is often unknown.

To address these challenges, we implement a different strategy for pocket conditioning, designed to (1) retain a single unified model, (2) ensure robustness to a partial specification of interacting residues, and (3) enable interaction site specification for polymer binders such as proteins or nucleic acids. During training, we incorporate pocket information for a randomly selected binder in 30% of iterations. For these cases, we draw the (maximum) number of pocket residues to reveal from a geometric distribution and randomly select residues from those with at least one heavy atom within 6˚A of the binder. This information is then encoded as an additional one-hot token feature provided to the model. The training process for this pocket-conditioning approach is described in detail in Algorithm 5.

### 3 Modeling

For the model architecture and training, we started by reproducing AlphaFold3 as described in the supplementary material of Abramson et al. [2024]. AlphaFold3 is a diffusion model that uses a

multi-resolution transformer-based model for the denoising of atom coordinates. The model operates at two levels of resolution: heavy atoms and tokens. Tokens are defined as amino acids for protein chains, nucleic acid bases for RNA and DNA, and individual heavy atoms for other molecules and modified residues or bases.

On top of the denoising transformer, critically, AlphaFold3 also employs a central trunk architecture that is used to initialize tokens’ representations and determine the denoising transformer’s attention pair bias. This trunk is computationally expensive due to its use of token pairs as fundamental “computational token” and its axial attention operations on these pair representations which results in a complexity that scales cubically with the number of input tokens. To make such encoding computationally tractable, the trunk is set to be independent of the specific diffusion time or input structure such that it can be run only once per complex.

Starting from this architecture, we designed and tested a number of potential alternative approaches. In the following sections, we describe the ones that yielded improvements and were therefore adopted into Boltz-1.2 Because of the significant computational budget required to train a full-sized model, we tested these changes on a smaller-sized architecture at different points of our development process. We expect our observations to hold for the final full-size model, but cannot present direct ablation studies.

#### 3.1 Architectural modifications

MSA module We find it beneficial to reorder the operations performed in the MSAModule (AlphaFold3 Algorithm 8) to better allow the updates on the single and pair representations to feed to one another. In particular, we change the order3 of its operations from:

OuterProductMean, PairWeightedAveraging, MSATransition, TriangleUpdates, PairTransition to:

PairWeightedAveraging, MSATransition, OuterProductMean, TriangleUpdates, PairTransition. Note that OuterProductMean propagates information from the single to the pair representation, so we now allow the single representations learned in the MSATransition to directly propagate to the pair representation.

Transformer layer Abramson et al. [2024] presents an unusual order of operations in their DiffusionTransformer layers where hidden representations are updated as (AlphaFold3 Algorithm 23):

a ← AttentionPairBias(a) + ConditionedTransitionBlock(a).

This has two issues (1) it lacks residual connections that may make backpropagation more complex and (2) it does not allow for the transformation learned in the AttentionPairBias to be fed in the ConditionedTransitionBlock at the same block. We found it to be beneficial to apply the following transformation order:

a ← a + AttentionPairBias(a) a ← a + ConditionedTransitionBlock(a).

#### 3.2 Training and inference procedures

Kabsch diffusion interpolation A key change between AlphaFold2 and AlphaFold3 was the non-equivariance of the denoising model of AlphaFold3 (compared to the equivariant IPA-based structure module of AlphaFold2) to rotations and translations. To encourage the robustness of the denoising model to such transformations their input is randomly translated and rotated before the denoising at training and inference times. To further reduce the variance of the denoising loss

- 2Some of these differences may simply be the result of reporting mistakes in the current version of the original manuscript from Abramson et al. [2024], as reported .
- 3We note that a similar strategy was also concurrently noticed by https://github.com/Ligo-Biosciences/ AlphaFold3.


###### Denoising model AlphaFold3 reverse diffusion Boltz-1 reverse diffusion

𝑥 𝑥 𝑥   / 

###### model predictions interpolation next step interpolation next step

- Figure 2: 2D representation of the difference between AlphaFold3 reverse diffusion and Boltz1 reverse diffusion with our Kapsch interpolation. Colors indicate correspondence between different points. Even though the prediction of the denoising model is “perfect” according to the aligned MSE loss, the unaligned interpolation may lead to poor structures fed to the next reverse diffusion step.


with respect to these variations, Abramson et al. [2024] use a rigid alignment between the predicted denoising coordinates and the true coordinates before computing the MSE loss.

However, we argue that on its own this procedure is theoretically problematic. One can define simple functions that would achieve zero rigid aligned MSE loss during training, but completely fail to sample realistic poses at inference time. For example, consider a model trying to fit a given structure with coordinates x. Let’s assume that for any noised structure within some reasonable noising perturbation (e.g. ∆ = 10σt), the model always predicts x:

x if ∥ϵt∥ < 10σt, 0 otherwise.

xˆdenoisedt = f(ˆxnoisyt ,t) = f(x ∗ R⊤ + T + ϵt,t) =

where R and T are respectively a random rotation matrix and a random translation vector, ϵt and σt represent respectively the random noise and noise standard deviation for some diffusion time t. This model will have a loss approaching zero during training (one will never sample something beyond 10 standard deviations, and one could make this ∆ arbitrarily large). However, when used at inference time, this model will consistently go out of distribution (and therefore predict a zero vector). This is because at low noise levels the interpolation between the current randomly rotated xˆnoisyt and the predicted xˆdenoisedt may lead to a pose xˆt−∆t that is very far from x and will fall beyond the 10σt mark. Figure 2 shows a graphical representation of this issue.

We overcome this issue by adding a rigid alignment with Kabsch algorithm after every step during the inference procedure before xˆnoisyt and xˆdenoisedt are interpolated (see Figure 2 for a visual explanation). Informally, our diffusion interpolation operates on the minimal projection between noisy and denoised structures, guaranteeing, under the assumption of a Dirac distribution, that the interpolated structure is more similar to the denoised sample than the noisy structure. Empirically, we note that this change to the reverse diffusion has a bigger effect when training models on subsets of the full data where the model is more likely to overfit, on the other hand, the final Boltz-1 seems to largely denoising close to the projection making the Kapsch alignment not critical.

Diffusion loss weighting For the weighting of the diffusion loss we use (tˆ2 + σdata2 )/(tˆ× σdata)2 in line with the EDM framework [Karras et al., 2022], rather than (tˆ2+σdata2 )/(tˆ+σdata)2 (AlphaFold3 Section 3.7.1 Eq. 6).

#### 3.3 Confidence model

AlphaFold3 trains the confidence model alongside the trunk and denoising models while, however, cutting all the gradients going from the confidence task to the rest of the model. Instead, training

Recycling

![image 3](Boltz-1 Democratizing Biomolecular Interaction Modeling_images/imageFile3.png)

![image 4](Boltz-1 Democratizing Biomolecular Interaction Modeling_images/imageFile4.png)

![image 5](Boltz-1 Democratizing Biomolecular Interaction Modeling_images/imageFile5.png)

![image 6](Boltz-1 Democratizing Biomolecular Interaction Modeling_images/imageFile6.png)

Atom Attention Encoder

PairFormer Module

MSA Module

Input Sequence

Stop Gradient

###### Trunk

![image 7](Boltz-1 Democratizing Biomolecular Interaction Modeling_images/imageFile7.png)

![image 8](Boltz-1 Democratizing Biomolecular Interaction Modeling_images/imageFile8.png)

Atom Attention Encoder

Confidence Output

PairFormer Module

MSA Module

Input Sequence

###### Confidence Model

Reverse Diffusion

Denoising Model

Denoising Model

Denoising Model

Structure Output

Random Input

Recursive Update

Recursive Update

Recursive Update

- Figure 3: Diagram of the architecture of Boltz-1. The critical difference with AlphaFold3 lies in the confidence model, which now not only has a PairFormerModule but follows a full trunk composition and is fed features coming from the denoising model through the recursive updates.


structure prediction and confidence models separately allowed us to disentangle experiments on each component and make several important improvements to the confidence prediction task.

In AlphaFold3 the architecture of the confidence model is composed of four PairFormer layers that take as input the final single and pair token representations from the model trunk as well as an encoding of the token pairwise distances predicted by the reverse diffusion. These four layers are followed by linear projections trained to predict whether each atom is resolved in the crystal structure, per-atom LDDT and per-token pair PAE and PDE.

Trunk architecture and initialization We noticed that, at a high level, the input-output composition of the confidence model is similar to that of the trunk. The trunk also takes as input its own final representations (through recycling) and outputs expressive representations used by the denoising model. Therefore, inspired by the way that researchers in the large language model community have been training reward models by fine-tuning the “trunk” of their pretrained generative models [Touvron et al., 2023], we define the architecture of our confidence model to contain all the components of the trunk and initialize its representation to the trained trunk weights. Hence, our confidence model presents an AtomAttentionEncoder, an MSAModule, and a PairFormerModule with 48 layers. In addition, we still integrate the predicted conformation as an encoding of the pairwise token distance matrix and decode the confidence with linear layers on the final PairFormer representation.

Diffusion model features We feed to the confidence model not only the representations coming from the trunk but also a learned aggregation of the final token representation at each reverse diffusion step. These representations are aggregated through the reverse diffusion trajectory with a timeconditioned recurrent block and then fed concatenated to the trunk token-level features at the start of the confidence model. We further modify the way that token-level features are fed to the pairwise representations adding an element-wise multiplication of linearly transformed token-level features.

Overall procedure and training We detail our new full inference procedure in Algorithm 1 and provide a schematic representation in Figure 3. To train the confidence model we initialize all the components borrowed by the trunk to the final trunk weights (from the exponentially moving average) and initialize the weights of all the other components of the network randomly but with zeroed final layers not to perturb initial rich representation from the pretrained weights.

Algorithm 1: Confidence model Input: diffusion module activations and timesteps A = [(a1, t1), ... , (aN, tN)]

where N is the number of sampling steps Input: distogram of the predicted token coordinates Di,j Input: trunk features s trunk, z trunk Input: input features feats

// Process diffusion model activations

acc diffusion = 0 for (a, t) in A do

t emb = FourierEmbedding(14log(t/σdata)) t emb = LayerNorm(t emb)

a = LayerNorm(a) acc diffusion += ConditionedTransitionBlock(a, cat(acc diffusion, t emb))

##### end

// Initialize single and pair representation

s inputs = InputFeatureEmbedder(feats) s = LinearNoBias(s inputs) s += LinearNoBias(LayerNorm(s trunk)) s += LinearNoBias(LayerNorm(acc diffusion)) z = LinearNoBias(s inputs[:, :, None]) + LinearNoBias(s inputs[:, None, :]) z += RelativePositionEncoding(feats) z += LinearNoBias(feats[token bonds]) z += LinearNoBias(z trunk) z += LinearNoBias(LinearNoBias(s inputs[:, :, None]) * LinearNoBias(s inputs[:,

None, :])) z += LinearNoBias(one hot(Di,j))

// Update single and pair representation

z += MSAModule(z, s inputs, feats) s, z += PairFormerModule(s, z) s, z = LayerNorm(s), LayerNorm(z)

// Predict confidence metrics

plddt = SoftMax(LayerNoBias(s)) pde = SoftMax(LayerNoBias(z + z⊤)) resolved = SoftMax(LayerNoBias(s)) pae = SoftMax(LayerNoBias(z)) Output: plddt, pde, resolved, pae

#### 3.4 Optimizations

Below we summarize some computational techniques we use to speed up and/or reduce the memory consumption of the model. For details on the implementation of each of these, please refer to our code repository.

Sequence-local atom representation The AtomAttentionEncoder and AtomAttentionDecoder include a pair-biased transformer on the representations of every atom. In particular, the attention of these transformers is sequence-local: blocks of 32 atoms only attend to the 128 atoms that are closest to them in sequence space. We developed a GPU-efficient implementation of the sequence-local attention precomputing a mapping (performed in blocks of 16 tokens) to the key and query sequence embeddings for each 32 key tokens block. The attention is then performed in parallel in each 32x128 block achieving a block sparse attention with dense matrices.

Attention bias sharing and caching At a high level the denoising model must be run repeatedly for every diffusion timestep for every separate sample we take, while the trunk can be run once and its representation fed to all those denoising model passes.

The most expensive components of the denoising model are represented by the computation of the attention pair bias for the token and atom transformers. However, by examining their computational graph, we find that these elements do not depend either on the particular input structure given to the denoising model or the diffusion timestep. In particular, these elements are: the attention bias of all the transformer layers in the AtomAttentionEncoder, AtomAttentionDecoder, and DiffusionTransformer, and the intermediate single and pairwise atom representations of the AtomAttentionEncoder. Therefore, we can also run these components once and share them across all the samples and the entirety of the reverse diffusion trajectory, significantly reducing the computational cost of the reverse diffusion at the cost of storing these representations and biases in memory.

Greedy symmetry correction During validation and confidence model training, the optimal alignment between the ground truth and predicted structure must be determined, accounting for permutations in the order of identical chains or symmetric atoms within those chains. Because the number of possible perturbations grows exponentially with the size of the complex, considering all of them is computationally unfeasible.

We devise the following procedure to perform an approximate, yet effective, atom matching. This operates in a hierarchical way searching (1) the optimal assignment of chains, and, then, (2) assuming chain assignment, to select atom perturbations greedily for every ligand or residue. For the first, for each symmetric chain, we compute the resulting global LDDT without changing any inner atom assignment. For the second step, iteratively for every ligand, amino acid, or nucleotide basis (one at a time), we find the perturbation of that ligand the most improves the global LDDT and greedily apply it.

Note that because the LDDT between pairs of elements that were not affected by the perturbation does not change, one can implement the test in the last step very efficiently only looking at the specific rows and columns of the distance matrix that change. In practice, we limit the number of perturbations of the chain assignment we consider to 100 and the perturbations of the atoms of each ligand to 1000.

Chunking for the MSA Module and Triangular Attention To optimize memory efficiency in our model, we implement a chunking strategy that significantly reduces peak memory usage during inference. We follow the OpenFold chunking implementation for the Triangular Attention layer [Ahdritz et al., 2024], and extend it to the MSA Module, applying it at three critical points: the transition layers, pair-weighted average layers, and outer product layers. This improvement ensures the scalability of our model to larger inputs while maintaining a similar speed.

![image 9](Boltz-1 Democratizing Biomolecular Interaction Modeling_images/imageFile9.png)

- Figure 4: Forwards runtime of trifast kernel compared to compiled PyTorch and DeepSpeed kernel.


Trifast kernel Triangle Self Attention, used in the PairFormer, suffers from O(n3) memory and time complexity. The memory complexity is often the limiting factor with regards to input size, for a given

GPU. At moderate input sizes, it also dominates the runtime. A common solution to the memory issue is applying chunking to the calculation, which is typically done in PyTorch. We implement a Triton kernel that performs the calculation via a chunked online softmax. As such, the memory complexity is improved to O(n2). It also exploits the GPU architecture to speed up the computation for practical input sizes. This is an extension of FlashAttention that allows for the inner bias term [Dao et al., 2022]. A plot of the forwards runtime, compared to compiled PyTorch and another efficient kernel implementation [Song et al., 2023] can be found in Figure 4. The implementation can be found at https://github.com/latkins/trifast.

### 4 Boltz steering

#### 4.1 Introduction

A visual inspection of several predictions from Boltz-1 revealed instances of hallucinations in the model’s outputs. The most prominent type of hallucination involved the placement of entire chains directly on top of one another. Abramson et al. [2024] noted a similar behaviour with AlphaFold3. Moreover, like previous machine learning-based structure prediction methods [Buttenschoen et al., 2024], we observe some non-physical structures predicted by the model. Examples of these behaviours include steric clashes between atoms, slightly incorrect bond lengths and angles, incorrect stereochemistry at chiral centers and stereobonds and aromatic rings predicted to be non-planar. While these issues are not strongly penalized in geometric measures of accuracy of the poses, they can prevent the predictions from being used in many downstream applications, both for expert and computational analyses (e.g. running molecular dynamics calculations). To tackle these issues, we introduce a new inference time steering technique that we refer to as Boltz-steering.

We aim to fix these issues by tilting the distribution defined by the trained diffusion model with a newly defined physics-inspired potential function.

ptarget (x0) ∝ pθ (x0)exp(−λE (x0))

where pθ is the data distribution and E the potential. To sample from this tilted distribution, one approach would be to sample k particles from our diffusion process {x(0i)} ∼ pθ(x0), and subsequently resample them based on their corresponding importance weights {exp(−λE(x(0i)))}. This approach would function similarly to the approach employed by Abramson et al. [2024] in AlphaFold3 where multiple samples of the diffusion model are then filtered based on physical-realism heuristics. However, as noted by Singhal et al. [2025], this approach has drawbacks. First, for constraints that are rarely satisfied by the model, importance sampling or filtering will be unable to bias the model towards the rare conformer that satisfies the constraint.

Related work In the space of biomolecular structures, there have been other works using inference time potentials to guide the diffusion process. RFDiffusion [Watson et al., 2023] computes potentials based on the x0 prediction at each time step and applies a gradient update to encourage specific symmetric protein motifs and inter-chain contacts. Ishitani and Moriwaki [2025] also applies gradient updates to improve ligand structures using an RDKit conformer to define loss functions based on the RMSE between the bond lengths, bond angles, and chiral volumes of the predicted x0 conformer and reference conformer. By contrast, we use a flat-bottom potential based on the distance bounds, to enforce that the potential is within the range of realistic conformers without forcing it to match the RDKit conformer, expand to other physical properties and not only use gradient updates but also resampling. Finally, DecompDiff [Guan et al., 2024] also uses gradient updates in the reverse diffusion to improve the physical quality of generated molecule conformers.

#### 4.2 Method

Boltz-steering takes a different and more effective approach, built on top the Feynmac-Kac (FK) steering framework introduced by Singhal et al. [2025]. We employ potential functions Gt (xT,...,xt)

to tilt the transition kernels of the diffusion process pθ (xt−1 | xt) at each intermediate timestep such that the trajectory is biased towards paths where the eventual x0 will have a low energy - or, equivalently, as described in the initial formulation, a large reward value.

During the steered reverse diffusion process, we begin with a sample from the initial tilted distribution at time t = T

p˜T(xT) ∝ pθ (xT)GT(xT) and at each subsequent timestep t < T, we sample from the tilted transition kernel pθ (xt | xt+1)Gt (xT,...,xt)

We define Gt in terms of the energy difference between the predicted denoised conformer xˆt = fθ(xt,t) at subsequent timesteps.

exp(λ(Et (xˆt+1) − Et (xˆt))) if t < T exp(−λEt (xˆt)) if t = T

Gt (xT,...,xt+1,xt) =

Et is a weighted sum of constraint potentials, each tackling a specific physical issue. For each of these constraint potentials con, is defined as a flat-bottomed energy function Econ(x), such that the energy Econ(x) = 0 for any conformer x that satisfies the constraint and Econ(x) is increasingly positive for conformers that violate the constraint to a greater degree. These potentials are summed to form Et with time-dependent weights as the different physical errors of the model occur at different timescales (e.g. overlapping chains are set at high noise levels, strained bonds at low noise levels).

Directly sampling from the tilted transition kernel is intractable, therefore, the FK steering framework uses Sequential Monte Carlo (SMC) to propose multiple particles at each timeste,p which are then resampled based on their importance weights. For ease of notation, we use τ (xt | xˆt+1,xt+1,t) to denote the sampling algorithm used by Boltz at timestep t, such that the transition distribution of the diffusion model corresponds to

pθ (xt | xt+1) = τ (xt | fθ(xt+1,t + 1),xt+1,t)

We further bias the diffusion trajectory towards low-energy conformers by incorporating guidance. Specifically, we employ backwards universal guidance introduced by Bansal et al. [2023], and define our proposal distribution as

τ (xt−1 | xˆt + ∆xˆt,xt,t) where ∆xˆt is computed by taking m steps of gradient descent with respect to E(xˆt + ∆xˆt) To adapt to these gradient steps we adjust the importance weights to be:

τ xt | xˆ(t+1i) ,x(t+1i) ,t τ xt | xˆt(+1i) + ∆xˆ(t+1i) ,x(t+1i) ,t

Gt x(Ti),...,x(ti)

G(ti) =

However, in practice we incorporate guidance at each time step while only resampling every 3 timesteps to facilitate sufficient exploration. The full Boltz-steering algorithm is presented in Algorithm 2.

#### 4.3 Constraint potentials

We define the overall potential Et as a linear combination of the various constraint potentials. Et(x) = αchiralEtetra(x) + αstereoEstereo(x) + αplanarEplanar(x) + αgeomEgeom(x)+

Eclash(x) + αoverlapEoverlapt (x) + αcovalentEcovalent(x)

+αclash t<t

clash

(1)

The clash potential is only applied for t < tclash. Below we present the formalization of each of the constraint potentials.

Algorithm 2: BOLTZ-STEERING

Initialize ∆xˆ(Ti) ← 0 for i ∈ [k] for t = T,...,1 do

##### if t = T then

Sample x(Ti) ∼ pθ x(Ti) | T else

Sample x(ti) ∼ τ xt | xˆ(t+1i) + ∆xˆ(t+1i) ,x(t+1i) ,t

end Predict xˆ(0i) ← fθ x(ti),t if T − t (mod 3) = 0 then

t|xˆ(ti+1) ,x(ti+1) ,t τ xt|xˆ(ti+1) +∆xˆ(ti+1) ,x(ti+1) ,t

Compute G(i) = τ x

Gt x(Ti),...,x(ti) Resample x(ti) ∼ Multinomial x(tj),G(j)

Initialize ∆xˆ(ti) ← 0 for j = 1,...,m do

∆xˆ(ti) ← ∆xˆ(ti) − ∇E xˆ(ti) + ∆xˆ(ti) end

##### end Output: x(1)0 + ∆xˆ(1)0

Tetrahedral Atom Chirality For a chiral center Z with substituents A, B, C, D in decreasing Cahn-Ingold-Prelog (CIP) priority order, we say that Z has R chirality if the bonds (Z-A, Z-B, Z-C) form a right handed system and S chirality if they form a left handed system. To enforce that the predicted conformers have the correct chirality, we define potentials based on the improper torsion angles (X1, X2, X3, Z).

Echiral(x) =

max

(i,j,k,l)∈SR chiral sets

+

max

(i,j,k,l)∈SS chiral sets

π 6 − DihedralAngle(xi,xj,xk,xl),0

π 6

+ DihedralAngle(xi,xj,xk,xl),0

Bond Stereochemistry For a bond Z1=Z2 where Z1 has substituents A1, B1 and Z2 has substituents A2, B2 in decreasing CIP priority order, we say that Z1=Z2 has E stereochemistry if the higher priority atoms A1 and A2 are on opposite sides of the bond and Z stereochemistry otherwise. To enforce that the predicted conformers have the correct stereochemistry, we define potentials based on the torsion angles (A1, Z1, Z2, A2) and (B1, Z1, Z2, B2).

5π 6 − DihedralAngle(xi,xj,xk,xl),0

Estereo(x) =

max

(i,j,k,l)∈SE stereo sets

π 6

max DihedralAngle(xi,xj,xk,xl) −

+

,0

(i,j,k,l)∈SZ stereo sets

Planar Double Bonds For planar double bonds C1=C2 between carbon atoms where C1 has substituents A1, B1, and C2 has substituents A2, B2, we define a flat bottom potential function to enforce planarity based on the improper torsion angles (A1, B1, C2, C1) and (A2, B2, C1, C2).

π 12

max DihedralAngle(xi,xj,xk,xl) −

Eplanar(x) =

,0

(i,j,k,l)∈Strigonal planar sets

Internal Geometry To ensure that the model generates ligand conformers with a physically realistic distance geometry, we define a flat-bottomed potential based on the bounds matrix which is generated by the RDKit package. For a ligand with N atoms, we define the lower and upper bounds matrices as L,U ∈ RN×N where for a pair of atoms (i, j), the lower and upper distance bounds are given by Li,j, and Ui,j respectively [Buttenschoen et al., 2024]:

max(∥xi − xj∥ − 1.2Uij,0) + max(0.8Lij − ∥xi − xj∥,0)

Egeom(x) =

(i,j)∈Sbonds

max(∥xi − xj∥ − 1.2Uij,0) + max(0.8Lij − ∥xi − xj∥,0)

+

(i,j)∈Sangles

max(∥xi − xj∥ − 1.2Uij,0) + max(0.8Lij − ∥xi − xj∥,0)

+

(i,j)̸∈Sbonds∪Sangles

Steric Clash To prevent steric clashes, we constrain the distance between atoms in distinct and non-bonded chains to be greater than 0.725 times the sum of the atoms’ Van der Waals radii.

max(0.725(ri + rj) − ∥xi − xj∥,0)

Eclash(x) =

(i,j)∈Scross chains

where the Van der Waals radius of atom i is denoted by ri

Overlapping Chains To prevent overlapping chains, we define a time dependent potential based on the distance between the centroids of symmetric chains with more than one atom.

Eoverlapt (x) =

max(bt − ∥x¯A − x¯B∥,0)

(A,B)∈Ssymmetric chains

where x¯A is the centroid of chain A and bt is a time dependent parameter which controls the minimum distance between centroids and smoothly interpolates between 5.0 ˚A at t = 1 and 1.0 ˚A at t = 0 according to the schedule

exp(−2(1 − t)) − 1 exp(−2) − 1

bt = 1 + 4

Covalently Bonded Chains To ensure that the model respects covalently bonded chains, we define a potential to enforce that covalently bonded atoms between separate chains are within 2˚A.

max(∥xi − xj∥ − 2,0)

Ecovalent(x) =

(i,j)∈Scovalent bonds

### 5 Results

We evaluate the performance of the model on two benchmarks: the diverse test set of recent PDB structures that we cured as discussed in Section 2.2, and CASP15, the last community-wide protein structure prediction competition where for the first time RNA and ligand structures were also evaluated [Das et al., 2023, Robin et al., 2023]. Both these benchmarks contain a very diverse set of structures including protein complexes, nucleic acids, and small-molecule, making them great testbeds for the assessment of models, such as Boltz-1, capable of predicting the structure of arbitrary biomolecules.

Benchmarks For CASP15, we extract all the competition targets with the following filters: (1) they were not canceled from the competition, (2) they have an associated PDB id to obtain the ground truth crystal structure, (3) the number of chains in the stochiometry information matches the number of provided chains, (4) the total number of residues with below 2000. This leaves a total of 76 structures. For our test set, we remove structures with covalently bounded ligands because the current version of the Chai-1 public repository does not provide a way to set these. Finally, for both datasets, we remove structures that go out of memory or fail for other reasons for any of the methods on A100 80GB GPUs. After these steps, we are left to evaluate 66 structures for CASP15 and 541 structures for the test set.

Baselines We evaluate our performance against AlphaFold3 [Abramson et al., 2024] and Chai-1 [Chai et al., 2024], current state-of-the-art biomolecular structure prediction models that were released under an exclusive commercial license and do not have training code and pipelines available. We ran the Chai-1 model using the chai lab package version 0.2.1.

All the models were run with 200 sampling steps and 10 recycling rounds, and producing 5 outputs. We also used the same pre-computed MSA’s up to 16384 sequences. Since Chai-1 requires annotating the source of the sequences, we annotated all Uniref sequences with the uniref90 label and all other sequences with the bfd uniclust label. We briefly experimented with alternative labelings but did not find these to impact the model substantially.

Performances on PDB Test with 95% CI (Bootstrap)

| |AF3 oracle<br><br>AF3 top-1<br><br>Chai-1 oracle<br><br>Chai-1 top-1<br><br>Boltz-1 oracle<br><br>Boltz-1 top-1<br><br>Boltz-1x oracle<br><br>Boltz-1x top-1| | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


1.0

0.8

0.6

Value

0.4

0.2

0.0

Mean LDDT DockQ > 0.23 Mean LDDT-PLI L-RMSD < 2A Physical Validity

- Figure 5: Visual summary of the performance of AlphaFold3, Chai-1, Boltz-1 and Boltz-1x on the test set.


Evaluation criteria We consider several well-established metrics to evaluate the performance of the models on these very diverse sets of biomolecules and structures. In particular, we compute:

- 1. The mean all-atom LDDT: measuring accuracy of local structures across all biomolecules;
- 2. The average DockQ success rates, i.e. the proportion of predictions with DockQ > 0.23, which measures the number of good protein-protein interactions predicted;
- 3. The average protein-ligand interface LDDT: measuring the quality of the ligand and pocket predicted interactions, official CASP15 metric to evaluate the ligand category;
- 4. The proportion of ligands with a pocket-aligned RMSD below 2˚A: a widely adopted measure of molecular docking accuracy.


Performances on CASP15 with 95% CI (Bootstrap)

1.0

AF3 oracle

Chai-1 oracle

Boltz-1 oracle

Boltz-1x oracle

AF3 top-1

Chai-1 top-1

Boltz-1 top-1

Boltz-1x top-1

0.8

0.6

Value

0.4

0.2

0.0

Mean LDDT DockQ > 0.23 Mean LDDT-PLI L-RMSD < 2A Physical Validity

- Figure 6: Visual summary of the performance of AlphaFold3, Chai-1, Boltz-1 and Boltz-1x on the CASP15 benchmark.


- 5. The physical quality of the poses generated by the different models by looking at the proportion of poses that pass a set of physical rules from PoseBusters [Buttenschoen et al., 2024]. In particular, we look at:


- (a) Whether ligand bonds are strained by checking if the distances between bonded atoms are within a realistic range determined by RDKit
- (b) Whether ligand angles are strained by checking if the 1-3 distances between atoms are within a realistic range determined by RDKit
- (c) Whether ligand internal clashes are present by checking if the distances between all other pairs of atoms are above a lower bound determined by RDKit
- (d) Whether tetrahedral atom chirality is preserved
- (e) Whether bond stereochemistry is preserved
- (f) Whether inter-chain clashes exist by checking if the distances between atoms in distinct and non-bonded chains with more than one atom are greater than 0.75 times the sum of their Van der Waals radii.


All metrics were computed using OpenStructure [Biasini et al., 2013] version 2.8.0. LDDT-PLI, DockQ and ligand RMSD success rates are computed over all the different protein-protein and protein-ligand interfaces, these proportions are averaged over interfaces within individual complexes and then averaged across complexes containing interfaces. Following a similar format to that used in CASP and to allow a fair comparison of the methods, we run all methods to generate 5 samples and evaluate both the best (oracle) and highest confidence prediction (top-1) out of the 5 for every metric.

To foster further development of methods and the convergence of the field towards well-curated and adopted benchmarks, we publicly release all the inputs, outputs, and evaluations of all the models in our benchmarks as well as the scripts we used to aggregate them. The instructions for downloading them are available on our GitHub repository4.

Results We report the performance of AlphaFold3, Chai-1 and Boltz-1 in Figures 5 and 7. Overall the models show comparable results across the different metrics across both CASP15 and the test set.

4https://github.com/jwohlwend/boltz

![image 10](Boltz-1 Democratizing Biomolecular Interaction Modeling_images/imageFile10.png)

Boltz-1 PDB id: 8GH8 Overlapping DNA chains

Boltz-1x PDB id: 8GH8 Physical DNA chain placement

![image 11](Boltz-1 Democratizing Biomolecular Interaction Modeling_images/imageFile11.png)

![image 12](Boltz-1 Democratizing Biomolecular Interaction Modeling_images/imageFile12.png)

![image 13](Boltz-1 Democratizing Biomolecular Interaction Modeling_images/imageFile13.png)

Boltz-1 PDB id: 8SUT Wrong small molecule chirality

Boltz-1x PDB id: 8SUT Correct small molecule chirality

- Figure 7: Examples of some failure modes of Boltz-1 leading to unphysical poses, on the left, and the fixed poses resulting from Boltz-1x, on the right.


AlphaFold3 has a slight edge over the other models on the mean LDDT metric, which likely derives from better handling complexes containing RNA and DNA thanks to its extra distillation datasets.

For protein-protein interactions, the performance of the methods is also aligned. AlphaFold3 slightly outperforms Boltz-1 and Chai-1 on the test set in terms of proportion of interfaces with DockQ > 0.23, however, all differences are well within the confidence intervals. Similarly, in the proteinligand metrics, AlphaFold3 and Boltz-1 obtain slightly better mean LDDT-PLI and proportion of ligand RMSD < 2˚A than Chai-1, but once again these differences are within the confidence intervals. These results demonstrate, especially in terms of the accuracy of predictions for protein-protein and protein-ligand interactions that Boltz-1 obtains a performance comparable to that of the state-ofthe-art models AlphaFold3 and Chai-1.

When evaluating Boltz-1 on the physical quality tests we see that 57% of top-1 poses do not pass these tests on the test set, suggesting that they likely have severe physical issues. Chai-1 and AlphaFold3 also have relatively low rates of complexes passing all the checks, with respectively around 27% and 58%. On the other hand, Boltz-1x gets 97% of the poses passing the checks, while maintaining a similar level of performance compared to the other models.

In Table 1, we report a number of ablations with respect to the number of recycling steps and diffusion steps. These show a generally monotonic improvement in the performance with more steps, which is relatively plateaued beyond 3 recycling and 50 diffusion steps. Finally, in Figure 1 we present two examples of hard targets from the test set where Boltz-1 performed remarkably well with TM scores around 95%

Table 1: Ablation on the number of recycling rounds and sampling steps for Boltz-1 on the test set. We run the ablation study generating 5 samples and evaluating both the best (oracle) and highest confidence prediction (top-1) out of the 5 for every metric. All models used pre-computed MSAs with up to 4,096 sequences. It is worth noting that the metrics are noisy, so minor inconsistencies (e.g., lack of improvement with increased recycling rounds or diffusion steps) should not be overinterpreted. Moreover, there is a slight difference with the results in Figures 5 and 7 due to differences in MSA parameters as well as the set of structures passing all ablations.

Mean LDDT DockQ > 0.23 Mean LDDT-PLI L-RMSD < 2˚A # rec. # steps oracle top-1 oracle top-1 oracle top-1 oracle top-1

3 200 0.729 0.716 0.654 0.625 0.621 0.580 0.581 0.545

- 0 200 0.698 0.681 0.579 0.544 0.573 0.530 0.582 0.541

- 1 200 0.718 0.702 0.656 0.635 0.623 0.573 0.588 0.535

- 2 200 0.726 0.710 0.651 0.632 0.616 0.581 0.587 0.546

- 3 200 0.729 0.716 0.654 0.625 0.621 0.580 0.581 0.545 6 200 0.732 0.714 0.644 0.635 0.630 0.593 0.595 0.555 8 200 0.733 0.717 0.644 0.633 0.630 0.584 0.588 0.545


10 200 0.735 0.720 0.644 0.631 0.619 0.577 0.575 0.541

3 20 0.720 0.693 0.615 0.592 0.577 0.547 0.550 0.532 3 50 0.727 0.710 0.645 0.627 0.621 0.579 0.586 0.540 3 200 0.729 0.716 0.654 0.625 0.621 0.580 0.581 0.545

### 6 Conclusion

We introduced Boltz-1, the first fully commercially accessible open-source model to achieve AlphaFold3-level accuracy in predicting the 3D structures of biomolecular complexes. To accomplish this, we replicated and expanded upon the AlphaFold3 technical report, incorporating several innovations in architecture, data curation, training, and inference processes. We empirically validated Boltz-1 against AlphaFold3 and Chai-1, the current state-of-the-art structure prediction methods, demonstrating comparable performance on both a diverse test set and the CASP15 benchmark.

Further, we introduced Boltz-1x an updated model that leverages Boltz-steering, a new inference time technique, to significantly improve the physical quality of the poses generated while maintaining their geometric accuracy of Boltz-1.

The open-source releases of Boltz-1 and Boltz-1x represent significant steps forward in democratizing access to advanced biomolecular modeling tools and improving their applicability across domains. By freely providing the training and inference code, model weights, and datasets under the MIT license, we aim to enable researchers and organizations to experiment and innovate using Boltz-1 and Boltz-1x. We envision Boltz models as a foundational platform for researchers to build upon, fostering collaboration to advance our collective understanding of biomolecular interactions and accelerating breakthroughs in drug design, structural biology, and beyond.

### 7 Acknowledgments

We would like to thank Sergey Ovchinnikov, Bowen Jing, Hannes Stark, Jason Yim, Peter Mikhael, Richard Qi, Wengong Jin, Rohith Krishna, Evan Feinberg, and Maruan Al-Shedivat for the invaluable discussions and help. We also thank the research community for all the feedback we received, that has helped us improve the usability of the model, understand its limitations, and help inform improvements that we are doing for future versions of the model.

Large portions of the GPU resources necessary to complete the project were provided by Genesis Therapeutics and the US Department of Energy. For the latter, we acknowledge our use of the National Energy Research Scientific Computing Center (NERSC), a Department of Energy Office of Science User Facility, via NERSC award GenAI@NERSC. This work was also supported by the NSF Expeditions grant (award 1918839: Collaborative Research: Understanding the World Through Code), the Abdul

###### Latif Jameel Clinic for Machine Learning in Health, the DTRA Discovery of Medical Countermeasures Against New and Emerging (DOMANE) Threats program, and the MATCHMAKERS project supported by the Cancer Grand Challenges partnership financed by CRUK (CGCATF-2023/100001) and the National Cancer Institute (OT2CA297463).

- Algorithm 3: Dense MSA Pairing Input: query complex C = [(sequence, chain id), ...] Input: unpaired MSAs M = [(sequence, chain id, taxonomy id), ...] // Add original sequence orig pairing, orig is paired = {}, {} for (sequence, chain id) in C do


orig pairing[chain id] = sequence orig is paired[chain id] = 1

end pairing, is paired = [orig pairing], [orig is paired]

// Sort and filter taxonomies

Group entries in M by taxonomy id Sort taxonomies by the number of unique chain id in its entries (descending) Filter all taxonomies equal to null or with a single unique chain id in its entries Store all entries outside the new taxonomy list in an available queue grouped by chain id

// Add paired MSAs

for taxonomy id in taxonomies do Group taxonomy id entries by chain id for i = 0 to the maximum number of entries per chain id do

row pairing, row is paired = {}, {}

// Add the chains present in the taxonomy

for (chain id, sequences) in taxonomy id entries do

row pairing[chain id] = sequences[i mod len(sequences)] row is paired[chain id] = 1

##### end

// Fill any missing chains with unpaired MSAs

for chain id in orig pairing but not row pairing do

row pairing[chain id] = available[chain id].pop(default=empty) row is paired[chain id] = 0

end Append row pairing to pairing Append row is paired to is paired Break if we have finished the rows

end end

// Fill MSA with remaining unpaired MSAs

while MSA not fill and available is not empty do row pairing, row is paired = {}, {} for chain id in orig pairing do

row pairing[chain id] = available[chain id].pop(default=empty) row is paired[chain id] = 0

end Append row pairing to pairing Append row is paired to is paired

end Output: pairing, is paired

- Algorithm 4: Unified Cropping Input: max tokens, max atoms and neighborhood sizes = [0, 2, ..., 40] Input: Token list tokens and sampled chain id or interface id Sample neighborhood size uniformly at random from neighborhood sizes. Sample center token uniformly within the tokens in the chain chain id or interface


interface id. Sort tokens by ascending the distance of their center atom to that of center token. Let cropped tokens be an empty set for token in tokens do

Let chain tokens be the entries in tokens with the same asym id of token. if len(chain tokens) ≤ neighborhood size then

selected tokens = chain tokens else

Let selected tokens be the entries in chain tokens with the same res idx of token.

// Expand the neighborhood until we have enough tokens.

min idx = max idx = token["res idx"] while len(selected tokens) < neighborhood size do

min idx = min idx - 1 max idx = max idx + 1 Let selected tokens be the entries in chain tokens with res idx ∈ [min idx,

max id]. end

##### end

// Compute new tokens and new atoms.

Let new tokens be the entries in selected tokens not present in cropped tokens. if adding new tokens to cropped tokens would exceed max tokens or max atoms limits

##### then

Break the for loop else

Add new tokens to cropped tokens. end

end Output: cropped tokens

- Algorithm 5: Robust pocket-conditioning // Pocket featurization step at training time Input: pocket conditioned prop = 0.3, pocket cutoff = 6˚A, pocket geometric p = 0.3 Input: tokens: list of cropped tokens for token in tokens do


token["pocket feature"] = "UNSPECIFIED"

end if r U[0,1], r < pocket conditioned prop then

// Choose as binder a random ligand in the crop, if there are no ligands select a chain

Let binder asym ids be the list of all unique ligand asym id. If binder asym ids is empty make it all unique asym id. Select binder asym id randomly from binder asym ids. For all tokens find the shortest distance of any of its resolved atoms to a resolved atom

with binder asym id. Let pocket tokens be all the tokens with asym id different from binder asym id and the

shortest distance below pocket cutoff. if pocket tokens is not empty then

N = min(len(pocket tokens), 1 + M) where

P(M = k) = (1 − pocket geometric p)k−1 ∗ pocket geometric p Sample N tokens from pocket tokens to form subset pocket tokens for token in tokens do

if token["asym id"] equals binder asym id then

token["pocket feature"] = "BINDER"

else if token in subset pocket tokens then

token["pocket feature"] = "POCKET" else

token["pocket feature"] = "UNSELECTED" end

end Output: tokens

### References

Josh Abramson, Jonas Adler, Jack Dunger, Richard Evans, Tim Green, Alexander Pritzel, Olaf Ronneberger, Lindsay Willmore, Andrew J Ballard, Joshua Bambrick, et al. Accurate structure prediction of biomolecular interactions with alphafold 3. Nature, pages 1–3, 2024.

Gustaf Ahdritz, Nazim Bouatta, Christina Floristean, Sachin Kadyan, Qinghui Xia, William Gerecke, Timothy J O’Donnell, Daniel Berenberg, Ian Fisk, Niccol`o Zanichelli, et al. Openfold: Retraining alphafold2 yields new insights into its learning mechanisms and capacity for generalization. Nature Methods, pages 1–11, 2024.

Arpit Bansal, Hong-Min Chu, Avi Schwarzschild, Soumyadip Sengupta, Micah Goldblum, Jonas Geiping, and Tom Goldstein. Universal guidance for diffusion models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 843–852, 2023.

Helen M Berman, John Westbrook, Zukang Feng, Gary Gilliland, Talapady N Bhat, Helge Weissig, Ilya N Shindyalov, and Philip E Bourne. The protein data bank. Nucleic acids research, 28(1): 235–242, 2000.

Marco Biasini, Tobias Schmidt, Stefan Bienert, Valerio Mariani, Gabriel Studer, Ju¨rgen Haas, Niklaus Johner, Andreas Daniel Schenk, Ansgar Philippsen, and Torsten Schwede. Openstructure: an integrated software framework for computational structural biology. Acta Crystallographica Section D: Biological Crystallography, 69(5):701–709, 2013.

Martin Buttenschoen, Garrett M Morris, and Charlotte M Deane. Posebusters: Ai-based docking methods fail to generate physically valid poses or generalise to novel sequences. Chemical Science, 15(9):3130–3139, 2024.

Discovery Chai, Jacques Boitreaud, Jack Dent, Matthew McPartlon, Joshua Meier, Vinicius Reis, Alex Rogozhnikov, and Kevin Wu. Chai-1: Decoding the molecular interactions of life. bioRxiv, pages 2024–10, 2024.

UniProt Consortium. Uniprot: a hub for protein information. Nucleic acids research, 43(D1):D204– D212, 2015.

Gabriele Corso, Hannes St¨ark, Bowen Jing, Regina Barzilay, and Tommi Jaakkola. Diffdock: Diffusion steps, twists, and turns for molecular docking. arXiv preprint arXiv:2210.01776, 2022.

Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher R´e. FlashAttention: Fast and memory-efficient exact attention with IO-awareness. In Advances in Neural Information Processing Systems (NeurIPS), 2022.

Rhiju Das, Rachael C Kretsch, Adam J Simpkin, Thomas Mulvaney, Phillip Pham, Ramya Rangan, Fan Bu, Ronan M Keegan, Maya Topf, Daniel J Rigden, et al. Assessment of three-dimensional rna structure prediction in casp15. Proteins: Structure, Function, and Bioinformatics, 91(12):1747– 1770, 2023.

Jiaqi Guan, Xiangxin Zhou, Yuwei Yang, Yu Bao, Jian Peng, Jianzhu Ma, Qiang Liu, Liang Wang, and Quanquan Gu. Decompdiff: diffusion models with decomposed priors for structure-based drug design. arXiv preprint arXiv:2403.07902, 2024.

Maria Hauser, Martin Steinegger, and Johannes S¨oding. Mmseqs software suite for fast and deep clustering and searching of large protein sequence sets. Bioinformatics, 32(9):1323–1330, 2016.

Ryuichiro Ishitani and Yoshitaka Moriwaki. Improving stereochemical limitations in protein-ligand complex structure prediction. bioRxiv, pages 2025–03, 2025.

John Jumper, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov, Olaf Ronneberger, Kathryn Tunyasuvunakool, Russ Bates, Augustin Zı´dek,ˇ Anna Potapenko, et al. Highly accurate protein structure prediction with alphafold. nature, 596(7873):583–589, 2021.

Tero Karras, Miika Aittala, Timo Aila, and Samuli Laine. Elucidating the design space of diffusionbased generative models. Advances in neural information processing systems, 35:26565–26577, 2022.

Milot Mirdita, Konstantin Sch¨utze, Yoshitaka Moriwaki, Lim Heo, Sergey Ovchinnikov, and Martin Steinegger. Colabfold: making protein folding accessible to all. Nature methods, 19(6):679–682, 2022.

Xavier Robin, Gabriel Studer, Janani Durairaj, Jerome Eberhardt, Torsten Schwede, and W Patrick Walters. Assessment of protein–ligand complexes in casp15. Proteins: Structure, Function, and Bioinformatics, 91(12):1811–1821, 2023.

Raghav Singhal, Zachary Horvitz, Ryan Teehan, Mengye Ren, Zhou Yu, Kathleen McKeown, and Rajesh Ranganath. A general framework for inference-time scaling and steering of diffusion models. arXiv preprint arXiv:2501.06848, 2025.

Shuaiwen Leon Song, Bonnie Kruft, Minjia Zhang, Conglong Li, Shiyang Chen, Chengming Zhang, Masahiro Tanaka, Xiaoxia Wu, Jeff Rasley, Ammar Ahmad Awan, et al. Deepspeed4science initiative: Enabling large-scale scientific discovery through sophisticated ai system technologies. arXiv preprint arXiv:2310.04610, 2023.

Martin Steinegger and Johannes S¨oding. Mmseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature biotechnology, 35(11):1026–1028, 2017.

Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288, 2023.

Shuzhe Wang, Kajo Krummenacher, Gregory A Landrum, Benjamin D Sellers, Paola Di Lello, Sarah J Robinson, Bryan Martin, Jeffrey K Holden, Jeffrey YK Tom, Anastasia C Murthy, et al. Incorporating noe-derived distances in conformer generation of cyclic peptides with distance geometry. Journal of Chemical Information and Modeling, 62(3):472–485, 2022.

Joseph L Watson, David Juergens, Nathaniel R Bennett, Brian L Trippe, Jason Yim, Helen E Eisenach, Woody Ahern, Andrew J Borst, Robert J Ragotte, Lukas F Milles, et al. De novo design of protein structure and function with rfdiffusion. Nature, 620(7976):1089–1100, 2023.

