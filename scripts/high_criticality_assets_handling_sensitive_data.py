# High-Criticality Assets Handling Sensitive Data

sensitive_critical_assets = assets[
(assets["Criticality"].isin(["Critical", "High"])) &
(assets["Data_Sensitivity"].isin(["Patient Data", "Research Data"]))
]
print("High/Critical assets associated with sensitive data:")
display(
sensitive_critical_assets[
[
"Asset_ID",
"Asset_Type",
"Criticality",
"Data_Sensitivity",
"Internet_Exposed",
"Vulnerability_Status"
]
]
)