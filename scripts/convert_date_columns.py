# Convert Date Columns

assets["Last_Patch_Date"] = pd.to_datetime(assets["Last_Patch_Date"])
assets["End_of_Support"] = pd.to_datetime(assets["End_of_Support"])
analysis_date = pd.Timestamp("2026-10-02")
assets["Days_Since_Patch"] = (
analysis_date - assets["Last_Patch_Date"]
).dt.days
assets["Days_Until_End_of_Support"] = (
assets["End_of_Support"] - analysis_date
).dt.days
display(
assets[
[
"Asset_ID",
"Last_Patch_Date",
"Days_Since_Patch",
"End_of_Support",
"Days_Until_End_of_Support"
]
]
)