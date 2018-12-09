from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/employee.html')
def employee():
    return render_template('employee.html')


@app.route('/salesperson.html')
def sales_person():
    return render_template('salesperson.html')


@app.route('/mech.html')
def mechanic():
    return render_template('mech.html')


@app.route('/customer.html')
def customer():
    return render_template('customer.html')


@app.route('/car.html')
def car():
    return render_template('car.html')


@app.route('/job.html')
def job():
    return render_template('job.html')


@app.route('/parts.html')
def parts():
    return render_template('parts.html')


if __name__ == '__main__':
    app.run(debug=True)
