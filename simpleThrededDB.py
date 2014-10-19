# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 13:54:12 2014

@author: Sandeep
"""

import urllib2
import re
import sqlite3


connect = sqlite3.connect('test.db')
cursor = connect.cursor()

def tableCreate():
    cursor.execute("CREATE TABLE Stocks(Time TEXT,Date TEXT,Stock TEXT,Price REAL)")