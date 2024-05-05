from flask import Flask, render_template
from userdata import *

app = Flask(__name__)

with app.app_context():
    create_tables()

@app.route('/')
def home_page():
    upcoming = get_next_alarm()
    low = get_low()
    return render_template('home.html', upcoming=upcoming, low=low)

@app.route('/alarms')
def alarm_page():
    alarms = get_alarms()
    return render_template('alarm-page.html', alarms=alarms)

# @app.route('/meds/<int:profile_id>')
# def meds_page(profile_id:int):
#     meds = get_medications_from_profile(profile_id)
#     return render_template('med-page.html', meds=meds)

@app.route('/meds')
def meds_page():
    return render_template('test.html', header='Meds page')

@app.route('/profiles')
def profile_page():
    profiles = get_profiles()
    return render_template('profile-page.html', profiles=profiles)

# run locally
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)