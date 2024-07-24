---
author: "Bernhard Beckert"
kind: "Regular Talk (20 min. + 10 min.)"
track: "Common Track, KeY-only Track"
title: "Towards Combining the Cognitive Abilities of Large Language Models with the Rigor of Deductive Progam Verification"
slot: 199
length: 15
order: 76
---

Recent investigations hint at the ability of large language models (LLMs) to generate formal specifications for given program code. We present preliminary quantitative experiments on the capabilities of LLMs to generate correct specifications. To this end, we use a prototypical integration of GPT (versions 3.5 and 4o) with the deductive program verifier KeY and the bounded model checker JJBMC. We evaluated our prototype on a set of Java programs that are partially annotated with specifications written in the Java Modeling Language (JML). We show that GPT 4o generates correct annotations in approximately half of all instances across the investigated scenarios. For the case of faulty specifications, we investigate how a feed-back loop can help to improve the original answer. Finally, we present a vision of how Large Language Models may support rigorous formal verification of software systems and describe the necessary next steps in this direction.

