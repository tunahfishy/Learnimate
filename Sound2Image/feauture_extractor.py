import os
import librosa
import pandas as pd

def extract_audio_features(file_path):
    y, sr = librosa.load(file_path)

    # Extract relevant features
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr).mean()
    spectral_contrast = librosa.feature.spectral_contrast(y=y, sr=sr).mean()
    mfcc = librosa.feature.mfcc(y=y, sr=sr).mean(axis=1)
    danceability = librosa.beat.beat_track(y, sr=sr)[1]

    # Combine features into a dictionary
    features = {
        'chroma_stft': chroma_stft,
        'spectral_contrast': spectral_contrast,
        'danceability': danceability
    }

    # Add MFCC features
    for i, mfcc_value in enumerate(mfcc):
        features[f'mfcc_{i + 1}'] = mfcc_value

    return features


# Set the folder path
folder_path = 'Album-Cover-GAN/audio'

# Get a list of all MP3 files in the folder
file_list = [f for f in os.listdir(folder_path) if f.endswith('.mp3')]

# Extract features and store them in a list
data = []
for file_name in file_list:
    print(f'Extracting features from {file_name}')
    file_path = os.path.join(folder_path, file_name)
    features = extract_audio_features(file_path)
    features['file_name'] = file_name
    data.append(features)

# Convert the list of dictionaries to a DataFrame and save it as a CSV file
df = pd.DataFrame(data)
df.to_csv('audio_features.csv', index=False)

print('Audio features extracted and saved to audio_features.csv')
