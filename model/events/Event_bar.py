from model.Event import Event

class EventBar(Event):
    def __init__(self, name, address, date, opening_time, place_name, city, ticket_office, artist_list=None):
        super().__init__(name, address, date, opening_time, place_name, city, ticket_office, artist_list)
        self.artist_payment = None
