from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# ✅ Define DummyModel so pickle can load it
class DummyModel:
    def predict(self, X):
        return ["High Performance"]  # Default dummy output

# ✅ Safe load of model.pkl
model_path = "model.pkl"
if os.path.exists(model_path):
    with open(model_path, "rb") as f:
        try:
            model = pickle.load(f)
        except Exception:
            # Fallback to DummyModel if pickle fails
            model = DummyModel()
else:
    model = DummyModel()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        try:
            # Example: just using dummy features
            features = [int(x) for x in request.form.values()]
            prediction = model.predict([features])[0]
        except Exception as e:
            prediction = f"Error: {str(e)}"

        return render_template("result.html", prediction=prediction)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
