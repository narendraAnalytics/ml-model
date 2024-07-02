import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score, precision_recall_curve, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

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

# Function to plot confusion matrix
def plot_confusion_matrix(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    st.pyplot(plt)

# Function to plot ROC curve
def plot_roc_curve(y_test, y_pred_proba):
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    auc = roc_auc_score(y_test, y_pred_proba)
    plt.figure(figsize=(6, 4))
    plt.plot(fpr, tpr, label=f'AUC = {auc:.2f}')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend()
    st.pyplot(plt)

# Function to plot Precision-Recall curve
def plot_precision_recall_curve(y_test, y_pred_proba):
    precision, recall, _ = precision_recall_curve(y_test, y_pred_proba)
    plt.figure(figsize=(6, 4))
    plt.plot(recall, precision)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    st.pyplot(plt)

# Load test data
test_data = pd.read_csv('/workspaces/ml-model/Breast_cancer_data.csv')  # Ensure you have a separate test dataset

# Extract features and target variable from test data
X_test = test_data.drop(columns=['diagnosis'])
y_test = test_data['diagnosis']

# Predict probabilities and labels
y_pred_proba = model.predict_proba(X_test)[:, 1]
y_pred = model.predict(X_test)

# Display performance metrics and plots
st.header('Model Performance')
st.write('### Confusion Matrix')
plot_confusion_matrix(y_test, y_pred)

st.write('### ROC Curve')
plot_roc_curve(y_test, y_pred_proba)

st.write('### Precision-Recall Curve')
plot_precision_recall_curve(y_test, y_pred_proba)

st.write('### Classification Report')
report = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()
st.dataframe(report_df)
