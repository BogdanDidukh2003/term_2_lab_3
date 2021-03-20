import unittest
from managers import *
from models import *


class TestConcertHallManager(unittest.TestCase):

    def setUp(self):
        result = list()
        self.a = SymphonyOrchestra("opera", 0, 5000, "Ban", [
                                   Instrument.TRUMPET, Instrument.CELLO])
        self.b = CircusShow("opera", 20, 15000, ["dog", "cat"], ["Ben", "Dan"])
        self.c = Disco("opera", 30, 25000, Color.RED, "techno")
        self.d = SymphonyOrchestra("opera", 40, 35000, "Ban",
                                   [Instrument.TRUMPET, Instrument.CELLO])
        result = [self.d, self.b, self.c, self.a]

        self.concertHallManager = ConcertHallManager(result)
        self.maxDiff = None

    def test_search_by_musicians_number(self):
        self.assertEqual(self.concertHallManager.search_by_musicians_number(),
                         [self.d, self.b, self.c])

    def test_sort_by_musicians_number(self):
        self.assertEqual(
            self.concertHallManager.sort_by_musicians_number(SortOrder.DESC),
            [self.d, self.c, self.b, self.a]
        )

    def test_sort_by_avg_price(self):
        self.assertEqual(
            self.concertHallManager.sort_by_avg_price(SortOrder.ASC),
            [self.a, self.b, self.c, self.d]
        )


if __name__ == "__main__":
    unittest.main()
