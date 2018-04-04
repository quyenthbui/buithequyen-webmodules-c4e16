import mlab
from flask import Flask, render_template
from models.customer import Customer

app = Flask(__name__)
mlab.connect()

@app.route('/customer')
def customer():
    all_customers = Service.objects()
    return render_template('search.html', all_services =all_services )


@app.route('/customer/male10')
def male10():
    best_customers = Customer.objects(gender=1,contacted=False)[:10]
    return render_template('search2.html', all_customers =best_customers )

if __name__ == '__main__':
  app.run(debug=True)
