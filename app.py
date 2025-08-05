import streamlit as st
import pandas as pd
import pickle

# ---------------------------
# Load the Trained Model
# ---------------------------
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:   # Change "model.pkl" to your actual filename
        loaded_model = pickle.load(file)
    return loaded_model

model = load_model()

# ---------------------------
# Web App UI
# ---------------------------
st.title("🏠 Gujarat House Price Prediction")
st.write("Enter the details below to predict the house price.")

# ---------------------------
# User Inputs
# ---------------------------
# Replace these with your actual feature names from training
feature_inputs = {}

# Example feature names (change these to match your dataset columns)
columns = ["Area", "Bedrooms", "Bathrooms", "Stories", "Parking"]

for col in columns:
    feature_inputs[col] = st.number_input(
        f"{col}",
        min_value=0.0,
        value=0.0
    )

# Convert input to DataFrame for prediction
input_df = pd.DataFrame([feature_inputs])

# ---------------------------
# Prediction
# ---------------------------
if st.button("🔮 Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Estimated House Price: ₹{prediction:,.2f}")

st.markdown("---")
st.caption("Powered by Machine Learning | Streamlit App")
