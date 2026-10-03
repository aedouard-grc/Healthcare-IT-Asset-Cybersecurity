# Basic Inventory Quality Check

inventory_quality_issues = pd.DataFrame()
inventory_quality_issues["Asset_ID"] = assets["Asset_ID"]
inventory_quality_issues["Missing_Owner"] = assets["Owner"].isna()
inventory_quality_issues["Missing_Location"] = assets["Location"].isna()
inventory_quality_issues["Missing_Security_Tool"] = (
assets["Security_Tool"].isin(["None", "", None])
)
inventory_quality_issues["Duplicate_ID"] = (
assets["Asset_ID"].duplicated(keep=False)
)
inventory_quality_issues["Inventory_Issue"] = (
inventory_quality_issues[
[
"Missing_Owner",
"Missing_Location",
"Missing_Security_Tool",
"Duplicate_ID"
]
].any(axis=1)
)
display(inventory_quality_issues)
