# Julie Renaud
# 11/29/2024
# CIT 117
# jmrenaud2001@student.stcc.edu
# Numerology Inheritance – Properties and Decorators


from Numerology import Numerology


class NumerologyLifePathDetails( Numerology ) :

    def __init__(self, sName, sDOB) :
        # call parent constructor
        super().__init__( sName, sDOB )

    # Getters to Properties
    @property
    def Personality(self) :
        return self.getPersonality()

    @property
    def SoulNumber(self) :
        return self.getSoulNumber()

    @property
    def LifePath(self) :
        return self.getLifePath()

    @property
    def Attitude(self) :
        return self.getAttitude()

    @property
    def BirthDay(self) :
        return self.getBirthDay()

    @property
    def PowerName(self) :
        return self.getPowerName()

    @property
    def Name(self) :
        return self.getName()

    @property
    def BirthDate(self) :
        return self.getBirthdate()

    @property
    def getLifePathDescription(self) :
        numerologyDescriptionsDict = {
            1 : "The Independent: Wants to work/think for themselves",
            2 : "The Mediator: Avoids conflict and wants love and harmony",
            3 : "The Performer: Likes music, art and to perform or get attention",
            4 : "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
            5 : "The Adventurer: Likes to travel and meet others, often an extrovert",
            6 : "The Inner Child: Is meant to be a parent and/or one that is young at heart",
            7 : "The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality",
            8 : "The Executive: Gravitates to money and power",
            9 : "The Humanitarian: Helps others and/or experiences pain and learns the hard way"
        }

        # Calls parent class get method for life path num
        lifePathNum = self.LifePath

        return numerologyDescriptionsDict.get( lifePathNum, "No description available" )
