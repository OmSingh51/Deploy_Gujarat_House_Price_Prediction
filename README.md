<h1>Gujarat House Price Prediction Project</h1></br>
<h3>Project Overview</h3></br>
<p>This project is a machine learning-based solution for predicting house prices in Gujarat, India. The system uses various regression models to estimate property prices based on features like location, property type, size, and other relevant attributes.</p></br>
</h3>Features</h3>
<p> - Data: Contains real estate data from multiple cities in Gujarat including Ahmedabad, Vadodara, Surat, Rajkot, and Bhavnagar.</br>
<p> - Models: Implements multiple machine learning algorithms:</br>
        - Linear Regression </br>
        - Random Forest</br>
        - XGBoost</br>
        - Support Vector Machine(SVM)</br>
        - Gradient Boosting</br>
<p> - Deployment: The trained models are deployed using Streamlit for easy access and interaction.</p></br>
<h3>Dataset Description</h3></br>
The dataset (gujarat_house_prices.csv) contains the following features:</br>
- City: Location of the property (e.g., Ahmedabad, Vadodara)</br>
- Area: Specific area/neighborhood within the city</br>
- BHK: Number of bedrooms</br>
- Square_Feet: Size of the property in square feet</br>
- Furnishing: Furnishing status (Fully Furnished, Semi-Furnished, Unfurnished)</br>
- Property_Type: Type of property (Apartment, Villa, Independent House)</br>
- Age_of_Property: Age of the property in years</br>
- Price: Target variable - price of the property in INR</br>
<h3>Installation</h3></br>
Install the required dependencies:</br>
    pip install -r requirements.txt</br>
<h3>Usage</h3></br>
1. Run the Streamlit application:</br>
    streamlit run app.py</br>
2. The application will open in your default web browser where you can:</br>
    - Input property details using the interactive form</br>
    - Select which model to use for prediction</br>
    - View the predicted price</br>
<h3>Models Performance</h3></br>
The project includes evaluation metrics for each model (MAE, MSE, R² score) which can be viewed in the application or in the model training code.</br>
<h3>File Structure</h3></br>
project-root/ </br>
│</br>
├── data/</br>
│   └── gujarat_house_prices.csv       # Dataset</br>
│</br>
├── models/</br>
│   ├── linear_model.pkl               # Linear Regression model</br>
│   ├── random_forest.pkl              # Random Forest model</br>
│   ├── svm_model.pkl                  # SVM model</br>
│   ├── xgboost_model.pkl              # XGBoost model</br>
│   └── gradient_boosting.pkl          # Gradient Boosting model</br>
│</br>
├── app.py                             # Streamlit application</br>
├── requirements.txt                   # Dependencies</br>
└── README.md                          # This file</br>