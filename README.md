# 💻 Laptop Price Predictor

A machine learning-powered web application built with **Streamlit** that predicts laptop market prices based on various hardware specifications such as brand, processor, RAM, storage, and build type with high precision.

---

## 🚀 Live Demo
🔗 **Access the Live App Here:** [Laptop Price Predictor Live](https://laptop-price-predictor-neelesh-verma.streamlit.app/)

---

## 🛠️ Tech Stack & Libraries
- **Language:** Python 🐍
- **Web Framework:** Streamlit
- **Machine Learning & Pipeline:** Scikit-learn, XGBoost
- **Data Manipulation:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Deployment:** Streamlit Community Cloud

---

## ⚙️ Application Features
The web interface is designed with a clean, responsive 3-column layout categorized into:
1. **General Specs:** Brand selection, dynamic Operating System filtering (macOS/Windows/Linux), Laptop Type, and RAM configuration.
2. **Display & Build:** Screen size, resolution, touchscreen support, IPS display, and weight (in kg).
3. **Performance & Storage:** CPU Brand, GPU Brand, SSD storage, and HDD capacity.

---

## 🧠 Machine Learning Approach & Models Explored
During the model development phase in the Jupyter Notebook, multiple regression algorithms were trained and evaluated using **Pipelines** and **ColumnTransformers** to handle categorical encoding seamlessly:
- Linear Regression, Ridge, and Lasso Regression
- K-Nearest Neighbors (KNN)
- Decision Tree & Support Vector Regressor (SVR)
- **Ensemble Techniques:** Random Forest, Extra Trees, AdaBoost, Gradient Boosting, XGBoost, Voting Regressor, and Stacking Regressor.

*(The final deployed model leverages an optimized **Random Forest Regressor** pipeline integrated with log-transformed target pricing for robust predictions).*

---

## 📂 Project Structure
```text
Laptop-Price-Predictor/
│
├── main_app.py               # Main Streamlit web application file
├── laptop_data.csv           # Original dataset used for training
├── Laptop_price_predictor.ipynb  # Jupyter Notebook for EDA & model training
├── df.pkl                    # Pickled dataframe for dropdown options mapping
├── pipe.pkl                  # Trained Machine Learning pipeline model
├── requirements.txt          # Project dependencies and libraries
└── README.md                 # Project documentation
