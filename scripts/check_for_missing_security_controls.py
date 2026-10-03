# Check for Missing Security Controls

assets_without_security_tool = assets[
assets["Security_Tool"].isin(["None", "", None])
]
print("Assets without an identified security tool:")
display(
assets_without_security_tool[
[
"Asset_ID",
"Asset_Type",
"Criticality",
"Data_Sensitivity",
"Internet_Exposed",
"Security_Tool"
]
]
)