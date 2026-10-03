## Internet Exposure Visualization — Yes vs No with distinct colors

# 1. Ensure consistent order and fill missing categories
internet_order = ["Yes", "No"]
internet_counts_filtered = (
    internet_counts
    .reindex(internet_order)
    .fillna(0)
    .astype(int)
)

# 2. Color map: red = exposed (risk), green = internal (safer)
color_map = {
    "Yes": "#d62728",   # red — internet-exposed
    "No":  "#2ca02c"    # green — internal only
}
bar_colors = [color_map[c] for c in internet_counts_filtered.index]

# 3. Plot
fig, ax = plt.subplots(figsize=(8, 5))

bars = ax.bar(
    internet_counts_filtered.index,
    internet_counts_filtered.values,
    color=bar_colors,
    edgecolor="white",
    linewidth=1.5
)

# 4. Add count labels on top of each bar
ax.bar_label(bars, fmt="%d", padding=3, fontsize=11, fontweight="bold")

# 5. Labels and title
ax.set_title(
    "Internet-Exposed vs Internal Assets",
    fontsize=13,
    fontweight="bold"
)
ax.set_xlabel("Internet Exposure")
ax.set_ylabel("Number of Assets")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()