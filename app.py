from flask import Flask, render_template, request

app = Flask(__name__)   # ✅ app is defined first

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/predict', methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        # Collect form data
        data = {
            "Quarter": request.form["Quarter"],
            "Department": request.form["Department"],
            "Day": request.form["Day"],
            "Team": request.form["Team"],
            "Targeted Productivity": request.form["Targeted Productivity"],
            "SMV": request.form["SMV"],
            "Incentive": request.form["Incentive"],
            "Over Time": request.form["Over Time"],
            "Idle Time": request.form["Idle Time"],
            "Idle Men": request.form["Idle Men"],
            "No. of Style Change": request.form["No. of Style Change"],
            "No. of Workers": request.form["No. of Workers"],
            "Month": request.form["Month"],
        }

        # Simple rule-based prediction for testing
        prod = float(data["Targeted Productivity"])
        if prod < 0.3:
            prediction = "Low Performance"
        elif prod < 0.7:
            prediction = "Medium Performance"
        else:
            prediction = "High Performance"

        return render_template("predict.html", prediction=prediction)
    else:
        return render_template("home.html")

@app.route('/submit')
def submit():
    return render_template("submit.html")

if __name__ == "__main__":
    app.run(debug=True)
