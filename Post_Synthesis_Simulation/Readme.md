# Gate Level Simulation of BabySoC
Gate-Level Simulation (GLS) is a critical verification step that checks the correctness of a digital design after synthesis. Unlike RTL or behavioral simulations, which work at a higher abstraction, GLS operates on the actual gate-level netlist, ensuring the design meets both functional and timing requirements.

For BabySoC, which integrates multiple modules like the RISC-V processor, PLL, and DAC, GLS validates that these components interact correctly under real-world conditions.

---
# Why GLS is Important for BabySoC

## Timing Verification
- GLS uses Standard Delay Format (SDF) files to incorporate real gate delays.
- Ensures the SoC behaves as expected when subjected to physical timing constraints.

## Design Validation Post-Synthesis
- Confirms that the synthesized netlist maintains the intended logical behavior.
- Detects issues like glitches or potential metastability.

## Simulation Tools
- Netlist compilation and simulation: Icarus Verilog or similar.
- Waveform visualization: GTKWave.

---

# Step-by-Step GLS Execution for BabySoC
## Step 1: Load the Top-Level Design and Modules

Launch Yosys and load the main design and supporting modules:
```bash
yosys
read_verilog src/module/vsdbabysoc.v
read_verilog -I src/include src/module/rvmyth.v
read_verilog -I src/include src/module/clk_gate.v
```

## Step 2: Load Standard Cell Libraries

Include the necessary .lib files for synthesis:
```bash
read_liberty -lib src/lib/avsdpll.lib
read_liberty -lib src/lib/avsddac.lib
read_liberty -lib src/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
```

## Step 3: Synthesize the Design

Target the top module:
```bash
synth -top vsdbabysoc
```

## Step 4: Map Flip-Flops to Standard Cells
```bash
dfflibmap -liberty src/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
```

## Step 5: Optimize and Map Technology
```bash
opt
abc -liberty src/lib/sky130_fd_sc_hd__tt_025C_1v80.lib -script +strash;scorr;ifraig;retime;{D};strash;dch,-f;map,-M,1,{D}
```

## Step 6: Clean-Up and Rename
```bash
flatten
setundef -zero
clean -purge
rename -enumerate
```

## Step 7: Check Design Statistics
```bash
stat
```

## Step 8: Export the Synthesized Netlist
```bash
write_verilog -noattr output/post_synth_sim/vsdbabysoc.synth.v
```
---

# Post-Synthesis Simulation

## Step 1: Compile the Testbench
```bash
iverilog -DFUNCTIONAL -DUNIT_DELAY=#1 \
  -I src/gls_model \
  -o output/post_synth_sim/post_synth_sim.out \
  src/module/testbench.v \
  src/gls_model/primitives.v \
  src/gls_model/sky130_fd_sc_hd.v \
  output/synthesized/vsdbabysoc.synth.v \
  src/module/avsdpll.v \
  src/module/avsddac.v
```

## Step 2: Navigate to Output Directory
```bash
cd output/post_synth_sim/
```

## Step 3: Run the Simulation
```bash
./post_synth_sim.out
```

## Step 4: View Waveforms
```bash
gtkwave post_synth_sim.vcd
```
---

This workflow ensures that BabySoC behaves correctly after synthesis and all timing constraints are met.
