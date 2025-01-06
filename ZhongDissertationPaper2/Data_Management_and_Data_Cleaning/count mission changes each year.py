import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "/Users/yinmanzhong/Desktop/Dissertation/1. My Dissertation Data/Mission Statements Extracted from Giving Tuesday (E20+E22)/Missions_E20+E21+E22/Final with Mission Change (2014-2021)/4_Missions_E20+E21+E22_AddStateInfo_Medicaid_NoShortMission_RemoveStopWords_balanced_MissionChanged.xlsx"  # Replace with your file path
df = pd.read_excel(file_path)

# Filter rows where 'NoExcelMissChange(String)' is "false"
df_filtered = df[df['NoExcelMissChange(String)'].str.lower() == 'false']

# Group by state and year, then count occurrences
counts = df_filtered.groupby(['state_code', 'TAXYEAR']).size().reset_index(name='False_Count')

# Pivot the DataFrame to match the table format
table = counts.pivot(index='state_code', columns='TAXYEAR', values='False_Count').fillna(0)

# Ensure all years from 2014 to 2021 are included, even if missing
all_years = list(range(2014, 2022))
table = table.reindex(columns=all_years, fill_value=0)

# Add a total column
table['Total'] = table.sum(axis=1)

# Sort by State for better readability
table = table.sort_index()

# Reset column order to match your LaTeX format
columns_order = all_years + ['Total']
table = table[columns_order]

# Convert numerical values to integers for cleaner formatting
table = table.astype(int)

# Create a new column summing totals by year
total_by_year = table[all_years].sum()

# Plot 1: Line chart of total number of changes each year
plt.figure(figsize=(10, 8))
plt.plot(all_years, total_by_year, marker='o', color='b', label='Total Changes')

# Add values to each point
for x, y in zip(all_years, total_by_year):
    plt.text(x, y + 2, str(y), ha='center', va='bottom', fontsize=10)  # Adjust text position slightly above each point

plt.title('Total Number of Hospitals that have Changed Their Mission Statements (All States Combined)',
          fontsize=14, fontweight='bold', pad=15)  # Add padding to title
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Total Changes', fontsize=12, fontweight='bold')
plt.xticks(all_years)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plot 2: Heatmap of changes by state and year, without annotations, and with a light-to-dark blue color scheme
plt.figure(figsize=(15, 10))

# Add state codes to the DataFrame as row labels
heatmap_table = table[all_years]
heatmap_table.index.name = 'State Code'  # Explicitly name the index for clarity

# Use 'Blues' color map for a light-to-dark blue gradient
sns.heatmap(
    heatmap_table,
    cmap='Blues',  # Lighter to darker blue color map
    annot=False,  # Remove annotations (numbers in each cell)
    cbar_kws={'label': 'Number of Changes'},  # Color bar label
    yticklabels=heatmap_table.index,  # Add state codes as row labels
    linewidths=0.5,  # Add slight separation between cells
    linecolor='gray'  # Set color for lines separating cells
)

# Bold the color bar label and the years
colorbar = plt.gca().collections[0].colorbar  # Access colorbar
colorbar.set_label('Number of Changes', fontsize=12, fontweight='bold')  # Bold color bar label

# Bold the year tick labels
plt.xticks(fontsize=12, fontweight='bold')  # Make the year tick labels bold

# Title and axis labels
plt.title('Total Number of Mission Statements Changed by State Annually',
          fontsize=14, fontweight='bold', pad=15)  # Title with padding for spacing
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('State Code', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()