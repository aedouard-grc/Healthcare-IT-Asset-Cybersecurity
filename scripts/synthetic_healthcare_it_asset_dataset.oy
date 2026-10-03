# Create Synthetic Healthcare IT Asset Dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

asset_data = {
    "Asset_ID": [
        "HC-001", "HC-002", "HC-003", "HC-004", "HC-005",
        "HC-006", "HC-007", "HC-008", "HC-009", "HC-010",
        "HC-011", "HC-012", "HC-013", "HC-014", "HC-015"
    ],
    "Asset_Type": [
        "Database Server", "Application Server", "Medical Device",
        "Workstation", "Laptop", "Network Switch", "Research Server",
        "Medical Device", "File Server", "Workstation",
        "Database Server", "Firewall", "Medical Device",
        "Application Server", "Laptop"
    ],
    "Operating_System": [
        "Windows Server 2022", "Windows Server 2019", "Embedded OS",
        "Windows 11", "Windows 11", "Network OS", "Ubuntu Linux",
        "Embedded OS", "Windows Server 2019", "Windows 10",
        "Windows Server 2016", "Network OS", "Embedded OS",
        "Windows Server 2022", "Windows 11"
    ],
    "Department": [
        "Health Information", "Clinical Operations", "Radiology",
        "Clinical Operations", "Administration", "Network Operations",
        "Research", "Cardiology", "Health Information",
        "Clinical Operations", "Health Information", "Network Operations",
        "Emergency Department", "Clinical Operations", "Research"
    ],
    "Location": [
        "Data Center", "Data Center", "Radiology", "Nursing Station",
        "Administration", "Data Center", "Research Lab", "Cardiology",
        "Data Center", "Nursing Station", "Data Center", "Network Room",
        "Emergency Department", "Data Center", "Research Lab"
    ],
    "Owner": [
        "Health IT", "Clinical IT", "Biomedical IT", "Clinical IT",
        "Corporate IT", "Network Team", "Research IT", "Biomedical IT",
        "Health IT", "Desktop Support", "Health IT", "Network Team",
        "Biomedical IT", "Clinical IT", "Research IT"
    ],
    "Status": [
        "Active", "Active", "Active", "Active", "Active",
        "Active", "Active", "Active", "Active", "Active",
        "Active", "Active", "Active", "Active", "Active"
    ],
    "Last_Patch_Date": [
        "2026-09-15", "2026-05-01", "2025-12-01", "2026-08-20",
        "2026-07-15", "2026-08-01", "2026-04-15", "2025-10-01",
        "2026-03-01", "2026-09-01", "2025-08-01", "2026-09-20",
        "2025-06-01", "2026-06-15", "2026-01-15"
    ],
    "Criticality": [
        "Critical", "High", "Critical", "High", "Medium",
        "High", "Critical", "High", "Critical", "Medium",
        "Critical", "Critical", "High", "High", "Medium"
    ],
    "Internet_Exposed": [
        "No", "Yes", "No", "No", "Yes",
        "No", "No", "No", "No", "No",
        "No", "Yes", "No", "Yes", "Yes"
    ],
    "Security_Tool": [
        "EDR", "EDR", "None", "EDR", "EDR",
        "Network Monitoring", "EDR", "None", "EDR", "EDR",
        "None", "Firewall Monitoring", "None", "EDR", "EDR"
    ],
    "Lifecycle_Status": [
        "Active", "Active", "Aging", "Active", "Active",
        "Active", "Active", "Aging", "Active", "End-of-Support",
        "End-of-Support", "Active", "End-of-Support", "Active", "Aging"
    ],
    "Vulnerability_Status": [
        "Current", "Review Required", "Vulnerable", "Current", "Current",
        "Current", "Review Required", "Vulnerable", "Review Required",
        "Vulnerable", "Vulnerable", "Current", "Vulnerable",
        "Review Required", "Review Required"
    ],
    "Asset_Condition": [
        "Healthy", "Healthy", "Degraded", "Healthy", "Healthy",
        "Healthy", "Healthy", "Defective", "Healthy", "Degraded",
        "Degraded", "Healthy", "Defective", "Healthy", "Degraded"
    ],
    "Data_Sensitivity": [
        "Patient Data", "Patient Data", "Patient Data", "Patient Data",
        "Organizational Data", "Infrastructure Data", "Research Data",
        "Patient Data", "Patient Data", "Organizational Data",
        "Patient Data", "Infrastructure Data", "Patient Data",
        "Patient Data", "Research Data"
    ],
    "Connectivity_Level": [
        "Restricted", "Internet-Facing", "Restricted", "Internal",
        "Internet-Facing", "Internal", "Restricted", "Internal",
        "Restricted", "Internal", "Restricted", "Internet-Facing",
        "Internal", "Internet-Facing", "Internet-Facing"
    ],
    "End_of_Support": [
        "2031-01-01", "2029-01-01", "2027-01-01", "2031-01-01",
        "2031-01-01", "2030-01-01", "2030-01-01", "2026-12-31",
        "2029-01-01", "2025-10-14", "2027-01-01", "2032-01-01",
        "2026-12-31", "2031-01-01", "2030-01-01"
    ]
}

# Build the DataFrame
assets = pd.DataFrame(asset_data)

# --- Display ALL 15 assets across ALL 17 columns ---
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)
pd.set_option("display.max_colwidth", 30)

print(f"Dataset shape: {assets.shape[0]} assets × {assets.shape[1]} columns\n")
display(assets)
     