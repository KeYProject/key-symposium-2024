---
author: "Aditi Kabra"
kind: "Short Talk (10 min. + 5 min.)"
track: "KeYmaera Track"
title: "Control Envelope Synthesis for KeYmaera X"
slot: 214
length: 30
order: 38
---

This talk presents an approach for synthesizing provably correct control envelopes for hybrid systems. Control envelopes characterize families of safe controllers and are used to monitor untrusted controllers at runtime. Our algorithm fills in the blanks of a hybrid system's sketch specifying the desired shape of the control envelope, the possible control actions, and the system's differential equations. In order to maximize the flexibility of the control envelope, the synthesized conditions saying which control action can be chosen when should be as permissive as possible while establishing a desired safety condition from the available assumptions, which are augmented if needed. An implicit, optimal solution to this synthesis problem is characterized using hybrid systems game theory, from which explicit solutions can be derived via symbolic execution and sound, systematic game refinements. Ideas for generalization to a broad class of envelope sketches, characterized by admitting a natural representation in differential game logic are presented. The resulting algorithm is demonstrated in a range of safe control envelope synthesis examples with different control challenges.
