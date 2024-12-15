# Julie Renaud
# 12/7/2024
# CIT 117
# jmrenaud2001@student.stcc.edu
# SQL Database Interaction with Python

from DataHandler import DataHandler
from DataReporter import DataReporter


def main() :
    # create database file
    dbName = "employeeData.db"

    # Part 1: create instance of DataHandler class for employeeData.db
    dataHandler = DataHandler( dbName )

    dataHandler.createTables()
    dataHandler.commitChanges()
    dataHandler.insertDataFromFiles()
    dataHandler.commitChanges()
    dataHandler.closeConnection()

    # Part 2: create instance of DataReporter class for employeeData.db
    dataReporter = DataReporter( dbName )

    dataReporter.generateReport()
    dataReporter.closeConnection()


main()
