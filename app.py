import streamlit as st
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load the models
def load_tfidf():
    return pickle.load(open("tf_idf.pkt", "rb"))

def load_model():
    return pickle.load(open("toxicity_model.pkt", "rb"))

# Function for toxicity prediction
def toxicity_prediction(text):
    tfidf = load_tfidf()
    text_tfidf = tfidf.transform([text]).toarray()
    nb_model = load_model()
    prediction = nb_model.predict(text_tfidf)
    return prediction[0]  # Return 1 for toxic, 0 for non-toxic

# Streamlit app setup
st.header("Youtude Video")
st.subheader("Comment")

# Store comments in session state
if 'comments' not in st.session_state:
    st.session_state.comments = []

# Input text for comments
text_input = st.text_area("Enter your comment")

# Button to submit the comment
if st.button("Post"):
    result = toxicity_prediction(text_input)
    
    if result == 1:  # Toxic comment
        st.warning("Detected: The comment was toxic it will be deletd automatically.")
    else:  # Non-toxic comment
        st.session_state.comments.append(text_input)
        st.success("Comment posted!")

# Displaying the comments section
st.subheader("Comment Section")
for comment in st.session_state.comments:
    st.write(comment)
