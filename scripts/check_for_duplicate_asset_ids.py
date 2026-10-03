# Check for Duplicate Asset IDs

duplicate_ids = assets[assets["Asset_ID"].duplicated(keep=False)]
if duplicate_ids.empty:
    print("No duplicate Asset_ID values detected.")
else:
    print("Duplicate asset IDs detected:")
    display(duplicate_ids)