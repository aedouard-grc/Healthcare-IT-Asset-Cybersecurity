# Calculate Number of Risk Indicators per Asset

risk_flags = []

for _, row in assets.iterrows():
    flags = 0

    # --- Criticality ---
    if row["Criticality"] == "Critical":
        flags += 1

    # --- Internet exposure ---
    if row["Internet_Exposed"] == "Yes":
        flags += 1

    # --- Vulnerability status ---
    if row["Vulnerability_Status"] == "Vulnerable":
        flags += 1

    # --- Patch status ---
    if row["Patch_Status"] == "Review Required":
        flags += 1

    # --- Missing security tool ---
    if row["Security_Tool"] == "None":
        flags += 1

    # --- Sensitive data ---
    if row["Data_Sensitivity"] in ["Patient Data", "Research Data"]:
        flags += 1

    # --- End-of-support ---
    if row["Lifecycle_Status"] == "End-of-Support":
        flags += 1

    # --- Asset condition ---
    if row["Asset_Condition"] in ["Degraded", "Defective"]:
        flags += 1

    risk_flags.append(flags)

assets["Risk_Factor_Count"] = risk_flags

# --- Display results, sorted by number of risk factors ---
display(
    assets[
        [
            "Asset_ID",
            "Risk_Factor_Count",
            "Risk_Score",
            "Triage_Priority"
        ]
    ].sort_values(
        "Risk_Factor_Count",
        ascending=False
    )
)
     