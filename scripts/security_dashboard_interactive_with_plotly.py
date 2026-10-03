# Security Dashboard — Interactive with Plotly

import plotly.express as px
from IPython.display import display, HTML

# --- 1. Build the dashboard DataFrame ---
security_dashboard = pd.DataFrame({
    "Metric": [
        "Total Assets",
        "Vulnerable Assets",
        "Internet-Facing Assets",
        "End-of-Support Assets",
        "Assets Without Security Tool",
        "Degraded Assets",
        "Defective Assets",
        "High-Priority Assets"
    ],
    "Count": [
        total_assets,
        vulnerable_count,
        internet_exposed_count,
        end_of_support_count,
        missing_security_tool_count,
        degraded_count,
        defective_count,
        high_priority_count
    ],
    "Severity": [
        "Neutral",
        "Critical",
        "High",
        "High",
        "High",
        "Medium",
        "Critical",
        "Critical"
    ],
    "Category": [
        "Overview",
        "Exposure",
        "Exposure",
        "Exposure",
        "Controls",
        "Condition",
        "Condition",
        "Triage"
    ]
})

# --- 2. Percentage of total ---
security_dashboard["Percent"] = (
    security_dashboard["Count"] / total_assets * 100
).round(1)

# --- 3. Severity color map ---
severity_colors = {
    "Critical": "#d62728",   # red
    "High":     "#ff7f0e",   # orange
    "Medium":   "#f1c40f",   # yellow
    "Low":      "#2ca02c",   # green
    "Neutral":  "#6c757d"    # gray
}

# --- 4. Interactive horizontal bar chart ---
fig = px.bar(
    security_dashboard.sort_values("Count", ascending=True),
    x="Count",
    y="Metric",
    orientation="h",
    color="Severity",
    color_discrete_map=severity_colors,
    text="Count",
    custom_data=["Category", "Percent"],
    title="Healthcare IT Asset Cybersecurity Dashboard",
    height=500
)

fig.update_traces(
    textposition="outside",
    textfont=dict(size=12, color="black"),
    marker_line_color="white",
    marker_line_width=1.5,
    hovertemplate=(
        "%{y}"
        "Count: %{x}"
        "Percent of total: %{customdata[1]}%"
        "Category: %{customdata[0]}"
        ""
    )
)

fig.update_layout(
    xaxis_title="Number of Assets",
    yaxis_title="",
    legend_title="Severity",
    font=dict(size=12),
    plot_bgcolor="white",
    title_font=dict(size=16),
    margin=dict(l=10, r=40, t=60, b=40)
)

fig.show()