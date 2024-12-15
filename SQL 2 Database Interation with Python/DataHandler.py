# Julie Renaud
# 12/7/2024
# CIT 117
# jmrenaud2001@student.stcc.edu
# SQL Database Interaction with Python


import sqlite3
import csv


class DataHandler :
    def __init__(self, dbName) :
        # initialize database connection

        try :
            self.dbName = dbName
            self.dbConnection = sqlite3.connect( dbName )  # connect/create to database
            self.dbCursor = self.dbConnection.cursor()  # create cursor object for SQL commands

        except Exception as e :
            print( f"Error in DataHandler __init__: {e}" )



    def createTables(self, ) :
        # creates 3 tables (Employee, Pay, SocialSecurityMin)
        # create tables - uses IF NOT EXISTS statements to error handle if table already exists

        try :
            self.dbCursor.execute( "CREATE TABLE IF NOT EXISTS Employee(\
                                        EmployeeID integer,\
                                        Name text)" )

            self.dbCursor.execute( "CREATE TABLE IF NOT EXISTS Pay(\
                                        EmployeeID integer,\
                                        Year integer,\
                                        Earnings real)" )

            self.dbCursor.execute( "CREATE TABLE IF NOT EXISTS SocialSecurityMin(\
                                        Year integer,\
                                        Minimum real)" )

        except Exception as e :
            print( f"Error in createTables method: {e}" )



    def insertDataFromFiles(self) :
        # Opens / imports data from text files and INSERTS data into the tables

        try:

            with open( 'Pay.txt', 'r' ) as file :
                reader = csv.reader(file)

                next( reader )  # skips header row

                for row in reader :
                    EmployeeID, Year, Earnings = row
                    self.dbCursor.execute(f"INSERT INTO Pay(EmployeeID, Year, Earnings) VALUES ({EmployeeID}, {Year}, {Earnings})" )

            with open( 'Employee.txt', 'r' ) as file :
                reader = csv.reader( file )

                next( reader )  # skips header row

                for row in reader :
                    EmployeeID, Name = row
                    self.dbCursor.execute( f"INSERT INTO Employee(EmployeeID, Name) values({EmployeeID}, '{Name}')" )

            with open( 'SocialSecurityMinimum.txt', 'r' ) as file :
                reader = csv.reader( file )

                next( reader )  # skips header row

                for row in reader :
                    Year, Minimum = row
                    self.dbCursor.execute( f"INSERT INTO SocialSecurityMin(Year, Minimum) values({Year}, {Minimum})" )

        except FileNotFoundError as e :
            print( f"File not found: {e}" )
        except sqlite3.Error as e :
            print( f"sqlite3 error: {e}" )
        except Exception as e:
            print(f"Error in insertDataFromFiles method: {e}")


    def commitChanges(self) :
        # saves changes to database
        try:
            self.dbConnection.commit()

        except Exception as e :
            print( f"Error in commit method: {e}" )


    def closeConnection(self) :
        # closes connection to database
        try :
            self.dbConnection.close()

        except Exception as e :
            print( f"Error in closeConnection method: {e}" )
