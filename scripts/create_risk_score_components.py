# Create Risk Score Components

assets["Risk_Score"] = 0

# --- Criticality ---
assets["Risk_Score"] += assets["Criticality"].map({
    "Critical": 3,
    "High": 2,
    "Medium": 1,
    "Low": 0
}).fillna(0)

# --- Internet exposure ---
assets["Risk_Score"] += np.where(
    assets["Internet_Exposed"] == "Yes",
    2,
    0
)

# --- Vulnerability status ---
assets["Risk_Score"] += np.where(
    assets["Vulnerability_Status"] == "Vulnerable",
    3,
    0
)

# --- Patch status ---
assets["Risk_Score"] += np.where(
    assets["Patch_Status"] == "Review Required",
    2,
    0
)

# --- Missing security tool ---
assets["Risk_Score"] += np.where(
    assets["Security_Tool"] == "None",
    2,
    0
)

# --- Sensitive data ---
assets["Risk_Score"] += np.where(
    assets["Data_Sensitivity"].isin(["Patient Data", "Research Data"]),
    2,
    0
)

# --- End-of-support ---
assets["Risk_Score"] += np.where(
    assets["Lifecycle_Status"] == "End-of-Support",
    2,
    0
)

# --- Asset condition ---
assets["Risk_Score"] += assets["Asset_Condition"].map({
    "Healthy": 0,
    "Degraded": 1,
    "Defective": 2
}).fillna(0)

# --- Display results ---
display(
    assets[
        [
            "Asset_ID",
            "Asset_Type",
            "Criticality",
            "Vulnerability_Status",
            "Internet_Exposed",
            "Data_Sensitivity",
            "Lifecycle_Status",
            "Asset_Condition",
            "Risk_Score"
        ]
    ]
)
     
