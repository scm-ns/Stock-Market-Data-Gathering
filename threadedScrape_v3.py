# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 16:55:40 2014

@author: Sandeep

Create an dictionary to store all the values .
Write to file from that dictionary rather than 
writing from the url request 
"""

from threading import Thread
import urllib2
from GetReqRegexFromText import getReqRegexFromText

 
mainDict = {}

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
        print("Exception URL")
        mainDict[query]="Unavaliable"
        return 0 
    #title = getReqRegexFromText(text,titleTag)
    #result =  str(query) + " : " + str(price)
    #print str(result)
    #return result
    #return mainDict

text = open("StockSymbols.txt",'r')
symols = text.read()
stockList = symols.split('\n')

threadlist = []

print(" STEP 1 WRITING TO THE DICT FROM MULTIPLE THREADS ")
for stock in stockList:
    print stock
    thread = Thread(target=threaded,args=(stock,))
    thread.start()
    threadlist.append(thread)

print("WAITING FOR ALL OF THEM TO END")
# THIS STEP IS NOT NEEDED IF WE DO NOT HAVE A MAIN THREAD TO EXECUTE
for line in threadlist:
   line.join(5)
   # Join stops execution of others threads until the current one is complete 
   # This slows down the process
   # But removing join , can lead to key Error in main dict as the values 
   # may be read from the dict before they finish executing 
   
   # In a new version Trying to stop the unwrapping of mainDict unitl 
   # every thread has been executed with out the time lag
    #print line
    # Using join makes everything into a single thread id .. ? Not sure about Thread , but id is made the same
#print threaded("AAPL")
    
#Printing from the main Dict 
# 
    
print(" PRINTING ALL OF THEM OUT FROM THE DICT")
StockDict = open("StockDictThreaded_v3.txt",'a')
for stock in stockList:
    try:
        temp = mainDict[stock]
    except Exception:
        print("EXCEPTION DICT")
        continue
        pass
    result = str(stock) + " : " + str(mainDict[stock])
    print result 
    StockDict.write(result)
    StockDict.write("\n")
    
    
    