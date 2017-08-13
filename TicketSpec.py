__author__ = 'skhsu91'
from datetime import date
from money import Money

class Ticket:
    artistName = ""
    venue = ""
    showDate = date.today()
    originalPrice = Money(amount='9.99', currency='USD')
    popularity = 10
    timeOfYear = 'Summer'


def calculate_rating(ticket):
    if ticket is not None:
        print(ticket.showDate)
        print(ticket.originalPrice)
        return 0


def get_ticket_info(url):
    return 0

calculate_rating(Ticket())
