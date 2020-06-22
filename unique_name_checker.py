import csv
from spellchecker import SpellChecker

def nameCompare(name1, name2):
    """the function checks if two names are the same and just been misspelled. returns false if differnent names and true if typo"""
    spell = SpellChecker(distance = 1)
    nameLst1 = spell.candidates(name1)
    nameLst2 = spell.candidates(name2)
    candidateSet1 = set()
    candidateSet2 = set()
    with open('nicknames.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            for name in nameLst1:
                if name == row[1].lower() or name == row[2].lower:
                    candidateSet1.add(row[1], row[2]) 

            for name in nameLst2:
               if name == row[1].lower() or name == row[2].lower():
                    candidateSet2.add(row[1], row[2]) 
                    
        if len(set.intersection(candidateSet1, candidateSet2))>0:
            return True
        else: return False
                   

def uniqueFullNameChecker(name1, name2):
    """checks if both first and middle names are equal. returns True if they are and False otherwise"""
    [Fname1 ,Mname1] = name1.split(' ')
    [Fname2 ,Mname2] = name2.split(' ') 
    if Mname1 == '' or Mname2 == '':
        return nameCompare(Fname1, Fname2)
    else : return nameCompare(Fname1, Fname2) and nameCompare(Mname1, Mname2)