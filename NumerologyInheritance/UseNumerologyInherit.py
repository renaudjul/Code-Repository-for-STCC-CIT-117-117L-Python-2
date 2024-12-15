# Julie Renaud
# 11/29/2024
# CIT 117
# jmrenaud2001@student.stcc.edu
# Numerology Inheritance – Properties and Decorators


from NumerologyLifePathDetails import NumerologyLifePathDetails


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
    numerologyDetails = NumerologyLifePathDetails( sName, sDOB)

    # Prints results
    print( f"{'Test Name:':20} {numerologyDetails.Name}" )
    print( f"{'Test DOB:':20} {numerologyDetails.BirthDate}" )
    print( f"{'Life Path Number:':20} {numerologyDetails.LifePath}" )
    print( f"{'Birth Day Number:':20} {numerologyDetails.BirthDay}" )
    print( f"{'Attitude Number:':20} {numerologyDetails.Attitude}" )
    print( f"{'Soul Number:':20} {numerologyDetails.SoulNumber}" )
    print( f"{'Personality Number:':20} {numerologyDetails.Personality}" )
    print( f"{'Power Name Number:':20} {numerologyDetails.PowerName}" )
    print( f"Life Path Description: {numerologyDetails.getLifePathDescription}" )


main()