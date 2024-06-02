class Event:
    def __init__(self, name, address, date, opening_time, place_name, city, ticket_office, artist_list=None):
        self.event_name = name
        self.event_address = address
        self.event_date = date
        self.opening_time = opening_time
        self.place_name = place_name
        self.event_city = city
        self.ticket_office = ticket_office
        self.artist_list = artist_list if artist_list is not None else []

    def add_artist(self, artist):
        self.artist_list.append(artist)

    def remove_artist(self, artist):
        self.artist_list = [a for a in self.artist_list if a.name != artist.name]

    def get_artist_list(self):
        return [str(artist) for artist in self.artist_list]

    def update_event_info(self, name=None, address=None, date=None, opening_time=None, place_name=None, city=None):
        if name:
            self.event_name = name
        if address:
            self.event_address = address
        if date:
            self.event_date = date
        if opening_time:
            self.opening_time = opening_time
        if place_name:
            self.place_name = place_name
        if city:
            self.event_city = city

    def __str__(self):
        return (f"Event: {self.event_name}\n"
                f"Address: {self.event_address}\n"
                f"Date: {self.event_date}\n"
                f"Opening Time: {self.opening_time}\n"
                f"Place: {self.place_name}\n"
                f"City: {self.event_city}\n"
                f"Ticket Office: {self.ticket_office}\n"
                f"Artists: {', '.join(self.get_artist_list())}")
