# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 13:38:20 2014

@author: Sandeep
"""

# http://www.bloomberg.com/markets/chart/data/1Y/AAPL:US This Year
# http://www.bloomberg.com/markets/chart/data/1D/AAPL:US This Day 

import urllib2
import json
import sql
import time
import matplotlib.pyplot as plt

time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370))

def retriveStock(ticker,storage,period="day"):
    """Retunrs a class Stock for the current ticker 
        the Current var refers to whether the stock market is currently open 
        if it is the page changes ? Only applies to yahoo ? 
        Ticker Must be in lower case
        Period should be one of the follwing month or year or day in quotes"""

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
        print('HTTPError = ' + str(e.code))
        pass
    except urllib2.URLError, e:
        print('URLError = ' + str(e.reason))
        pass
    except Exception:
        print('Exception: Url not found')
        pass
    
    try: 
        text = json.load(jsonfile)
        text =  text["data_values"]
    except Exception:
        print('Exception: Json')
        price = " Unavaliable"
        pass
    #return price
    Date = time.strftime('%Y-%m-%d ', time.gmtime())
    print Date
    #storage.write(Date +'\n'+'\n')  #Write in the date to File
    # the File will be like a table. 
    # Stock Price Time
    
    
    graphTimeStamp = []
    humanTimeStamp =[]
    Price = []
    try:
        for point in text:
            epoch = point[0]/1000
            price = point[1]
    
            Time = time.strftime('%H:%M:%S', time.gmtime(epoch))
            graphTime = Time.split(":")
            graphTime = int(graphTime[0])*100 + int(graphTime[1])
            graphTimeStamp.append(graphTime)
            Price.append(price)
            humanTimeStamp.append(Time)
            storage.write('\n')
            storage.write(str(query)+"\t"+str(price)+"\t"+str(Time))
    except Exception:
        print("Error")
        pass
        #print Time ," : ",price 
    storage.write('\n'+'\n')  
    try: 
        maxVal = max(Price)
        maxIndex = Price.index(maxVal)
        maxTime = humanTimeStamp[maxIndex]
        result = "Max Value of " , str(query) , " is : " , maxVal , ' at ' , maxTime 
        storage.write('\n') 
        print result
        storage.write(str(result))
        #plt.plot(timeStamp,Price)
        print query
        plt.plot(graphTimeStamp,Price)
        plt.show()
    except Exception:
        print('Exception: Max|Plotting')
        price = " Unavaliable"
        pass
   
    storage.close()
    return humanTimeStamp ,Price
    
    #print Price
    #print timeStamp
    


def searchAllStocks(period="day"):        
    text = open("StockSymbols.txt",'r')
    symols = text.read()
    stockList = symols.split('\n')
    storage = open("Stock Prices.txt","w")
    Date = time.strftime('%Y-%m-%d ', time.gmtime())
    print Date
    storage.write(Date +'\n'+'\n')  #Write in the date to File
    storage.write("Stock"+"\t"+"Price"+"\t"+"Time"+'\n')
    for stock in stockList:
        stockLower = stock.lower()
        #print stock.upper() 
        storage = open("Stock Prices.txt","a")
        retriveStock(str(stockLower),storage,period="day")
        #time.sleep(3)
  
          
          
          
def main():
    searchAllStocks()
        
if __name__ == "__main__":
    main()
    