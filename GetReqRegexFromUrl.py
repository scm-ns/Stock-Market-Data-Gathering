# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 01:56:17 2014
... Give the regex coding and this will give a list of the result for the regex patter 
@author: Sandeep
"""


import urllib2
import re

#urlList = ["http://google.com","http://a","http://nytimes.com","http://cnn.com"]

stockhtml = <span id="yfs_l84_aapl">(.+?)</span>

def getReqRegexFromText(regex=stockhtml ):
    # REGEX for extractions 
    #regex = '<title>(.+?)</title>' # Retreives all chach between them
    pattern= re.compile(regex)
                                                                       #DEBUG
    if(url.find("http://") == -1 ):
        continue#Least expensive 
    try: 
        htm = urllib2.urlopen(url)
    except urllib2.HTTPError, e:
        print('HTTPError = ' + str(e.code))
        pass
    except urllib2.URLError, e:
        print('URLError = ' + str(e.reason))
        pass
    except Exception:
        print('Exception')
        pass
            
    htm_txt = htm.read()
    title = re.findall(pattern_title,htm_txt)
        #print titles                                                                       #DEBUG
    titles += title
    return titles
    
#print getTitleFromUrl(urlList)