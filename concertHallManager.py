from sortOrder import SortOrder


class ConcertHallManager:

    def __init__(self, performances=list):
        self.performances = list(performances)

    def search_by_musicians_number(self):
        output = list()
        for i in self.performances:
            if (i.musicians_number != 0):
                output.append(i)
        self.performances = output
        return output

    def sort_by_musicians_number(self, order=SortOrder):
        output = list()
        self.performances.sort(key=lambda c: c.musicians_number, reverse=False)
        output = self.performances
        return output

    def sort_by_avg_price(self, order=SortOrder):
        pass

    def print_performances(self):
        for i in self.performances:
            i.print_info()
            print("----------------------------------------------------------")
