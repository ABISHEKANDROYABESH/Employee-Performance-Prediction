from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load trained model
model = pickle.load(open("gwp.pkl", "rb"))

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/submit")
def submit():
    return render_template("submit.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            # Collect form inputs
            data = {
                "Quarter": int(request.form["Quarter"]),
                "Department": request.form["Department"],
                "Day": request.form["Day"],
                "Team": int(request.form["Team"]),
                "Targeted Productivity": float(request.form["Targeted Productivity"]),
                "SMV": float(request.form["SMV"]),
                "Incentive": float(request.form["Incentive"]),
                "Over Time": float(request.form["Over Time"]),
                "Idle Time": float(request.form["Idle Time"]),
                "Idle Men": float(request.form["Idle Men"]),
                "No. of Style Change": int(request.form["No. of Style Change"]),
                "No. of Workers": int(request.form["No. of Workers"]),
                "Month": request.form["Month"]
            }

            # Convert to DataFrame
            df = pd.DataFrame([data])

            # One-hot encode categorical features (align with training features)
            df_processed = pd.get_dummies(df)
            model_features = model.get_booster().feature_names if hasattr(model, "get_booster") else None
            if model_features:
                for col in model_features:
                    if col not in df_processed:
                        df_processed[col] = 0
                df_processed = df_processed[model_features]

            # Prediction
            prediction = model.predict(df_processed)[0]

            # Convert numeric prediction into labels
            if prediction < 0.33:
                label = "Low Productive"
            elif prediction < 0.66:
                label = "Medium Productive"
            else:
                label = "High Productive"

            return render_template("predict.html",
                                   prediction_text=f"Based on the given input, the employee is {label} (Predicted Score: {prediction:.2f})")

        except Exception as e:
            return render_template("predict.html", prediction_text=f"Error: {str(e)}")

    return render_template("predict.html", prediction_text="Please enter details on Home page.")

if __name__ == "__main__":
    app.run(debug=True)
