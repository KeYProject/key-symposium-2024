---
author: "Philipp Kern"
kind: "Regular Talk (20 min. + 10 min.)"
track: "Common Track, KeY-only Track"
title: "Towards Precise Linear Relaxations for Verification of LSTMs"
length: 30
slot: 32
order: 104
---

Verification of neural networks is essential for their deployment in
safety-critical applications. While most verification approaches target
ReLU networks, the activation functions used in Long Short-Term Memory
(LSTM) networks, crucial for sequence and time series data, still pose
significant challenges.

Existing approaches for verification of LSTMs neglect dependencies
between input variables, when computing linear relaxations of their
activation functions.

In this talk, I am going to present ongoing work for enhancing the
precision of the linear relaxations by leveraging zonotopes to capture
such input dependencies.


