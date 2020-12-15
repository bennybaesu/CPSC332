import pandas as pd
import menu
import mysql.connector

def showCustomer(c):
    customerDF = pd.DataFrame([])
     # Get customer dataframe
    c.execute("SELECT * FROM Customer")
    result = c.fetchall()
    for x in result:
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


def showArtist(c):
    artistDF = pd.DataFrame([])
     # Get artist dataframe
    c.execute("SELECT * FROM Artist")
    result = c.fetchall()
    for x in result:
        df = pd.DataFrame([x])
        artistDF = artistDF.append(df)
        
    # Rename column labels
    artistDF = artistDF.rename(columns={0:"NAME", 1:"PHONE",
                                            2:"ADDRESS", 3:"BIRTH_PLACE",
                                        4:"AGE", 5:"STYLE"})

    # Print tables to console
    print("-----------------")
    print("'Artist' Table")
    print("-----------------")
    print(artistDF)


def showArtWork(c):
    artWorkDF = pd.DataFrame([])
    # Get art_work dataframe
    c.execute("SELECT * FROM Art_work")
    result = c.fetchall()
    for x in result:
        df = pd.DataFrame([x])
        artWorkDF = artWorkDF.append(df)
        
    # Rename column labels
    artWorkDF = artWorkDF.rename(columns={0:"ARTIST", 1:"TITLE",
                                            2:"TYPE", 3:"CREATION_DATE",
                                        4:"DATE_ACCQUIRED", 5:"PRICE", 6:"LOCATION"})
    # Print table to console
    print("-----------------")
    print("'Art_work' Table")
    print("-----------------")
    print(artWorkDF)

def showArtShow(c):
    artShowDF = pd.DataFrame([])
    
    # Get art_show dataframe
    c.execute("SELECT * FROM Art_Show")
    result = c.fetchall()
    for x in result:
        df = pd.DataFrame([x])
        artShowDF = artShowDF.append(df)
        
    # Rename column labels
    artShowDF = artShowDF.rename(columns={0:"ARTIST", 1:"DATE",
                                            2:"TIME", 3:"LOCATION",
                                        4:"CONTACT", 5:"CONTACT_PHONE"})
    # Print table to console
    print("-----------------")
    print("'Art_Show' Table")
    print("-----------------")
    print(artShowDF)
    

def showAll(c):
    showCustomer(c)
    showArtist(c)
    showArtWork(c)
    showArtShow(c)

def attributeSort(c):
    column = ''
    table = ''
    df = pd.DataFrame([])
    choice = menu.attributeSortMenu()

    # Get the table and column that we're searching in
    if choice == 1:
        table = 'Customer'
        column = menu.customerAttribute()
    elif choice == 2:
        table = 'Artist'
        column = menu.artistAttribute()
    elif choice == 3:
        table = 'Art_work'
        column = menu.artWorkAttribute()
    elif choice == 4:
        table = 'Art_Show'
        column = menu.artShowAttribute()

    # Get the attribute we're searching for
    attribute = input("Enter attribute value to search for: ")
    command = "SELECT * FROM " + table + " WHERE " + column + " ='" + attribute + "'"

    # Print out the results
    c.execute(command)
    results = c.fetchall()

    if len(results) == 0:
        print("There were no matches to that attribute")
        return
    else:
        for x in results:
            temp = pd.DataFrame([x])
            df = df.append(temp)
            

    # Rename columns
    if table == 'Customer':
        df = df.rename(columns={0:"NAME", 1:"CUSTOMER_NUMBER",
                                                2:"PHONE", 3:"ART_PREFERENCE"})
    elif table == 'Artist':
        df = df.rename(columns={0:"NAME", 1:"PHONE",
                                                2:"ADDRESS", 3:"BIRTH_PLACE",
                                            4:"AGE", 5:"STYLE"})
    elif table == 'Art_Show':
        df = df.rename(columns={0:"ARTIST", 1:"DATE",
                                                2:"TIME", 3:"LOCATION",
                                            4:"CONTACT", 5:"CONTACT_PHONE"})
    elif table == 'Art_work':
        df = df.rename(columns={0:"ARTIST", 1:"TITLE",
                                                2:"TYPE", 3:"CREATION_DATE",
                                            4:"DATE_ACCQUIRED", 5:"PRICE", 6:"LOCATION"})

    print(df)
    input("Press Enter to continue...")


def sortByArtStyle(c, table):
    customerDF = pd.DataFrame([])
    artistDF = pd.DataFrame([])
    artWorkDF = pd.DataFrame([])

    customerCommand = 'SELECT * FROM Customer ORDER BY Art_Preferences'
    c.execute(customerCommand)
    customerResult = c.fetchall()
    for x in customerResult:
        temp = pd.DataFrame([x])
        customerDF = customerDF.append(temp)

    artistCommand = 'SELECT * FROM Artist ORDER BY Style'
    c.execute(artistCommand)
    artistResult = c.fetchall()
    for x in artistResult:
        temp = pd.DataFrame([x])
        artistDF = artistDF.append(temp)
    
    artWorkCommand = 'SELECT * FROM Art_work ORDER BY Type'
    c.execute(artWorkCommand)
    artWorkResult = c.fetchall()
    for x in artWorkResult:
        temp = pd.DataFrame([x])
        artWorkDF = artWorkDF.append(temp)

    
    customerDF = customerDF.rename(columns={0:"NAME", 1:"CUSTOMER_NUMBER",
                            2:"PHONE", 3:"ART_PREFERENCE"})
   
    artistDF = artistDF.rename(columns={0:"NAME", 1:"PHONE",
                            2:"ADDRESS", 3:"BIRTH_PLACE",
                            4:"AGE", 5:"STYLE"})
   
    artWorkDF = artWorkDF.rename(columns={0:"ARTIST", 1:"TITLE",
                            2:"TYPE", 3:"CREATION_DATE",
                            4:"DATE_ACCQUIRED", 5:"PRICE", 6:"LOCATION"})

    if table == 'all':
        print("------------------")
        print("'Customer' Table")
        print("------------------")
        print(customerDF)

        print("------------------")
        print("'Artist' Table")
        print("------------------")
        print(artistDF)

        print("------------------")
        print("'Art_work' Table")
        print("------------------")
        print(artWorkDF)
    elif table == 'Customer':
        print("------------------")
        print("'Customer' Table")
        print("------------------")
        print(customerDF)
    elif table == 'Artist':
        print("------------------")
        print("'Artist' Table")
        print("------------------")
        print(artistDF)
    elif table == 'Art_work':
        print("------------------")
        print("'Art_work' Table")
        print("------------------")
        print(artWorkDF)

    

    
    
   
    
