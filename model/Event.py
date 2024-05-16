
class Event:
    def __init__(self, name, artist_list, place,date,opening_event_time, direccion,city):
        self.event_name = name
        self.artist = artist_list
        self.event_place = place
        self.event_date = date  
        self.opening_time = opening_event_time
        self.direccion_event = direccion
        self.event_city = city