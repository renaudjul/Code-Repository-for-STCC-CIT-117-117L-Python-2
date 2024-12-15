# Julie Renaud
# 11/11/2024
# CIT 117
# jmrenaud2001@student.stcc.edu
# Numerology V3


from Numerology import Numerology


def main() :
    # Name Input
    while True :

        sName = input( "Client Name: " ).strip()

        if sName == "" :
            print( "Invalid name input. Must be at least one character." )
            continue
        break

    # DOB Input
    while True :

        sDOB = input( "Client DOB: " ).strip()

        if len(sDOB) < 10 or len(sDOB) > 10 :
            print( "Invalid DOB input. Format is mm-dd-yyyy with a total of 10 characters." )
            continue
        break

    # Create an instance of Numerology Class
    numerology = Numerology( sName, sDOB)

    # Prints results
    print( f"{'Test Name:':20} {numerology.getName()}" )
    print( f"{'Test DOB:':20} {numerology.getBirthdate()}" )
    print( f"{'Life Path Number:':20} {numerology.getLifePath()}" )
    print( f"{'Birth Day Number:':20} {numerology.getBirthDay()}" )
    print( f"{'Attitude Day Number:':20} {numerology.getAttitude()}" )
    print( f"{'Soul Number:':20} {numerology.getSoulNumber()}" )
    print( f"{'Personality Number:':20} {numerology.getPersonality()}" )
    print( f"{'Power Name Number:':20} {numerology.getPowerName()}" )


main()
