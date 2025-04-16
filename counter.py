
from threading import Thread, Event
from time import sleep


class myCounter():
    
    def __init__(self, App, e: Event, max: int=100):
        self.master = App
        self.event = e 
        self.maximumCount = max


    def startCounting(self):

        for i in range(1, self.maximumCount+1):
            print(f"Count = {i:3}")
            sleep(.1)

            if i % 5 == 0 and self.event.isSet():
                print('\nThe thread was aborted.')
                break

        else:
            print('\nThe thread ran to completion.')
            



