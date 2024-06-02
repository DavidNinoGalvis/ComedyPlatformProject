from model.Event import Event

class EventTheater(Event):
    def __init__(self, name, address, date, opening_time, place_name, city, ticket_office, artist_list=None, ticket_price=0.0):
        super().__init__(name, address, date, opening_time, place_name, city, ticket_office, artist_list)
        self.ticket_price = ticket_price
        self.loss_percentage = 0.07  # 7% loss per ticket sold

    def calculate_net_revenue(self, tickets_sold):
        gross_revenue = tickets_sold * self.ticket_price
        net_revenue = gross_revenue * (1 - self.loss_percentage)
        return net_revenue