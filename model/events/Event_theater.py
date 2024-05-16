from model.Event import Event

class EventTheater(Event):
    def __init__(self, event_name, artist_name, event_place,event_date,opening_event_time, direccion_event,event_city,sponsor_list) -> None:
        super().__init__(event_name, artist_name, event_place,event_date,opening_event_time, direccion_event,event_city)
        self.sponsors = sponsor_list