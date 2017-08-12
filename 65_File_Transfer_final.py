# -*- coding: cp1252 -*-
#   65_PyDrill_UI_File_Transfer_34_idle
#
#   John Goya
#
#   For Python Drill #65 - UI for File Transfer with Python 3.4 & idle.
#
import os
import time
import shutil
import datetime
import tkinter
from tkinter import *
from tkinter.filedialog import askdirectory
#create root window
root = Tk()
#title for root window
root.title('Backup new files')
#create frames
#top frame
topFrame = Frame(root, width=300, height=50)
topFrame.pack_propagate(0)
topFrame.pack()
#bottom frame
bottomFrame = Frame(root, width=300, height=50)
bottomFrame.pack_propagate(0)
bottomFrame.pack(side=BOTTOM)

src=StringVar()
dst=StringVar()

def src_callback():
    dir_src = askdirectory()
    src.set(dir_src)
    #return dir_src   
    print (dir_src)
    
#function for destination folder button press - need to output directory path to dir_src in file transfer script
def dest_callback():   
    dir_dst = askdirectory()
    dst.set(dir_dst)
    #return dir_dst
    print (dir_dst)
     
def fileTransfer():
    now = datetime.datetime.now()
    ago = now-datetime.timedelta(hours=24)
    srcS=src.get()
    dstD=dst.get()
    #for root,dirs,files in os.walk(dir_src):
    for fname in os.listdir(srcS):
        #path = os.path.join(root, fname)
        path = os.path.join(srcS, fname)
        st = os.stat(path)    
        mtime = datetime.datetime.fromtimestamp(st.st_mtime)        
        if mtime > ago:
            shutil.copy(path, dstD)
            print (fname)

#size window
sourceButton = Button(topFrame, wraplength=120, text='Select folder to backup:',
    command= src_callback, width=15).pack(padx=15, pady=5, side=LEFT)
destinationButton = Button(topFrame, wraplength=120, text='Select backup destination folder:',
    command=dest_callback, width=15).pack(padx=15, pady=5, side=RIGHT)
executeButton = Button(bottomFrame, wraplength=120, text='Check files and backup!',
    command=fileTransfer, width=15, fg='green').pack(pady=5)

#main event loop - to keep buttons on screen
root.mainloop()
