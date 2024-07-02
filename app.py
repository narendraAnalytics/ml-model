import streamlit as st
import pickle
import pandas as pd

# Load the trained model
model_filename = 'random_forest_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Function to make predictions
def predict_diagnosis(mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness):
    data = pd.DataFrame({
        'mean_radius': [mean_radius],
        'mean_texture': [mean_texture],
        'mean_perimeter': [mean_perimeter],
        'mean_area': [mean_area],
        'mean_smoothness': [mean_smoothness]
    })
    prediction = model.predict(data)
    return 'Diagnosis Needed' if prediction[0] == 1 else 'No Diagnosis Needed'

# Streamlit app
st.title('Breast Cancer Diagnosis Prediction')

st.sidebar.header('Input Features')
mean_radius = st.sidebar.number_input('Mean Radius', min_value=0.0)
mean_texture = st.sidebar.number_input('Mean Texture', min_value=0.0)
mean_perimeter = st.sidebar.number_input('Mean Perimeter', min_value=0.0)
mean_area = st.sidebar.number_input('Mean Area', min_value=0.0)
mean_smoothness = st.sidebar.number_input('Mean Smoothness', min_value=0.0)

if st.sidebar.button('Predict'):
    result = predict_diagnosis(mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness)
    st.write(f'Result: {result}')
