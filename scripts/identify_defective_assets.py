# Identify Defective Assets

defective_assets = assets[
assets["Asset_Condition"] == "Defective"
]
print("Defective assets:")
display(
defective_assets[
[
"Asset_ID",
"Asset_Type",
"Criticality",
"Data_Sensitivity",
"Asset_Condition"
]
]
)
