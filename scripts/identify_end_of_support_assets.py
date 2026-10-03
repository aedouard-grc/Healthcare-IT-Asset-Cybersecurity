# Identify End-of-Support Assets

eos_assets = assets[
assets["Lifecycle_Status"] == "End-of-Support"
]
print("Assets classified as End-of-Support:")
display(
eos_assets[
[
"Asset_ID",
"Asset_Type",
"Operating_System",
"Criticality",
"Data_Sensitivity",
"End_of_Support"
]
]
)