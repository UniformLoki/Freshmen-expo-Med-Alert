<<<<<<< HEAD
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        return render_template('test.html', header=(request.form.get("weight")))
    else:
        return render_template('test.html', header='Home page')
=======
from flask import Flask, render_template, redirect, request, url_for
from userdata import *
from datetime import datetime

app = Flask(__name__)

with app.app_context():
    create_tables()

# VISIBLE ROUTES

@app.route('/')
def home_page():
    upcoming = get_next_alarm()
    low = get_low()
    return render_template('home.html', upcoming=upcoming, low=low)
>>>>>>> sql

@app.route('/alarms')
def alarm_page():
    alarms = get_alarms()
    return render_template('alarm-page.html', alarms=alarms)

@app.route('/meds', methods=['GET','POST'])
def meds_page():
    profiles = get_profiles()
    if request.method == 'POST':
        profile_id = int(request.form['profile_id'])
        meds = get_medications_from_profile(profile_id)
        if len(meds) > 0:
            schedules = {}
            for med in meds:
                schedules[med.id] = get_formatted_schedule(med.id)
            return render_template('med-page.html', profiles=profiles, sel_profile=profile_id, meds=meds, schedules=schedules)
        else:
            return render_template('med-page.html', profiles=profiles, sel_profile=profile_id)
    else:
        profile_id = profiles[0].id
        meds = get_medications_from_profile(profile_id)
        if len(meds) > 0:
            schedules = {}
            for med in meds:
                schedules[med.id] = get_schedule(med.id)
            return render_template('med-page.html', profiles=profiles, sel_profile=profile_id, meds=meds, schedules=schedules)
        else:
            return render_template('med-page.html', profiles=profiles, sel_profile=profile_id)
    
@app.route('/medication-settings', methods=['GET', 'POST'])
def medication_settings():
    if request.method == 'POST':
        med_id = request.form['med_id']

        update_med_name(med_id, request.form['name'])
        update_med_profile(med_id, request.form['profile_id'])
        update_dose(med_id, request.form['dose'])
        update_pill_weight(med_id, request.form['weight'])
        update_full_amount(med_id, request.form['amount'])

        timeslots = int(request.form['timeslot_count'])
        print(f"\n\n{timeslots}\n\n")
        schedule = [request.form[f'timeslot-{i}'] for i in range(timeslots)]
        update_schedule(med_id, schedule)
            
        return redirect(url_for('meds_page'))
    else:
        med_id = request.args.get('med_id')
        med = get_medication(med_id)
        schedule = get_schedule(med_id)
        profiles = get_profiles()
        return render_template('med-form.html', med=med, schedule=schedule, profiles=profiles, function='Update Medication')

@app.route('/new-medication', methods=['GET', 'POST'])
def new_medication():
    if request.method == 'POST':
        name = request.form['name']
        profile_id = request.form['profile_id']
        dose = request.form['dose']
        weight = request.form['weight']
        amount = request.form['amount']

        timeslots = int(request.form['timeslot_count'])
        schedule = [request.form[f'timeslot-{i}'] for i in range(timeslots)]

        add_medication(profile_id, name, dose, amount, weight, schedule)
        return redirect(url_for('meds_page'))
    else:
        profiles = get_profiles()
        return render_template('med-form.html', profiles=profiles, function='Create Medication')

@app.route('/profiles')
def profile_page():
    profiles = get_profiles()
    return render_template('profile-page.html', profiles=profiles)

@app.route('/new-profile', methods=['GET','POST'])
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
    
@app.route('/running-alarm/<profile_id>/<med_id>/<return_to>')
def running_alarm(profile_id, med_id, return_to):
    # profile_id = request.args.get('profile_id')
    # med_id = request.args.get('med_id')
    # return_to = request.args.get('from')

    time = datetime.strftime(datetime.now(), "%I:%M %p")
    profile = get_profile(profile_id)
    med = get_medication(med_id)

    return render_template('running-alarm.html', time=time, profile=profile, med=med, return_to=return_to)


# run locally
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)