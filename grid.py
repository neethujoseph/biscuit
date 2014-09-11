from Tkinter import *

win = Tk()
win.title('inspection observation')
def inspect_bis():
    list = ['bis1','bis2','bis3','bis4']
    print len(list)


b1 = Button(win,text="Perimeter of biscuit",width=25).grid(row=0, column=0)
b2 = Button(win,text="No: of raisins",width=25).grid(row=1, column=0)
b3  =Button(win,text='Overcooked or undercooked',width=25).grid(row=2,column=0)
b4  =Button(win,text='Colour',width=25).grid(row=3,column=0)



e1=Entry(win).grid(row=0, column=1)
e2=Entry(win).grid(row=1, column=1)
e3=Entry(win).grid(row=2,column=1)
e4=Entry(win).grid(row=3,column=1)


mainloop()

