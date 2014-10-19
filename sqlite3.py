# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 01:26:27 2014

@author: Sandeep
"""

import sqlite3

connect = sqlite3.connect('stocks.db')
cursor = connect.cursor()

def tableCreate():
    cursor.execute("CREATE TABLE Stocks(Time TEXT,Date TEXT,Stock TEXT,Price REAL)")
        # INDEX IS PORVIDED IN BUILT

def enterData():
    text = open("Stock Prices.txt","r")
    Date = text.readline()

   
    for line in text:
        if line[0] != " " and line[0] !="(" and line[0] != "\n":
            line = line.rstrip('\n')
            line = line.split("\t")
            Stock = line[0]
            Price = line[1]
            Time = line[2]
            cursor.execute("INSERT INTO Stocks (Time,Date,Stock,Price) VALUES(?,?,?,?)",(Time,Date,Stock,Price))
    connect.commit()
tableCreate()
enterData()

