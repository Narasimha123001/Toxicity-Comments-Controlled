Here’s the **README** with specific sections for the scripts used in your project:

---

# **Toxicity Comments Controlled - Automatic Toxic Comment Detection and Deletion**

## **Project Overview**
"Toxicity Comments Controlled" is an AI-powered system that automatically detects and deletes toxic comments in real-time on social media platforms. It leverages machine learning and NLP to moderate comments, helping reduce negativity online.

## **Key Features**
- Real-time sentiment analysis and toxicity detection of YouTube comments.
- Automatic deletion of toxic comments.
- Integration of FastAPI for serving predictions and Streamlit for a user-friendly interface.
- Scalable to other platforms for toxicity management.

## **Project Structure**

### **1. `collection_of_comments.ipynb`**
- **Purpose**: Collect comments from YouTube videos using the YouTube Data API.
- **Usage**: 
   - Extracts comments from videos using the video URL.
   - Stores comments in `collection_of_comments.csv`.
   - Filters and classifies negative comments for later use.

### **2. `toxicity.ipynb`**
- **Purpose**: Train a machine learning model to classify comments as toxic or non-toxic.
- **Usage**:
   - Loads the collected data (from `collection_of_comments.csv`).
   - Processes comments using TF-IDF (Term Frequency-Inverse Document Frequency).
   - Trains a classifier on the dataset to detect toxic comments.
   - Saves the model (`toxicity_model.pkt`) and the TF-IDF vectorizer (`tf_idf.pkt`) for use in the main application.

### **3. `main.py`**
- **Purpose**: Provide an API for predicting comment toxicity using FastAPI.
- **Usage**:
   - Loads the pre-trained model (`toxicity_model.pkt`) and TF-IDF vectorizer (`tf_idf.pkt`).
   - Exposes endpoints to accept new comments and return predictions on whether they are toxic or not.
   - Supports integration into various platforms for real-time comment moderation.
   
   **Run the FastAPI server**:
   ```bash
   uvicorn main:app --reload
   ```

### **4. `app.py`**
- **Purpose**: Build a front-end user interface using Streamlit for testing the toxicity detection system.
- **Usage**:
   - Provides a user-friendly input field where users can submit comments for toxicity analysis.
   - Connects to the FastAPI backend to make predictions in real-time.
   - Displays whether the comment is toxic or non-toxic and automatically deletes toxic comments from the display.
   
   **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

## **How It Works**
1. **Data Collection**: YouTube comments are collected and stored using the YouTube API.
2. **Toxicity Detection Model**: A custom machine learning model is trained to classify comments as toxic or non-toxic.
3. **Real-Time Prediction**: Users can input comments through the Streamlit app, which communicates with the FastAPI backend for real-time predictions.
4. **Automatic Deletion**: Toxic comments are automatically deleted from the comments section.

## **Installation**

1. Clone the repository:
   ```bash
   git clone https:/Narasimha123001/github.com//toxicity-comments-controlled.git
   ```

2. Navigate to the project folder:
   ```bash
   cd toxicity-comments-controlled
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Replace the placeholder `API_KEY` in `collection_of_comments.ipynb` with your YouTube Data API key.

5. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

6. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## **Requirements**
- Python 3.x
- Pandas
- Scikit-learn
- TextBlob
- FastAPI
- Uvicorn
- Streamlit
- YouTube Data API key

## **Project Goal**
The primary objective of this project is to reduce toxicity in social media environments by automatically detecting and deleting harmful comments in real-time.

