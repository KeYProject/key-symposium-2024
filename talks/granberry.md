---
author: "George Granberry"
kind: "Regular Talk (20 min. + 10 min.)"
track: "KeY-only Track"
title: "Specify What? Enhancing Neural Specification Synthesis by Symbolic Methods"
length: 25
slot: 17
---

We investigate how combinations of Large Language Models (LLMs) and symbolic analyses can be used to synthesise specifications of C programs. The LLM prompts are augmented with outputs from two formal methods tools in the Frama-C ecosystem, Pathcrawler and EVA, to produce C program annotations in the specification language ACSL. We demonstrate how the addition of symbolic analysis to the workflow impacts the quality of annotations: information about input/output examples from Pathcrawler produce more context-aware annotations, while the inclusion of EVA reports yields annotations more attuned to runtime errors. In addition, we show that the method infers rather the programs intent than its behaviour, by generating specifications for buggy programs and observing robustness of the result against bugs.
