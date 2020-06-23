import unittest
from Unique_name_counter import countUniqueNames
from spellchecker import SpellChecker
class TestUniqueNameCounter(unittest.TestCase):

    def test_AllEqual(self):
        self.assertEqual(countUniqueNames("Deborah","Egli","Deborah","Egli","Deborah Egli"), 1)
        self.assertEqual(countUniqueNames("Aaron","Roudrigez","Aaron","Roudrigez","Aaron Roudrigez"), 1)
    
    def test_withNicknames(self):
        self.assertEqual(countUniqueNames("Deborah","Egli","Debbie","Egli","Debbie Egli"), 1)
        self.assertEqual(countUniqueNames("Deborah","Egli","Imri","Egli","Debbie Egli"), 1)
        self.assertEqual(countUniqueNames("Ronnie","Egli","Aaron","Egli","Aaron Egli"), 1)
        self.assertEqual(countUniqueNames("Aaron","Egli","Ronnie","Egli","Aaron Egli"), 1)
        self.assertEqual(countUniqueNames("Ronnie","Egli","Ronnie","Egli","Aaron Egli"), 1)
        
    def test_withMname(self):
        self.assertEqual(countUniqueNames("Deborah S","Egli","Deborah","Egli","Egli Deborah"), 1)
        self.assertEqual(countUniqueNames("Deborah","Egli","Deborah S","Egli","Egli Deborah"), 1)
        self.assertEqual(countUniqueNames("Deborah","Egli","Deborah","Egli","Egli Deborah S"), 1)
        self.assertEqual(countUniqueNames("Deborah","Egli","Deborah Ronnie","Egli","Egli Deborah S"), 2)
    
    def test_withTypo(self):
        self.assertEqual(countUniqueNames("Deborah","Egni","Deborah","Egli","Deborah Egli"), 1)
        self.assertEqual(countUniqueNames("Aaron","Roudrigez","Aaron","Roukrigez","Dave Smith"), 2)
        self.assertEqual(countUniqueNames("Aaron","Roudrigez","Aapon","Roudrigez","Aarok Roudrigez"), 1)

    def test_threeDifferentNames(self):
        self.assertEqual(countUniqueNames("Aaron","Roudrigez","Lidia","Thomas","Debbie Egli"), 3)
    
    def test_twoDifferentNames(self):
        self.assertEqual(countUniqueNames("Michele","Egli","Deborah","Egli","Michele Egli"), 2)

if __name__ == '__main__':
    unittest.main()
    