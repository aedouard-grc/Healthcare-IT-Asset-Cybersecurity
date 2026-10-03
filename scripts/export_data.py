# Export Data — robust with timestamp, verification, and Colab download

import os
from datetime import datetime

# --- 1. Create an exports folder (keeps the workspace tidy) ---
export_dir = "exports"
os.makedirs(export_dir, exist_ok=True)

# --- 2. Build timestamped filenames so runs don't overwrite each other ---
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

files_to_export = {
    "healthcare_it_asset_inventory_analyzed": assets,
    "healthcare_it_asset_triage_report":       triage_report,
    "healthcare_security_dashboard":           security_dashboard
}

exported_paths = []

# --- 3. Export each DataFrame with error handling ---
for name, df in files_to_export.items():
    try:
        path = os.path.join(export_dir, f"{name}_{timestamp}.csv")
        df.to_csv(path, index=False)
        exported_paths.append(path)
        print(f"✅ Exported: {path}  ({len(df)} rows, {len(df.columns)} columns)")
    except NameError as e:
        print(f"❌ Skipped '{name}' — variable not defined: {e}")
    except Exception as e:
        print(f"❌ Failed to export '{name}': {e}")

# --- 4. Verify files exist and report sizes ---
print("\n--- Export Summary ---")
for path in exported_paths:
    size_kb = os.path.getsize(path) / 1024
    print(f"{os.path.basename(path):60s}  {size_kb:8.2f} KB")

print(f"\n✅ {len(exported_paths)} file(s) exported successfully to ./{export_dir}/")

# --- 5. In Google Colab: trigger a download of each file ---
try:
    from google.colab import files
    IN_COLAB = True
except ImportError:
    IN_COLAB = False

if IN_COLAB:
    print("\n Downloading files to your local machine...")
    for path in exported_paths:
        files.download(path)
else:
    print("\n Not running in Colab — files remain in the ./exports/ folder.")
     