# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 00:17:52 2014

@author: Sandeep
"""
import urllib2

def getURL(text,findString,findString2,findString3):
    urlBegin = text.find(str(findString))
    if(urlBegin == -1): 
     #   print("urlBe") #DEBUG
        return None , 0
    quoteBegin = text.find(findString2,urlBegin)
    quoteEnd = text.find(findString3,quoteBegin + 1)
    url = text[quoteBegin+1:quoteEnd]
   # print url #DEBUG
    return url ,quoteEnd ;



def getAllUrlWith(data,findString,findString2,findString3,urlList = []):
    while(1):
        url , end = getURL(data,str(findString),str(findString2),str(findString3))
     #   print("get") #DEBUG
        data = data[end:]
        if(url == None):
     #       print("break") #DEBUG
            break 
        if(url.find("http://") == -1 ):
            #print "fake"
            continue
        urlList.append(url)       
    return urlList

def getOutput(data,fileName,findString,findString2,findString3):
    result = getAllUrlWith(data,findString,findString2,findString3)
    output = open(str(fileName),"w")
    output.write('\n')
    noOfLinks = 0
    
    if(result[0] == None):
        print ("No url found ")  
        output.write("No url found ")
    #    print("if") #DEBUG
        return
        
    for page in result:
     #   print("for")
        noOfLinks = noOfLinks + 1
        output.write(page)
        output.write('\n')
        
    output.write('\n')
    output.write("No of Links :")
    output.write(str(noOfLinks))


def getStringFromFile(fileName):
    '''Get string from file name'''
    f = open(str(fileName),"r")
    data = f.read()
    return data
    
def getFileFromList(List,filename):
    """" getFileFromList(List,filename):"""
    f = open(str(filename),'w')
    for elem in List:
        f.write(elem)
        f.write('\n')
    
    
def getStringFromUrl(url):
    '''Import urllib2'''
    fileBuffer = urllib2.urlopen('http://www.google.com')
    try:
        fileBuffer = urllib2.urlopen(url)
    except:
        pass
    String = fileBuffer.read()
    return String 
         
def getFileFromUrl(url,outputFileName):
    '''Uses getStringFromUrl(url): and write output'''   
    output = getStringFromUrl(url)
    f = open(outputFileName,'w')
    f.write(output)
    
    
def betterWebCrawl(Furl,maxPages=20):
    """ """
    data = getStringFromUrl(Furl)
    seed = getAllUrlWith(data,"<a href",'"','"')
    crawled =[]
    toCrawl = seed
    while(toCrawl): # This becomes false when the list becomes zero 
        if len(crawled) >= maxPages :
            break
        url = toCrawl.pop(0)
        if(url.find("http://") == -1):
            continue
        if(url in crawled):
            continue
        crawled.append(url)
        data = getStringFromUrl(url)
        subToCrawl = getAllUrlWith(data,"<a href",'"','"')
        for elem in subToCrawl:
            #print elem
            if(elem.find("http://") == -1 ):
                #print "cont"
                continue#Least expensive 
            #print "url",elem
            if(elem not in crawled):     #More expensice
                if(elem not in toCrawl ): 
                    print "url",elem
                    toCrawl.append(elem)  #Most expensive
                    
        getFileFromList(toCrawl,str("toCrawl.txt"))
        print "Crawled: ",len(crawled) ,"toCrawl",len(toCrawl)
       
        print '-'
        
        #getFileFromList(crawled,str("Crawled.txt"))
       # print "toCrawl: ",len(toCrawl)
       # print '+'
    #Saving the files
    #getFileFromList(crawled,str("Crawled.txt"))
    #getFileFromList(toCrawl,str("toCrawl.txt"))
        
    urlList = crawled + toCrawl
    return urlList
    
    
def main():
    #find <a href tags
    url = 'http://www.cnn.com'
    betterWebCrawl(url,100)
    
    
if __name__ == "__main__":
    main()