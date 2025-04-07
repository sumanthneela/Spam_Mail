# Spam Mail Prediction

## Project Overview
Spam Mail Prediction is a machine learning-based web application designed to classify email content as either *Spam* or *Not Spam*. This project leverages Natural Language Processing (NLP) techniques and machine learning models to analyze email text and predict its category. The application is built using Python, Flask, and scikit-learn, providing a user-friendly interface for inputting email content and viewing predictions.

## Features
- **Email Classification**: Predicts whether an email is spam or not based on its content.
- **Interactive Web Interface**: Users can input email text via a simple web form.
- **Real-Time Predictions**: Displays classification results immediately after submission.
- **Suggestions**: Offers guidance for safe handling of emails.

## Screenshots
### Output Example 1: Not a Spam Mail

![Screenshot 2025-04-07 at 3 22 39 PM](https://github.com/user-attachments/assets/26171a56-b711-4cef-bb51-866becd06fc0)

### Output Example 2: It's a Spam Mail

![Screenshot 2025-04-07 at 3 24 17 PM](https://github.com/user-attachments/assets/0b03236e-713c-4d44-8230-50070aa27a54)

## Installation and Run Instructions

Follow these steps to get the project running on your local system:

1. Clone the Repository
git clone https://github.com/yourusername/Spam-Mail-Prediction.git
cd Spam-Mail-Prediction

3. Install Required Libraries
It's best to use a virtual environment.

pip install -r requirements.txt

3. Start the Flask App
python app.py

5. Visit in Browser
http://127.0.0.1:5000/predict

You should see the UI to enter email content and test the prediction.

## Future Enhancements
To set up the project locally, follow these steps:

1. Deploy on Heroku or AWS EC2
2. Add email address-based spam features (e.g., blacklist check)
3. Use TF-IDF or word embeddings for better vectorization
4. Implement LSTM or BERT-based models for more contextual accuracy
5.  Add an email parser to accept .eml files
6. Mobile-friendly responsive UI

