import pandas as pd

# Load the Excel and CSV files
excel_file_path = '.../Main_2018_Added_Simplified_EIN_(E20+E21+E22).xlsx'
csv_file_path = '.../Missions_E20+E21+E22/2024_06_21_All_Missions_Raw.csv'

# Read the Excel file
excel_df = pd.read_excel(excel_file_path)
ein_list = excel_df['FILEREIN'].tolist()  # Create a list of EINs to match

# Read the CSV file
csv_df = pd.read_csv(csv_file_path, dtype={'TAXYEAR': 'Int64'}, low_memory=False)

# Filter the CSV data to include only rows with EINs present in the Excel file
filtered_df = csv_df[csv_df['FILEREIN'].isin(ein_list)]

# Define the output path for the filtered file and save it as an Excel
output_path = ('.../2024_06_21_All_Missions_E20+E21+E22.xlsx')

# Save the filtered data to the specified local folder
filtered_df.to_excel(output_path, index=False)

