# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 00:47:41 2014

@author: Sandeep
"""

from WebCrawler import betterWebCrawl,getFileFromList
from urlExtract import getTitleFromUrl




def getLinkedTitle(url):
    urlList = betterWebCrawl(url,maxPages=1)
    getFileFromList(urlList,"urlList.txt")
    titleList = getTitleFromUrl(urlList)
    getFileFromList(titleList,"titleList.txt")
    
    for title in titleList:
        print title
    print "Summary :\n Sites found : ", len(urlList) ,"\n Titles found :" , len(titleList)




def main():
    getLinkedTitle("http://cnn.com")


if __name__ == "__main__":
    main()