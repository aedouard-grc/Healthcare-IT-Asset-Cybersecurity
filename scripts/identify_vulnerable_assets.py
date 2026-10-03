# Identify Vulnerable Assets

vulnerable_assets = assets[
assets["Vulnerability_Status"] == "Vulnerable"
].copy()
print("Number of vulnerable assets:", len(vulnerable_assets))
display(
vulnerable_assets[
[
"Asset_ID",
"Asset_Type",
"Criticality",
"Internet_Exposed",
"Data_Sensitivity",
"Lifecycle_Status",
"Asset_Condition"
]
]
)
