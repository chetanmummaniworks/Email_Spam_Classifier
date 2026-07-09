import streamlit as st
import numpy as np
import pickle

st.set_page_config(
    page_title="Spam Email Detector",
    page_icon="📧",
    layout="centered"
)

with open("spam_classifier.pkl", "rb") as file:
    loaded_model = pickle.load(file)

with open("tfidf_vectorizer.pkl", "rb") as file:
    loaded_vectorizer = pickle.load(file)

st.markdown(
    """
    <h1 style='text-align:center;color:#4CAF50;'>
        📧 Email Spam Classifier
    </h1>
    <p style='text-align:center;font-size:18px;'>
        Detect whether an email is <b>Spam</b> or <b>Ham</b> using Machine Learning.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

email = st.text_area(
    "✉️ Enter Email",
    placeholder="Paste your email message here...",
    height=220
)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    predict_button = st.button(
        "🔍 Check Email",
        use_container_width=True
    )
if predict_button:

    if email.strip() == "":
        st.warning("Please enter an email.")
    else:

        X = loaded_vectorizer.transform([email])
        prediction = loaded_model.predict(X)[0]

        st.divider()

        if prediction == 1:
            st.error("🚨 Spam Email Detected!")

        else:
            st.success("✅ This Email is Safe.")

st.divider()
