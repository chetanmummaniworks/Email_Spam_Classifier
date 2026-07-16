
# 📧 Email Spam Classifier
A machine learning-powered web application that classifies email messages as **Spam** or **Not Spam (Ham)** using Natural Language Processing (NLP) techniques.

## 🔗 Deployed Link

https://emailspamclassifier-bhve2aosse5mevnkx4uegp.streamlit.app/

## 📖 Project Overview
This project is an email spam detection system built using the **Multinomial Naive Bayes** algorithm. It analyzes the text of an email, applies text preprocessing and TF-IDF vectorization, and predicts whether the email is **Spam** or **Ham**.

## 🛠️ Tech Stack
- **Language:** Python
- **Frontend:** Streamlit
- **Machine Learning Model:** Multinomial Naive Bayes
- **Feature Extraction:** TF-IDF Vectorizer
- **Libraries:** Scikit-learn, Pandas, NumPy, NLTK
- **Deployment:** Streamlit Cloud


## 📂 Dataset Overview
The dataset contains:

- Email text/message
- Target label
  - **0 → Ham (Not Spam)**
  - **1 → Spam**
### Data Preprocessing

The following preprocessing steps were applied:

- Converted text to lowercase
- Tokenization
- Removed special characters
- Removed stopwords
- Applied stemming using Porter Stemmer
- Transformed text using TF-IDF Vectorization

## 🧠 Model Pipeline
### 1. Data Preprocessing

- Cleaned email text
- Removed punctuation and stopwords
- Applied stemming
- Converted processed text into TF-IDF vectors

### 2. Feature Engineering

- TF-IDF Vectorization

### 3. Model Training

- Trained a **Multinomial Naive Bayes** classifier
- Evaluated using classification metrics

### 4. Prediction

- User enters an email message.
- The message is preprocessed.
- TF-IDF transforms the text into numerical features.
- The trained model predicts whether the email is Spam or Ham.

---

## 💡 How to Use
1. Open the deployed Streamlit application.
2. Enter or paste an email message.
3. Click **Predict**.
4. The application displays whether the email is:

- 📩 Ham (Not Spam)
- 🚨 Spam

## 📁 Project Files
- **app.py** — Streamlit application
- **spam_classifier.pkl** — Trained Machine Learning model
- **tfidf_vectorizer.pkl** — Saved TF-IDF Vectorizer
- **requirements.txt** — Project dependencies
- **README.md** — Project documentation


## 📊 Model Performance
Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1 Score
  
