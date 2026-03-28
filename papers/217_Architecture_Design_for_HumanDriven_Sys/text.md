# Architecture Design for Human-Driven Systems

Mahyar T. Moghaddam∗, Moamin B. Abughazala†, Vittorio Cortellessa†, Antinisca Di Marco†, Henry Muccini†, Fabrizio Rossi†, Karthik Vaidhyanathan† ∗MMMI Institute, University of Southern Denmark, Odense, Denmark †DISIM Department, University of L’Aquila, L’Aquila, Italy

arXiv:2109.10073v1[cs.SE]21 Sep 2021

Abstract—This paper highlights humans’ social and mobility behaviors’ role in the continuous engineering of sustainable sociotechnical systems. Our approach relates the humans’ characteristics and intentions with the system’s goals, and models such interaction. Such a modeling approach aligns the architectural design and associated quality of service (QoS) with humans’ quality of experience (QoE). We design a simulation environment that combines agent-based social simulation (ABSS) with architectural models generated through a model-driven engineering approach. Our modeling approach facilitates choosing the best architectural model and system conﬁguration to enhance both the humans’ and system’s sustainability. We apply our approach to the Ufﬁzi Galleries crowd management system. Taking advantage of real data, we model different scenarios that impact QoE. We then assess various architectural models with different SW/HW conﬁgurations to propose the optimal model based on different scenarios concerning QoS-QoE requirements.

Index Terms—Software Architecture, Agent-based Modeling, Human Behavior, Sustainability, Quality of Experience, Quality of Service.

I. INTRODUCTION

Architectural design decisions are historically driven by technical reasoning and concerns. More recently, other aspects such as business value and sustainability. The growing importance of sustainable development is highlighting additional concerns regarding social, individual, economics, and environmental interlinked with technical dimensions [1]. Literature on sustainable software development generally focuses on environmental aspects; still, little attention is dedicated to social and individual human sustainability. In this paper, we propose a human-oriented architecture design approach for socio-technical systems. We analyze how the understanding of human behavior may drive the selection of different and alternative architectural models [2] and conﬁgurations, with the objective of minimizing energy consumption. In order to do so, we present a comprehensive approach comprising: i) an agent-based modeling (ABM) to model humans behavior, ii) an ABM and model-driven engineering integration engine, iii) a simulation environment (fed by real data) that simulates human behavior with respect to Internet of Tings (IoT) resources, iv) the application on the Ufﬁzi Galleries crowd management system.

mtmo@mmmi.sdu.dk moamin.abughazala@graduate.univaq.it vittorio.cortellessa@univaq.it antinisca.dimarco@univaq.it henry.muccini@univaq.it fabrizio.rossi@univaq.it karthik.vaidhyanathan@univaq.it

The paper is organized as follows. Background is presented in Section II. Our agent-based and architectural modeling methodologies are presented in Section III. The method is applied to a real case study in Section IV, and the conclusions are ﬁnally drawn in Section V.

II. BACKGROUND

In agent-based modeling (ABM), the environment and what is included in it are modeled as agents [3]. Each agent has a set of characteristics and behaviors. For simulation of human behavior, agent-based social simulations (ABSS) are generally used. In ABSS, an agent is deﬁned as an autonomous software entity that can act upon and perceive its environment. When agents are put together, they form an artiﬁcial society, each perceiving, moving, performing actions, communicating, and transforming the local environment, much like human beings in real society. In this paper, we use PedSim 1 to simulate IoT environment and moving agents. Modeling the IoT system’s architecture implies considering the IoT components, their interactions, the underlying hardware conﬁgurations of the different IoT components, as well as constraints from the environment in which these IoT components will be deployed. To this end, we use our CAPS modeling framework2 [4] to provide a multi-view (software, hardware, physical space) approach. In this work, we use CupCarbon, a state-of-the-art smart city IoT simulator3, widely used in research, especially for energy and data simulation of IoT systems.

III. METHODOLOGY

This section presents the methodology that links ABM and ABSS with IoT architectural modeling and simulation, thereby allowing architects to analyze the models and design an optimal architecture with respect to QoS and QoE requirements. Our methodology consists of four stages: i) Agent Modeling and Simulation stage that deals with the modeling and simulation of different agents using the ABM and ABSS approaches. The agent-based model for IoT socio-technical systems consists of four classes of agents: humans, cyber elements, physical space, and IoT resources which all are part of the environment class. ii) Agent-IoT composition stage receives the results of the agent-based simulations to generate the data required for the IoT simulation. This step consists of a single process, namely, Agent IoT Data Composition (AIDC).

- 1https://www.pedsim.net/
- 2http://caps.disim.univaq.it/
- 3http://cupcarbon.com/


iii) IoT modeling and simulation stage involves modeling and simulation of different architectural models and conﬁgurations based on the data received from the agent-IoT composition step. iv) Analysis stage processes the IoT simulation results by taking into account the QoS/QoE goals (which can be speciﬁed by stakeholders). It then identiﬁes the optimal architectural model and conﬁguration for a given agent behavior. It achieves this with the help of a utility metric, namely trade-off score, ts = ws ∗ Qs + we ∗ Qe; where ws and we represents the weights given to QoS and QoE goals respectively and Qs and Qe are piece-wise functions that captures the satisfaction of QoS and QoE goals respectively.

