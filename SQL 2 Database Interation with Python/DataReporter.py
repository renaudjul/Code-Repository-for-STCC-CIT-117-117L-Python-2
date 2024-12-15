# Julie Renaud
# 12/7/2024
# CIT 117
# jmrenaud2001@student.stcc.edu
# SQL Database Interaction with Python


import sqlite3

class DataReporter:
    def __init__(self, dbName):
        try:
            # initialize database connection
            self.connection = sqlite3.connect(dbName)
            self.cursor = self.connection.cursor()

        except Exception as e:
            print( f"Error in generateReport method: {e}" )


    def generateReport(self):
        try:

            # execute query to JOIN all three tables and remove repeats of column data
            self.cursor.execute("SELECT \
                                    Employee.EmployeeID, \
                                    Employee.Name,\
                                    Pay.Year,\
                                    Pay.Earnings,\
                                    SocialSecurityMin.Minimum \
                                FROM \
                                    Employee\
                                JOIN \
                                    Pay ON Employee.EmployeeID = Pay.EmployeeID\
                                JOIN \
                                    SocialSecurityMin ON Pay.Year = SocialSecurityMin.Year\
                                ORDER BY\
                                    Employee.Name")


            # process results list
            print(f"{'Employee Name':<20} {'Year':<6} {'Earnings':<10} {'Minimum':<10} {'Include':<6}")
            print("-" * 57)

            # loops through what was selected in query above
            for row in self.cursor.fetchall():
                fResult = None

                if row[3] >= row[-1]:
                    fResult = "Yes"
                else:
                    fResult = "No"

                print(f"{ row[1]:<20} {row[2]:<6} {row[3]:<10} {row[4]:<10}", fResult)

        except sqlite3.Error as e :
            print( f"Database error: {e}" )
        except Exception as e :
            print( f"Error in generateReport method: {e}" )



    def closeConnection(self):
        try:
            self.connection.close()

        except Exception as e:
            print( f"Error in the closeConnection method: {e}" )

