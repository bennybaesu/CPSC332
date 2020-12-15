import mysql.connector
import pandas as pd
import menu
import data

# Connect to the database
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='MySQL_1234',
    database='Art_Gallery')

# Set cursor
c = mydb.cursor()

# Print welcome message
print("--------------------------------------------")
print("Welcome to the Art Gallery Database Viewer")
print("--------------------------------------------")

while True:
    # Start main menu
    choice = menu.main_menu()

    # Print records for database menu
    if choice == 1:
        while True:
            x = menu.choice1()

            # Show all records
            if x == 1:
                data.showAll(c)
                input("Press Enter to continue")
            elif x == 2:
                data.showCustomer(c)
                input("Press Enter to continue")
            elif x == 3:
                data.showArtist(c)
                input("Press Enter to continue")
            elif x == 4:
                data.showArtShow(c)
                input("Press Enter to continue")
            elif x == 5:
                data.showArtWork(c)
                input("Press Enter to continue")
            else:
                break
    elif choice == 2:
        data.attributeSort(c)
    elif choice == 3:
        x = menu.choice3()
        if x == 1:
            data.sortByArtStyle(c, 'all')
            input("Press Enter to continue...")
        elif x == 2:
            data.sortByArtStyle(c, 'Customer')
            input("Press Enter to continue...")
        elif x == 3:
            data.sortByArtStyle(c, 'Artist')
            input("Press Enter to continue...")
        elif x == 4:
            data.sortByArtStyle(c, 'Art_work')
            input("Press Enter to continue...")
        
            
    elif choice == 4:
        menu.choice4(c)
        input("Press Enter to continue...")
    else:
        break
        





        

