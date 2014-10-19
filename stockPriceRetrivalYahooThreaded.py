# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 01:53:55 2014

Give the name of the stock . 
Current Price will be given . 
Yahoo Finance
@author: Sandeep
"""

## FAILED

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


    ## Main Function 
def retriveStock(ticker,current=True):
    """Retunrs a class Stock for the current ticker 
        Ticker Must be in lower case """
    
    # convert url into text
#    print ticker
    query = ticker.upper()
    print query
    try: 
        htmlfile = urllib2.urlopen("http://finance.yahoo.com/q?s="+str(query))
    except urllib2.HTTPError, e:
        print('HTTPError = ' + str(e.code))
        pass
    except urllib2.URLError, e:
        print('URLError = ' + str(e.reason))
        pass
    except Exception:
        print('Exception: Url not found')
        pass
    text = htmlfile.read()
    if not current:
    #The diffrent regex used for extraction
        ## str ticker is not actually needed for easness replace it with [^.]* ie. any character repeted multiple times
        priceTag = "<span id=\"yfs_l84_"+str(ticker)+"\">(.+?)</span>"
        percentTag = "<span id=\"yfs_p20_"+str(ticker)+"\">(.+?)</span>"
        timeTag = "<span id=\"yfs_t53_"+str(ticker)+"\">(.+?)</span>"
        titleTag = "<h2>(.+?)</h2>"
    else:
        priceTag = "<span id=\"yfs_l84_"+str(ticker)+"\">(.+?)</span>"
        percentTag = "<span id=\"yfs_p43_"+str(ticker)+"\">(.+?)</span>"
        timeTag = "<span id=\"yfs_t53_"+str(ticker)+"\">(.+?)</span>"
        timeTagInner = "<span id=\"yfs_t53_"+str(ticker)+"\">(.+?)EDT" # using EDT as a border , will add on EDT later
        titleTag = "<h2>(.+?)</h2>"
        marketCapTag = "<span id=\"yfs_j10_[^.]*\">(.+?)</span>"

    # getting the values 
    title = getReqRegexFromText(text,titleTag)[1]   # an array is returned , using the second value of that array 
    price = getReqRegexFromText(text,priceTag)
    ## There is an inner span id , get outer , then extract inner 
    #print str(getReqRegexFromText(text,timeTag)[0])
    time =  getReqRegexFromText(str(getReqRegexFromText(text,timeTag)),timeTagInner)
    
    percent = getReqRegexFromText(text,percentTag)
    marketCap = getReqRegexFromText(text,marketCapTag)
    try:
        price = price[0]
    except Exception:
        price = " Unavaliable"
    try:
        percent = percent[0]
    except Exception:
        percent = " Unavaliable"
    try:
       time = (str(time[0])+" EDT")
    except Exception:
        time = " Unavaliable"
        #print('Exception : MarketCat not found')                                                               #DEBUG
        pass
    try:
        netCap = marketCap[0]
    except Exception:
        netCap = " Unavaliable"
        #print('Exception : MarketCat not found')                                                               #DEBUG
        pass
    #creating stock
    stock = Stock(name=title,price = price ,percent = percent ,ticker=ticker,time = time,netcap=netCap)

    print stock
    ## Write to file 
    text = open("StocksThreaded.txt","a")
    text.write(stock)
    #return stock    

    
#stockList = ["aapl","spy","goog","nflx"]
#print retriveStock("aapl")\



text = open("StockSymbols.txt",'r')
symols = text.read()
stockList = symols.split('\n')

#getFileFromList(listStockPrice,"listStockPrice.txt")



## HANDLING THE THREADING 
## The need for threading is because of network latency . 

## loop over all the stocks and send each of them in a seperate url .... 
## Since we loose determinism while using threads , we will have to order it at the end if we are to ensure that is it alphabetical 


from threading import Thread



threadlist = []

for stock in stockList:
    stockLower = stock.lower()
    ticker = str(stockLower)
    thread = Thread(target=retriveStock,args=(ticker,))
    thread.start()
    threadlist.append(thread)
    
for line in threadlist:
    line.join()    

