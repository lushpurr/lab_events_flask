from flask import render_template, request, redirect
from app import app
from app.models.event import * 
from app.models.event_list import events, add_new_event, delete_event, clear_all_events

@app.route('/')
def index():
    return render_template('index.html', title="Event", events=events)

@app.route('/add-event', methods=['POST'])
def add_event():
    date = request.form['date']
    nameEvent = request.form['name']
    numGuests = request.form['num_guests']
    roomLocation = request.form['room_location']
    description = request.form['description']
    new_event = Event(date=date, name=nameEvent, num_guests=numGuests, room_location=roomLocation, description=description)
    add_new_event(new_event)
    return redirect('/')

@app.route('/delete/<name>', methods=['POST'])
def delete(name):
    delete_event(name)
    return redirect('/')

@app.route('/clear-all-events', methods=['POST'])
def clear_all(event_list):
    clear_all_events(events_list)
    return redirect('/')