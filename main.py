from models import *
from managers import *


def main():
    a = SymphonyOrchestra("opera", 0, 5000, "Ban", [Instrument.TRUMPET,
                                                    Instrument.CELLO])
    b = CircusShow("opera", 20, 15000, ["dog", "cat"],
                   ["Ben", "Dan"])
    c = Disco("opera", 30, 25000, Color.RED, "techno")
    d = SymphonyOrchestra("opera", 40, 35000, "Ban", [Instrument.TRUMPET,
                                                      Instrument.CELLO])
    l_dbac = [d, b, c, a]
    f = ConcertHallManager(l_dbac)

    f.sort_by_avg_price(SortOrder.ASC)
    f.print_performances()

    f.search_by_musicians_number()
    f.sort_by_musicians_number(SortOrder.DESC)
    f.print_performances()


if __name__ == "__main__":
    main()
