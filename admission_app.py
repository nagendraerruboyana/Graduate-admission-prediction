import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("artifacts\model.pkl")
scaler = joblib.load("artifacts\scaler.pkl")

#Title
st.write(" ## Jamboree Graduate Admission Prediction ")
st.markdown("""
This application predicts a student's chance of admission to a graduate program based on academic scores, application strengths, and research experience.

Upload your profile details and get an instant prediction!
""")

# === Section: Academic Scores ===
st.subheader("Academic Scores", divider="gray")
col_cgpa, col_gre, col_toefl = st.columns(3, border=True)

CGPA = col_cgpa.number_input("Enter CGPA", min_value=0.0, max_value=10.0, step=0.01)
GRE_Score = col_gre.number_input("Enter GRE Score", min_value=260, max_value=340, step=1)
TOEFL_Score = col_toefl.number_input("Enter TOEFL Score", min_value=0, max_value=120, step=1)

# === Section: Application Strengths ===
st.subheader("Application Strengths", divider="gray")
col_lor, col_sop, col_uni = st.columns(3, border=True)

LOR = col_lor.slider('Strength of LOR', min_value=1.0, max_value=5.0, step=0.5)
SOP = col_sop.slider('Strength of SOP', min_value=1.0, max_value=5.0, step=0.5)
University_Rating = col_uni.slider('University Rating', min_value=1, max_value=5, step=1)
Research = st.toggle("Research Experience")

# === Form Submission ===
if st.button("Submit"):
    if CGPA < 6.0 or GRE_Score < 280 or TOEFL_Score < 60:
        st.warning("⚠️ Please note: your academic scores are relatively low; predictions may be less reliable.")

    # Create feature array
    input_features = np.array([[GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, int(Research)]])
    
    # Scale features
    scaled_input = scaler.transform(input_features)
    
    # Predict
    prediction = model.predict(scaled_input)[0]  # Output between 0 and 1
    
    # Show result
    st.success(f"🎯 Predicted Chance of Admission: **{np.round(prediction * 100,2)}%**")