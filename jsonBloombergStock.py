# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 11:13:36 2014

@author: Sandeep
"""
import urllib2
import json
import sql



def retriveStock(ticker,current=True):
    """Retunrs a class Stock for the current ticker 
        Ticker Must be in lower case """

    query = ticker.upper()
    try: 
        jsonfile = urllib2.urlopen("http://www.bloomberg.com/markets/watchlist/recent-ticker/"+str(query)+":US")
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
        price = text['last_price']
    except Exception:
        print('Exception: Json')
        price = " Unavaliable"
        pass
    return price
    
    
text = open("StockSymbols.txt",'r')
symols = text.read()
stockList = symols.split('\n')

for stock in stockList:
    stockLower = stock.lower()
    print stock.upper()+"  "+ str(retriveStock(str(stockLower)))