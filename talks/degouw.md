---
author: "Stijn de Gouw"
kind: "Regular Talk (20 min. + 10 min.)"
track: "Common Track, KeY-only Track"
title: "Analyzing OpenJDK's BitSet"
slot: 117
length: 30 
---

We analyse OpenJDK's BitSet class with a combination of formal specification, testing and preliminary verification. The BitSet class represents a vector of bits that grows as required. During our analysis, we uncovered a number of bugs. We propose and compare various solutions, supported by our formal specification. Until a solution is chosen for the discovered problems, the source code is not (sufficiently) fixed to allow full mechanical verification in KeY of the class. But we do show initial steps taken towards verification, discuss our experience and identify necessary extensions (particularly for bitwise operations) required to make a complete proof possible once the source code is stable.
