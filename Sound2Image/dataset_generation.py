import os
import json
import pandas as pd

# Set the path to your 'audio_features' folder
audio_features_path = 'Album-Cover-GAN/audio_features'

# Initialize an empty list to store the data
data = []

# Traverse the 'audio_features' folder and read the JSON files
for filename in os.listdir(audio_features_path):
    if filename.endswith('.json'):
        file_path = os.path.join(audio_features_path, filename)

        with open(file_path, 'r') as f:
            json_data = json.load(f)

            # Add the corresponding image path to the json_data dictionary
            image_filename = os.path.splitext(filename)[0] + '.jpeg'
            json_data['image_path'] = f'Album-Cover-GAN/images/{image_filename}'

            # Append the json_data to the list
            data.append(json_data)

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Save the combined dataset as a CSV file
df.to_csv('combined_data.csv', index=False)
