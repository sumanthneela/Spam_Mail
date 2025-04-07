import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
raw_mail_data = pd.read_csv('mail_data.csv')
mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)), '')

# Label encoding: spam = 0, ham = 1
mail_data.loc[mail_data['Category'] == 'spam', 'Category'] = 0
mail_data.loc[mail_data['Category'] == 'ham', 'Category'] = 1

# Features (X) and Labels (Y)
X = mail_data['Message']
Y = mail_data['Category']

# Split data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

# Fit TF-IDF Vectorizer on training data
feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
X_train_features = feature_extraction.fit_transform(X_train)  # Fit and transform training data
X_test_features = feature_extraction.transform(X_test)        # Transform test data

# Convert labels to integers
Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train_features, Y_train)

# Evaluate model accuracy on training data
training_accuracy = accuracy_score(Y_train, model.predict(X_train_features))
print('Accuracy on training data:', training_accuracy)

# Save both the trained model and fitted TF-IDF vectorizer
with open('spam_mail.pickle', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('tfidf_vectorizer.pickle', 'wb') as vectorizer_file:
    pickle.dump(feature_extraction, vectorizer_file)

print("Model and vectorizer saved successfully!")
