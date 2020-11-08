from app import app
from flask import render_template, url_for
from app.goog_cal import service, get_todays_events

@app.route('/')
@app.route('/index')
def index():

    todays_events = get_todays_events(service=service)

    return render_template('index.html', todays_events=todays_events)