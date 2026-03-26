## fake news detection
## ⚙️ Backend Setup (Python)
Step 1: Go to backend folder
cd backend
Step 2: Install dependencies
pip install -r requirements.txt
Step 3: Download required files

Run these commands inside the backend folder:

curl -L "https://drive.google.com/uc?export=download&id=YOUR_MODEL_ID" -o model.pkl
curl -L "https://drive.google.com/uc?export=download&id=YOUR_VECTOR_ID" -o vectorizer.pkl

👉 Also download dataset files (Fake.csv, True.csv) and place them inside the backend folder.

Step 4: Run backend server
python app.py
## 💻 Frontend Setup (React + Vite)
Step 1: Go to frontend folder
cd 01-project
Step 2: Install dependencies
npm install
Step 3: Run frontend
npm run dev

