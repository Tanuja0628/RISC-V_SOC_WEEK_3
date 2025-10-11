# Load technology library
read_liberty ./sky130RTLDesignAndSynthesisWorkshop/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

# Read synthesized netlist
read_verilog ./sky130RTLDesignAndSynthesisWorkshop/verilog_files/good_mux_netlist.v

# Link design
link_design good_mux

# Define clock (adjust the port name if your top-level clock is different)
create_clock -name clk -period 10 [get_ports clk]

# Define input and output delays (for realistic paths)
set_input_delay 2 -clock clk [all_inputs]
set_output_delay 2 -clock clk [all_outputs]

# Propagate clock through the network
set_propagated_clock [get_clocks clk]

# Report all checks (unconstrained and constrained)
report_checks -path_delay min_max -fields {slew cap input_pins nets fanout} -digits 3 > timing_report.txt

# Report unconstrained paths (if any)
report_checks -unconstrained > unconstrained_report.txt

# Generate clock waveform report
report_clock_properties [get_clocks clk] > clock_report.txt


# Save timing data for visualization
report_checks -path_delay min_max -fields {slew cap input_pins nets fanout} -digits 3 > timing_report.txt





