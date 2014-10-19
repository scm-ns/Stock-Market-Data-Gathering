# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 16:55:40 2014

@author: Sandeep
"""

from threading import Thread
import urllib2
import re

def threaded(url):
    regex="<title>(.+?)</title>"
    pattern = re.compile(regex)
    text  = urllib2.urlopen(url).read()
    result = re.findall(pattern,text)
    print result

urls = "http://yaroslavvb.blogspot.com/ http://stackoverflow.com/questions/4706499/how-do-you-append-to-file-in-python https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=append%20to%20a%20file%20python".split()

threadlist = []

for url in urls:
    thread = Thread(target=threaded,args=(url,))
    thread.start()
    threadlist.append(thread)
    
for line in threadlist:
    print line
   