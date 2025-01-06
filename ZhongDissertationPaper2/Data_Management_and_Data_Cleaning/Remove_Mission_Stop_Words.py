import pandas as pd
import re
from nltk.corpus import stopwords
import nltk

# Download stopwords
nltk.download('stopwords')

# Define stop words
stop_words = set(stopwords.words('english'))

# Function to remove stop words and numbers
def clean_text(text):
    if isinstance(text, str):  # Ensure input is a string
        # Remove numbers
        text = re.sub(r'\d+', '', text)
        # Remove non-alphanumeric characters (optional, for punctuation)
        text = re.sub(r'[^\w\s]', '', text)
        # Split text into words, filter out stop words, and join back into a single string
        return ' '.join(word for word in text.split() if word.lower() not in stop_words)
    return text  # Return the original text if it's not a string

# Read the Excel file
file_path = ".../4_Missions_E20+E21+E22_AddStateInfo_Medicaid_NoShortMission_(2014-2021)_balanced.xlsx" 
df = pd.read_excel(file_path)

# Apply the clean_text function to the MISSION column
df['MISSION'] = df['MISSION'].apply(clean_text)

# Save the cleaned data to a new Excel file
output_path = file_path.replace('.xlsx', '_RemoveStopWords.xlsx')
df.to_excel(output_path, index=False)

print(f"Cleaned file saved as {output_path}")
