# Asset Condition Visualization — Healthy, Degraded, Defective with distinct colors

# 1. Ensure consistent order and fill missing categories
condition_order = ["Healthy", "Degraded", "Defective"]
condition_counts_filtered = (
    condition_counts
    .reindex(condition_order)
    .fillna(0)
    .astype(int)
)

# 2. Color map: green = healthy, orange = degraded, red = defective
color_map = {
    "Healthy":   "#2ca02c",   # green  — no issues
    "Degraded":  "#ff7f0e",   # orange — declining performance
    "Defective": "#d62728"    # red    — hardware/software failure
}
bar_colors = [color_map[c] for c in condition_counts_filtered.index]

# 3. Plot
fig, ax = plt.subplots(figsize=(8, 5))

bars = ax.bar(
    condition_counts_filtered.index,
    condition_counts_filtered.values,
    color=bar_colors,
    edgecolor="white",
    linewidth=1.5
)

# 4. Add count labels on top of each bar
ax.bar_label(bars, fmt="%d", padding=3, fontsize=11, fontweight="bold")

# 5. Labels and title
ax.set_title(
    "Healthcare IT Asset Condition",
    fontsize=13,
    fontweight="bold"
)
ax.set_xlabel("Asset Condition")
ax.set_ylabel("Number of Assets")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()