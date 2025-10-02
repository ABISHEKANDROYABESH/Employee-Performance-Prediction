from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load your trained model (make sure model.pkl exists)
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def index():
    return render_template("home.html", background="images/home_bg.png")

@app.route('/home')
def home():
    return render_template("home.html", background="images/home_bg.png")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            Quarter = int(request.form['Quarter'])
            Department = request.form['Department']
            Day = request.form['Day']
            Team = int(request.form['Team'])
            Targeted_Productivity = float(request.form['Targeted Productivity'])
            SMV = float(request.form['SMV'])
            Incentive = int(request.form['Incentive'])
            Over_Time = int(request.form['Over Time'])
            Idle_Time = int(request.form['Idle Time'])
            Idle_Men = int(request.form['Idle Men'])
            No_of_Style_Change = int(request.form['No. of Style Change'])
            No_of_Workers = int(request.form['No. of Workers'])
            Month = request.form['Month']

            # Example input for prediction (adjust as per your model training)
            input_data = [[Quarter, Team, Targeted_Productivity, SMV, Incentive, Over_Time,
                           Idle_Time, Idle_Men, No_of_Style_Change, No_of_Workers]]
            
            prediction = model.predict(input_data)[0]

            if prediction == 1:
                result = "High Performance"
            else:
                result = "Low Performance"

            return render_template("predict.html", prediction_text=f"Predicted Performance: {result}", background="images/predict_bg.png")
        
        except Exception as e:
            return render_template("predict.html", prediction_text=f"Error: {str(e)}", background="images/predict_bg.png")

    return render_template("predict.html", prediction_text="Submit employee details to get prediction.", background="images/predict_bg.png")

@app.route('/about')
def about():
    return render_template("about.html", background="images/about_bg.png")

@app.route('/submit')
def submit():
    return render_template("submit.html", background="images/submit_bg.png")


if __name__ == "__main__":
    app.run(debug=True)
