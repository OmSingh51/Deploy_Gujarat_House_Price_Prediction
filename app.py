import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model, scaler and columns
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)

# Sample city and area mapping (same as your training data)
city_area_mapping = {
    "Ahmedabad": ["Satellite", "Bopal", "Maninagar", "Gota", "Navrangpura"],
    "Surat": ["Adajan", "Vesu", "City Light", "Piplod", "Katargam"],
    "Vadodara": ["Alkapuri", "Gotri", "Fatehgunj", "Waghodia", "Manjalpur"],
    "Rajkot": ["Kalavad Road", "Mavdi", "Raiya Road", "150 Feet Ring Road", "University Road"],
    "Bhavnagar": ["Kaliabid", "Panwadi", "Vidhyanagar", "Nari Road", "Chitra"]
}

furnishing_options = ["Unfurnished", "Semi-Furnished", "Fully Furnished"]
property_types = ["Apartment", "Villa", "Independent House"]

# Streamlit UI
st.title("🏠 Gujarat House Price Predictor")

city = st.selectbox("Select City", list(city_area_mapping.keys()))
area = st.selectbox("Select Area", city_area_mapping[city])
bhk = st.selectbox("BHK", [1, 2, 3, 4])
sqft = st.number_input("Total Square Feet", min_value=300, max_value=10000)
furnishing = st.selectbox("Furnishing Type", furnishing_options)
property_type = st.selectbox("Property Type", property_types)
age = st.slider("Age of Property (Years)", 0, 50)

if st.button("Predict Price"):
    input_dict = {
        "BHK": bhk,
        "Square_Feet": sqft,
        "Age_of_Property": age,
        f"City_{city}": 1,
        f"Area_{area}": 1,
        f"Furnishing_{furnishing}": 1,
        f"Property_Type_{property_type}": 1
    }

    # Prepare input DataFrame with all model columns
    input_df = pd.DataFrame([input_dict])
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    # Scale and predict
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]

    st.success(f"🏷️ Estimated House Price: ₹{int(prediction):,}")
