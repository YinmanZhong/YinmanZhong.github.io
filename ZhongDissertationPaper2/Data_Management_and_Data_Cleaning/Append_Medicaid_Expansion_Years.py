import pandas as pd

# Load the dataframe 
df = pd.read_excel('.../2024_06_21_All_Missions_E20+E21+E22_AddStateInfo.xlsx')

# Define a dictionary mapping each state abbreviation to its Medicaid expansion year
medicaid_expansion_years = {
    'AL': 'N/A',
    'AK': 2015,
    'AZ': 2014,
    'AR': 2014,
    'CA': 2014,
    'CO': 2014,
    'CT': 2014,
    'DE': 2014,
    'DC': 2014,
    'FL': 'N/A',
    'GA': 'N/A',
    'HI': 2014,
    'ID': 2020,
    'IL': 2014,
    'IN': 2015,
    'IA': 2014,
    'KS': 'N/A',
    'KY': 2014,
    'LA': 2016,
    'ME': 2019,
    'MD': 2014,
    'MA': 2014,
    'MI': 2014,
    'MN': 2014,
    'MS': 'N/A',
    'MO': 2021,
    'MT': 2016,
    'NE': 2020,
    'NV': 2014,
    'NH': 2014,
    'NJ': 2014,
    'NM': 2014,
    'NY': 2014,
    'NC': 2023,
    'ND': 2014,
    'OH': 2014,
    'OK': 2021,
    'OR': 2014,
    'PA': 2015,
    'RI': 2014,
    'SC': 'N/A',
    'SD': 2023,
    'TN': 'N/A',
    'TX': 'N/A',
    'UT': 2020,
    'VT': 2014,
    'VA': 2019,
    'WA': 2014,
    'WV': 2014,
    'WI': 'N/A',
    'WY': 'N/A'
}

# Map the Medicaid expansion years to a new column in the DataFrame based on the state_code column
df['medicaid_expansion_year'] = df['state_code'].map(medicaid_expansion_years)

# Create the treatment variable
# Treatment is 1 if the hospital is in a Medicaid expansion state and Year >= medicaid_expansion_year
df['treated'] = df.apply(
    lambda row: 1 if row['medicaid_expansion_year'] != "N/A" and pd.notna(row['medicaid_expansion_year'])
                and row['TAXYEAR'] >= int(row['medicaid_expansion_year'])
                else 0,
    axis=1
)

# Create the time_since_expansion variable
# Calculate the number of years since Medicaid expansion for expansion states, "N/A" for non-expansion states
df['time_since_expansion'] = df.apply(
    lambda row: row['TAXYEAR'] - int(row['medicaid_expansion_year'])
    if row['medicaid_expansion_year'] != "N/A" and pd.notna(row['medicaid_expansion_year']) else "N/A",
    axis=1
)


# Calculate the number of years since Medicaid expansion using 2021 as the reference year, "N/A" for non-expansion states
df['yearstreated'] = df.apply(
    lambda row: 2021 - int(row['medicaid_expansion_year'])
    if row['medicaid_expansion_year'] != "N/A" and pd.notna(row['medicaid_expansion_year']) else "N/A",
    axis=1
)


# Save the updated DataFrame to a new Excel file
output_file_path = ('.../Missions_E20+E21+E22/2024_06_21_All_Missions_E20+E21+E22_AddStateInfo_Medicaid.xlsx')
df.to_excel(output_file_path, index=False)

print("Updated file saved successfully at:", output_file_path)
