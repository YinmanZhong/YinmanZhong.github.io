import pandas as pd

# Load the dataset
file_path = "/Users/yinmanzhong/Desktop/Dissertation/1. My Dissertation Data/Mission Statements Extracted from Giving Tuesday (E20+E22)/Missions_E20+E21+E22/3_Missions_E20+E21+E22_AddStateInfo_Medicaid.xlsx"  # Replace with your actual file path
df = pd.read_excel(file_path)

# Function to count the number of words in a mission statement
def word_count(text):
    if pd.isnull(text):
        return 0
    # Split the text into words and count the length
    return len(str(text).split())

# Apply the word count function to the "MISSION" column
df['word_count'] = df['MISSION'].apply(word_count)

# Filter the dataframe to keep only the rows with more than 20 words in the "MISSION" column
df_filtered = df[df['word_count'] > 20]

# Save the filtered dataframe back to an Excel file
output_file_path = "/Users/yinmanzhong/Desktop/Dissertation/1. My Dissertation Data/Mission Statements Extracted from Giving Tuesday (E20+E22)/Missions_E20+E21+E22/4_Missions_E20+E21+E22_AddStateInfo_Medicaid_NoShortMission.xlsx"  # Replace with your desired output path
df_filtered.to_excel(output_file_path, index=False)

# Optionally, print the first few rows of the filtered dataframe
print(df_filtered.head())
