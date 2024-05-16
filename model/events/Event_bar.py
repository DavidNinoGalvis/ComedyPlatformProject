from model.Event import Event

class EventBar(Event):
    def __init__(self, event_name, artist_name, event_place,event_date,opening_event_time, direccion_event,event_city,payment) -> None:
        super().__init__(event_name, artist_name, event_place,event_date,opening_event_time, direccion_event,event_city)
        self.artist_payment = payment