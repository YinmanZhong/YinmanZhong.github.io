import pandas as pd

# Load your dataset (assuming it's already loaded as df)
df = pd.read_excel('.../4_Missions_E20+E21+E22_AddStateInfo_Medicaid_NoShortMission_RemoveStopWords.xlsx')

# Filter the dataset to include only the years 2014 to 2021
df_filtered = df[df['TAXYEAR'].between(2014, 2021)]

# Group by hospital (FILEREIN) and check the number of unique years for each hospital
valid_hospitals = df_filtered.groupby('FILEREIN')['TAXYEAR'].nunique()

# Find hospitals that have data for all years between 2014 and 2021 (8 years total)
valid_hospitals = valid_hospitals[valid_hospitals == 8].index

# Filter the original dataset to only include those hospitals
df_balanced = df_filtered[df_filtered['FILEREIN'].isin(valid_hospitals)]

# Save the balanced dataset to a new excel file
df_balanced.to_excel('.../4_Missions_E20+E21+E22_AddStateInfo_Medicaid_NoShortMission_RemoveStopWords_balanced.xlsx', index=False)

# Display the balanced dataset
print(df_balanced)
