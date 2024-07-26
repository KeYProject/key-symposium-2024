---
author: "Lukas Grätz"
kind: "Regular Talk (20 min. + 10 min.)"
track: "Common Track"
title: "Single Path Verification for Validation or Debugging"
slot: 14
length: 30
order: 62
---

More than 15 years ago, a paper ""Better bug reporting with better privacy"" solved the two problems of automatic bug reports: Specifically, memory dumps might not be sufficient to reconstruct an issue/crash while leaking private information. However, their approach of generating new input-data had limited applicability.

Our tool instruments the source code to record (with low overhead) a compressed control flow trace, which can be directly added to a bug-report (instead of input-data or memory dumps). The trace format is designed to be adaptable to different programming languages.

In the second part, these traces are used not only by visualizing the control-flow in the code: On the developers side, we can debug a trace using symbolic execution (we call that retracing). Our current implementation works on top of either KeY, CBMC or angr.

We also see how to record a trace with KeY and how to restrict symbolic execution (or a part of it) to a single control flow, to avoid loop invariants and path explosion.
