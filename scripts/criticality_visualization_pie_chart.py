# Criticality Visualization — Pie Chart (Critical, High, Medium)

# 1. Define the categories to display, in severity order
criticality_order = ["Critical", "High", "Medium"]

# 2. Filter and reorder the counts
criticality_counts_filtered = (
    criticality_counts
    .reindex(criticality_order)
    .fillna(0)
    .astype(int)
)

# 3. Drop any tier that has zero assets (avoids empty slices in the pie)
criticality_counts_filtered = criticality_counts_filtered[criticality_counts_filtered > 0]

# 4. Custom colors matching severity
color_map = {
    "Critical": "#d62728",   # red
    "High":     "#ff7f0e",   # orange
    "Medium":   "#1f77b4"    # blue
}
colors = [color_map[c] for c in criticality_counts_filtered.index]

# 5. Build labels that include both count and percentage
total = criticality_counts_filtered.sum()
labels = [
    f"{cat}\n{count} ({count/total:.0%})"
    for cat, count in criticality_counts_filtered.items()
]

# 6. Plot the pie chart
fig, ax = plt.subplots(figsize=(8, 6))

ax.pie(
    criticality_counts_filtered.values,
    labels=labels,
    colors=colors,
    autopct=None,          # we already embed % in the labels
    startangle=90,
    counterclock=False,    # so Critical (largest severity) starts at top and goes clockwise
    wedgeprops={"edgecolor": "white", "linewidth": 2},
    textprops={"fontsize": 11}
)

ax.set_title(
    "Healthcare IT Assets by Criticality\n(Critical, High, Medium)",
    fontsize=13,
    fontweight="bold"
)
ax.axis("equal")   # ensures the pie is a perfect circle
plt.tight_layout()
plt.show()
     