# Triage Priority Visualization — High, Medium, Low with distinct colors

# 1. Compute counts and enforce severity order
priority_order = ["High Priority", "Medium Priority", "Low Priority"]
priority_counts = (
    assets["Triage_Priority"]
    .value_counts()
    .reindex(priority_order)
    .fillna(0)
    .astype(int)
)

# 2. Color map: red = high, orange = medium, green = low
color_map = {
    "High Priority":   "#d62728",   # red    — immediate attention
    "Medium Priority": "#ff7f0e",   # orange — schedule review
    "Low Priority":    "#2ca02c"    # green  — routine monitoring
}
bar_colors = [color_map[c] for c in priority_counts.index]

# 3. Plot
fig, ax = plt.subplots(figsize=(8, 5))

bars = ax.bar(
    priority_counts.index,
    priority_counts.values,
    color=bar_colors,
    edgecolor="white",
    linewidth=1.5
)

# 4. Add count labels on top of each bar
ax.bar_label(bars, fmt="%d", padding=3, fontsize=11, fontweight="bold")

# 5. Labels and title
ax.set_title(
    "Cybersecurity Asset Triage Priority",
    fontsize=13,
    fontweight="bold"
)
ax.set_xlabel("Triage Priority")
ax.set_ylabel("Number of Assets")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
     