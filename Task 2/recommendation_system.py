import os
import pandas as pd
import tabula

# Convert the PDF dataset to a list of DataFrames
pdf_file = 'movies_dataset.csv.pdf'
dfs = tabula.read_pdf(pdf_file, pages='all', multiple_tables=True)

# Combine all DataFrames into a single DataFrame (for multiple pages)
df = pd.concat(dfs)

# Save the combined DataFrame as a CSV file
csv_file = 'movies_dataset.csv'
df.to_csv(csv_file, index=False)

# Load the CSV dataset
df = pd.read_csv(csv_file)

# Define user preferences
user_preferences = "Adventure, Action, Drama, Fantasy, Romance, Sci-Fi"

# Initialize an empty list to store recommendations
recommendations = []

# Loop through each row (item) in the dataset
for index, row in df.iterrows():
    item_features = row['genres']
    
    # Simple similarity measure: count common features
    common_features = len(set(user_preferences.split(', ')).intersection(item_features.split(', ')))
    
    # Append recommendations only if there are common features
    if common_features > 0:
        recommendations.append({"name": row['item_name'], "score": common_features})

# Sort recommendations by similarity score (higher score means more similar)
recommendations.sort(key=lambda x: x["score"], reverse=True)

# Display Recommendations
for item in recommendations:
    print(f"Recommended: {item['name']} (Score: {item['score']})")
