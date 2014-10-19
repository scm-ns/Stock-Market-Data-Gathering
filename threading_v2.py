# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 21:51:29 2014

@author: Sandeep
"""

import threading
import time

def thread1():
    global var
    while (var<10):
      #  time.sleep(1)
        var += 1
        print "+"
        print var
        print
        
    
def thread2():
    global var
    print "-----------"
    while (var<20):
       # time.sleep(1)
        var += 1  
        print "-"
        print var
        print


def main():
    global var
    var = 0
    thread_1 = threading.Thread(target=thread1)
    thread_2 = threading.Thread(target =thread2)
    
    thread_1.start()
    thread_1.join()

    thread_2.start()
    #thread_2.join()
    
    print "############"
    while (var<30):
      #  time.sleep(1)
    
        var += 1
        print "*"
        print var       

if (__name__ == "__main__"):
    main()
    