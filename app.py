from flask import Flask, render_template, request
import pickle

# Load the trained model from file
with open('spam_mail.pickle', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the fitted TF-IDF vectorizer from file
with open('tfidf_vectorizer.pickle', 'rb') as vectorizer_file:
    feature_extraction = pickle.load(vectorizer_file)

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from form
    input_mail = request.form['mail']
    
    # Transform input using the loaded TF-IDF vectorizer
    input_data_features = feature_extraction.transform([input_mail])
    
    # Predict using the loaded model
    prediction = model.predict(input_data_features)
    
    # Determine if it's spam or ham based on prediction result
    if prediction[0] == 1:
        prediction_text = "Ham Mail"
    else:
        prediction_text = "Spam Mail"
    
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
