---
author: "Tabea Bordis"
kind: "Either Regular or Short. Whatever fits best into the program."
track: "Common Track"
title: "Free Facts: An Alternative to Inefficient Axioms in Dafny"
slot:  15
length: 30
order: 63
---

Formal software verification relies on properties of functions and built-in operators. Unless these properties are handled directly by decision procedures, an automated verifier includes them in verification conditions by supplying them as universally quantified axioms or theorems. The use of quantifiers sometimes leads to bad performance, especially if automation causes the quantifiers to be instantiated many times.

In this presentation, I will talk about free facts as an alternative to some axioms. A free fact is a pre-instantiated axiom that is generated alongside the formulas in a verification condition that can benefit from the facts. Replacing an axiom with free facts thus reduces the number of quantifiers in verification conditions. Free facts are statically triggered by syntactic occurrences of certain patterns in the proof terms. This is less powerful than the dynamically triggered patterns used during proof construction. However, we found that free facts perform well in practice.
