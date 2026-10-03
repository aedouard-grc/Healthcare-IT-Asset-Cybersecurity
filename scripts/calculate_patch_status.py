# Calculate Patch Status

patch_threshold = 90
assets["Patch_Status"] = np.where(
assets["Days_Since_Patch"] > patch_threshold,
"Review Required",
"Current"
)
display(
assets[
[
"Asset_ID",
"Asset_Type",
"Last_Patch_Date",
"Days_Since_Patch",
"Patch_Status"
]
]
)

     