from flask import Flask, render_template

app = Flask (__name__)

result=""

@app.route("/bmi/<int:w>/<int:h>")
def add(w, h):
    bmi = w/((h/100)*(h/100))
    if bmi < 16:
        result = "Severely underweight"
    elif 16 <= bmi <18.5:
        result = "Underweight"
    elif 18.5 <= bmi <25:
        result = "Normal"
    elif 25 <= bmi < 30:
        result = "Overweight"
    else:
        result = "Obese"
    return "Your BMI is {0}. {1}".format(bmi, result)

if __name__ == "__main__":
    app.run(debug=True)