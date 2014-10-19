# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 01:53:55 2014

Give the name of the stock . 
Current Price will be given . 
Yahoo Finance
@author: Sandeep
"""



import urllib2
from GetReqRegexFromText import getReqRegexFromText




class Stock:
    def __init__(self,name="none",ticker="none",netcap=0,price=0,percent=0,time=0):
        self.name = name
        self.ticker = ticker
        self.netcap = netcap
        self.price = price
        self.percent = percent
        self.time = time 
        
    def __str__(self):
        return 'Name :'+str(self.name)+'\n'+'Price : '+str(self.price)+' $'+'\n'+'Percent : '+str(self.percent)+'\n'+'Time : '+str(self.time)+'\n'+'MarketCap : '+str(self.netcap)



def retriveStock(ticker,current=True):
    """Retunrs a class Stock for the current ticker 
        Ticker Must be in lower case """

    query = ticker.upper()
    try: 
        htmlfile = urllib2.urlopen("https://www.google.com/finance/getprices?q="+str(query)+"&f=c")
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
        text = htmlfile.read()
    except Exception:
        print('Exception: Url not found')
        pass
    array = text.split()
    return array[-1]

    
#stockList = ["aapl","spy","goog","nflx"]
#print retriveStock("aapl")
text = open("StockSymbols.txt",'r')
symols = text.read()
stockList = symols.split('\n')

for stock in stockList:
    stockLower = stock.lower()
    print stock.upper()+"  "+ retriveStock(str(stockLower))
     
#getFileFromList(listStockPrice,"listStockPrice.txt")