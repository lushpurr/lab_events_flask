from flask import render_template, request
from app import app
from app.models.event import * 
from app.models.event_list import events, add_new_event

@app.route('/')
def index():
    return render_template('index.html', title="Event")

@app.route('/add-event', methods=['POST'])
def add_event():
    date = request.form['date']
    name_event = request.form['name_event']
    num_guests = request.form['num_guests']
    room_location = request.form['room_location']
    description = request.form['description']
    event_list = Event(date=date, name_event=name_event, num_guests=num_guests, room_location=room_location, description=description)
    add_new_event(event_list)

    return render_template('index.html', title='Events list', events=events)

    