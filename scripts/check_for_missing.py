# Check for Missing

missing_values = assets.isnull().sum()
print("Missing values by column:")
display(missing_values[missing_values > 0])
if missing_values.sum() == 0:
    print("No missing values detected.")
else:
    print("Missing values detected. Review the columns listed above.")