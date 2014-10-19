# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 21:51:29 2014

@author: Sandeep

Learn about Locks
"""

import threading
import time

def thread1():
    global var , lock
    lock.acquire()
    try:
        while (var<10):
          #  time.sleep(1)
            var += 1
            print "+"
            print var
    finally:
        lock.release()
        
    
def thread2():
    global var ,lock
    lock.acquire()
    print "Lock acquired by 2 thread"
    try:
        while (var<20):
           # time.sleep(1)
            var += 1  
            print "-"
            print var
            print
    finally:
        lock.release()


def main():
    lock = threading.Lock()
    global var , lock
    
    var = 0
    thread_1 = threading.Thread(target=thread1)
    thread_2 = threading.Thread(target =thread2)
    
    thread_1.start()
 

    thread_2.start()

    lock.acquire()
    print "Lock acquired by main thread"
    while (var<30):
      #  time.sleep(1)
    
        var += 1
        print "*"
        print var       

if (__name__ == "__main__"):
    main()
    