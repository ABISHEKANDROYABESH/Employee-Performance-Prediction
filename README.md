Employee Performance Prediction (Flask + Machine Learning)
📌 Project Overview

This project predicts Employee Performance (Low, Medium, High) using Machine Learning models trained on the Garment Worker Productivity Dataset.
The model is integrated into a Flask Web Application, deployed on Render, and hosted with a live link.

📂 Dataset

We used the dataset "Productivity Prediction of Garment Employees" from Kaggle.

🔗 Dataset Link: Kaggle - Productivity Prediction of Garment Employees

This dataset contains:

Quarter

Department

Day

Team

Targeted Productivity

SMV

Incentive

Over Time

Idle Time

Idle Men

Style Change

Number of Workers

Month

⚙️ Tools & Environment

Python (via Anaconda) → For running ML libraries & Flask app

Jupyter Notebook → For Exploratory Data Analysis & Model building

Flask → Backend Web framework

HTML/CSS → Frontend Templates

GitHub → Version control & repo hosting

Render → Deployment & Live Demo

🎯 Project Objectives

Build ML models to predict employee performance.

Integrate ML model into a Flask web app.

Deploy application on Render.

Provide a clean UI for user input & prediction output.

🔄 Project Workflow

Data Collection & Cleaning (Kaggle dataset)

Data Preprocessing

Model Building (Linear Regression, Random Forest, XGBoost)

Model Evaluation → Saved best model (gwp.pkl)

Flask Application Development

Frontend (HTML Templates)

Testing & Deployment on Render

📁 Project Structure
Employee-Performance-Prediction/
│── app.py                # Flask main application
│── create_model.py       # Model training script
│── gwp.pkl               # Trained ML model
│── model.pkl             # Backup model
│── requirements.txt      # Dependencies
│── README.md             # Documentation
│
├── templates/            # HTML Templates
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── predict.html
│   └── submit.html
│
├── static/               # Static assets
│   └── images/
│       ├── home_bg.png
│       ├── predict_bg.png
│       ├── submit_bg.png
│       └── about_bg.png
│
└── Dataset/              # Kaggle dataset
    └── garments_worker_productivity.csv

🚀 Deployment on Render

The Flask app is deployed using Render Free Web Service.

🔗 Live Demo: Employee Performance Prediction App

📸 Screenshots
🏠 Home Page

Form for Employee Data Input


ℹ️ About Page

Project details and info


📊 Prediction Output

Result of Employee Performance Prediction


✅ Submission Page

Confirmation after form submission


📊 Example Inputs & Outputs
Example 1 → Low Performance

Input: Targeted Productivity = 0.2, SMV = 10, Incentive = 50
Output: Low Performance

Example 2 → Medium Performance

Input: Targeted Productivity = 0.5, SMV = 15, Incentive = 100
Output: Medium Performance

Example 3 → High Performance

Input: Targeted Productivity = 0.9, SMV = 20, Incentive = 200
Output: High Performance

✅ SmartInternz Deliverables

GitHub Repository: Employee Performance Prediction Repo

Project Documentation: This README.md report

Demo Link: ✅ Live on Render

Screenshots: ✅ Uploaded (see above)

🔮 Future Scope

Database integration for storing inputs/results

Improved UI/UX with better frontend styling

Experiment with Deep Learning models

✍️ Author: Abishek A J
