---
author: "Jonathan Laurent"
kind: "Regular Talk (20 min. + 10 min.)"
track: "Common Track"
title: "[Temporary Title] Few-Shot Programming: a new paradigm for programming with large language models"
length: 30
slot: 18
---

[Temporary abstract] Large-language models such as GPT4 have proved surprisingly good at solving a wide range of tasks from a handful of examples and at generating structured data such as programs or mathematical formulas. Yet, their lack of reliability puts a limit on their ability to solve large problems that require many steps of reasoning.

Our work proposes a new programming paradigm called “few-shot programming”, where domain ex- perts write high-level problem-solving strategies in the form of nondeterministic programs whose choice-points are annotated with examples. This induces a search space that can be explored by querying large-language models for guidance. In addition, once enough examples are provided by humans for a strategy to bootstrap, this strategy can self-improve via an AlphaZero-like scheme, by solving a series of problems with search and extracting annotations from successful solutions.

In this talk, we’ll introduce the “few-shot programming“ paradigm and demonstrate an early implementation prototype on an invariant-synthesis case study.
