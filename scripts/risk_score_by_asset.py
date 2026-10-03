# Risk Score by Asset — Horizontal Bar Chart with Severity Colors

# 1. Sort ascending so highest-risk assets appear at the TOP of the horizontal chart
risk_plot = assets.sort_values("Risk_Score", ascending=True)

# 2. Color each bar by its risk tier (using the same thresholds as Step 12)
def risk_color(score):
    if score >= 10:
        return "#d62728"   # red    — High Priority
    elif score >= 6:
        return "#ff7f0e"   # orange — Medium Priority
    else:
        return "#2ca02c"   # green  — Low Priority

bar_colors = risk_plot["Risk_Score"].apply(risk_color)

# 3. Plot
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(
    risk_plot["Asset_ID"].astype(str),
    risk_plot["Risk_Score"],
    color=bar_colors,
    edgecolor="white",
    linewidth=1.2
)

# 4. Add score labels at the end of each bar
ax.bar_label(bars, fmt="%d", padding=3, fontsize=10, fontweight="bold")

# 5. Labels and title
ax.set_xlabel("Educational Risk Score", fontsize=11)
ax.set_ylabel("Asset ID", fontsize=11)
ax.set_title(
    "Healthcare IT Asset Risk Score",
    fontsize=13,
    fontweight="bold"
)

# 6. Ensure all asset labels are visible
ax.set_xlim(0, max(risk_plot["Risk_Score"].max() + 2, 5))
plt.tight_layout()
plt.show()
  