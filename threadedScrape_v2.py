# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 16:55:40 2014

@author: Sandeep
"""

from threading import Thread
import urllib2
from GetReqRegexFromText import getReqRegexFromText

 

def threaded(query):
        # Different tags for different items
    ticker = query.lower()
    priceTag = "<span id=\"yfs_l84_"+str(ticker)+"\">(.+?)</span>"
   # percentTag = "<span id=\"yfs_p20_"+str(ticker)+"\">(.+?)</span>"
    #timeTag = "<span id=\"yfs_t53_"+str(ticker)+"\">(.+?)</span>"
   # titleTag = "<h2>(.+?)</h2>"
    
    
    text  = urllib2.urlopen("http://finance.yahoo.com/q?s="+str(ticker)).read()
    price = getReqRegexFromText(text,priceTag)
    #title = getReqRegexFromText(text,titleTag)
    result =  str(query) + " : " + str(price)
    print str(result)
    #return result


text = open("StockSymbols.txt",'r')
symols = text.read()
stockList = symols.split('\n')

threadlist = []

for stock in stockList:
    print stock
    thread = Thread(target=threaded,args=(stock,))
    thread.start()
    threadlist.append(thread)
    
for line in threadlist:
    line.join()
    print line

#print threaded("AAPL")