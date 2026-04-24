# 🏢 MSME Loan Default Prediction System

A machine learning web app built with **Streamlit** that predicts whether an MSME loan applicant is likely to default, based on key business and loan parameters.

---

## 🚀 Live Demo

👉 [Click here to open the app](https://your-app-link.streamlit.app)

> Replace the link above with your actual Streamlit URL after deployment.

---

## 📌 Features

- Predicts loan default risk (High Risk / Low Risk)
- Shows default probability percentage
- Visual risk progress bar
- Simple and clean UI for loan officers

---

## 🧠 Model Details

| Property | Details |
|---|---|
| Algorithm | Logistic Regression |
| Scaler | Standard Scaler |
| Input Features | 7 |
| Output | Default / No Default |

---

## 📋 Input Features

| Feature | Description |
|---|---|
| Loan Amount (₹) | Total loan amount requested |
| Loan Tenure | Duration in months (1–120) |
| Business Size | Number of employees (1–500) |
| Business Type | Manufacturing / Retail / Service |
| Existing Credit Line | Yes / No |
| Documentation Quality | Complete / Incomplete |
| Location | Rural / Semi-Urban / Urban |

---

## 📁 Project Structure

```
msme-loan-predictor/
├── app.py              # Streamlit application
├── model.pkl           # Trained Logistic Regression model
├── scaler.pkl          # Fitted Standard Scaler
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Requirements

```
streamlit
numpy
scikit-learn==1.7.2
joblib
```

---

## 🛠️ Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/your-username/msme-loan-predictor.git
cd msme-loan-predictor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

---

## ☁️ Deployed On

[Streamlit Community Cloud](https://share.streamlit.io) — Free hosting for Streamlit apps.

---

## 👨‍💻 Author

Made with ❤️ using Python, Scikit-learn, and Streamlit.
