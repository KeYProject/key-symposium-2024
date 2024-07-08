---
author: "Floran Lanzinger"
kind: "Regular Talk (20 min. + 10 min.)"
track: "Common Track, KeY-only Track"
title: "Types as Contracts: Scalable and Precise Verification"
length: 30
slot: 114
---

Refinement type systems allow programmers to use logical conditions to constrain admissible values of variables. However, most practical refinement type systems limit the expressiveness in the logic to remain automatically decidable and easy to use. Deductive verification tools, on the other hand, often come with expressive specification languages and powerful proof calculi that require interaction and scale badly with the program size.

We introduce Kukicha, a refinement type system framework for Java that enables the interoperation of efficient type checking and deductive program verification. Kukicha combines refinement types with uniqueness types to track aliasing and packing types to track temporary violations. The use of a packing mechanism in combination with deductive verification allows Kukicha to be more expressive than similar type systems. Kukicha first performs an efficient syntactic well-typedness check. If this does not succeed, it emits a translated program where type annotations are replaced JML by specifications that can be proven in KeY.
