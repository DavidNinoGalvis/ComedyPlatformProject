from model.Event import Event

class EventPhilanthropic(Event):
    def __init__(self, name, address, date, opening_time, place_name, city, ticket_office, artist_list=None, sponsor_list=None):
        super().__init__(name, address, date, opening_time, place_name, city, ticket_office, artist_list)
        self.sponsors = sponsor_list if sponsor_list is not None else {}

    def get_total_sponsorship(self):
        return sum(self.sponsors.values())
