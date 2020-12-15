import pandas as pd
# User Main Menu Function
def main_menu():
    print("\t----------")
    print("\tMAIN MENU")
    print("\t----------")
    print("(1) - Print records from database")
    print("(2) - Access record based on attribute value")
    print("(3) - Sort a report according to art style")
    print("(4) - Show report of customers with similar art preferences")
    print("(5) - Quit")

    # Input validation
    while True:
        try:
            menuChoice = int(input("Enter menu choice: "))
            if menuChoice < 1 or menuChoice > 5:
                raise ValueError
            break
        except ValueError:
            print("That menu choice is not an option. Please try again.")

    if menuChoice == 1:
        return 1
    elif menuChoice == 2:
        return 2
    elif menuChoice == 3:
        return 3
    elif menuChoice == 4:
        return 4

# Menu for getting attributes
def attributeSortMenu():
    print("------------------")
    print("Attribute Sorting")
    print("------------------")
    print("Which table would you like to search in?")
    print("(1) - Customer")
    print("(2) - Artist")
    print("(3) - Art_work")
    print("(4) - Art_Show")
    while True:
        try:
            menuChoice = int(input("Enter table choice: "))
            if menuChoice < 1 or menuChoice > 4:
                raise ValueError
            break
        except ValueError:
            print("That table choice is not an option. Please try again.")

    if menuChoice == 1:
        return 1
    elif menuChoice == 2:
        return 2
    elif menuChoice == 3:
        return 3
    elif menuChoice == 4:
        return 4

# Menu for selecting a column in the customer table
def customerAttribute():
    print("---------------------------")
    print("Customer Table Attributes")
    print("---------------------------")
    print("Which column would you like to search in?")
    print("(1) - Name")
    print("(2) - Customer_Number")
    print("(3) - Phone")
    print("(4) - Art_Preference")
    while True:
        try:
            menuChoice = int(input("Enter table attribute choice: "))
            if menuChoice < 1 or menuChoice > 4:
                raise ValueError
            break
        except ValueError:
            print("That table attribute choice is not an option. Please try again.")

    if menuChoice == 1:
        return 'Name'
    elif menuChoice == 2:
        return 'Customer_Number'
    elif menuChoice == 3:
        return 'Phone'
    elif menuChoice == 4:
        return 'Art_Prefernce'

# Menu for selecting a column in the artist table
def artistAttribute():
    print("---------------------------")
    print("Artist Table Attributes")
    print("---------------------------")
    print("Which column would you like to search in?")
    print("(1) - Name")
    print("(2) - Phone")
    print("(3) - Address")
    print("(4) - Birth_Place")
    print("(5) - Age")
    print("(6) - Style")
    while True:
        try:
            menuChoice = int(input("Enter table attribute choice: "))
            if menuChoice < 1 or menuChoice > 6:
                raise ValueError
            break
        except ValueError:
            print("That table attribute choice is not an option. Please try again.")

    if menuChoice == 1:
        return 'Name'
    elif menuChoice == 2:
        return 'Phone'
    elif menuChoice == 3:
        return 'Address'
    elif menuChoice == 4:
        return 'Birth_Place'
    elif menuChoice == 5:
        return 'Age'
    elif menuChoice == 6:
        return 'Style'

# Menu for selecting a column in the Art_Show table
def artShowAttribute():
    print("---------------------------")
    print("Art_Show Table Attributes")
    print("---------------------------")
    print("Which column would you like to search in?")
    print("(1) - Artist")
    print("(2) - Date")
    print("(3) - Time")
    print("(4) - Location")
    print("(5) - Contact")
    print("(6) - Contact_Phone")
    while True:
        try:
            menuChoice = int(input("Enter table attribute choice: "))
            if menuChoice < 1 or menuChoice > 6:
                raise ValueError
            break
        except ValueError:
            print("That table attribute choice is not an option. Please try again.")

    if menuChoice == 1:
        return 'Artist'
    elif menuChoice == 2:
        return 'Date'
    elif menuChoice == 3:
        return 'Time'
    elif menuChoice == 4:
        return 'Location'
    elif menuChoice == 5:
        return 'Contact'
    elif menuChoice == 6:
        return 'Contact_Phone'

