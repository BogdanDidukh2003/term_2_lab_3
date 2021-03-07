class ConcertHallManager:

    def __init__(self, performances=list):
        self.__performances = performances

    def search_by_musicians_number(self):
        output = list()
        for i in self.__performances:
            if (i._musicians_number != 0):
                output.append(i)
        self.__performances = output
        return output

    def sort_by_musicians_number(self, order):
        output = list()
        self.__performances.sort(key=lambda c: c.get_musicians_number(),
                                 reverse=bool(order.value))
        output = self.__performances
        return output

    def sort_by_avg_price(self, order):
        output = list()
        self.__performances.sort(key=lambda c: c.get_avg_ticket_price(),
                                 reverse=bool(order.value))
        output = self.__performances
        return output

    def print_performances(self):
        for i in self.__performances:
            i.print_info()
            print("----------------------------------------------------------")
        print("\n\n\n")
