# Executive Summary Statistics — Color-Coded Table

# --- 1. Compute all summary metrics ---
total_assets = len(assets)

vulnerable_count = (assets["Vulnerability_Status"] == "Vulnerable").sum()
internet_exposed_count = (assets["Internet_Exposed"] == "Yes").sum()
end_of_support_count = (assets["Lifecycle_Status"] == "End-of-Support").sum()
missing_security_tool_count = (assets["Security_Tool"] == "None").sum()
degraded_count = (assets["Asset_Condition"] == "Degraded").sum()
defective_count = (assets["Asset_Condition"] == "Defective").sum()
high_priority_count = (assets["Triage_Priority"] == "High Priority").sum()
medium_priority_count = (assets["Triage_Priority"] == "Medium Priority").sum()
low_priority_count = (assets["Triage_Priority"] == "Low Priority").sum()

# --- 2. Build a summary DataFrame ---
summary = pd.DataFrame({
    "Metric": [
        "Total Assets",
        "Vulnerable Assets",
        "Internet-Facing Assets",
        "End-of-Support Assets",
        "Assets Without Security Tool",
        "Degraded Assets",
        "Defective Assets",
        "High-Priority Assets",
        "Medium-Priority Assets",
        "Low-Priority Assets"
    ],
    "Count": [
        total_assets,
        vulnerable_count,
        internet_exposed_count,
        end_of_support_count,
        missing_security_tool_count,
        degraded_count,
        defective_count,
        high_priority_count,
        medium_priority_count,
        low_priority_count
    ]
})

# --- 3. Add percentage of total ---
summary["% of Total"] = (summary["Count"] / total_assets * 100).round(1).astype(str) + "%"

# --- 4. Assign a severity category for coloring ---
severity_map = {
    "Total Assets":                "neutral",
    "Vulnerable Assets":           "critical",
    "Internet-Facing Assets":      "high",
    "End-of-Support Assets":       "high",
    "Assets Without Security Tool":"high",
    "Degraded Assets":             "medium",
    "Defective Assets":            "critical",
    "High-Priority Assets":        "critical",
    "Medium-Priority Assets":      "medium",
    "Low-Priority Assets":         "low"
}
summary["Severity"] = summary["Metric"].map(severity_map)

# --- 5. Apply color styling ---
severity_colors = {
    "critical": "background-color: #f8d7da; color: #721c24; font-weight: bold;",
    "high":     "background-color: #ffe5cc; color: #8a4b00; font-weight: bold;",
    "medium":   "background-color: #fff3cd; color: #856404;",
    "low":      "background-color: #d4edda; color: #155724;",
    "neutral":  "background-color: #e2e3e5; color: #383d41; font-weight: bold;"
}

def style_row(row):
    return [severity_colors[row["Severity"]]] * (len(row) - 1) + [""]

styled = (
    summary[["Metric", "Count", "% of Total", "Severity"]]
    .style
    .apply(style_row, axis=1)
    .hide(axis="columns", subset=["Severity"])
    .set_caption("Healthcare IT Asset Cybersecurity Summary")
    .set_table_styles([
        {"selector": "caption",
         "props": [("font-size", "16px"),
                   ("font-weight", "bold"),
                   ("text-align", "left"),
                   ("padding-bottom", "8px")]},
        {"selector": "th",
         "props": [("background-color", "#343a40"),
                   ("color", "white"),
                   ("text-align", "left"),
                   ("padding", "6px 12px")]},
        {"selector": "td",
         "props": [("padding", "6px 12px"),
                   ("border-bottom", "1px solid #dee2e6")]}
    ])
)

display(styled)
     
Healthcare IT Asset Cybersecurity Summary
 