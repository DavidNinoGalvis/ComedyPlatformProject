import streamlit as st

from model.events.Event_bar import EventBar 
from model.events.Event_philanthropic import EventPhilanthropic
from model.events.Event_theater import EventTheater

class GestionController:
    def __init__(self):
        self.events_bar = {}
        self.events_theater = {}
        self.events_philanthropic = {}
        self.artist = None
    
    def create_event(self,selected_event_type,artist_name,event_name,event_place,event_date,opening_event_time,direccion_event,event_city,diferent):
        pass

    def visualize_event(self, selected_event_type):
        pass
