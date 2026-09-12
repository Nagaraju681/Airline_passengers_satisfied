import streamlit as st
import joblib

model = joblib.load("logistic_regression_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

st.title("🍴 Amazon Fine Food Sentiment Analysis")

st.write("Enter a food review and predict whether it is Positive or Negative.")

review = st.text_area(
    "Enter your review",
    placeholder="Example: This product tastes great and I really enjoyed it."
)

if st.button("Predict Sentiment"):

    if review.strip() == "":
        st.warning("Please enter a review.")

    else:
        review_tfidf = tfidf.transform([review])

        prediction = model.predict(review_tfidf)[0]

        if prediction == 1:
            st.success("😊 Positive Review")
        else:
            st.error("😞 Negative Review")