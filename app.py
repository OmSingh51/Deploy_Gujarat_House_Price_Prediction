import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ---------------------------
# Load Trained Model
# ---------------------------
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        return pickle.load(file)

model = load_model()

# ---------------------------
# Read dataset to get feature names
# ---------------------------
df = pd.read_csv(r"C:\Users\hp\Downloads\gujarat_house_prices.csv")
feature_columns = [col for col in df.columns if col.lower() != "price"]

# ---------------------------
# Streamlit UI
# ---------------------------
st.title("🏠 Gujarat House Price Prediction")
st.write("Enter details to predict house price.")

# Collect user inputs dynamically based on dataset
user_data = {}
for col in feature_columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        min_val = float(df[col].min())
        max_val = float(df[col].max())
        default_val = float(df[col].mean())
        user_data[col] = st.number_input(f"{col}", min_value=min_val, max_value=max_val, value=default_val)
    else:
        options = df[col].dropna().unique().tolist()
        if not options:
            st.warning(f"No options available for {col}")
            user_data[col] = ""
        else:
            user_data[col] = st.selectbox(f"{col}", options, index=0)

# Convert to DataFrame with correct column order
input_df = pd.DataFrame([user_data], columns=feature_columns)

# Apply same encoding as training
input_df_encoded = pd.get_dummies(input_df)

# Align columns with training data
model_features = model.feature_names_in_ if hasattr(model, "feature_names_in_") else input_df_encoded.columns
input_df_encoded = input_df_encoded.reindex(columns=model_features, fill_value=0)

# ---------------------------
# Predict
# ---------------------------
if st.button("🔮 Predict Price"):
    if "" in user_data.values():
        st.warning("Please fill all fields before predicting.")
    else:
        prediction = model.predict(input_df_encoded)[0]
        st.success(f"💰 Estimated House Price: ₹{prediction:,.2f}")
