from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('test.html', header='Home page')

@app.route('/alarms')
def alarm_page():
    return render_template('test.html', header='Alarm page')

@app.route('/meds')
def meds_page():
    return render_template('test.html', header='Meds page')

@app.route('/profiles')
def profile_page():
    return render_template('test.html', header='Profile page')

# run locally
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)