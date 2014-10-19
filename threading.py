# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 21:51:29 2014

@author: Sandeep
"""

import threading
import time

def printRubbish():
    print "This gets executed first"
    #time.sleep(10)
    print "HELLO THREADS"
    global kill_thread
    while ( not kill_thread ):
        pass
    print("All THreads will be ended ")
    

def main():
    
    global kill_thread
    kill_thread = False
    thread = threading.Thread(target=printRubbish)
    thread.start()
    print threading.active_count() # Returns number of counts
    print threading.enumerate() # Returns list of counts
    print threading.current_thread()
    # a global varible defined in one thread is observable by the other threads
    raw_input("Press Enter to Kill all threads :")
    kill_thread = True
    
    
if (__name__ == "__main__"):
    main()
    