import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Read the combined_data.csv file
df = pd.read_csv('combined_data.csv')

# List of audio attributes to analyze
attributes = [
    'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
    'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
    'duration_ms', 'time_signature'
]

# Extract the audio features
X = df[attributes]

# Handle missing values using SimpleImputer
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Standardize the feature matrix (important for PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)

# Perform PCA
pca = PCA()
X_pca = pca.fit_transform(X_scaled)

# Print explained variance ratio (useful to understand how many components to keep)
print('Explained variance ratio:', pca.explained_variance_ratio_)

# Find the top 4 most relevant attributes
sorted_attributes = sorted(
    zip(attributes, np.abs(pca.components_[0]), np.abs(pca.components_[1]), np.abs(pca.components_[2]), np.abs(pca.components_[3])),
    key=lambda x: -sum(x[1:])
)

top_4_attributes = [attr for attr, *_ in sorted_attributes[:4]]
print('Top 4 most relevant attributes for determining album covers:', top_4_attributes)
