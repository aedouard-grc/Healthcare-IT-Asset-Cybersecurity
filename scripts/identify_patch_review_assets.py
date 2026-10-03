# Identify Patch Review Assets

patch_review = assets[
    assets["Patch_Status"] == "Review Required"
].copy()

print("Assets requiring patch review:", len(patch_review))

display(
    patch_review[
        [
            "Asset_ID",
            "Asset_Type",
            "Criticality",
            "Last_Patch_Date",
            "Days_Since_Patch",
            "Vulnerability_Status"
        ]
    ]
)