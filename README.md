**🫀 Heart Disease Prediction Web App**
This project is a Machine Learning-powered Web Application that predicts the likelihood of a person having heart disease based on various health metrics. The app is built using Python, scikit-learn, and Streamlit.

**🚀 Features**
Logistic Regression-based Heart Disease Risk Prediction.

Interactive Web App built with Streamlit.

Exploratory Data Analysis (EDA) with visualizations.

Displays ROC Curve, Confusion Matrix, Feature Importance.

Modular project structure for scalability.

**📊 Dataset**
Dataset: Heart Disease UCI Dataset (Kaggle)

Columns include: Age, Sex, Chest Pain Type, Resting Blood Pressure, Cholesterol, Max Heart Rate, etc.

Target variable: Presence of Heart Disease (1 = Yes, 0 = No)

**🖥️ Installation & Running Locally**
1. Clone the Repository
git clone https://github.com/Nasir-Raza-AI/Heart_Disease_Prediction.git
cd Heart_Disease_Prediction

3. Install Dependencies
pip install -r requirements.txt

5. Train the Model (Generate Model & Scaler)
cd scripts
python train_model.py

7. Run the Streamlit App
cd ../app
streamlit run heart_app.py

**🏷️ Tech Stack**
Python 3.x

Streamlit for frontend UI

scikit-learn for Machine Learning

Pandas & NumPy for data manipulation

Seaborn & Matplotlib for visualizations

**🎯 Project Workflow**
Data Preprocessing & EDA (Jupyter Notebook)

Model Training & Saving Artifacts (train_model.py)

Streamlit Web App for Predictions (heart_app.py)

**📜 License**
This project is licensed under the MIT License.
You are free to use, modify, and distribute this project.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...

**✨ Future Improvements**
Add option to switch between Logistic Regression & Decision Tree.

Deploy the app on Streamlit Cloud or Render.

Add more visualization dashboards for users.

⭐ If you found this project helpful, give it a star on GitHub!
