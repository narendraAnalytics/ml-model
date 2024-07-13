import pandas as pd
import numpy as np
import random

# Function to generate random data for the dataset
def generate_breast_cancer_data(num_records):
    data = []
    for i in range(num_records):
        id = i + 1
        radius_mean = round(random.uniform(10, 30), 2)
        texture_mean = round(random.uniform(10, 40), 2)
        perimeter_mean = round(random.uniform(50, 200), 2)
        area_mean = round(random.uniform(100, 2500), 2)
        smoothness_mean = round(random.uniform(0.05, 0.2), 4)
        compactness_mean = round(random.uniform(0.02, 0.35), 4)
        concavity_mean = round(random.uniform(0.02, 0.4), 4)
        concave_points_mean = round(random.uniform(0.01, 0.2), 4)
        symmetry_mean = round(random.uniform(0.1, 0.4), 4)
        fractal_dimension_mean = round(random.uniform(0.05, 0.15), 4)
        radius_worst = round(random.uniform(10, 40), 2)
        texture_worst = round(random.uniform(10, 50), 2)
        perimeter_worst = round(random.uniform(50, 250), 2)
        area_worst = round(random.uniform(100, 3000), 2)
        smoothness_worst = round(random.uniform(0.05, 0.3), 4)
        compactness_worst = round(random.uniform(0.02, 0.6), 4)
        concavity_worst = round(random.uniform(0.02, 0.6), 4)
        concave_points_worst = round(random.uniform(0.01, 0.3), 4)
        symmetry_worst = round(random.uniform(0.1, 0.6), 4)
        fractal_dimension_worst = round(random.uniform(0.05, 0.2), 4)
        diagnosis = random.choice([0, 1])
        
        data.append([
            id, radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean,
            concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_worst, texture_worst, perimeter_worst,
            area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst,
            fractal_dimension_worst, diagnosis
        ])
    
    return data

# Column names for the dataset
columns = [
    'ID', 'Radius (mean)', 'Texture (mean)', 'Perimeter (mean)', 'Area (mean)', 'Smoothness (mean)', 'Compactness (mean)', 
    'Concavity (mean)', 'Concave points (mean)', 'Symmetry (mean)', 'Fractal dimension (mean)', 'Radius (worst)', 
    'Texture (worst)', 'Perimeter (worst)', 'Area (worst)', 'Smoothness (worst)', 'Compactness (worst)', 
    'Concavity (worst)', 'Concave points (worst)', 'Symmetry (worst)', 'Fractal dimension (worst)', 'Diagnosis'
]

# Generate the dataset
num_records = 1080
data = generate_breast_cancer_data(num_records)

# Convert to DataFrame
df = pd.DataFrame(data, columns=columns)

# Save the dataset to a CSV file
file_path = 'breast_cancer_data.csv'
df.to_csv(file_path, index=False)

print(f"Dataset generated and saved to {file_path} successfully.")
