---
author: "Eduard Kamburjan"
kind: "Regular Talk (20 min. + 10 min.)"
track: "KeY-only Track"
title: "Multi-perspective correctness of programs"
length: 30
slot: 116
order: 30
---

Programs must be correct with respect to their application domain. Yet, current the program specification and verification approaches only consider correctness in terms of computations.
In this work, we present a Hoare Logic that manages two different perspectives on a program during a correctness proof: the computational view and the domain view.
This enables to not only specify the correctness of a program in terms of the domain without referring to the computational details, but also enables to interpret failed proof attempts in the domain.
For domain specification, we illustrate the use of description logics and base our approach on semantic lifting, a recently proposed approach to interpret a program as a knowledge graph.
We present a calculus that uses translations between both kinds of assertions, thus separating the concerns in specification, but enabling the use of description logic in verification.
