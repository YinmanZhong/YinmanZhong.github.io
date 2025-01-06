import pandas as pd
from collections import Counter

# Load the dataset
df = pd.read_excel('.../7_Missions_E20+E21+E22_AddStateInfo_Medicaid_NoShortMission_balanced_Equity_withTF-IDF.xlsx')

# Ensure the relevant columns exist
assert 'filtered_mission' in df.columns, "Column 'filtered_mission' not found"
assert 'MedicaidState' in df.columns, "Column 'MedicaidState' not found"
assert 'TAXYEAR' in df.columns, "Column 'TAXYEAR' not found"

# Split words in 'filtered_mission' into individual words and expand rows
df['filtered_mission'] = df['filtered_mission'].fillna('')  # Handle NaN values
df['filtered_words'] = df['filtered_mission'].str.split()  # Split into lists of words

# Expand rows for each word in 'filtered_words'
expanded_df = df.explode('filtered_words')

# Remove any empty words (in case of empty cells in 'filtered_mission')
expanded_df = expanded_df[expanded_df['filtered_words'].notnull() & (expanded_df['filtered_words'] != '')]

# Count occurrences of each word by MedicaidState and TAXYEAR
word_counts = (
    expanded_df
    .groupby(['filtered_words', 'MedicaidState', 'TAXYEAR'])
    .size()
    .reset_index(name='count')
)

# Separate counts for Expanded and Non-Expanded states
expanded_counts = word_counts[word_counts['MedicaidState'] == 'Expanded State']
non_expanded_counts = word_counts[word_counts['MedicaidState'] == 'Non-Expanded State']

# Save results to separate CSV files
expanded_counts.to_csv('expanded_counts.csv', index=False)
non_expanded_counts.to_csv('non_expanded_counts.csv', index=False)

# Summary output
print("Word counts in expanded states (sample):")
print(expanded_counts.head())

print("\nWord counts in non-expanded states (sample):")
print(non_expanded_counts.head())
