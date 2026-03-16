from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


df = pd.read_csv("../heart_new.csv")

@app.route("/")
def dashboard():

    total_patients = len(df)
    heart_cases = df["HeartDisease"].sum()
    avg_bmi = round(df["BMI"].mean(),2)
    avg_sleep = round(df["SleepTime"].mean(),2)

    stats = {
        "patients": total_patients,
        "heart_cases": heart_cases,
        "avg_bmi": avg_bmi,
        "avg_sleep": avg_sleep
    }

    return render_template("index.html",stats=stats)

if __name__ == "__main__":
    app.run(debug=True)