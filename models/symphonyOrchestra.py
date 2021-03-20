from .performance import Performance


class SymphonyOrchestra(Performance):
    def __init__(self, name, musicians_number, avg_ticket_price, soloist_name,
                 instruments):
        Performance.__init__(self, name, musicians_number, avg_ticket_price)
        self.__soloist_name = soloist_name
        self.__instruments = instruments

    def print_info(self):
        print(f"In symphony orchestra {self._name} there are "
              f"{self._musicians_number} musicians.\nSoloist name is "
              f"{self.__soloist_name}.\nAverage ticket price is "
              f"{self._avg_ticket_price}.\nHere are the instruments that are "
              f"used:"
              )
        for i in self.__instruments:
            print(i.name)

    def get_soloist_name(self):
        return self.__soloist_name

    def get_instruments(self):
        return self.__instruments

    def set_soloist_name(self, soloist_name):
        self.__soloist_name = soloist_name

    def set_instruments(self, instruments):
        self.__instruments = instruments
