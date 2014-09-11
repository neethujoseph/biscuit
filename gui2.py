
from Tkinter import *
import pylab
from repeated_timer import repeatedTimer

import numpy
import cv2


def video():
	
	Gray_1 = cv2.cvtColor(Video.read()[1], cv2.COLOR_BGR2GRAY)
	img = PhotoImage(Gray_1)
	cv2.imshow('',img)
def start():
	print 'hai'
	##video()
	#pass
	
	
def stop():
	pass

Video = cv2.VideoCapture(0)
t = repeatedTimer(0,video)


window=Tk()
window.title('biscuit gui')
window.geometry('600x600') 

win=Frame(window)
win.pack(side='bottom')

canvas=Canvas(window,width=300,height=300)
canvas.config(bg='white')
canvas.pack(side='left')
canvas.bind=("<Button-1>", video())

button1 = Button(win, text="START", width=8,command=video)
button1.pack(side='left',padx=5,pady=5)

button2 = Button(win, text="STOP",width=8, command=stop)
button2.pack(side='left',padx=5,pady=5)

window.mainloop()
