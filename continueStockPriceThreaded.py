# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 13:38:20 2014

@author: Sandeep



    cursor.execute("INSERT INTO Stocks (Time,Date,Stock,Price) VALUES(?,?,?,?)",(humanTimeStamp,Date,str(query),Price))
ProgrammingError: SQLite objects created in a thread can only be used in that same thread.The object was created in thread id 25100 and this is thread id 22092


FAILED

Go thru the dictionary and then trasnfer into DataBase
"""

# http://www.bloomberg.com/markets/chart/data/1Y/AAPL:US This Year
# http://www.bloomberg.com/markets/chart/data/1D/AAPL:US This Day 

import urllib2
import json

import time
import matplotlib.pyplot as plt
import sqlite3 

import threading


#time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370))
## Creating database to store values arriving from different threads

"""
connect = sqlite3.connect('Stocks Threaded.db')
cursor = connect.cursor()
# DO this step only during the first run 
cursor.execute("CREATE TABLE Stocks(Time TEXT,Date TEXT,Stock TEXT,Price REAL)")


Final Step to enter into database 
cursor.execute("INSERT INTO Stocks (Time,Date,Stock,Price) VALUES(?,?,?,?)",(Time,Date,Stock,Price))
    connect.commit()

"""

## GLOBAL CONTAINERS

humanTimeStamp = {}
Price = {}




def retriveStock(ticker,Date,cursor,period="day"):
    """
        Retunrs a class Stock for the current ticker 
        the Current var refers to whether the stock market is currently open 
        if it is the page changes ? Only applies to yahoo ? 
        Ticker Must be in lower case
        Period should be one of the follwing month or year or day in quotes
        
        I am not ot concerned about single values , so if an error is given 
        I will end the function  .
        3000 threds are started , lose of one is not a huge Cost         
        
        
        
        """

    query = ticker.upper()
    #print query
    if (period == "day"):
        url = "http://www.bloomberg.com/markets/chart/data/1D/"+query+":US"
    elif period == "month":  
        url = "http://www.bloomberg.com/markets/chart/data/1M/"+query+":US"
    elif period == "year":
        url = "http://www.bloomberg.com/markets/chart/data/1Y/"+query+":US"
    else:
        print "wrong period year month day only " 
        return False 
        
    try: 
        jsonfile = urllib2.urlopen(url)
        #Json wants a file not the string 
    except urllib2.HTTPError, e:
        return 0
        #print('HTTPError = ' + str(e.code))
        pass
    except urllib2.URLError, e:
        return 0
        #print('URLError = ' + str(e.reason))
        pass
    except Exception:
        return 0 
        #print('Exception: Url not found')
        pass
    
    try: 
        text = json.load(jsonfile)
        text =  text["data_values"]
    except Exception:
        #print('Exception: Json')
        #price = " Unavaliable"
        return 0 
        pass

    try:
        for point in text:
            epoch = point[0]/1000
            price = point[1]
    
            Time = time.strftime('%H:%M:%S', time.gmtime(epoch))
            graphTime = Time.split(":")
            graphTime = int(graphTime[0])*100 + int(graphTime[1])
            
            ## WRTING TO THE DICT
            ## KEY of form 1204 AAPL
            ## USe split to get the stock name 
            Price[str(graphTime)+ " " + str(query)] = price
            humanTimeStamp[str(graphTime) + " " + str(query)] = Time
            ## WILL USE THE RETURN VALUE OF TRAVERSING the array to write the price to DB

    except Exception:
        return 0
        #print("Error")
        pass
    return 0 

    
text = open("StockSymbols.txt",'r')
symols = text.read()
stockList = symols.split('\n')
period="day"

    
Date = time.strftime('%Y-%m-%d ', time.gmtime())
connect = sqlite3.connect('Stocks Threaded .db')
cursor = connect.cursor()
# DO this step only during the first run 
statement = "CREATE TABLE Stocks_"+str(Date.replace("-",""))+"(Time TEXT,Date TEXT,Stock TEXT,Continous_Time REAL ,Price REAL)"
#print statement
cursor.execute(statement)
threadlist = []
for stock in stockList:
    stockLower = stock.lower()
    thread = threading.Thread(target=retriveStock,args=(stockLower,Date,cursor))
    thread.start()
    threadlist.append(thread)
        


    
print(" Giving some time before unwarpping of Dict to finish execution") 
# sleep until number of active_count == 0

sec = 0 
while(threading.active_count() > 25): 
    print "sec :" ,sec,"active_count :",threading.active_count()
    print "~"
    time.sleep(1)
    sec += 1
print "WRITING INTO THE DATA BASE "   
## UNWRAPING TH DICT AND WRITING IT TO THE DATABSAE

print "NO OF VALUES - ",len(Price)

for key in Price.keys(): 
    
    Time = humanTimeStamp[key]  
    price = Price[key] 
    splitKey = key.split()
    Continous_Time = splitKey[0]
    Stock = splitKey[1]    
    cursor.execute("INSERT INTO  Stocks_"+str(Date.replace("-",""))+"(Time,Date,Stock,Continous_Time,Price) VALUES(?,?,?,?,?)",(Time,Date,Stock,Continous_Time,price))
    

connect.commit()









          
          
          
