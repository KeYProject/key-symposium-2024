---
author: "Lukas Grätz"
kind: "Regular Talk (20 min. + 10 min.)"
track: "Common Track"
title: "Single Path Verification for Validation or Debugging"
slot: 14
length: 30
order: 62
---


More than 15 years ago, a paper "Better bug reporting with better privacy" solved the two problems of automatic bug reports: Specifically, memory dumps might not be sufficient to reconstruct an issue/crash while leaking private information.

In this talk, we will follow a related approach with improved overhead and portability: Our tool instruments the source code to record (with low overhead) a compressed control flow trace, which can be directly added to a bug-report. The trace format is designed to be adaptable to different programming languages.

In the second part, we see what a developer can do with these traces apart from visualizing in the source code: We use symbolic execution to retrace (partial program run reconstruction), to inspect variable values and to check against specifications/assertions. Our current implementation works on top of either KeY, CBMC or angr.

We also see how to record a trace with KeY, useful for debugging a KeY-proof and restricting it to a single control flow (and then retrying, i.e., with different proof strategy settings).
