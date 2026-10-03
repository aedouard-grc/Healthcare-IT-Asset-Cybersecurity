# High-Priority Asset Investigation

high_priority = assets[
assets["Triage_Priority"] == "High Priority"
].copy()
print("High-priority assets:")
display(
high_priority[
[
"Asset_ID",
"Asset_Type",
"Criticality",
"Data_Sensitivity",
"Internet_Exposed",
"Vulnerability_Status",
"Patch_Status",
"Lifecycle_Status",
"Asset_Condition",
"Security_Tool",
"Risk_Score"
]
].sort_values(
"Risk_Score",
ascending=False
)
)