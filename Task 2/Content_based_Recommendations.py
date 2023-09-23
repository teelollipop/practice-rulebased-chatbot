import pandas as pd

# Replace 'dataset_path' with the actual path to our movies dataset within Replit
dataset_path = 'movies_dataset.csv'

# Read the dataset using pd.read_csv
df = pd.read_csv(dataset_path)

# Define user preferences (customize as needed)
user_preferences = "Adventure, Action, Fantasy, Mystery, Romance, Sci-Fi"

# Initialize an empty list to store recommendations
recommendations = []

# Loop through each row (item) in the dataset
for index, row in df.iterrows():
    item_features = row['item_features']  # Replace 'item_features' with your item feature column name
    # Simple similarity measure: count common features
    common_features = len(set(user_preferences.split(', ')).intersection(item_features.split(', ')))
    recommendations.append({"name": row['item_name'], "score": common_features})

# Sort recommendations by similarity score (higher score means more similar)
recommendations.sort(key=lambda x: x["score"], reverse=True)

# Display Recommendations
for item in recommendations:
    print(f"Recommended: {item['name']} (Score: {item['score']})")
 