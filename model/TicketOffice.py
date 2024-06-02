class TicketOffice:
    def __init__(self):
        self.soldTickets = 0
        self.courtesyTickets = 0
        self.tickets = {}

    def createCategory(self, ticketID, ticket):
        self.tickets[ticketID] = ticket

    def updateCategory(self, ticketID, newTicket):
        if ticketID in self.tickets:
            self.tickets[ticketID] = newTicket
        else:
            raise KeyError(f"Ticket ID {ticketID} not found.")

    def setCourtesies(self, numberOfCourtesies):
        self.courtesyTickets = numberOfCourtesies

    def findTicket(self, ticketID):
        return self.tickets.get(ticketID, None)
