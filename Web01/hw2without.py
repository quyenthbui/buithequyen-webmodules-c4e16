from flask import Flask,render_template
app = Flask(__name__)

@app.route('/BMI/<int:weight>/<int:height>')
def bmi(weight,height):
    bmi = int(weight)/int(height)/int(height)*10000
    return render_template('bmi.html',bmi = bmi)

if __name__ == '__main__':
  app.run(debug=True)
