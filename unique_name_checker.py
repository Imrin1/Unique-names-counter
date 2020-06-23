import csv
from spellchecker import SpellChecker

def nameCompare(name1, name2):
    """the function checks by typo's and nicknames if two names are equals. returns false if differnent names and true if equals"""
    spell = SpellChecker(distance = 1)
    nameSet1 = spell.edit_distance_1(name1)
    nameSet2 = spell.edit_distance_1(name2)
    print(nameSet1)
    print(nameSet2)
    candidateSet1 = set()
    candidateSet2 = set()
    with open('nicknames.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            row1 = row[1][1:].lower()
            row2 = row[2][1:].lower()
            for name in nameSet1:
                if name.lower() == row1 or name.lower() == row2:
                    candidateSet1.add(row1)
                    candidateSet1.add(row2)  
                    
            for name in nameSet2:
               if name.lower() == row1 or name.lower() == row2:
                    candidateSet2.add(row1)
                    candidateSet2.add(row2)  
                    
        if len(set.intersection(candidateSet1, candidateSet2))>0:
            return True
        else: return False

def SurNameCompare(name1, name2):
    """checks if two surnames are equals by surnames database and typo's. returns false if differnent names and true if equals"""
    spell = SpellChecker(distance = 1)
    nameSet1 = spell.edit_distance_1(name1)
    nameSet2 = spell.edit_distance_1(name2)
    candidateSet1 = set()
    candidateSet2 = set()
    with open('surnames.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')  
        for row in csv_reader:
            for name in nameSet1:
                if name.lower() == row[0].lower():
                    candidateSet1.add(row[0].lower())  
                    
            for name in nameSet2:
               if name.lower() == row[0].lower():
                    candidateSet2.add(row[0].lower())
                    
        if len(set.intersection(candidateSet1, candidateSet2))>0:
            return True
        else: return False

def uniqueFirstMiddleNameChecker(name1, name2):
    """checks if both first and middle names are equal. returns True if they are and False otherwise"""
    if len(name1.split(' '))==1 or len(name2.split(' '))==1:
        return nameCompare(name1, name2)
    [Fname1 ,Mname1] = name1.split(' ')
    [Fname2 ,Mname2] = name2.split(' ') 
    return nameCompare(Fname1, Fname2) and nameCompare(Mname1, Mname2)

def uniqueFullNameChecker(Fname1,Lname1, Fname2, Lname2):
    """checks if the full names are equal"""
    return uniqueFirstMiddleNameChecker(Fname1, Fname2) and SurNameCompare(Lname1, Lname2)