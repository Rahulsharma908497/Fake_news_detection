from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

# -------------------------
# 1️⃣ Load model & vectorizer
# -------------------------
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# -------------------------
# 2️⃣ Flask setup
# -------------------------
app = Flask(__name__)
CORS(app)

# -------------------------
# 3️⃣ Prediction endpoint
# -------------------------
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    
    if not text.strip():
        return jsonify({"prediction": "⚠️ Please enter the news first"})
    
    if len(text.split()) < 5:
        return jsonify({"prediction": "⚠️ Please enter proper news content"})
    
    # convert text
    text_vector = vectorizer.transform([text])
    
    # prediction
    prediction = model.predict(text_vector)[0]
    
    # result
    if prediction == 0:
        return jsonify({"prediction": "🔴 Fake News"})
    else:
        return jsonify({"prediction": "🟢 Real News"})

# -------------------------
# 4️⃣ Run app
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)