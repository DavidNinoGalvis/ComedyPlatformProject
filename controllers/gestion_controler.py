from model.events.Event_bar import EventBar
from model.events.Event_philanthropic import EventPhilanthropic
from model.events.Event_theater import EventTheater
from model.Artist import Artist
from model.TicketOffice import TicketOffice
from model.Ticket import Ticket

class GestionController:
    def __init__(self):
        self.events_bar = {}
        self.events_theater = {}
        self.events_philanthropic = {}
        self.artists = {}
        self.event_data_base = []
        self.tickets = []

    def create_ticket(self, price, buyerID, category, phase, saleCode, paymentMethod, refundMethod, isActive=True):
        ticket = Ticket(price, buyerID, category, phase, saleCode, paymentMethod, refundMethod, isActive)
        self.tickets.append(ticket)
        return ticket

    def create_event(self, selected_event_type, name, address, date, opening_time, place_name, city, rating, ticket_price):
        # Crear eventos basado en el tipo seleccionado
        if selected_event_type == "Evento Bar":
            event = EventBar(name, address, date, opening_time, place_name, city, rating, ticket_price)
            self.events_bar[name] = event
            self.event_data_base.append(event)
        elif selected_event_type == "Evento Filantropico":
            event = EventPhilanthropic(name, address, date, opening_time, place_name, city, rating, ticket_price)
            self.events_philanthropic[name] = event
            self.event_data_base.append(event)
        elif selected_event_type == "Evento Teatro":
            event = EventTheater(name, address, date, opening_time, place_name, city, rating, ticket_price)
            self.events_theater[name] = event
            self.event_data_base.append(event)
        else:
            raise ValueError("Invalid event type")
        return event

    def add_artist(self, name, genre):
        artist = Artist(name, genre)
        self.artists[name] = artist
        return artist
    
    def get_artist(self, name):
        return self.artists.get(name)

    def visualize_event(self, selected_event_type, event_name):
        if selected_event_type == "Bar":
            return self.events_bar.get(event_name)
        elif selected_event_type == "Philanthropic":
            return self.events_philanthropic.get(event_name)
        elif selected_event_type == "Theater":
            return self.events_theater.get(event_name)
        else:
            raise ValueError("Invalid event type")

    def list_events(self, selected_event_type):
        if selected_event_type == "Bar":
            return list(self.events_bar.keys())
        elif selected_event_type == "Philanthropic":
            return list(self.events_philanthropic.keys())
        elif selected_event_type == "Theater":
            return list(self.events_theater.keys())
        else:
            raise ValueError("Invalid event type")

    def delete_event(self, selected_event_type, event_name):
        if selected_event_type == "Bar":
            return self.events_bar.pop(event_name, None)
        elif selected_event_type == "Philanthropic":
            return self.events_philanthropic.pop(event_name, None)
        elif selected_event_type == "Theater":
            return self.events_theater.pop(event_name, None)
        else:
            raise ValueError("Invalid event type")

    def update_event(self, selected_event_type, event_name, **kwargs):
        event = self.visualize_event(selected_event_type, event_name)
        if event:
            old_name = event.event_name  # Guardar el nombre antiguo
            for key, value in kwargs.items():
                if hasattr(event, key):
                    setattr(event, key, value)
            new_name = kwargs.get('event_name', event.event_name)
            if old_name != new_name:
                if selected_event_type == "Bar":
                    self.events_bar.pop(old_name)
                    self.events_bar[new_name] = event
                elif selected_event_type == "Philanthropic":
                    self.events_philanthropic.pop(old_name)
                    self.events_philanthropic[new_name] = event
                elif selected_event_type == "Theater":
                    self.events_theater.pop(old_name)
                    self.events_theater[new_name] = event

            return event
        else:
            raise ValueError("Event not found")
        

    def all_events(self):
        return self.event_data_base

    def search_events(self, search_criteria):
        results = []
        for event in self.all_events():
            if self.meets_criteria(event, search_criteria):
                results.append(event)
        return results
    
    def meets_criteria(self, event, search_criteria):
        # Implement your search criteria logic here
        return True  # Placeholder implementation

    def find_event_by_name(self, event_name):
        # Buscar evento por nombre en todas las categorías
        if event_name in self.events_bar:
            return self.events_bar[event_name], "Bar"
        elif event_name in self.events_philanthropic:
            return self.events_philanthropic[event_name], "Philanthropic"
        elif event_name in self.events_theater:
            return self.events_theater[event_name], "Theater"
        else:
            return None, None