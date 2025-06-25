from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/result_form", methods=["GET", "POST"])
def result_form():
    return render_template("result.html")

@app.route("/user_input", methods=["POST"])

def user_input():
    input_data = [{
        "date": request.form.get("date"),
        "sale": float(request.form.get("sales")),
        "num_customer": int(request.form.get("customer_num")),
        "num_staff": int(request.form.get("staffCount")),
        "assign_staff": request.form.get("staffName"),
        "Festival": bool(int(request.form.get("festival")))
    }]
    df = pd.DataFrame(input_data)
    df.to_csv("data/user_input.csv", mode="a", index=False, header=False)
    return "saved"
 
if __name__ == '__main__':
    app.run(debug=True)