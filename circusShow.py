from performance import Performance


class CircusShow(Performance):
    def __init__(self, name, musicians_number, avg_ticket_price, animals:
                 list, acrobats_names: list):

        Performance.__init__(self, name, musicians_number, avg_ticket_price)
        self.animals = animals
        self.acrobats_names = acrobats_names

    def print_info(self):
        print(f"In circus show {self.name} there are "
              f"{self.musicians_number} musicians.\nAverage ticket price is "
              f"{self.avg_ticket_price}.\nHere are the names of acrobats:"
              )
        for i in self.acrobats_names:
            print(i)
        print(f"Here are animals that perform:")
        for i in self.animals:
            print(i)

    def get_animals(self):
        return self.animals

    def get_avg_ticket_price(self):
        return self.avg_ticket_price

    def set_animals(self, animals):
        self.animals = animals

    def set_avg_ticket_price(self, avg_ticket_price):
        self.avg_ticket_price = avg_ticket_price
