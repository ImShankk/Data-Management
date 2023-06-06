import json
import helper

# Load the games data from JSON file
with open("gameData.json", "r") as gameFile:
    dataString = gameFile.read()
    videoGames = json.loads(dataString)

# Users information from the JSON file
with open("UserInf.json", "r") as userInfoFile:
    dataStringUser = userInfoFile.read()
    userInformation = json.loads(dataStringUser)

# User variables
favouriteList = []
usingUser = ""

# Search for user
def userSearch():
    # Use linear search since the array is small
    userLocation = helper.diffBinary(userInformation, "username", usingUser)
    # The bookmarked or the games the user stars/favourites
    starredList = userInformation[userLocation]["bookmarked"]
    return starredList

# Main Loop
mainLoop = False

# MAKING ACCOUNTS
def startProgram():
    # GLOBAL VARIABLES SO THEY CAN BE CHANGED INSIDE THE FUNCTION
    global mainLoop
    global favouriteList
    global usingUser

    # Main Loop for program itself
    registerLogin = True
    while registerLogin:
        # MAIN MENU
        print("Select One Of The Following")
        print("Enter 1 to register and create an account!!! ")
        print("Enter 2 to login to an existing account!!!")
        print("Enter 3 to exit the program")

        # User input for menu selection
        menuOption = input("Please Select A Menu Option: ")

        # Option 1: Registering An Account
        if menuOption == "1":
            # Register the user
            username = input("Please create a username: ")
            password = input("Please create a secure password: ")

            # Check UserInf.json to see if the username already exists
            if any(user["username"] == username for user in userInformation):
                print("THE ACCOUNT USERNAME YOU HAVE PROVIDED ALREADY EXISTS. PLEASE TRY AGAIN WITH A NEW USERNAME!")
            else:
                userInformation.append({"username": username, "password": password, "bookmarked": []})
                print("Congratulations! You Have Successfully Created An Account!!!")
                usingUser = username
                favouriteList = userSearch()
                mainLoop = True
                startProgram()
                break

        elif menuOption == "2":
            # Find the username and password
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")

            for user in userInformation:
                if user["username"] == username and user["password"] == password:
                    print("You have successfully logged in")
                    usingUser = username
                    favouriteList = userSearch()
                    mainLoop = True
                    registerLogin = False
                    break
            else:
                print("Username or Password Incorrect")

        elif menuOption == "3":
            # End the program
            registerLogin = False
            mainLoop = False
            print("You have exited the program")

        else:
            print("Please select one of the following options")

# Function to update the JSON file
def updateJson():
    with open("UserInf.json", "w") as z:
        json.dump(userInformation, z)

# Run the program
startProgram()

# Call the function to update the file after the program runs
updateJson()

# Options for the program itself
while mainLoop:
    # Option List
    print("DATA MANAGEMENT MAIN MENU")
    print("1: Display All Data")
    print("2: Display Data Based On Certain Criteria")
    print("3: Sort Data Based On Criteria")
    print("4: Select Data to add to a favourites/bookmarks")
    print("5: Remove Data from favourites/bookmarks")
    print("6: Display the favourites list/bookmarks")
    print("7: Exit and Logout")
    print("")

    # Option Select
    optionSelect = input("Please Select One Of The Following Options: ")

    # Displaying All Data
    if optionSelect == "1":
        # LOOP TO SHOW DATA
        for game in videoGames:
            print(game["title"], ",", game["developer"], ",", game["year"], ",", game["players"])

    # Display based on certain criteria
    elif optionSelect == "2":
        # CRITERIA FINDER
        criteriaLookingfor = input("Please Enter the Developer of The Game: ")
        located = False
        # LOOP TO SEARCH
        for game in videoGames:
            if criteriaLookingfor.lower() == game["developer"].lower():
                located = True
                print(game["title"], ",", game["developer"], ",", game["year"], ",", game["players"])

        # NOT FOUND
        if not located:
            print("Doesn't seem to be a game by that developer")

    # Sort Data on Criteria
    elif optionSelect == "3":
        # Sort on Criteria
        criteriaSort = input("What criteria would you like to sort by?")