IV. RESULTS

We applied our approach on Ufﬁzi Gallery crowed management, the most visited museums in Florence, Italy [5]. In our agent-based model (ABM) of the Ufﬁzi galleries, we set the simulation parameters either by real data gathered or according to the literature. We considered two scenarios. In the ﬁrst scenario we used the Ufﬁzi historical data to assign different characteristics to human agents regarding age, gender, origin, and physical condition. In the second scenario we modeled social attachment and grouping in Ufﬁzi to assess its impact on QoE and QoS. Getting input from the ABSS, we modeled the IoT architecture of the Ufﬁzi case study using the CAPS modeling framework. In the Ufﬁzi museum, IoT devices need to be deployed in the entrance, exits, and corridors to monitor the movement of humans into, outside of, and within the museum. The IoT device’s choice can impact the overall QoS and QoE offered by the system. To deﬁne the conﬁguration of the IoT components in the models, we use the concept of modes provided by CAPS. Every IoT component operates in two modes, i) normal mode when the sensor reads/sends data at a lower frequency; ii) critical mode where the sensor reads/sensor at a higher frequency due to some critical condition (high queuing). However, the choice of the frequency in either mode can impact the QoS and QoE. We performed 36 simulations (6 models × 3 conﬁgurations × 2 scenarios). Each simulation was performed for a total time of 2 hours in a Windows-based desktop machine running on an Intel i7, 2.6-3.2 GHz processor with 16 Gb RAM. We analyze the results to identify the optimal architectural model and conﬁguration for the two scenarios modeled by ABSS.

Regarding Scenario 1 (Congestion), we calculate the tradeoff score (ts) by giving more weight to QoE. We set the goals such that we want the system to consume not more than 100 joules and the server to capture the movement of at least 1200 people every 15 minutes. Our simulations show that using 1 counter in the entrance, 3 counters in exit, and a mix of 5 cameras and 4 RFID in corridors provides the highest ts. In the mentioned conﬁguration, in normal and critical modes, cameras and RFID readers send packets with a frequency of 30 and 10 per second, and people counters send them by a frequency of 10 and 1, respectively. This conﬁguration gives more preference to QoE without compromising too much on the QoS. In scenario 2, we calculated the trade-off score, ts

for each of the model conﬁguration pairs, with the goal of consuming no more than 150 joules and the server to capture the movement of at least 800 people every 15 minutes. We observed that as opposed to Scenario 1, using 1 QR Reader in the entrance, 3 Counters in exit and 9 RFID in corridors provides the highest ts. In the mentioned conﬁguration, in normal and critical modes, QR Reader sends packets with a frequency of 20 and 5, RFID sends them with a frequency of 40 and 20, and counters send them with a frequency of 20 and 5. The above evaluations indicate how our approach could allow architects to model the expected human behavior and select the appropriate architectural models and conﬁgurations to optimize the overall QoS/QoE (or a combination) offered by the system. Moreover, our approach provides architects with a set of models and conﬁgurations to handle different human behavioral scenarios.

V. CONCLUSION

In this work, we demonstrated that using a human-oriented approach can allow software architects to better design sociotechnical systems. It achieves this with the help of a modeldriven approach which enables architects to model the expected behaviors of humans, the architecture of the IoT system and further provides mechanisms to simulate and perform trade-off analysis of different design alternatives with respect to QoE and QoS requirements. Our evaluation on a real case study shows that our approach can allow architects to select optimal architectural models and conﬁgurations by considering the expected human behavior. We plan to evolve this approach into a tool that can be used by software architects to better design socio-technical systems.

ACKNOWLEDGMENT

We acknowledge the support given by the Ufﬁzi Galleries and its director Dr. Eike Schmidt. This research is supported by the VASARI PON R&I 2014-2020 and FSC project.

REFERENCES

- [1] Christoph Becker, Ruzanna Chitchyan, Leticia Duboc, Steve Easterbrook, Birgit Penzenstadler, Norbert Seyff, and Colin C Venters. Sustainability design and software: The karlskrona manifesto. In 2015 IEEE/ACM 37th IEEE International Conference on Software Engineering, volume 2, pages 467–476. IEEE, 2015.
- [2] Henry Muccini and Mahyar Tourchi Moghaddam. Iot architectural styles. In European Conference on Software Architecture, pages 68–85. Springer, 2018.
- [3] Julie Dugdale, Mahyar T Moghaddam, and Henry Muccini. Agent-based simulation for iot facilitated building evacuation. In 2019 International Conference on Information and Communication Technologies for Disaster Management (ICT-DM), pages 1–8. IEEE, 2019.
- [4] H. Muccini and M. Sharaf. Caps: Architecture description of situational aware cyber physical systems. In 2017 IEEE International Conference on Software Architecture (ICSA), pages 211–220, April 2017.
- [5] Julie Dugdale, Mahyar T Moghaddam, and Henry Muccini. Human behaviour centered design: developing a software system for cultural heritage. In Proceedings of the ACM/IEEE 42nd International Conference on Software Engineering: Software Engineering in Society, pages 85–94, 2020.


This figure "fig1.png" is available in "png"  format from:

http://arxiv.org/ps/2109.10073v1

