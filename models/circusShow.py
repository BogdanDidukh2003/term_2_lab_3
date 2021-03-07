from .performance import Performance


class CircusShow(Performance):
    def __init__(self, name, musicians_number, avg_ticket_price, animals:
                 list, acrobats_names: list):

        Performance.__init__(self, name, musicians_number, avg_ticket_price)
        self.__animals = animals
        self.__acrobats_names = acrobats_names

    def print_info(self):
        print(f"In circus show {self._name} there are "
              f"{self._musicians_number} musicians.\nAverage ticket price is "
              f"{self._avg_ticket_price}.\nHere are the names of acrobats:"
              )
        for i in self.__acrobats_names:
            print(i)
        print(f"Here are __animals that perform:")
        for i in self.__animals:
            print(i)

    def get_animals(self):
        return self.__animals

    def set_animals(self, animals):
        self.__animals = animals

    def get_acrobats_names(self):
        return self.__acrobats_names

    def set_acrobats_names(self, acrobats_names):
        self.__acrobats_names = acrobats_names
