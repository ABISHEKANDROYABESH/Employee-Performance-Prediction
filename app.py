from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open("gwp.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        # Collect form data
        features = [
            float(request.form["Quarter"]),
            request.form["Department"],
            request.form["Day"],
            float(request.form["Team"]),
            float(request.form["Targeted Productivity"]),
            float(request.form["SMV"]),
            float(request.form["Incentive"]),
            float(request.form["Over Time"]),
            float(request.form["Idle Time"]),
            float(request.form["Idle Men"]),
            float(request.form["No. of Style Change"]),
            float(request.form["No. of Workers"]),
            request.form["Month"]
        ]
        # Dummy prediction for now (replace with model.predict)
        prediction = "High Performance"
        return render_template("predict.html", prediction=prediction)

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
