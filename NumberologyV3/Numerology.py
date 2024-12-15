# Julie Renaud
# 11/11/2024
# CIT 117
# jmrenaud2001@student.stcc.edu
# Numerology V3


class Numerology :

    def __init__(self, sName, sDOB) :
        # public input vars
        self.sName = sName
        self.sDOB = sDOB

        # private computed vars
        self.__iPersonalityNumber = 0
        self.__iSoulNumber = 0
        self.__iLifePathNumber = 0
        self.__iAttitudeNumber = 0
        self.__iBirthdayNumber = 0
        self.__iPowerName = 0
        self.__sDOBList = [0, 0, 0]

        # process calculated private vars
        self.__processNameVars()
        self.__processDOBVars()


    # proces name
    def __processNameVars(self) :
        # gets the vowels and constants from name
        sVowels = self.__getVowels( self.sName )
        sConstants = self.__getConstants( self.sName )

        # private vars for the soul, personality, and Power name nums each var calls the same methods to calculate
        # the text and reduces the num value for sVowels, sConstants, and sName
        self.__iSoulNumber = self.__reduceNumber( self.__calculateValue( sVowels ) )
        self.__iPersonalityNumber = self.__reduceNumber( self.__calculateValue( sConstants ) )
        self.__iPowerName = self.__reduceNumber( self.__calculateValue( self.sName ) )


    # process DOB
    def __processDOBVars(self) :
        try :
            # split date into a three part list
            if '-' in self.sDOB :
                self.__sDOBList = self.sDOB.split( '-' )
            elif '/' in self.sDOB :
                self.__sDOBList = self.sDOB.split( '/' )
            else :
                raise ValueError( "Invalid date format. Use 'YYYY-MM-DD' or 'MM/DD/YYYY'." )

            # check if exactly three part list (day, month, year)
            if len( self.__sDOBList ) != 3 :
                raise ValueError( "Invalid date format. Must have three parts." )

            # create mm-dd-yyyy vars from list
            birthDay = int( self.__sDOBList[1] )
            birthMonth = int( self.__sDOBList[0] )
            birthYear = int( self.__sDOBList[2] )

            # private vars for the life path, attitude, and birthday nums
            self.__iLifePathNumber = self.__reduceNumber( birthDay + birthMonth + birthYear )
            self.__iAttitudeNumber = self.__reduceNumber( birthDay + birthMonth )
            self.__iBirthdayNumber = self.__reduceNumber( birthDay )

        except Exception as e :
            print( f"Error processing DOB: {e}" )



    # private methods for calculating
    def __getVowels(self, sName) :
        vowels = ""
        for char in sName :  # Loop through each char in sName
            # Check if the character is a vowel
            if char.upper() in 'AEIOU' :
                vowels += char
        return vowels

    def __getConstants(self, sName) :
        consonants = ""
        for char in sName :
            if char.isalpha() and char.upper() not in 'AEIOU' :
                consonants += char
        return consonants

    def __calculateValue(self, sString) :
        total_value = 0
        for char in sString :
            charValue = self.__convertCharToInt( char )  # call method to convert char to int
            total_value += charValue
        return total_value

    def __convertCharToInt(self, sCharacter) :
        iCharToNumValue = 0
        if sCharacter.isalpha() :
            iCharToNumValue = ((ord( sCharacter.upper() ) - 65) % 9 + 1)
        return iCharToNumValue

    def __reduceNumber(self, iNumber) :
        while (len( str( iNumber ) ) > 1) :
            iNumber = (iNumber % 10) + (iNumber // 10)
        return iNumber



    # Getters
    def getPersonality(self) :
        return self.__iPersonalityNumber

    def getSoulNumber(self) :
        return self.__iSoulNumber

    def getLifePath(self) :
        return self.__iLifePathNumber

    def getAttitude(self) :
        return self.__iAttitudeNumber

    def getBirthDay(self) :
        return self.__iBirthdayNumber

    def getPowerName(self) :
        return self.__iPowerName

    def getName(self) :
        return self.sName

    def getBirthdate(self) :
        return self.sDOB
