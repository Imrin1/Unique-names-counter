import unittest
import Unique_name_counter

class TestUniqueNameCounter(unittest.TestCase):
   
    def test_AllEqual(self):
        self.assertEqual(1, Unique_name_counter.countUniqueNames("Deborah","Egli","Deborah","Egli","Deborah Egli"))
        self.assertEqual(1, Unique_name_counter.countUniqueNames("david","Egli","david","Egli","david Egli"))


if __name__ == '__main__':
    unittest.main()