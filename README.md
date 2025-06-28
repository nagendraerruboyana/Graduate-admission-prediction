# 🎓 Graduate Admission Predictor – Jamboree Business Case

This project builds a machine learning model to predict the probability of a student's admission to graduate programs, based on profile features like GRE, TOEFL, CGPA, SOP strength, and research experience.

It is inspired by a real-world educational use case by **Jamboree**, a leading test prep and admissions service provider.

---

## 🚀 Project Overview

- 📊 Performed exploratory data analysis (EDA) on applicant profiles
- 🤖 Built and evaluated a **Linear Regression** model using Scikit-learn and Statsmodels
- ✅ Checked for model assumptions: normality, multicollinearity, heteroskedasticity
- 🌐 Developed an interactive **Streamlit app** to visualize predictions

---

## 📂 Folder Structure
````
graduate-admission-prediction/
│
├── artifacts/
│   ├── Jamboree_Admission.csv             # Dataset
│   ├── model.pkl                          # Trained linear regression model
│   ├── scaler.pkl                         # StandardScaler for feature scaling
│   └── Jamboree_Business_Case.ipynb      # Jupyter notebook with full analysis
│
├── admission_app.py                       # Streamlit app
├── requirements.txt                       # Dependencies
├── .gitignore                            # To exclude venv, cache files, etc.
└── README.md                             # This file


````

---

## 📌 Features Used

| Feature              | Description                                       |
|----------------------|---------------------------------------------------|
| `GRE_Score`          | GRE test score (0–340)                            |
| `TOEFL_Score`        | TOEFL test score (0–120)                          |
| `University_Rating` | Institutional reputation (1–5)                    |
| `SOP`                | Statement of Purpose strength (1–5)              |
| `LOR`                | Letter of Recommendation strength (1–5)          |
| `CGPA`               | Undergraduate GPA (0–10 scale)                   |
| `Research`           | Research experience (1 = Yes, 0 = No)            |

Target: `Chance_of_Admit` (0 to 1)

---

## ✅ Model Performance

| Metric       | Value        |
|--------------|--------------|
| R² (Train)   | ~0.825       |
| R² (Test)    | ~0.819       |
| MAE          | ~0.043       |
| RMSE         | ~0.053       |

- ✅ Low multicollinearity (VIF < 5 for all features)
- ✅ Normally distributed residuals
- ✅ No significant heteroskedasticity

---

## 🎯 Streamlit Web App

🔗 **Live Demo**: [Click to Launch](https://your-streamlit-url.streamlit.app)

### 📥 How to Run Locally

1. Clone the repo:
```bash
git clone https://github.com/your-username/graduate-admission-prediction.git
cd graduate-admission-prediction
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run admission_app.py
```

---

## 👨‍💻 Tech Stack

* Python 3.10+
* Pandas, NumPy, Seaborn, Matplotlib
* Scikit-learn, Statsmodels
* Streamlit
* Joblib

---

## 📚 Project Motivation

This project simulates a real-world data science workflow for a business case — helping Jamboree provide students with data-driven insights into their admission probabilities. It showcases:

* Applied machine learning (supervised regression)
* Business interpretation of results
* UI/UX thinking through the Streamlit interface

---

## 📬 Contact

📧 Made by \[Nagendra Erruboyana]
🔗 [LinkedIn](https://linkedin.com/in/yourhandle) | [GitHub](https://github.com/yourusername)

```

---

Replace the following placeholders:
- `https://your-streamlit-url.streamlit.app`
- `https://github.com/yourusername/graduate-admission-prediction`
- `[Your Name]`, `[LinkedIn]`, `[GitHub]`