import pandas as pd

# File paths
input_file = ".../4_Missions_E20+E21+E22_AddStateInfo_Medicaid_NoShortMission_RemoveStopWords_balanced.xlsx" 
output_file = input_file.replace(".xlsx", "_MissionChanged.xlsx")

# Load the Excel file
df = pd.read_excel(input_file)

# Normalize the NoExcelMissChange column for consistent comparison
df['NoExcelMissChange(String)'] = df['NoExcelMissChange(String)'].astype(str).str.strip().str.upper()

# Debugging: Print unique values
print("Unique values in 'NoExcelMissChange(String)':", df['NoExcelMissChange(String)'].unique())

# Filter organizations where "NoExcelMissChange" contains at least one "FALSE"
filtered_df = df.groupby('FILEREIN').filter(lambda group: 'FALSE' in group['NoExcelMissChange(String)'].values)

# Debugging: Print the number of organizations before and after filtering
print("Number of organizations before filtering:", df['FILEREIN'].nunique())
print("Number of organizations after filtering:", filtered_df['FILEREIN'].nunique())

# Save the filtered dataset to a new file
filtered_df.to_excel(output_file, index=False)

print(f"Filtered file saved as {output_file}")

