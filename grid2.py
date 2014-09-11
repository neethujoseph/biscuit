from Tkinter import *

win = Tk()
win.title('inspection observation')
def inspect_bis():
    list = ['bis1','bis2','bis3','bis4']
    print len(list)

b1 = Button(win, text="No: of biscuits inspected", width=25)
b2 = Button(win, text="Passed biscuits", width=25)
b3 = Button(win, text='Failed biscuits', width=25)
b4 = Button(win, width=10, command=inspect_bis())
b5 = Button(win, width=10)
b6 = Button(win, width=10)

b1.grid(row=0, column=0)
b2.grid(row=1, column=0)
b3.grid(row=2, column=0)
b4.grid(row=0, column=1)
b5.grid(row=1, column=1)
b6.grid(row=2, column=1)
mainloop()

