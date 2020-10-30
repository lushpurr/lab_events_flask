from app.models.event import *

event1 = Event("2020-10-17", "Beers", "Four", "Pub", "Relax")
event2 = Event("2020-10-17", "wine", "Three", "Wine Bar", "Chat")
events = [event1, event2]

def add_new_event(event):
    events.append(event)

def delete_event(name):
    event_to_delete = None
    for event in events:
        if event.name == name:
            event_to_delete = event
            break
    events.remove(event) 

def clear_all_events(events):
    events.clear()



 
