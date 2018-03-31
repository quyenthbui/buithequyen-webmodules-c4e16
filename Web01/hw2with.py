from flask import Flask
app = Flask(__name__)

@app.route('/BMI/<int:weight>/<int:height>')
def bmi(weight,height):
    bmi = str(int(weight)/int(height)/int(height)*10000)
    if float(bmi) < 16 :
        return bmi + 'Severely underweight'
    elif 16 <= float(bmi) < 18.5:
        return bmi + 'Underweight'
    elif 18.5 <= float(bmi) < 25:
        return bmi + 'Normal'
    elif 25 <= float(bmi) < 30:
        return bmi + 'Overweight'
    elif float(bmi) > 30:
        return bmi + 'Obese'

    return

if __name__ == '__main__':
  app.run(debug=True)
