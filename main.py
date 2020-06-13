# main.py
#
# Everardo Gutierrez
# Project Show Streaming LookUp
#   Program is to read in file containing shows streamed on multiple platforms. 
#   User can enter in multiple commands to get show titles based on criteria
#   entered and show what streaming platforms they are available on.
import pandas as pd 

def displayCommands():
    """
        Function: printCommands
        Display all the commands available for the user to enter
        Parameters: 
            none
        Returns:
            none
    """
    print("Available commands: ")
    print("Enter 'help' to display all commands")
    print("Enter year to display all shows released (e.g. year 2019)")
    print("Enter to search for specific age group (e.g. 18)")
    print("Enter age to search age group greater than or equal to (e.g. >19)")
    print("Enter IMDB rating for really high rated shows (e.g. rating 8.0)")
    print("Enter Rotten Tomatoes rating to find really good shows (e.g. rotten 90)")

def yayOrNay(value):
    """
        Function: yayOrNay
            Determines if string passed is Yes (value = 1) or No (value = 0)
        Parameters: 
            value - sring
        Returns:
            Yes | No - string
    """
    if value == 1:
        return "Yes"
    else: 
        return "No"

pd.set_option('display.max_rows', None)
fileName = 'Show_streaming.csv'

print("**Show Streaming Analysis Program**")
print("Reading in file", fileName, "....")
data = pd.read_csv(fileName) # create DataFrame from file entered

command = input('Please enter a command, help, or #>') # request command from user for what criteria to search on
while command != "#": # keep searching until user enters # to quit program
    if command == "help": # user requests to see all commands available to be entered
        displayCommands()
    elif command.startswith("year"): # user requests to search based on year
        command = int(command[5:])
        d = data.loc[data.Year == command] # refine dataframe to contain only shows that have the criteria met
        print("----------Request of Show(s) for year",command,"----------")
    elif command.isdigit(): # user requests to search based on age rating
        command = command + '+'
        d = data.loc[data.Age == command]
        print("----------Request of Show(s) for Age",command,"----------")
    elif command[0] == '>': # user requests to search based on age rating greater than value entered
        ageGroup = ["7+", "16+", "18+", "all"]
        command = int(command.replace('>','',1))
        if command < 16:
            index = 0
        elif command >= 16 & command < 18:
            index = 1
        else: 
            index = 2
        ageGroup = ageGroup[index:]
        d = data.loc[data.Age.isin(ageGroup)]
        print("----------Request of Show(s) for Age greater than",command,"----------")
    elif command.startswith("rating"): # user requests to search based on IMDb rating
        command = float(command[7:])
        d = data.loc[data.IMDb == command]
        print("----------Request of Show(s) for IMDb rating of",command,"----------")
    elif command.startswith("rotten"): # user requests to search based on Rotten Tomatoe Rating
        command = command[7:] + '%'
        d = data.loc[data.RottenTomatoes == command]
        print("----------Request of Show for Rotten Tomatoes rating of",command,"----------")
    else: # default search by show title name
        d = data.loc[data.Title.str.contains(command, na = False)]
        if d.empty:
            print("Invalid input\n")
            command = input('Please enter a command, help, or #>')
            continue
        print("----------Request of Show for Title of " + command + "----------")
    # loop through the refined datafram and sisplay show title name along
    # with streaming platforms the show is available on
    for i, j, k, l, m in zip(d['Title'], d['Netflix'], d['Hulu'],d['PrimeVideo'],d['Disney+']):
        print(i)
        print(" Netflix: " + ("Yes" if j == 1 else "No"))
        print(" Hulu: " + ("Yes" if j == 1 else "No"))
        print(" Prime Video: " + ("Yes" if j == 1 else "No"))
        print(" Disney+: " + ("Yes" if j == 1 else "No") + '\n')
    # request choice and command from user once again
    command = input('Please enter a command, help, or #>')

