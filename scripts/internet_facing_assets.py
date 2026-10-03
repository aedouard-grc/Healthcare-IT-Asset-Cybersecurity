# Internet-Facing Assets

internet_facing = assets[
assets["Internet_Exposed"] == "Yes"
].copy()
print("Internet-facing assets:", len(internet_facing))
display(
internet_facing[
[
"Asset_ID",
"Asset_Type",
"Criticality",
"Data_Sensitivity",
"Security_Tool",
"Vulnerability_Status"
]
]
)