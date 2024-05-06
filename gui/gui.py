from flask import Flask, render_template, redirect, request, url_for
from userdata import *

app = Flask(__name__)

with app.app_context():
    create_tables()

# VISIBLE ROUTES

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

@app.route('/new_profile', methods=['GET','POST'])
def new_profile():
    if request.method == 'POST':
        name = request.form['name']
        birthdate = request.form['birthdate']
        email = request.form['email']
        phone = request.form['phone']

        if request.form['paired'] == "True":
            contact_name = request.form['contact-name']
            if request.form['contact-relation'] == "Other":
                contact_relation = request.form['contact-relation-other']
            else:
                contact_relation = request.form['contact-relation']
            contact_email = request.form['contact-email']
            contact_phone = request.form['contact-phone']

            add_profile(name, birthdate, email, phone, True, contact_name, contact_relation, contact_email, contact_phone)
        else:
            add_profile(name, birthdate, email, phone, False)

        return redirect(url_for('profile_page'))

    else:
        return render_template('profile-form.html', function='Create profile', action=url_for('new_profile'))

@app.route('/profile-settings', methods=['GET','POST'])
def profile_settings():
    if request.method == 'POST':
        profile_id = int(request.form['profile_id'])
        old_profile = get_profile(profile_id)
        print(f"{old_profile.name} paired: {old_profile.paired}")

        update_name(profile_id, request.form['name'])
        update_birthdate(profile_id, request.form['birthdate'])
        update_email(profile_id, request.form['email'])
        update_phone(profile_id, request.form['phone'])

        if request.form['paired'] == "True":
            contact_name = request.form['contact-name']
            if request.form['contact-relation'] == "Other":
                contact_relation = request.form['contact-relation-other']
            else:
                contact_relation = request.form['contact-relation']
            contact_email = request.form['contact-email']
            contact_phone = request.form['contact-phone']

            if old_profile.paired == 0:
                update_paired(profile_id, True, contact_name, contact_relation, contact_email, contact_phone)
            else:
                contact_id = old_profile.contact.id
                update_contact_name(contact_id, contact_name)
                update_contact_relation(contact_id, contact_relation)
                update_contact_email(contact_id, contact_email)
                update_contact_phone(contact_id, contact_phone)
        else:
            if old_profile.paired != 0:
                update_paired(profile_id, False)

        return redirect(url_for('profile_page'))

    else:
        profile_id = request.args.get('profile_id')
        profile = get_profile(profile_id)
        return render_template('profile-form.html', profile=profile, function='Update Profile', action=url_for('profile_settings'))

# run locally
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)