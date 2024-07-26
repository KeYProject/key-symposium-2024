---
author: "Dirk Beyer"
kind: "Invited Talk"
track: "Common Track"
title: "Distributed Automatic Contract Construction"
slot:  207
length: 60
type: invited
order: 70
---


The presentation consists of two parts. The first part presents an approach to automatic contract construction that is more modular, scalable, and precise compared to existing automatic approaches. We decompose the program into code blocks, and for each code block, we compute a postcondition and a violation condition. The postcondition of a block is given to successors in order to refine their precondition and derive a proof of correctness. The violation condition is a condition that describes states leading to a specification violation. The approach is scalable because each block can be analyzed independently: the blocks communicate only via postconditions and violation conditions. The precision of the approach can be defined by the underlying program analysis. In a second part, we describe an approach to conserve tools for formal methods. We collect and maintain essential data about tools for formal methods in a central repository, called FM-Tools, available at https://gitlab.com/sosy-lab/benchmarking/fm-tools. The repository contains metadata, such as which tools are available, which versions are advertized for each tool, and what command-line arguments to use for default usage. The actual tool executables are stored in tool archives at Zenodo, and for technically deep documentation, references point to archived publications or project web sites. With this approach, we can conserve today's tools for the future.
