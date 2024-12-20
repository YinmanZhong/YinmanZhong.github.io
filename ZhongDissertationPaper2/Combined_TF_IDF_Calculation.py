import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
import seaborn as sns
import re


# Load the dataset
file_path = "path/to/missionstatements"  # Replace with your file path
combined_tfidf_output_path = ("path/to/output.xlsx")  # Output path for Combined TF-IDF

df = pd.read_excel(file_path)

# Define the list of equity-related words
equity_words = [
    #equity-related terms
    "equity", "equities", "equitable", "equitably", "inequity", "inequities", "inequitable", "inequitably",
    "fairness", "fair", "unfairness", "unfair", "justice", "equal", "equality", "equalities", "unequal", "disparity", "disparities", "marginalized",

    # access-related words
    "access", "accesses", "accessible", "inaccessible", "accessibility", "accessive",

    #cost-related words
    "cost", "costs", "payment", "payments", "reimbursement", "reimbursements", "charity", "charitable",

    # quality-related words
    "quality", "qualities", "performance",

    #community-related words
    "community", "communities", "society", "societies", "social", "diverse", "diversity", "diversities"
]

# Preprocess the equity words list: Convert to lowercase, remove special characters, and remove hyphens
equity_words = [re.sub(r'[^\w\s-]', '', phrase.lower()).replace('-', '') for phrase in equity_words]

# Preprocess the mission statements: Convert to lowercase, remove special characters, and remove hyphens
df['MISSION'] = df['MISSION'].fillna("").str.lower().apply(lambda x: re.sub(r'[^\w\s-]', '', x)).str.replace('-', '')


# Filter out rows with empty mission statements
df = df[df['MISSION'].str.strip() != '']

# Split the dataframe into expanded and non-expanded state groups
expanded_states_df = df[df['MedicaidState'] == 'Expanded State'].copy()
non_expanded_states_df = df[df['MedicaidState'] == 'Non-Expanded State'].copy()


# Function to calculate combined_tfidf and equity_words_found
def process_tfidf(df, equity_words):
    # Reset the index to ensure alignment
    df.reset_index(drop=True, inplace=True)

    # Step 1 in Zhong's paper: Generate TF-IDF matrix
    # Note: While Zhong's paper explains the equations for calculating TF-IDF, this code uses TfidfVectorizer from sklearn to handle this calculation automatically via the vectorizer.
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df['MISSION'])

    # Convert to DataFrame with proper column names
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())

    # Ensure tfidf_df has the same index as df
    tfidf_df.index = df.index

    # Step 2 in Zhong's paper: Calculate combined TF-IDF scores
    df['combined_tfidf'] = df.index.map(
        lambda i: sum([tfidf_df.loc[i, word] for word in equity_words if word in tfidf_df.columns])
    )

    # Save Additional Information to the Excel dataset
    # Find equity words present in each mission
    df['equity_words_found'] = df.index.map(
        lambda i: ', '.join([word for word in equity_words if word in tfidf_df.columns and tfidf_df.loc[i, word] > 0])
    )
    # Add word count for each document
    df['document_word_count'] = df['MISSION'].apply(lambda x: len(x.split()))

    return df


# Saving the outputs
# Process expanded and non-expanded states
if not expanded_states_df.empty:
    expanded_states_df = process_tfidf(expanded_states_df, equity_words)

if not non_expanded_states_df.empty:
    non_expanded_states_df = process_tfidf(non_expanded_states_df, equity_words)

# Combine both groups into one dataframe
combined_df = pd.concat([expanded_states_df, non_expanded_states_df])

# Save the combined dataframe to the specified output file
combined_df.to_excel(combined_tfidf_output_path, index=False)



# Data Visualization
# Scatter Plot: combined_tfidf vs document_word_count for expanded vs non-expanded states
plt.figure(figsize=(10, 6))
sns.scatterplot(x="document_word_count", y="combined_tfidf", hue="MedicaidState", data=pd.concat([expanded_states_df, non_expanded_states_df]), palette="muted", alpha=0.6, edgecolor='none')
#plt.title('Combined TF-IDF vs Document Word Count (Scatter Plot)', fontsize=16, fontweight='bold')
plt.xlabel('Document Word Count', fontsize=20)
plt.ylabel('Combined TF-IDF Scores', fontsize=20)
plt.legend(title='Medicaid Status Group',  fontsize=12, title_fontsize=14)
plt.xticks(rotation=45, fontsize=16)  # Bold years on the x-axis
plt.yticks(fontsize=16)  # Bold numbers on the y-axis
plt.show()



# Bar Chart: Average Combined_tfidf by MedicaidState and TAXYEAR
plt.figure(figsize=(12, 8))
avg_combined_tfidf = pd.concat([expanded_states_df, non_expanded_states_df]).groupby(['MedicaidState', 'TAXYEAR'])['combined_tfidf'].mean().reset_index()
sns.barplot(x="TAXYEAR", y="combined_tfidf", hue="MedicaidState", data=avg_combined_tfidf, palette="muted")
#plt.title('Average Combined TF-IDF by Medicaid Status and Tax Year', fontsize=16, fontweight='bold')
# Adjust the y-axis limit to give more space on top so the legend can fit in
plt.ylim(0, 0.18)
plt.xlabel('Tax Year', fontsize=20)
plt.ylabel('Average Combined TF-IDF Scores', fontsize=20)
plt.legend(title='Medicaid Status Group', fontsize=12, title_fontsize=14)
plt.xticks(rotation=45, fontsize=16)  # Bold years on the x-axis
plt.yticks(fontsize=16)  # Bold numbers on the y-axis
plt.show()



# Plotting the trend of combined_tfidf over time for Both Expanded and Non-Expanded States
plt.figure(figsize=(12, 6))
# Plotting the trend for Expanded States with a 95% confidence interval
sns.lineplot(x="TAXYEAR", y="combined_tfidf", data=expanded_states_df,
             marker='o', label="Expanded States", color='blue', linewidth=2.5)
# Plotting the trend for Non-Expanded States with a 95% confidence interval
sns.lineplot(x="TAXYEAR", y="combined_tfidf", data=non_expanded_states_df,
             marker='o', label="Non-Expanded States", color='red', linewidth=2.5)
# Add title, labels, and legend
#plt.title('Trend of Combined TF-IDF over Time (Expanded vs Non-Expanded States)', fontsize=16, fontweight='bold')
plt.xlabel('Tax Year', fontsize=20)  # Bold and larger font size for x-axis title
plt.ylabel('Combined TF-IDF Scores', fontsize=20)  # Bold and larger font size for y-axis title
plt.xticks(rotation=45, fontsize=16)  # Bold years on the x-axis
plt.yticks(fontsize=16)  # Bold numbers on the y-axis
plt.legend(title="Medicaid Status Group", fontsize=12, title_fontsize=14)
# Remove grid lines
plt.grid(False)
# Remove top and right spines for a cleaner look
sns.despine()
# Show the plot
plt.show()
