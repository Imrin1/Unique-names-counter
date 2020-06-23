from unique_name_checker import uniqueFullNameChecker

def countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard):
    """counts the number of unique names in a transaction"""
    counter = 3
    billFirstName.lower()
    billLastName.lower()
    shipFirstName.lower()
    shipLastName.lower()
    billNameOnCard.lower()
    FnameOnCard= '' 
    MnameOnCard = '' 
    LnameOnCard = ''

    #checks for a full name inside the bill name on card
    if len(billNameOnCard.split(' ')) == 3:
        [FnameOnCard, MnameOnCard, LnameOnCard] = billNameOnCard.split(' ')
        if uniqueFullNameChecker(FnameOnCard + " " + MnameOnCard, LnameOnCard, billFirstName, billLastName):
            counter-=1
        else:
            if uniqueFullNameChecker(MnameOnCard + " " + LnameOnCard, FnameOnCard, billFirstName, billLastName):
                counter-=1
        if uniqueFullNameChecker(FnameOnCard + " " + MnameOnCard, LnameOnCard, shipFirstName, shipLastName):
            counter-=1
        else:
            if uniqueFullNameChecker(MnameOnCard + " " + LnameOnCard, FnameOnCard, shipFirstName, shipLastName):
                counter-=1
    if counter == 1:
        return counter
    
    #checks for name without middle name  inside the bill name on card
    if len(billNameOnCard.split(' ')) == 2:
        [FnameOnCard, LnameOnCard] = billNameOnCard.split(' ')
        if uniqueFullNameChecker(FnameOnCard,LnameOnCard, billFirstName, billLastName):
            counter -= 1
        else:
            if uniqueFullNameChecker(LnameOnCard,FnameOnCard, billFirstName, billLastName):
                counter -= 1 
        if uniqueFullNameChecker(FnameOnCard, LnameOnCard, shipFirstName, shipLastName):
            counter -= 1
        else:
            if uniqueFullNameChecker(LnameOnCard, FnameOnCard, shipFirstName, shipLastName):
                counter -= 1
    if counter == 1:
        return counter
    
    if uniqueFullNameChecker(billFirstName, billLastName, shipFirstName, shipLastName):
        counter-=1
    return counter
    

        



