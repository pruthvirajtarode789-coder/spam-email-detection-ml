import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load dataset
df = pd.read_csv("Spam Email Detection - spam.csv")

print("Columns in dataset:", df.columns)

# Detect columns automatically
if 'v1' in df.columns and 'v2' in df.columns:
    y = df['v1']          # spam / ham
    X = df['v2']          # email content

elif 'Category' in df.columns and 'Message' in df.columns:
    y = df['Category']
    X = df['Message']

elif 'label' in df.columns and 'message' in df.columns:
    y = df['label']
    X = df['message']

else:
    raise Exception("❌ Unsupported CSV format. Check column names.")

# Convert text to numbers
vectorizer = TfidfVectorizer(stop_words="english")
X_vec = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vec, y)

# Save model
pickle.dump(model, open("spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Spam model trained successfully")
