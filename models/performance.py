from abc import ABC
from abc import abstractmethod


class Performance(ABC):

    def __init__(self, name, musicians_number, avg_ticket_price):
        self._name = name
        self._musicians_number = musicians_number
        self._avg_ticket_price = avg_ticket_price

    @abstractmethod
    def print_info(self):
        pass

    def get_name(self):
        return self._name

    def set_name(self, _name):
        self._name = _name

    def get_musicians_number(self):
        return self._musicians_number

    def set_musicians_number(self, _musicians_number):
        self._musicians_number = _musicians_number

    def get_avg_ticket_price(self):
        return self._avg_ticket_price

    def set_avg_ticket_price(self, _avg_ticket_price):
        self._avg_ticket_price = _avg_ticket_price
