from tkinter import *
from tkinter import ttk


mainfrm = Tk()  # create root obb

ladevar = StringVar()
def get_value_scale (e):
    value_servo1 = value_servo1_scale.get()
    ladevar.set(value_servo1_scale.get())
    
def btn_callback():
    Scale_servo1.bind('<B1-Motion>',get_value_scale)

btn_add_servo1 = Button(mainfrm,bd =0.5,text ="add",height = 3,padx = 5,command = btn_callback)
btn_add_servo1.grid(column = 0,row =0,padx = 5,pady=5)
btn_add_servo1.invoke()

Scale_servo1 = Scale(mainfrm,from_=0 , to=180,label ="GRIPPER", orient = HORIZONTAL , resolution = 0.01,sliderlength = 10,variable = value_servo1_scale,repeatdelay = 5,takefocus = 0)
Scale_servo1.grid(column = 1,row = 0)
Scale_servo1.set(90)
Scale_servo1.bind('<B1-Motion>',get_value_scale)

btn_reduce_servo1 = Button(mainfrm,bd =0.5,text ="reduce",height = 3,padx = 5)
btn_reduce_servo1.grid(column = 2,row =0,padx = 5,pady=5)

Label_ = Label(mainfrm,textvariable = ladevar,text="display value")
Label_.grid()

mainfrm.mainloop()
