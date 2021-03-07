from disco import Disco
from symphonyOrchestra import SymphonyOrchestra
from circusShow import CircusShow
from sortOrder import SortOrder
from concertHallManager import ConcertHallManager
from instrument import Instrument
from color import Color


def main():
    a = SymphonyOrchestra("opera", 0, 5000, "Ban", [Instrument.TRUMPET,
                                                    Instrument.CELLO])
    b = CircusShow("opera", 20, 15000, ["dog", "cat"],
                   ["Ben", "Dan"])
    c = Disco("opera", 30, 25000, Color.RED, "techno")
    d = SymphonyOrchestra("opera", 40, 35000, "Ban", [Instrument.TRUMPET,
                                                      Instrument.CELLO])
    l_dbac = [a, b, c, d]
    f = ConcertHallManager(l_dbac)
    f.search_by_musicians_number()
    f.print_performances()
    f.sort_by_musicians_number(SortOrder.ASC)


if __name__ == "__main__":
    main()
