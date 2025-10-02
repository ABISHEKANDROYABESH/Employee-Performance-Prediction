import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# ✅ Load the dummy dictionary model instead of a class
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # For now, return the dummy prediction stored in model.pkl
        return render_template("result.html", prediction=model["predict"])
    return render_template("predict.html")

@app.route('/submit')
def submit():
    return render_template("submit.html")

if __name__ == '__main__':
    app.run(debug=True)
