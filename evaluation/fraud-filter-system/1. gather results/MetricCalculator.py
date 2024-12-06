import pandas as pd
from pathlib import Path

# Load the CSV data into a DataFrame
df = pd.read_csv("real-estate-webiste/src/data/Authentic.csv")

# Count images based on AI and authentic percentages
copyright_images = df[(df["Copyright Status"] == "Medium Risk") & (df["AI"] < df["Authentic"])].shape[0]
ai_generated_images = df[df["AI"] >= df["Authentic"]].shape[0]
authentic_images = df[df["AI"] <= df["Authentic"]].shape[0]

# Calculate total images
total_images = df.shape[0] 

# Calculate percentages
copyright_percentage = (copyright_images / total_images) * 100
ai_generated_percentage = (ai_generated_images / total_images) * 100
authentic_percentage = (authentic_images / total_images) * 100

# Print the counts
print("Copyright Images:", copyright_images)
print("AI Generated Images:", ai_generated_images)
print("Authentic Images:", authentic_images)

# Create a new DataFrame with the results
results_df = pd.DataFrame({
    "Copyright": [copyright_images, copyright_percentage],
    "AI Generated": [ai_generated_images, ai_generated_percentage],
    "Authentic": [authentic_images, authentic_percentage],
    "Total": [total_images, 100]
})

save_path = Path("real-estate-webiste/src/data") / "AuthenticMetrics.csv"

# Save the results to a new CSV file
results_df.to_csv(save_path, index=False)