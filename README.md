# 📧 Email Spam Classifier

A machine learning-based web application that classifies email messages as **Spam** or **Ham**.

---

## 🔗 Deployed Link

**Email Spam Classifier Web App**

https://emailspamclassifier-bhve2aosse5mevnkx4uegp.streamlit.app/

---

## 📖 Project Overview

This project is an email spam classification application built using Scikit-learn. It predicts whether an email is Spam or Ham using TF-IDF Vectorization and a trained machine learning model.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Frontend:** Streamlit
- **Machine Learning:** Scikit-learn
- **Vectorization:** TF-IDF
- **Deployment:** Streamlit Cloud

---

## 📂 Dataset Overview

The dataset contains:

- Email message
- Label (Spam / Ham)

The email text was converted into numerical features using TF-IDF Vectorization before training the model.

---

## 🧠 Model Pipeline

1. **Data Preparation**
   - Loaded and explored the dataset.

2. **Feature Extraction**
   - Applied TF-IDF Vectorization.

3. **Model Training**
   - Trained the MultiNomial NaiveBayes ML Model.
   - Achieved F1 Score of 0.93
   - Saved the trained model and vectorizer.

---

## 💡 How to Use

1. Open the deployed application.
2. Enter an email message.
3. Click **Predict**.
4. The app displays whether the email is **Spam** or **Ham**.

---

## 📁 Project Files

- **app.py** — Streamlit application
- **spam_classifier.pkl** — Trained Multi Nomial Naive Bayes model
- **tfidf_vectorizer.pkl** — Saved TF-IDF vectorizer
- **requirements.txt** — Project dependencies
- **README.md** — Project documentation

---

