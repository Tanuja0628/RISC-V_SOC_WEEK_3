# Static Timing Analysis (STA) – Part I: Mandatory Timing Checks

## Introduction
Static Timing Analysis (STA) is essential for timing verification at each physical design step. This course addresses **signoff timing checks**.
It presents fundamentals of timing, practical STA techniques, and builds a foundation for further STA topics.
The course begins from the ground up and moves towards intermediate/advanced timing analysis.

---

## Principal Learning Outcomes
- Familiarize yourself with **timing path, arrival time (AAT), required arrival time (RAT), and slack**.  
- Check **setup and hold for flip-flops and latches**.  
- Examine **data, clock, slew, and load effects**.  
- Study **transistor-level timing** for flops and latches.  
- Perform **jitter analysis and factor variations** (etching, oxide thickness, etc.).  
- Obtain knowledge of **industry-standard STA practices**.

---  

## Fundamental Concepts
- **Timing Path:** Chain of logic cells from source to sink.
- **Arrival Time (AAT):** When the data arrives at a node.
- **Required Arrival Time (RAT):** When the data should arrive to satisfy timing.
- **Slack:** The difference between RAT and AAT; positive slack = timing satisfied, negative slack = violation.
- **Setup & Hold Checks:** Data is stable before/after clock edge.

---

## STA Steps Covered
1. Convert **logic gates and pins into nodes** for timing calculations.  
2. Compute **AAT, RAT, and slack** for all paths.  
3. Perform **GBA-PBA analysis** (Graphical vs. Path-based analysis).  
4. Transistor-level understanding of **flop/latch operation**.  
5. Compute **library setup times** and **clk-to-q delays**.  
6. **Jitter analysis** via eye diagrams.  
7. **Setup and hold timing** accounting for pessimism (OCV adjustments).
8. Examine **variation sources**: etching, oxide thickness, resistance, drain current.

---

## Practical Applications
- **Signoff timing verification** for actual designs.
- **Quality analysis** of the timing closure in industry processes.
- **Converting graphical STA reports** into textual information for design choices.
- Leads to **advanced STA and physical design optimization**.

---

## Prerequisites
- Familiarity with **physical design flow** is beneficial but not necessary.
- Familiarity with **flip-flops and basic sequential logic**.

---

## Conclusion
At the completion of this course, students can **analyze timing paths, detect violations, and execute STA with industry-standard quality**.
It lays the groundwork for **advanced timing analysis, signoff procedures, and optimization** in physical design.
