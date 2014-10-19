# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 01:56:17 2014
... Give the regex coding and this will give a list of the result for the regex patter 
@author: Sandeep
"""



import re

#urlList = ["http://google.com","http://a","http://nytimes.com","http://cnn.com"]

stockhtml = "<span id=\"yfs_l84_aapl\">(.+?)</span>"

def getReqRegexFromText(text,regex):
    """  
    getReqRegexFromText(text,regex=stockhtml):
    
    Input :
        Function needs the text and regex
    Output: 
        Gives output of regex pattern
    function creates a pattern with the given regex and then finds it from 
    the text
    
    """
    # REGEX for extractions 
    #regex = '<title>(.+?)</title>' # Retreives all chach between them
    pattern= re.compile(regex)      
    result = re.findall(pattern,text)
        #print titles                                                                       #DEBUG
    return result
    
#print getTitleFromUrl(urlList)