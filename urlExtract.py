# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 00:24:31 2014

@author: Sandeep
"""

import urllib2
import re

#urlList = ["http://google.com","http://a","http://nytimes.com","http://cnn.com"]



def getTitleFromUrl(urlList):
    # REGEX for extractions 
    re_title = '<title>(.+?)</title>' # Retreives all chach between them
    pattern_title = re.compile(re_title)
    titles = []
    for url in urlList:
        #print url                                                                        #DEBUG
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