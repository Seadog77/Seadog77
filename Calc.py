from tkinter import *
import math 

root=Tk()
root.title('Useless Combinatory Calculator')
root.geometry('400x500+200+200')
root.configure(background='green')
root.columnconfigure([0,1,2],weight=1,minsize=75)
root.rowconfigure([0,1,2,3,4],weight=1,minsize=75)

display = Entry(root,width=35,borderwidth=5)
display.grid(row=0,column=0,columnspan=3,padx=10,pady=10,sticky='nsew')
def Add(value):
    display.insert('end',value)

def Fact():
    inp=display.get()
    display.delete(0,'end')
    if inp != '0' and inp:
        res=math.factorial(int(inp))
        if res<=1000000000:
            dis_res = f'{res:,}'
            display.insert(0,dis_res)
        else:
            dis_res = f'{res:e}'
            display.insert(0,dis_res)
    else:
        display.delete(0,'end')

def Quad():
    values=display.get()
    new_values=values.split()
    base=new_values[0]
    exp=new_values[1]
    display.delete(0,'end')            
    if base != '0' and base:
        res=math.pow(float(base),float(exp))
        if res<=1000000000:
            dis_res = f'{res:,}'
            display.insert(0,dis_res)
        else:
            dis_res = f'{res:e}'
            display.insert(0,dis_res)
    else:
        display.delete(0,'end')
    

def Clear():
    display.delete(0,'end')

def Log():
    inp=display.get()
    display.delete(0,'end')
    if inp != '0' and inp:
        res=math.log(int(inp))
        if res<=1000000000:
            dis_res = f'{res:,}'
            display.insert(0,dis_res)
        else:
            dis_res = f'{res:e}'
            display.insert(0,dis_res)
    else:
        display.delete(0,'end')

def Open():
    top = Toplevel()
    top.title('Help')
    top.geometry('700x100+800+200')
    help = Label(top,text = 'If you need to calculate the possible combination of n elemet use n!\n If you need to calculate the possible combination of n elements on m position use ^m separate base and exp with space\n If you need to calculate the O(log n) for a range of n use log n ')
    help.pack()
    close = Button(top,text='Close',command = top.destroy).pack()

button_1 = Button(root,text=1,padx=40,pady=20,command=lambda: Add(1)).grid(row=3,column=0,sticky='nsew')
button_2 = Button(root,text=2,padx=40,pady=20,command=lambda: Add(2)).grid(row=3,column=1,sticky='nsew')
button_3 = Button(root,text=3,padx=40,pady=20,command=lambda: Add(3)).grid(row=3,column=2,sticky='nsew')
button_4 = Button(root,text=4,padx=40,pady=20,command=lambda: Add(4)).grid(row=2,column=0,sticky='nsew')
button_5 = Button(root,text=5,padx=40,pady=20,command=lambda: Add(5)).grid(row=2,column=1,sticky='nsew')
button_6 = Button(root,text=6,padx=40,pady=20,command=lambda: Add(6)).grid(row=2,column=2,sticky='nsew')
button_7 = Button(root,text=7,padx=40,pady=20,command=lambda: Add(7)).grid(row=1,column=0,sticky='nsew')
button_8 = Button(root,text=8,padx=40,pady=20,command=lambda: Add(8)).grid(row=1,column=1,sticky='nsew')
button_9 = Button(root,text=9,padx=40,pady=20,command=lambda: Add(9)).grid(row=1,column=2,sticky='nsew')
button_0 = Button(root,text=0,padx=40,pady=20,command=lambda: Add(0)).grid(row=4,column=1,sticky='nsew')
button_factorial = Button(root,text='n!',padx=40,pady=20,command=Fact).grid(row=4,column=0,sticky='nsew')
button_clear = Button(root,text='C',padx=40,pady=20,command=Clear,fg='red').grid(row=4,column=2,sticky='nsew')
button_quad = Button(root,text='^m',padx=40,pady=20,command=Quad).grid(row=5,column=0,sticky='nsew')
button_quad = Button(root,text='log n',padx=40,pady=20,command=Log).grid(row=5,column=1,sticky='nsew')
button_quad = Button(root,text='Help',padx=40,pady=20,command=Open).grid(row=5,column=2,sticky='nsew')





root.mainloop()

