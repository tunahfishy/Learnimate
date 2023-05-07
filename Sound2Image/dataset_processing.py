import os
import json
import shutil
import zipfile
from PIL import Image
import pandas as pd

# Define paths
csv_file = 'Album-Cover-GAN/combined_data.csv'
images_folder = 'Album-Cover-GAN/images'
output_folder = 'Album-Cover-GAN/png_images'
output_zip = 'Album-Cover-GAN/dataset.zip'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Read the combined_data.csv file
df = pd.read_csv(csv_file)

# Create a dictionary to store the metadata
metadata = {}

# Convert JPEG images to PNG and create metadata
for index, row in df.iterrows():
    input_image_path = row['image_path']
    img_id = os.path.splitext(os.path.basename(input_image_path))[0]
    output_image_path = os.path.join(output_folder, f'{img_id}.png')

    # Convert JPEG to PNG
    image = Image.open(input_image_path)
    image.save(output_image_path)

    # Add metadata
    metadata[img_id] = {
        'danceability': row['danceability'],
        'energy': row['energy'],
        'key': row['key'],
        'loudness': row['loudness'],
        'mode': row['mode'],
        'speechiness': row['speechiness'],
        'acousticness': row['acousticness'],
        'instrumentalness': row['instrumentalness'],
        'liveness': row['liveness'],
        'valence': row['valence'],
        'tempo': row['tempo'],
        'duration_ms': row['duration_ms'],
        'time_signature': row['time_signature']
    }

# Save metadata as dataset.json
metadata_path = os.path.join(output_folder, 'dataset.json')
with open(metadata_path, 'w') as f:
    json.dump(metadata, f)

# Create a ZIP archive containing the PNG images and metadata
with zipfile.ZipFile(output_zip, 'w') as archive:
    for root, dirs, files in os.walk(output_folder):
        for file in files:
            file_path = os.path.join(root, file)
            archive.write(file_path, os.path.relpath(file_path, output_folder))
