# spam_detector.py

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Step 1: Sample dataset
data = [
    ("Free entry in 2 a weekly competition", "spam"),
    ("Win cash now!!!", "spam"),
    ("Call your mom today", "not spam"),
    ("Meeting at 10am", "not spam"),
    ("You have won a free ticket", "spam"),
    ("Lunch at 1?", "not spam")
]

texts, labels = zip(*data)

# Step 2: Convert text into features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Step 3: Train model
model = MultinomialNB()
model.fit(X, labels)

# Function for prediction
def predict_message(message):
    vec = vectorizer.transform([message])
    return model.predict(vec)[0]
