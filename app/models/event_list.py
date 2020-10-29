from app.models.event import *

event1 = Event("Monday", "Beers", "Four", "Pub", "Relax")
event2 = Event("Tuesday", "wine", "Three", "Wine Bar", "Chat")
events = [event1, event2]

def add_new_event(event):
    events.append(event)
    