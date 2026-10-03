# Basic Dataset Inspection

import pandas as pd

# Ensure the full dataset renders (all rows, all columns)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)
pd.set_option("display.max_colwidth", 30)

print("Number of assets:", len(assets))
print("Number of columns:", len(assets.columns))
print("\nColumns:")
print(list(assets.columns))
print("\nDataset shape:")
print(assets.shape)
print("\nData types:")
print(assets.dtypes)
print("\nAll 15 assets across all 17 columns:")
display(assets)