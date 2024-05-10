from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        return render_template('test.html', header=(request.form.get("weight")))
    else:
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