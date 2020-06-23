import unittest
import Unique_name_counter

class TestUniqueNameCounter(unittest.TestCase):

    def test_AllEqual(self):
        self.assertEqual(Unique_name_counter.countUniqueNames("Aaron","Roudrigez","Aaron","Roudrigez","Aaron Roudrigez"), 1)
        self.assertEqual(Unique_name_counter.countUniqueNames("Deborah","Egli","Deborah","Egli","Deborah Egli"), 1)

if __name__ == '__main__':
    unittest.main()