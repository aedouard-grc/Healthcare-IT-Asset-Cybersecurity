# Generate Triage Report

triage_report = assets[
[
"Asset_ID",
"Asset_Type",
"Department",
"Criticality",
"Data_Sensitivity",
"Internet_Exposed",
"Connectivity_Level",
"Lifecycle_Status",
"Vulnerability_Status",
"Asset_Condition",
"Security_Tool",
"Patch_Status",
"Days_Since_Patch",
"Risk_Score",
"Triage_Priority"
]
].sort_values(
["Triage_Priority", "Risk_Score"],
ascending=[True, False]
)
display(triage_report)
