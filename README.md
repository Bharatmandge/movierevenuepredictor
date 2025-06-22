# 🎬 Movie Revenue Predictor

A Machine Learning-powered web app built using **Streamlit** that predicts the box office revenue of a movie based on various features like budget, cast, crew, genre, runtime, and more. The model is trained on real-world movie data from TMDB.

---

## 📌 Features

- ✅ Cleaned and preprocessed TMDB dataset  
- 📊 Exploratory Data Analysis (EDA) using Jupyter Notebooks  
- 🤖 Machine Learning model for revenue prediction  
- 💻 Interactive Streamlit web application  
- 💾 Model training & saving using joblib/pickle  
- 📈 Real-time predictions using user inputs  

---

## 🧠 Tech Stack

| Layer        | Tools Used                          |
|--------------|-------------------------------------|
| Language     | Python 3.10                         |
| Libraries    | Pandas, NumPy, Scikit-learn, Seaborn|
| Visualization| Matplotlib, Seaborn                 |
| ML Model     | Linear Regression / Random Forest   |
| Web App      | Streamlit                           |
| Others       | Jupyter Notebook, Git, GitHub       |

---

## 🗂️ Project Structure

movie-revenue-predictor/
│
├── data/ # Raw & processed data
│ └── raw/
│
├── models/ # Saved ML models (.pkl)
│
├── notebooks/ # Jupyter notebooks for EDA & Modeling
│ ├── 1_EDA.ipynb
│ └── 2_Modeling.ipynb
│
├── src/ # Scripts for data preprocessing and training
│ ├── preprocess.py
│ └── train_model.py
│
├── app/ # Streamlit web app
│ └── streamlit_app.py
│
├── requirements.txt # Dependencies
└── README.md

yaml
Copy
Edit

---

## 🚀 How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/Bharatmandge/movierevenuepredictor.git
cd movierevenuepredictor
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Streamlit App
bash
Copy
Edit
streamlit run app/streamlit_app.py
The app will open in your default browser at http://localhost:8501

📊 Dataset Used
TMDB 5000 Movies Dataset

Source: Kaggle - TMDB Movie Dataset



⚙️ Model Performance
Metric	Value
R² Score	~0.82
MAE	~18 Million USD
Algorithm	Random Forest

🙋‍♂️ Author
Bharat Mandge
🎓 Aspiring Data Scientist
🌐 GitHub
🔗 LinkedIn(https://www.linkedin.com/in/bharat-mandge/)
