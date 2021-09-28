#import the libraries required for this function
import pandas as pd
import os

#change the working directory
os.chdir("files")

#input the searches
search = input("1 = Search Query\n2 = Search Suburb\n3 = Search Date\nq = quit\nPlease choose an option: ")

#search functions
#this one still has work to be done on it.
def Query():
    #another selection screen
    search = input("1 = Listings\n2 = reviews\nPlease select one of the options: ")
    #searching the listings
    if(search == "1"):
        #opening the file + loading message
        print("Loading, Please Wait")
        f = pd.read_csv("listings_dec18.csv", sep=',', low_memory = False)
        print("Dates Have Now Been Loaded")
        #the actual search query for the date
        search = input("Search: ")
        #indexing the csv file
        f.set_index(["space"], inplace=True)
        #printing all results
        print(f.loc[search])
    #searching the reviews
    elif(search == "2"):
        print("Loading, Please Wait")
        f = pd.read_csv("reviews_dec18.csv", sep=",")
        print("Listings Have Now Been Loaded")
        #searching the listings
        search = input("Search: ")
        #indexing the summary
        f.set_index("comments", inplace=True)
        print(f.loc[search])
    else:
        print("Invalid Option")
        quit()
def Suburb():
    #opening the file + loading messages
    print("Loading, Please Wait")
    f = pd.read_csv("listings_summary_dec18.csv")
    print("Suburbs Have Now Been Loaded")
    #the actual search query
    search = input("Please input a suburb in the Sydney area: ")
    #indexing the neighbourhoods
    f.set_index("neighbourhood", inplace=True)
    #searching for the suburb
    print(f.loc[search])
#searching the dates
def Date():
    #opening the file + loading messages
    print("Loading, Please Wait")
    f = pd.read_csv("calendar_dec18.csv", sep=',')
    print("Dates Have Now Been Loaded")
    #the actual search query for the date
    search = input("Please input a date in the following format(yyyy-mm-dd): ")
    #indexing the csv file
    f.set_index("date", inplace=True)
    #printing all results
    print(f.loc[search])

#selecting the options
if(search == "1"):
    Query()
elif(search == "2"):
    Suburb()
elif(search == "3"):
    Date()
elif(search == "q"):
    quit()
else:
    print("Invalid input, please try again.")
    quit()
