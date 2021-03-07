from performance import Performance


class SymphonyOrchestra(Performance):
    def __init__(self, name, musicians_number, avg_ticket_price, soloist_name,
                 instruments: list):
        Performance.__init__(self, name, musicians_number, avg_ticket_price)
        self.soloist_name = soloist_name
        self.instruments = instruments

    def print_info(self):
        print(f"In symphony orchestra {self.name} there are "
              f"{self.musicians_number} musicians.\nSoloist name is "
              f"{self.soloist_name}.\nAverage ticket price is "
              f"{self.avg_ticket_price}.\nHere are the instruments that are "
              f"used:"
              )
        for i in self.instruments:
            print(i)

    def get_soloist_name(self):
        return self.soloist_name

    def get_instruments(self):
        return self.instruments

    def set_soloist_name(self, soloist_name):
        self.soloist_name = soloist_name

    def set_instruments(self, instruments):
        self.instruments = instruments
