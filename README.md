# Spam Mail Prediction

## Project Overview
Spam Mail Prediction is a machine learning-based web application that classifies email content as either *Spam* or *Not Spam*. This project leverages Natural Language Processing (NLP) techniques and machine learning models to analyze email text and predict its category. The application is built using Python, Flask, and scikit-learn, providing a user-friendly interface for inputting email content and viewing predictions.

## Project Objective

The objective of this project is to **identify spam emails** using historical data and a trained machine learning model. Spam emails often follow recognizable patterns like promotional language, urgency, suspicious links, and prize announcements. By training a model to recognize these patterns, this system can help users determine if an email is safe to read or should be marked as spam.

## Problem Statement

Spam mails not only clutter our inboxes but may also contain malicious links, phishing attempts, or fraud schemes. Traditional rule-based systems are limited and can’t adapt quickly. This project aims to:

- Automatically classify emails based on their content
- Build a lightweight yet effective web application
- Utilize natural language techniques for robust feature extraction
- Provide real-time results to users through an interactive UI

## Key Features

- Classifies email content as **Spam** or **Not Spam**
- Handles text cleaning using NLP techniques like:
  - Lowercasing
  - Removing punctuation
  - Stopword removal
  - Stemming
- Trained on thousands of labeled emails for high accuracy
- User interface developed with Flask + HTML/CSS
- Gives prediction with confidence and safety suggestions
- Visual examples of inputs and results

## Screenshots
### Output Example 1: Not a Spam Mail

An informative or professional message that is identified as safe.

![Screenshot 2025-04-07 at 3 22 39 PM](https://github.com/user-attachments/assets/26171a56-b711-4cef-bb51-866becd06fc0)

### Output Example 2: It's a Spam Mail

A message with suspicious language patterns, fake prizes, urgency — flagged as spam.

![Screenshot 2025-04-07 at 3 24 17 PM](https://github.com/user-attachments/assets/0b03236e-713c-4d44-8230-50070aa27a54)

## 🛠 Technologies Used

| Layer              | Tools / Libraries |
|--------------------|-------------------|
| Programming Language | Python |
| Data Processing     | Pandas, NumPy |
| NLP Tools           | NLTK (Stopwords, PorterStemmer, Tokenization) |
| Vectorization       | CountVectorizer (Bag of Words model) |
| ML Model            | Logistic Regression |
| Web Framework       | Flask |
| Frontend            | HTML5, CSS3 |
| Model Deployment    | Localhost via Flask |

---

### 🧠 Model Details

- Model Used: **Logistic Regression**
- Accuracy: ~97% (can vary based on preprocessing and split)
- Fast and lightweight — perfect for real-time inference


## Application Workflow

1. User enters email content into the form.
2. Text is preprocessed and vectorized.
3. Preprocessed vector is passed to the ML model.
4. Prediction is returned: **Spam** or **Not Spam**.
5. UI shows result with color-coded message and safety tips.

---

## Installation and Run Instructions 

Follow these steps to get the project running on your local system:

1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/Spam-Mail-Prediction.git
   cd Spam-Mail-Prediction
   ```

2. **Install Dependencies**
   It's best to use a virtual environment.
   
   ```sh
   pip install -r requirements.txt
   ```

4. **Start the Flask App**  
   ```sh
   python app.py
   ```

5. **Visit in Browser**
     
   ```sh
   http://127.0.0.1:5000
   ```

---
You should see the UI to enter email content and test the prediction.

## Future Enhancements
To set up the project locally, follow these steps:

1. Deploy on Heroku or AWS EC2
2. Add email address-based spam features (e.g., blacklist check)
3. Use TF-IDF or word embeddings for better vectorization
4. Implement LSTM or BERT-based models for more contextual accuracy
5.  Add an email parser to accept .eml files
6. Mobile-friendly responsive UI

## Project Structure

```bash
Spam-Mail-Prediction/
│
├── app.py                    # Main Flask application
├── main.py                   # Script to train & save the model
├── mail_data.csv             # Dataset used for training
├── spam_mail.pickle          # Serialized ML model (MultinomialNB)
├── tfidf_vectorizer.pickle   # Serialized TF-IDF vectorizer
├── Testing.ipynb             # Jupyter Notebook with EDA & testing
│
├── templates/
│   └── index.html            # HTML template for the web interface
│
├── static/
│   ├── css/
│   │   └── main.css          # CSS styling for frontend
│   └── js/
│       └── scripts.js        # Optional JS scripts
│
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── .gitignore                # Git ignored files
└── venv/                     # Python virtual environment (optional)


