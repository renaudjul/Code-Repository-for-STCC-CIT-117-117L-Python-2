# Julie Renaud
# CIT 117-D01
# 10/17/2024
# jmrenaud2001@student.stcc.edu
# InterPlanetaryWeights2

import pickle


########################################################################
# Opens pickling file that stored previous values
def pickleOpen() :
    # Declare an empty dictionary to transfer history contents into
    dictPlanetHistory = {}

    # declare bool for error handling
    eof = False

    try :
        # open file
        inputFile = open( 'jrPlanetaryWeights.db', 'rb' )

        while not eof :
            try :
                # load open file into empty dictionary
                dictPlanetHistory = pickle.load( inputFile )

            except EOFError :
                eof = True
        # once file is loaded it's closed
        inputFile.close()

    except FileNotFoundError :
        print( "no file found" )

    return dictPlanetHistory


########################################################################
# Function that prompts user if they want to see file history and prints if true
def getHistory(dictPlanetHistory) :
    if input( "Would you like to see the history (y/n): " ).strip().upper() == "Y" :

        # first loops through the dict hist
        for name, dictWeight in dictPlanetHistory.items() :
            print( f"{name}, here are your weights on Solar System's planets" )

            # for each "value" of the loop above (which is a dict of it's own) it
            # needs a second loop to process those key/value pairs and prints
            for key, value in dictWeight.items() :
                print( f"Weight on {key:10s} {value:10,.2f}" )


########################################################################
# Function to validate and get user weight input
def validateWeight(sPrompt) :
    while True :
        try :
            weight = float( input( sPrompt ) )
            if weight <= 0 :
                print( "Weight must be a positive number. Try again." )
            else :
                return weight
        except ValueError :
            print( "Input must be a numeric value." )


########################################################################
def pickleClose(dictPlanetHistory) :
    output_file = open( 'jrPlanetaryWeights.db', 'wb' )
    pickle.dump( dictPlanetHistory, output_file )
    output_file.close()


########################################################################
def main() :
    # Call pickleFile() to open up the pickling file
    dictPlanetHistory = pickleOpen()

    # Call getHistory() to see if user wants to print the history of the file just opened
    getHistory( dictPlanetHistory )

    # declare empty dictionary to store current user entries
    dictPersonWeights = {}

    # dictionary of planet surface gravity factors
    dictPlanetSurfaceGravity = {
        'Mercury' : 0.38,
        'Venus' : 0.91,
        'Moon' : 0.165,
        'Mars' : 0.38,
        'Jupiter' : 2.34,
        'Saturn' : 0.93,
        'Uranus' : 0.92,
        'Neptune' : 1.12,
        'Pluto' : 0.066,
    }

    # Loop to get user input for username and weight
    sName = "x"
    while sName != "" :

        sName = input( "What is your name (enter key to quit): " )

        if sName.strip().casefold() in dictPlanetHistory :
            print( f"{sName} is already in the history file. Enter a unique name." )
            continue

        if sName == "" :
            break

        # calls validateWeight() function
        fEarthWeight = validateWeight( "What is your weight: " )

        print( f"{sName}, here are your weights on our Solar System's planets" )

        # loops through the surface gravity factor dict and calculates and stores new data for current user
        for key, value in dictPlanetSurfaceGravity.items() :
            fComputedWeight = fEarthWeight * value
            dictPersonWeights[key] = fComputedWeight
            print( f"Weight on {key:10s} {fComputedWeight:10,.2f}" )

        # Once a new dictionary is created from loop above (of current users weights), it's added to the history dict
        dictPlanetHistory[sName] = dictPersonWeights

    # Call function pickleClose() to output the dictPlanetHistory to the db file
    pickleClose( dictPlanetHistory )


main()
