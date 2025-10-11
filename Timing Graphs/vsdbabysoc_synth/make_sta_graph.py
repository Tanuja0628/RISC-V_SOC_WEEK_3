from graphviz import Digraph
import re

# Input file name
report_file = "unconstrained_report.txt"

# Create a directed graph
g = Digraph("timing_path", format="png")
g.attr(rankdir="LR", fontsize="10")

with open(report_file) as f:
    lines = f.readlines()

# Extract relevant lines from the report
path_lines = []
for line in lines:
    # Match lines like "8.43    8.43 ^ core/_9211_/Q (sky130_fd_sc_hd__dfxtp_1)"
    if re.search(r'\s[\^v]\s', line):
        path_lines.append(line.strip())

prev_node = None
for line in path_lines:
    # Split fields
    parts = line.split()
    if len(parts) < 4:
        continue
    delay = parts[0]
    total_time = parts[1]
    trans = parts[2]  # ^ or v
    name = parts[3]
    cell = re.search(r'\((.*?)\)', line)
    cell_name = cell.group(1) if cell else ""
    
    label = f"{name}\n({cell_name})\nDelay={delay}ns"
    g.node(name, label=label, shape="box", style="rounded,filled", fillcolor="#E0F7FA")
    
    if prev_node:
        g.edge(prev_node, name, label=f"{delay}ns")
    prev_node = name

# Render as PNG
g.render("timing_graph", cleanup=True)
print("✅ Timing graph generated: timing_graph.png")

