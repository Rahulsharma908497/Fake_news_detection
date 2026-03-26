import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score

# load datasets
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

# add labels
fake["label"] = 0
true["label"] = 1

# merge datasets
data = pd.concat([fake, true])

# combine title and text
data["content"] = data["title"] + " " + data["text"]

# features and labels
X = data["content"]
y = data["label"]

# convert text to numbers
vectorizer = TfidfVectorizer(
    stop_words="english", ngram_range=(1,2), max_df=0.7, max_features=50000
)
X_vector = vectorizer.fit_transform(X)

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vector, y, test_size=0.2, random_state=42
)

# train model
model = PassiveAggressiveClassifier(max_iter=1000, tol=1e-3)
model.fit(X_train, y_train)

# prediction
y_pred = model.predict(X_test)

# accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# save model
pickle.dump(model, open("model.pkl", "wb"))

# save vectorizer
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model and vectorizer saved successfully!")