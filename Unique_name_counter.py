import unique_name_checker

def countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard):
    counter = 3
    str.lower(billFirstName)
    str.lower(billLastName)
    str.lower(shipFirstName)
    str.lower(shipLastName)
    str.lower(billNameOnCard)
    FnameOnCard= '' 
    MnameOnCard = '' 
    LnameOnCard = ''
    if len(billNameOnCard.split(' ')) == 3:
        [FnameOnCard, MnameOnCard, LnameOnCard] = billNameOnCard.split(' ')
        if unique_name_checker.uniqueFullNameChecker(FnameOnCard + " " + MnameOnCard, billFirstName) and unique_name_checker.uniqueFullNameChecker(LnameOnCard, billLastName):
            counter-=1
        else:
            if unique_name_checker.uniqueFullNameChecker(MnameOnCard + " " + LnameOnCard, billFirstName) and unique_name_checker.uniqueFullNameChecker(FnameOnCard, billLastName):
                counter-=1
        if unique_name_checker.uniqueFullNameChecker(FnameOnCard + " " + MnameOnCard, shipFirstName) and unique_name_checker.uniqueFullNameChecker(LnameOnCard, shipLastName):
            counter-=1
        else:
            if unique_name_checker.uniqueFullNameChecker(MnameOnCard + " " + LnameOnCard, shipFirstName) and unique_name_checker.uniqueFullNameChecker(FnameOnCard, shipLastName):
                counter-=1
    if counter == 1:
        return 1
    if len(billNameOnCard.split(' ')) == 2:
        [FnameOnCard, LnameOnCard] = billNameOnCard.split(' ')
        if unique_name_checker.uniqueFullNameChecker(FnameOnCard, billFirstName) and unique_name_checker.uniqueFullNameChecker(LnameOnCard, billLastName):
            counter -= 1
        else:
            if unique_name_checker.uniqueFullNameChecker(LnameOnCard, billFirstName) and unique_name_checker.uniqueFullNameChecker(FnameOnCard, billLastName):
                counter -= 1 
        if unique_name_checker.uniqueFullNameChecker(FnameOnCard, shipFirstName) and unique_name_checker.uniqueFullNameChecker(LnameOnCard, shipLastName):
            counter -= 1
        else:
            if unique_name_checker.uniqueFullNameChecker(LnameOnCard, shipFirstName) and unique_name_checker.uniqueFullNameChecker(FnameOnCard, shipLastName):
                counter -= 1
    if unique_name_checker.uniqueFullNameChecker(billFirstName, shipFirstName) and unique_name_checker.uniqueFullNameChecker(billLastName, shipLastName):
        counter-=1
    return counter
    

        



