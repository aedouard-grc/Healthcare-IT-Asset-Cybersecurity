# Identify Assets Approaching End-of-Support

approaching_eos = assets[
(assets["Days_Until_End_of_Support"] >= 0) &
(assets["Days_Until_End_of_Support"] <= 365)
]
print("Assets reaching end-of-support within one year:")
display(
approaching_eos[
[
"Asset_ID",
"Asset_Type",
"Criticality",
"Data_Sensitivity",
"End_of_Support",
"Days_Until_End_of_Support"
]
]
)