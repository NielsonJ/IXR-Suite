import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import  Button, Canvas, Entry, Frame, Label, LabelFrame, Scrollbar, StringVar, Text, ttk
import sys
import z_flow_separateThread
import threading

class Z_suite():

    def __init__(self,root):
    
        #setting title
        root.title("Z-suite mini v0.1")
        #setting window size
        root.configure(width=900, height=600)
        root.configure(bg='#264653')
        root.resizable(False, False)
        
        # move window center
        winWidth = root.winfo_reqwidth()
        winwHeight = root.winfo_reqheight()
        posRight = int(root.winfo_screenwidth() / 2 - winWidth / 2)
        posDown = int(root.winfo_screenheight() / 2 - winwHeight / 2)
        root.geometry("+{}+{}".format(posRight, posDown))
        
        # title
        titleLabel=tk.Label(root)
        titleLabel["bg"] = "#264653"
        ft = tkFont.Font(family='Helvetica',size=25)
        titleLabel["font"] = ft
        titleLabel["fg"] = "#168aad"
        titleLabel["justify"] = "center"
        titleLabel["text"] = "Z-Suite Mini"
        titleLabel.place(x=350,y=20,width=200,height=25)
        
        # progress bar
        pb=ttk.Progressbar(root,orient='horizontal', mode='determinate',length=600)
        pb.place(x=250, y=507)

        # terminal frame
        
        self.textbox=Text(root)
        self.textbox.pack()
        self.textbox.configure(bg="black",fg="white")
        self.textbox.place(x=400,y=100,width=450,height=310)
        
        scrollbar = tk.Scrollbar(self.textbox, orient="vertical", command=self.textbox.yview)
        scrollbar.pack(side="right", fill="y")

        self.textbox.configure(yscrollcommand=scrollbar.set)
        def redirector(inputStr):
            self.textbox.insert('0.0', inputStr)
           
        sys.stdout.write = redirector #whenever sys.stdout.write is called, redirector is called.
        
        self.boardidEnt=tk.Entry(root)
        self.boardidEnt["bg"] = "#e9f5db"
        self.boardidEnt["borderwidth"] = "1px"
        ft = tkFont.Font(family='Helvetica',size=13)
        self.boardidEnt["font"] = ft
        self.boardidEnt["fg"] = "#264653"
        self.boardidEnt["justify"] = "center"
        self.boardidEnt.insert(END,'39')
        #self.boardidEnt["textvariable"] = self.text_boardid
        self.boardidEnt.place(x=250,y=80,width=70,height=25)
        
        boardidLabel=tk.Label(root)
        boardidLabel["bg"] = "#264653"
        ft = tkFont.Font(family='Helvetica',size=11)
        boardidLabel["font"] = ft
        boardidLabel["fg"] = "#e9f5db"
        boardidLabel["justify"] = "center"
        boardidLabel["text"] = "board ID"
        boardidLabel.place(x=40,y=80,width=200,height=25)
        CreateToolTip(boardidLabel, text = 'Muse 2 is 38, Muse S is 39 (default = 39)')
        
        self.timeoutEnt=tk.Entry(root)
        self.timeoutEnt["bg"] = "#e9f5db"
        self.timeoutEnt["borderwidth"] = "1px"
        ft = tkFont.Font(family='Helvetica',size=13)
        self.timeoutEnt["font"] = ft
        self.timeoutEnt["fg"] = "#264653"
        self.timeoutEnt["justify"] = "center"
        self.timeoutEnt.insert(END,'30')
        self.timeoutEnt.place(x=250,y=120,width=70,height=25)
        
        timeoutLabel=tk.Label(root)
        timeoutLabel["bg"] = "#264653"
        ft = tkFont.Font(family='Helvetica',size=12)
        timeoutLabel["font"] = ft
        timeoutLabel["fg"] = "#e9f5db"
        timeoutLabel["justify"] = "center"
        timeoutLabel["text"] = "timeout"
        timeoutLabel.place(x=40,y=120,width=200,height=25)
        CreateToolTip(timeoutLabel, text = 'Timeout when trying to connect to the board (default = 30)')
        
        self.logBrainDataEnt=tk.Entry(root)
        self.logBrainDataEnt["bg"] = "#e9f5db"
        self.logBrainDataEnt["borderwidth"] = "1px"
        ft = tkFont.Font(family='Helvetica',size=13)
        self.logBrainDataEnt["font"] = ft
        self.logBrainDataEnt["fg"] = "#264653"
        self.logBrainDataEnt["justify"] = "center"
        self.logBrainDataEnt.insert(END,'0')
        self.logBrainDataEnt.place(x=250,y=160,width=70,height=25)
        
        
        braindataLabel=tk.Label(root)
        braindataLabel["bg"] = "#264653"
        ft = tkFont.Font(family='Helvetica',size=12)
        braindataLabel["font"] = ft
        braindataLabel["fg"] = "#e9f5db"
        braindataLabel["justify"] = "center"
        braindataLabel["text"] = "record brain data"
        braindataLabel.place(x=40,y=160,width=200,height=25)
        CreateToolTip(braindataLabel, text = 'Will be stored next to this program (default = 0)')

        self.logConsoleEnt=tk.Entry(root)
        self.logConsoleEnt["bg"] = "#e9f5db"
        self.logConsoleEnt["borderwidth"] = "1px"
        ft = tkFont.Font(family='Helvetica',size=13)
        self.logConsoleEnt["font"] = ft
        self.logConsoleEnt["fg"] = "#264653"
        self.logConsoleEnt["justify"] = "center"
        self.logConsoleEnt.insert(END,'0')
        self.logConsoleEnt.place(x=250,y=200,width=70,height=25)
        
        logConsoleLabel=tk.Label(root)
        logConsoleLabel["bg"] = "#264653"
        ft = tkFont.Font(family='Helvetica',size=12)
        logConsoleLabel["font"] = ft
        logConsoleLabel["fg"] = "#e9f5db"
        logConsoleLabel["justify"] = "center"
        logConsoleLabel["text"] = "log console"
        logConsoleLabel.place(x=40,y=200,width=200,height=25)
        CreateToolTip(logConsoleLabel, text = 'Will be stored next to this program (default = 0)')

        self.calibrationHistoryEnt=tk.Entry(root)
        self.calibrationHistoryEnt["bg"] = "#e9f5db"
        self.calibrationHistoryEnt["borderwidth"] = "1px"
        ft = tkFont.Font(family='Helvetica',size=13)
        self.calibrationHistoryEnt["font"] = ft
        self.calibrationHistoryEnt["fg"] = "#264653"
        self.calibrationHistoryEnt["justify"] = "center"
        self.calibrationHistoryEnt.insert(END,'600')
        self.calibrationHistoryEnt.place(x=250,y=240,width=70,height=25)
        
        calibrationHistoryLabel=tk.Label(root)
        calibrationHistoryLabel["bg"] = "#264653"
        ft = tkFont.Font(family='Helvetica',size=12)
        calibrationHistoryLabel["font"] = ft
        calibrationHistoryLabel["fg"] = "#e9f5db"
        calibrationHistoryLabel["justify"] = "center"
        calibrationHistoryLabel["text"] = "calibration history length"
        calibrationHistoryLabel.place(x=40,y=240,width=200,height=25)
        CreateToolTip(calibrationHistoryLabel, text = 'Duration of the rolling calibration in seconds (default = 600)')


        self.powerHistoryEnt=tk.Entry(root)
        self.powerHistoryEnt["bg"] = "#e9f5db"
        self.powerHistoryEnt["borderwidth"] = "1px"
        ft = tkFont.Font(family='Helvetica',size=13)
        self.powerHistoryEnt["font"] = ft
        self.powerHistoryEnt["fg"] = "#264653"
        self.powerHistoryEnt["justify"] = "center"
        self.powerHistoryEnt.insert(END,'10')
        self.powerHistoryEnt.place(x=250,y=280,width=70,height=25)

        
        powerHistoryLabel=tk.Label(root)
        powerHistoryLabel["bg"] = "#264653"
        ft = tkFont.Font(family='Helvetica',size=12)
        powerHistoryLabel["font"] = ft
        powerHistoryLabel["fg"] = "#e9f5db"
        powerHistoryLabel["justify"] = "center"
        powerHistoryLabel["text"] = "power history length"
        powerHistoryLabel.place(x=40,y=280,width=200,height=25)
        CreateToolTip(powerHistoryLabel, text = 'Duration of the current brain power measurement in s (default = 10)')
        
        self.scaleEnt=tk.Entry(root)
        self.scaleEnt["bg"] = "#e9f5db"
        self.scaleEnt["borderwidth"] = "1px"
        ft = tkFont.Font(family='Helvetica',size=13)
        self.scaleEnt["font"] = ft
        self.scaleEnt["fg"] = "#264653"
        self.scaleEnt["justify"] = "center"
        self.scaleEnt.insert(END,'1.0')
        self.scaleEnt.place(x=250,y=320,width=70,height=25)
        
        
        scale=tk.Label(root)
        scale["bg"] = "#264653"
        ft = tkFont.Font(family='Helvetica',size=12)
        scale["font"] = ft
        scale["fg"] = "#e9f5db"
        scale["justify"] = "center"
        scale["text"] = "scale"
        scale.place(x=40,y=320,width=200,height=25)
        CreateToolTip(scale, text = 'Adjusts the scale of the BCI.\n'
                                    'SMALLER values make it EASIER to reach maximum and minimum \n'
                                    '(recommended between 0.7 and 1.3, default = 1).')

        self.centerEnt=tk.Entry(root)
        self.centerEnt["bg"] = "#e9f5db"
        self.centerEnt["borderwidth"] = "1px"
        ft = tkFont.Font(family='Helvetica',size=13)
        self.centerEnt["font"] = ft
        self.centerEnt["fg"] = "#264653"
        self.centerEnt["justify"] = "center"
        self.centerEnt.insert(END,'0.4')
        self.centerEnt.place(x=250,y=360,width=70,height=25)

        center=tk.Label(root)
        center["bg"] = "#264653"
        ft = tkFont.Font(family='Helvetica',size=12)
        center["font"] = ft
        center["fg"] = "#e9f5db"
        center["justify"] = "center"
        center["text"] = "center"
        center.place(x=40,y=360,width=200,height=25)
        CreateToolTip(center, text = 'The value around which the brainpower should be centered.\n'
                                     'If at 0.5 then your "normal" brain power is 0.5.\n'
                                     'If at 0.3 then your normal brain power is 0.3 and it is more difficult to reach max focus (default = 0.4).')
                                     
                                     
        self.headStrengthEnt=tk.Entry(root)
        self.headStrengthEnt["bg"] = "#e9f5db"
        self.headStrengthEnt["borderwidth"] = "1px"
        ft = tkFont.Font(family='Helvetica',size=13)
        self.headStrengthEnt["font"] = ft
        self.headStrengthEnt["fg"] = "#264653"
        self.headStrengthEnt["justify"] = "center"
        self.headStrengthEnt.insert(END,'0.2')
        self.headStrengthEnt.place(x=250,y=400,width=70,height=25)

        headStrength=tk.Label(root)
        headStrength["bg"] = "#264653"
        ft = tkFont.Font(family='Helvetica',size=12)
        headStrength["font"] = ft
        headStrength["fg"] = "#e9f5db"
        headStrength["justify"] = "center"
        headStrength["text"] = "head impact strength"
        headStrength.place(x=40,y=400,width=200,height=25)
        CreateToolTip(headStrength, text = 'The amount of impact the head movement can have on the brain power (default = 0.2)')
        
        
        
        connectBtn=tk.Button(root,command=self.connectBtn_command)
        connectBtn["activebackground"] = "#989898"
        connectBtn["anchor"] = "w"
        connectBtn["bg"] = "#2a9d8f"
        ft = tkFont.Font(family='Helvetica',size=13)
        connectBtn["font"] = ft
        connectBtn["fg"] = "#000000"
        connectBtn["justify"] = "center"
        connectBtn["text"] = "  Connect"
        connectBtn.place(x=100,y=500,width=90,height=36)

    def connectBtn_command(self):
    
        boardid = int(self.boardidEnt.get())
        timeout = int(self.timeoutEnt.get())
        record = int(self.logBrainDataEnt.get())
        log = int(self.logConsoleEnt.get())
        calib_length = int(self.calibrationHistoryEnt.get())
        power_length = int(self.powerHistoryEnt.get())
        scale = float(self.scaleEnt.get())
        center = float(self.centerEnt.get())
        headStrength = float(self.headStrengthEnt.get())
        
        print('headStrength: ' + self.headStrengthEnt.get())
        print('center: ' + self.centerEnt.get())
        print('scale: ' + self.scaleEnt.get())
        print('power hist length: ' + self.powerHistoryEnt.get())
        print('calib length: ' + self.calibrationHistoryEnt.get())
        print('log: ' + self.logConsoleEnt.get())
        print('record data: ' + self.logBrainDataEnt.get())
        print('timeout: ' + self.timeoutEnt.get())
        print('board ID: ' + str(boardid))
        print('----------------------------------')
        print('Connecting!')
        print('----------------------------------')
        
        x = threading.Thread(target=z_flow_separateThread.connect, args=(boardid, timeout, calib_length, power_length, scale, center, headStrength, record))
        x.start()

        
# class to define message boxes for labels
class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = Z_suite(root)
    root.mainloop()