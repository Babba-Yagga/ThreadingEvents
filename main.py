#!/usr/bin/python3

from tkinter import *
from threading import Thread, Event
import ttkbootstrap as tb
from counter import myCounter


class App(tb.Window):

    def __init__(self):
        super().__init__(themename="superhero")
        self.title("Threading & Events")
        self.centerWindow(width=425, height=80)
        self.resizable(width=False, height=False)
        self.appFonts = {}
        self.defineFonts()
        self.defineStyles()        
        self.createButtons()
        self.bindEventsCommands()
        self.configureGrid()

        self.counterThread: Thread = None
        self.counterEvent: Event = None


    def defineFonts(self):
        fontFamily = "Tahoma" 
        self.appFonts['button'] = tb.font.Font(family=f"{fontFamily}", size=12) 


    def defineStyles(self):
        self.btnStyleOutline = tb.Style(tb.DEFAULT_THEME)
        self.btnStyleOutline.configure("primary.Outline.TButton", 
                                       font=self.appFonts['button'], 
                                       width=20)
        
    def createButtons(self):
        self.frmControls = tb.Frame(master=self)
        self.frmControls.pack(pady=(15,12), padx=15, fill="x")

        self.btnStart=tb.Button(
                            master=self.frmControls, 
                            text="Start", 
                            bootstyle=(tb.PRIMARY, tb.OUTLINE),
                            style="primary.Outline.TButton",
                            width=10
                            )

        self.btnExit=tb.Button(
                            master=self.frmControls, 
                            text="Exit", 
                            bootstyle=(tb.PRIMARY, tb.OUTLINE),
                            style="primary.Outline.TButton",
                            width=10                            
                            )


    def btnStartClickEventHandler(self):
        if self.btnStart.cget("text").lower() == "start":
            self.startCount()
        else:
            self.stopCount()


    def startCount(self):
        self.counterEvent = Event()
        counter = myCounter(self, self.counterEvent)
        self.counterThread = Thread(target=myCounter.startCounting, args=(counter,), daemon=True) 
        self.counterThread.start()
        self.btnStart.config(text="Abort")        


    def stopCount(self):
        if (self.counterEvent is not None):
            self.counterEvent.set()
            self.btnStart.config(text="Start")            


    def bindEventsCommands(self):
        self.btnStart.configure(command=self.btnStartClickEventHandler)
        self.btnExit.configure(command=self.destroy)


    def configureGrid(self):
        self.btnStart.grid(padx=(10,10), pady=(0,5), sticky="EW", row=1, column=0)
        self.btnExit.grid(padx=(55,10), pady=(0,5), sticky="EW", row=1, column=1)
        

    def centerWindow(self, width: int, height: int):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")    


if __name__ == "__main__": 
    app = App()
    app.mainloop()
