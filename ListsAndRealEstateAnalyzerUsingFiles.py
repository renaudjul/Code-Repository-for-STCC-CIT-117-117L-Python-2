# Julie Renaud
# jmrenaud2001@student.stcc.edu
# CIT 117
# 11/2/2024
# Lists and Real Estate Analyzer Using Files V2


import csv


# reads entire file onto one list and returns it
def getDataInput() :
    try :
        with open( 'RealEstateData.csv', 'r' ) as file :
            reader = csv.reader( file )
            # The CSV Reader takes each "row" and makes a list of it, inside one big list "sDataList"
            sDataList = [row for row in reader][1 :]  # Excludes header row [1:]

            return sDataList
    except Exception as err :
        # err states what the exact error is
        print( "General error: " + format( err ) )


def getMedian(sSortedList) :
    # get length of sorted list for if statement
    nLengthList = len( sSortedList )

    # if list length is odd / else if even using Modulus
    try :
        # Check if the list has an odd or even number of elements
        if nLengthList % 2 != 0 :  # Odd number of elements
            nMedianIndex = nLengthList // 2
            nMedian = sSortedList[nMedianIndex]
        else :  # Even number of elements
            # Calculate the two middle indices
            nMaxIndex = nLengthList // 2
            nMinIndex = nMaxIndex - 1
            # Average the two middle values
            nMedian = (sSortedList[nMinIndex] + sSortedList[nMaxIndex]) / 2

        return float( nMedian )

    except IndexError :
        raise SystemExit( "Error in getMedian(): List index out of range" )
    except TypeError :
        raise SystemExit( "Error in getMedian(): Invalid data type in list" )


def main() :
    try :
        # calls function to retrieve data from file in single list "dataFileList"
        dataFileList = getDataInput()

        # Desired Lists and dictionaries to catch each iteration of record lists in dataFileList
        sCityList = []
        sPropertyTypeList = []
        fPriceList = []
        dictPropertyTypeSummary = {}
        dictCitySummary = {}

        # Loops through each record/list inside dataFileList
        for sRecord in dataFileList :

            # append desired indices to city, type, price lists
            sCityList.append( sRecord[1] )
            sPropertyTypeList.append( sRecord[7] )
            try :
                fPriceList.append( float( sRecord[8] ) )  # catches error if data type not a float
            except ValueError :
                print( "Bad data to convert on: ", fPriceList.append( float( sRecord[8] ) ) )

            # checks to see if property type index exists in property summary dictionary
            # if yes, adds price to existing value for that key
            # else, creates new key and value
            if sRecord[7] in dictPropertyTypeSummary :
                dictPropertyTypeSummary[sRecord[7]] += float( sRecord[8] )
            else :
                dictPropertyTypeSummary[sRecord[7]] = float( sRecord[8] )

            # checks to see if city index exists in city summary dictionary
            # if yes, adds price to existing value for that key
            # else, creates new key and value
            if sRecord[1] in dictCitySummary :
                dictCitySummary[sRecord[1]] += float( sRecord[8] )
            else :
                dictCitySummary[sRecord[1]] = float( sRecord[8] )

        # **********************   Printing  Section  ************************
        # sorts the priceList created from Loop above
        sortedPPriceList = sorted( fPriceList )

        print( "Minimum       \t", format( min( sortedPPriceList ), "10,.2f" ) )
        print( "Maximum       \t", format( max( sortedPPriceList ), "10,.2f" ) )
        print( "Sum           \t", format( sum( sortedPPriceList ), "10,.2f" ) )
        print( "Avg           \t", format( sum( sortedPPriceList ) / len( sortedPPriceList ), "10,.2f" ) )
        print( "Median        \t", format( getMedian( sortedPPriceList ), "10,.2f" ) )

        # Prints property type summary dictionary
        print( "\nSummary by Property Type:" )
        for key, value in dictPropertyTypeSummary.items() :
            print( "{:12}\t".format( key ) + "{:14,.2f}".format( value ) )

        # Prints price summary dictionary
        print( "\nSummary by City:" )
        for key, value in dictCitySummary.items() :
            print( "{:12}\t".format( key ) + "{:13,.2f}".format( value ) )

    except Exception as err :
        # err states what the exact error is
        print( "General error: " + format( err ) )


main()
