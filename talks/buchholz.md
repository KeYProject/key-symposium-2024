---
author: "Nils Buchholz"
kind: "Regular Talk (20 min. + 10 min.)"
track: "KeY-only Track"
title: "Transferring proof obligations from KeY to Isabelle/HOL"
slot: 31
length: 15/30 
---

*Can be reduced to short talk if necessary*

Guarantees of correctness of programs are becoming more and more important nowadays. KeY is one tool, which can be used to prove the formal correctness of Java programs. It uses syntactic rewriting rules, called taclets, to successively simplify proofs. These taclet rules can be applied by an automated proving mode in KeY. Because the automation can be insufficient for closing some proofs and because proofs can contain thousands of rule applications, it is desirable to provide stronger automated tools to the user. One such tool is the Satisfiablity Modulo Theories (SMT) translation of KeY, which allows the use of SMT provers to close proofs. The SMT translation also lacks the required rules or proving strength for some proofs. It is thus still desirable to improve the already present automated toolset of KeY users.

This work designs a translation of KeY proofs to the higher-order logic prover Isabelle/HOL. In addition to designing this translation this work also shows that the translation can be automated and integrated within KeY by implementing it as a GUI-Extension of KeY.

This work tests the developed Isabelle translation on over 2 400 example proof obligations of KeY. In doing so the Isabelle translation has been found to offer some advantages over the SMT translation and the KeY automation. Although the Isabelle translation does not manage to close all proofs the KeY automation or SMT translation could close, it is able to close proofs, which the KeY automation or the SMT translation could not close.

Thus the Isabelle translation expands the KeY user’s automated toolset in a meaningful way, while also building a foundation for using Isabelle in ways outside automated proof solving in KeY.
