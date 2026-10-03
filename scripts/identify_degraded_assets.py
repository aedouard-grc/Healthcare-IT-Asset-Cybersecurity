# Identify Degraded Assets

degraded_assets = assets[
assets["Asset_Condition"] == "Degraded"
]
print("Degraded assets:")
display(
degraded_assets[
[
"Asset_ID",
"Asset_Type",
"Criticality",
"Lifecycle_Status",
"Asset_Condition"
]
]
)
