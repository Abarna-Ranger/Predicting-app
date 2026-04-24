# =========================================
# MSME Loan Default Prediction App
# =========================================

import streamlit as st
import numpy as np
import os
import joblib
from pathlib import Path

# ================================
# App Config (must be first Streamlit call)
# ================================
st.set_page_config(page_title="MSME Loan Predictor", page_icon="🏢", layout="wide")

# ================================
# ROBUST PATH LOADING FOR STREAMLIT CLOUD
# ================================
BASE_DIR = Path(__file__).resolve().parent

model_path = BASE_DIR / "model.pkl"
scaler_path = BASE_DIR / "scaler.pkl"

@st.cache_resource
def load_model():
    model = joblib.load(str(model_path))
    scaler = joblib.load(str(scaler_path))
    return model, scaler

try:
    model, scaler = load_model()
except Exception as e:
    st.error(f"❌ Error loading model files: {e}")
    st.info("Make sure `model.pkl` and `scaler.pkl` are in the same folder as `app.py` in your GitHub repo.")
    st.stop()

# ================================
# Title
# ================================
st.title("🏢 MSME Loan Default Prediction System")
st.markdown("Fill in the loan details below and click **Predict** to assess default risk.")
st.divider()

# ================================
# Input Section
# ================================
st.subheader("📋 Enter Loan Details")

col1, col2 = st.columns(2)

with col1:
    loan_amount = st.number_input("Loan Amount (₹)", min_value=0, step=10000)
    loan_tenure = st.slider("Loan Tenure (Months)", 1, 120, 24)
    business_size = st.slider("Business Size (Employees)", 1, 500, 10)
    business_type_ui = st.radio("Business Type", ["Manufacturing", "Retail", "Service"])

with col2:
    credit_line_ui = st.selectbox("Existing Credit Line", ["Yes", "No"])
    documentation_ui = st.selectbox("Documentation Quality", ["Complete", "Incomplete"])
    location_ui = st.selectbox("Location", ["Rural", "Semi-Urban", "Urban"])

# ================================
# Encoding
# ================================
business_type = {"Manufacturing": 0, "Retail": 1, "Service": 2}[business_type_ui]
credit_line = 1 if credit_line_ui == "Yes" else 0
documentation = 1 if documentation_ui == "Complete" else 0
location = {"Rural": 0, "Semi-Urban": 1, "Urban": 2}[location_ui]

# ================================
# Prediction
# ================================
st.divider()
if st.button("🔍 Predict", use_container_width=True, type="primary"):

    if loan_amount == 0:
        st.warning("⚠️ Please enter a valid loan amount.")

    elif loan_amount > 20000000 and loan_tenure < 36:
        st.error("🚨 High Risk: Loan amount too high for the given short tenure.")

    elif loan_amount > 50000000:
        st.error("🚨 High Risk: Extremely high loan amount detected.")

    else:
        data = np.array([[loan_amount, loan_tenure, business_size,
                          business_type, credit_line, documentation, location]])
        data_scaled = scaler.transform(data)

        prediction = model.predict(data_scaled)
        prob = model.predict_proba(data_scaled)[0][1]

        st.subheader("📊 Prediction Result")

        col_res1, col_res2 = st.columns(2)
        with col_res1:
            if prediction[0] == 1:
                st.error("🚨 **High Risk: Likely to Default**")
            else:
                st.success("✅ **Low Risk: Safe Loan**")

        with col_res2:
            st.metric(label="Default Probability", value=f"{prob:.2%}")

        st.progress(prob, text=f"Risk Level: {prob:.2%}")
