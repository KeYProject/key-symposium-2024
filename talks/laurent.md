---
author: "Jonathan Laurent"
kind: "Regular Talk (20 min. + 10 min.)"
track: "Common Track"
title: "Oracular Programming"
length: 25
slot: 18
order: 74
---

Large Language Models have proved surprisingly effective at solving a wide range of tasks from just a handful of examples. However, their lack of reliability limits their capacity to tackle large problems that require many steps of reasoning. In response, researchers have proposed advanced pipelines that leverage domain-specific knowledge to chain smaller prompts, provide intermediate feedback and improve performance through search. However, the current complexity of writing, debugging, tuning and maintaining such pipelines has put a bound on their sophistication.

We propose a new paradigm for programming with LLMs called _oracular programming_. In this paradigm, domain experts are invited to define high-level problem-solving strategies as nondeterministic programs. Such programs are reified into infinite search trees for LLM oracles to navigate. A separate _demonstration language_ allows annotating choice points with examples, while keeping them grounded and synchronized as the associated program evolves.

In this talk, we motivate and explain the key concepts of oracular programming. We introduce Delphyne, a framework for oracular programming based on Python, and discuss the associated tooling. We demonstrate our prototype on a preliminary invariant-synthesis case study. We hope that our proposed framework can foster research on intersymbolic AI and facilitate creative combinations of LLMs with symbolic provers.
