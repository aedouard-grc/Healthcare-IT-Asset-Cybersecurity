# Assign Triage Priority

def assign_priority(score):
    if score >= 10:
        return "High Priority"
    elif score >= 6:
        return "Medium Priority"
    else:
        return "Low Priority"

assets["Triage_Priority"] = assets["Risk_Score"].apply(assign_priority)

display(
    assets[
        [
            "Asset_ID",
            "Asset_Type",
            "Risk_Score",
            "Triage_Priority"
        ]
    ].sort_values(
        "Risk_Score",
        ascending=False
    )
)