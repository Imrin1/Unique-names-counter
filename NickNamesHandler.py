import csv
 
def isNickname(name1, name2):
    """ the function checks if a certain name is a nickname of another or vice-versa"""
    with open('nicknames.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if (name1 == row[1] and name2 == row[2]) or (name1 == row[2] and name2 == row[1]):
                return True

