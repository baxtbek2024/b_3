from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/agecalc", methods=["GET", "POST"])
def agecalc():
    if request.method == "POST":
        year = int(request.form["year"])

        current_year = datetime.datetime.now().year

        age = current_year - year

        return render_template("result24.html", age=age)

    return render_template("index24.html")

if __name__ == "__main__":
    app.run(debug=True)
