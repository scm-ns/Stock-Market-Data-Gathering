# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 16:55:40 2014

@author: Sandeep

Create an dictionary to store all the values .
Write to file from that dictionary rather than 
writing from the url request 
"""

from threading import Thread,active_count
import urllib2
from GetReqRegexFromText import getReqRegexFromText
from time import sleep

 
mainDict = {}

# THiS FUNCTION FORMS MANY THREADS
def threaded(query):
        # Different tags for different items
    ticker = query.lower()
    priceTag = "<span id=\"yfs_l84_"+str(ticker)+"\">(.+?)</span>"
   # percentTag = "<span id=\"yfs_p20_"+str(ticker)+"\">(.+?)</span>"
    #timeTag = "<span id=\"yfs_t53_"+str(ticker)+"\">(.+?)</span>"
   # titleTag = "<h2>(.+?)</h2>"
    
    try:
        text  = urllib2.urlopen("http://finance.yahoo.com/q?s="+str(ticker)).read()
        price = getReqRegexFromText(text,priceTag)
        mainDict[query]=price
    except Exception:
        #print("Exception URL")
        mainDict[query]="Unavaliable"
        return 0 
    #title = getReqRegexFromText(text,titleTag)
    #result =  str(query) + " : " + str(price)
    #print str(result)
    #return result
    

text = open("StockSymbols.txt",'r')
symols = text.read()
stockList = symols.split('\n')

threadlist = []

print(" STEP 1 WRITING TO THE DICT FROM MULTIPLE THREADS ")
for stock in stockList:
    #print stock
    thread = Thread(target=threaded,args=(stock,))
    thread.start()
    threadlist.append(thread)
    

print(" Giving some time before unwarpping of Dict to finish execution") 
# sleep until number of active_count == 0

sec = 0 
while(active_count() > 25): 
    print "sec :" ,sec,"active_count :",active_count()
    print "~"
    sleep(1)
    sec += 1
    
print(" PRINTING ALL OF THEM OUT FROM THE DICT")
StockDict = open("StockDictThreaded_v4.txt",'w')
for stock in stockList:
    try:
        temp = mainDict[stock]
    except Exception:
        #print("EXCEPTION DICT")
        continue
        pass
    result = str(stock) + " : " + str(mainDict[stock])
    print result 
    StockDict.write(result)
    StockDict.write("\n")
print active_count()
    
    