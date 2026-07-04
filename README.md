
🌸 FastAPI KNN Iris Classification API 

A simple Machine Learning web application built using **FastAPI** that classifies Iris flowers using a trained **K-Nearest Neighbors (KNN)** model.
The project provides a REST API and a basic web interface for predictions.

🚀 Features
- 🌿 Iris flower classification (Setosa, Versicolor, Virginica)
- ⚡ FastAPI backend (high-performance API)
- 🤖 Trained KNN machine learning model
- 🌐 Simple HTML frontend
- 📊 Swagger UI for testing APIs

------------------------------------------------------------------------------------------------------------------------
⚙️ Installation & Setup

1. Clone the repository
  git clone https://github.com/your-username/FASTAPI_KNN.git
  cd FASTAPI_KNN


2. Create virtual environment
  python -m venv venv
  venv\Scripts\activate   # Windows

3. Install dependencies
  pip install -r requirements.txt

▶️ Run the Application
  uvicorn app:app --reload

------------------------------------------------------------------------------------------------------------------------

🌐 Access the App

* Web UI: (http://127.0.0.1:8000)
* API Docs:(http://127.0.0.1:8000/docs)

------------------------------------------------------------------------------------------------------------------------

📊 Example Input

{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}


---------------------------

📌 Example Output

{
  "prediction": "Iris-setosa"
}

------------------------------------

🛠️ Tech Stack

* Python 🐍
* FastAPI ⚡
* Scikit-learn 🤖
* Joblib 💾
* HTML/CSS 🌐

---------------------------------------

Author

Ruqhayya Mehreen
GitHub: [https://github.com/RuqhayyaMehreen](https://github.com/RuqhayyaMehreen)

---------------------------------------------------------------------------------------------------------------------------

⭐ If you like this project, don't forget to star it!