# Menu for selecting a column in the Art_work table
def artWorkAttribute():
    print("---------------------------")
    print("Art_work Table Attributes")
    print("---------------------------")
    print("Which column would you like to search in?")
    print("(1) - Artist")
    print("(2) - Title")
    print("(3) - Type")
    print("(4) - Date_of_Creation")
    print("(5) - Date_Accquired")
    print("(6) - Price")
    print("(7) - Location")
    while True:
        try:
            menuChoice = int(input("Enter table attribute choice: "))
            if menuChoice < 1 or menuChoice > 7:
                raise ValueError
            break
        except ValueError:
            print("That table attribute choice is not an option. Please try again.")

    if menuChoice == 1:
        return 'Artist'
    elif menuChoice == 2:
        return 'Title'
    elif menuChoice == 3:
        return 'Type'
    elif menuChoice == 4:
        return 'Date_of_Creation'
    elif menuChoice == 5:
        return 'Date_Accquired'
    elif menuChoice == 6:
        return 'Price'
    elif menuChoice == 7:
        return 'Location'
    

# Print records for database menu
def choice1():
    print("")
    print("----------------------------")
    print("Print records from database")
    print("----------------------------")
    print("(1) - Show all records")
    print("(2) - Show 'Customer' records")
    print("(3) - Show 'Artist' records")
    print("(4) - Show 'Art_Show' records")
    print("(5) - Show 'Art_work' records")
    print("(6) - Main Menu")
    while True:
        try:
            menuChoice = int(input("Enter menu choice: "))
            if menuChoice < 1 or menuChoice > 6:
                raise ValueError
            break
        except ValueError:
            print("That menu choice is not an option. Please try again.")

    if menuChoice == 1:
        return 1
    elif menuChoice == 2:
        return 2
    elif menuChoice == 3:
        return 3
    elif menuChoice == 4:
        return 4
    elif menuChoice == 5:
        return 5
    elif menuChoice == 6:
        return 6

# Sorting by art style
def choice3():
    print("----------------------")
    print("Sorting by Art Style")
    print("----------------------")
    print("What tables would you like to view sorted art styles from?")
    print("(1) - All Tables")
    print("(2) - Customer Table")
    print("(3) - Artist Table")
    print("(4) - Art_work Table")
    print("(5) - Main Menu")
    while True:
        try:
            menuChoice = int(input("Enter menu choice: "))
            if menuChoice < 1 or menuChoice > 5:
                raise ValueError
            break
        except ValueError:
            print("That menu choice is not an option. Please try again.")

    if menuChoice == 1:
        return 1
    elif menuChoice == 2:
        return 2
    elif menuChoice == 3:
        return 3
    elif menuChoice == 4:
        return 4
    elif menuChoice == 5:
        return 5

def choice4(c):
    print("------------------------------------------")
    print("Customers Interested Particular Art Show")
    print("------------------------------------------")
    
    print("Art_Show table:")

    artShowDF = pd.DataFrame([])
    # Get art_work dataframe
    c.execute("SELECT * FROM Art_Show")
    result = c.fetchall()
    for x in result:
        df = pd.DataFrame([x])
        artShowDF = artShowDF.append(df)
        
    # Rename column labels
    artShowDF = artShowDF.rename(columns={0:"ARTIST", 1:"DATE",
                                            2:"TIME", 3:"LOCATION",
                                        4:"CONTACT", 5:"CONTACT_PHONE"})
    artShowDF = artShowDF.reset_index()
    artShowDF = artShowDF.drop(columns=['index'])
    print(artShowDF)

    while True:
        try:
            menuChoice = int(input("Enter index number of art show: "))
            if menuChoice < 0 or menuChoice > len(result):
                raise ValueError
            break
        except ValueError:
            print("That index is not an option. Please try again.")

    artist_name = artShowDF.iloc[menuChoice]['ARTIST']

    command = "SELECT * FROM Artist WHERE Name = '" + artist_name + "'"
    c.execute(command)
    results = c.fetchall()

    artType = ''

    for x in results:
        temp = pd.DataFrame([x])
        artType = temp.iloc[0][5]

    command = "SELECT * FROM Customer WHERE Art_Preferences = '" + artType + "'"
    c.execute(command)
    results = c.fetchall()

    customerDF = pd.DataFrame([])
    for x in results:
        df = pd.DataFrame([x])
        customerDF = customerDF.append(df)
        
    # Rename column labels
    customerDF = customerDF.rename(columns={0:"NAME", 1:"CUSTOMER_NUMBER",
                                            2:"PHONE", 3:"ART_PREFERENCE"})
    # Print table to console
    print("-----------------")
    print("'Customer' Table")
    print("-----------------")
    print(customerDF)
    





        
