import pandas as pd

# Load the main Excel file into a DataFrame
main_file_path = ('.../2024_06_21_All_Missions_E20+E21+E22.xlsx')
main_df = pd.read_excel(main_file_path)

# Load the mission file into a DataFrame
second_file_path = ('.../Main_2018_Added_Simplified_EIN_(E20+E21+E22).xlsx')
Addition_Info_df = pd.read_excel(second_file_path)

#Append multiple columns selected:
Addition_Info_df = Addition_Info_df[['FILEREIN', 'state_code', 'zip_code','country_code']]

# Merge the mission DataFrame into the main DataFrame based on FILEREIN
main_df = pd.merge(main_df, Addition_Info_df, on='FILEREIN', how='left')

# Save the updated DataFrame to a new Excel file
output_file_path = ('.../2024_06_21_All_Missions_E20+E21+E22_AddStateInfo.xlsx')
main_df.to_excel(output_file_path, index=False)

print("Updated file saved successfully.")
