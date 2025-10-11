# Static Timing Analysis (STA) – Part I: Essential Timing Checks

## Overview
Static Timing Analysis (STA) is crucial for verifying timing at every step of physical design. This course focuses on **signoff timing checks**.  
It covers timing basics, real-world STA methods, and prepares learners for advanced STA topics.  
The course starts from fundamentals and progresses to intermediate/advanced timing analysis.

---

## Key Learning Outcomes
- Understand **timing path, arrival time (AAT), required arrival time (RAT), and slack**.  
- Perform **setup and hold checks** for flip-flops and latches.  
- Analyze **data, clock, slew, and load effects**.  
- Learn **transistor-level timing** for flops and latches.  
- Conduct **jitter analysis and account for variations** (etching, oxide thickness, etc.).  
- Gain insights into **industry-standard STA practices**.  

---

## Fundamental Concepts
- **Timing Path:** Series of logic elements from source to sink.  
- **Arrival Time (AAT):** When data reaches a node.  
- **Required Arrival Time (RAT):** When data must arrive to meet timing.  
- **Slack:** Difference between RAT and AAT; positive slack = timing met, negative slack = violation.  
- **Setup & Hold Checks:** Ensure data is stable before/after clock edge.  

---

## STA Steps Covered
1. Convert **logic gates and pins into nodes** for timing calculations.  
2. Compute **AAT, RAT, and slack** for all paths.  
3. Perform **GBA-PBA analysis** (Graphical vs. Path-based analysis).  
4. Transistor-level understanding of **flop/latch operation**.  
5. Compute **library setup times** and **clk-to-q delays**.  
6. **Jitter analysis** via eye diagrams.  
7. **Setup and hold timing** accounting for pessimism (OCV adjustments).  
8. Analyze **sources of variation**: etching, oxide thickness, resistance, drain current.  

---

## Practical Applications
- **Signoff timing verification** for real designs.  
- **Quality analysis** of timing closure in industry workflows.  
- **Translating graphical STA reports** to textual data for design decisions.  
- Prepares for **advanced STA and physical design optimization**.  

---

## Prerequisites
- Basic knowledge of **physical design flow** is helpful but not mandatory.  
- Understanding of **flip-flops and basic sequential logic**.  

---

## Conclusion
By the end of this course, learners can **analyze timing paths, identify violations, and perform STA with industry-standard rigor**.  
It provides a foundation for **advanced timing analysis, signoff procedures, and optimization** in physical design.
