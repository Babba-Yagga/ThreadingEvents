
import threading
from threading import Thread, Event
from time import sleep


class myCounter():
    
    def __init__(self, App, e: Event, max: int=100):
        self.master = App
        self.event = e 
        self.maximumCount = max


    def startCounting(self):
        threadID = threading.get_native_id()

        print(f"\nThread [{threadID}] has started...")

        for i in range(1, self.maximumCount+1):
            print(f"  Count = {i:3}")
            sleep(.1)

            if self.event.isSet():
                print(f"\nThread [{threadID}] was aborted!")
                return

        else:
            print(F"\nThread [{threadID}] ran to completion!")
            



