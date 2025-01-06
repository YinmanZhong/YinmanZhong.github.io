import pandas as pd

# Load the Excel file
file_path = ".../4_Missions_E20+E21+E22_AddStateInfo_Medicaid_NoShortMission_RemoveStopWords.xlsx"  # Replace with the actual path to your Excel file
df = pd.read_excel(file_path)

# Check for duplicates based on 'FILEREIN' and 'TAXYEAR'
duplicates = df[df.duplicated(subset=['FILEREIN', 'TAXYEAR'], keep=False)]

# Print the duplicated combinations
if not duplicates.empty:
    print("The following FILEREIN and TAXYEAR combinations are duplicated:")
    duplicated_combinations = duplicates.groupby(['FILEREIN', 'TAXYEAR']).size().reset_index(name='Count')
    for _, row in duplicated_combinations.iterrows():
        print(f"FILEREIN: {row['FILEREIN']}, TAXYEAR: {row['TAXYEAR']}, Count: {row['Count']}")
else:
    print("No duplicates found based on FILEREIN and TAXYEAR.")
