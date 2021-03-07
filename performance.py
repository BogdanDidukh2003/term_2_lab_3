from abc import ABC
from abc import abstractmethod


class Performance(ABC):

    def __init__(self, name, musicians_number, avg_ticket_price):
        self.name = name
        self.musicians_number = musicians_number
        self.avg_ticket_price = avg_ticket_price

    @abstractmethod
    def print_info(self):
        pass

    def get_name(self):
        return self.name

    def get_musicians_number(self):
        return self.musicians_number

    def get_avg_ticket_price(self):
        return self.avg_ticket_price

    def set_name(self, name):
        self.name = name

    def set_musicians_number(self, musicians_number):
        self.musicians_number = musicians_number

    def set_avg_ticket_price(self, avg_ticket_price):
        self.avg_ticket_price = avg_ticket_price
