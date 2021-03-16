from tkinter import *
from tkinter import ttk

root = Tk()
joit_1 = DoubleVar()
joit_2 = DoubleVar()
joit_3 = DoubleVar()
joit_4 = DoubleVar()


def btn_add(x):
    if(x == 1):
        get_value = float(joit_1.get())
        get_value += 0.50
        joit_1.set(get_value)


def btn_reduce(x):
    if(x == 1):
        get_value = float(joit_1.get())
        get_value -= 0.50
        joit_1.set(get_value)


# laout joint 1
label_joint_1 = ttk.Label(root, text='joint 1')
label_joint_1.grid(row=0, column=0, padx=5, pady=5)

btn_add1 = Button(root, text="add", padx=5, pady=5, command=lambda: btn_add(1))
btn_add1.grid(row=1, column=0, padx=5, pady=5)


btn_reduce1 = Button(root, text="reduce", padx=5, pady=5,
                     command=lambda: btn_reduce(1))
btn_reduce1.grid(row=1, column=2, padx=5, pady=5)

scale_joint_1 = Scale(root, orient=HORIZONTAL, from_=180,
                      to=0, repeatdelay=5, resolution=0.5, showvalue=1, variable=joit_1)
scale_joint_1.grid(row=1, column=1, padx=5, pady=5)
# end laout joint 1

# laout joint 2
label_joint_2 = ttk.Label(root, text='joint 2')
label_joint_2.grid(row=3, column=0, padx=5, pady=5)

btn_add2 = Button(root, text="add", padx=5, pady=5)
btn_add2.grid(row=4, column=0, padx=5, pady=5)

btn_reduce2 = Button(root, text="reduce", padx=5, pady=5)
btn_reduce2.grid(row=4, column=2, padx=5, pady=5)

scale_joint_2 = Scale(root, orient=HORIZONTAL, from_=0,
                      to=180, repeatdelay=5, resolution=0.5, showvalue=1)
scale_joint_2.grid(row=4, column=1, padx=5, pady=5)
# end laout joint 2

# laout joint 3
label_joint_3 = ttk.Label(root, text='joint 3')
label_joint_3.grid(row=5, column=0, padx=5, pady=5)

btn_add3 = Button(root, text="add", padx=5, pady=5)
btn_add3.grid(row=6, column=0, padx=5, pady=5)

btn_reduce3 = Button(root, text="reduce", padx=5, pady=5)
btn_reduce3.grid(row=6, column=2, padx=5, pady=5)

scale_joint_3 = Scale(root, orient=HORIZONTAL, from_=0,
                      to=180, repeatdelay=5, resolution=0.5, showvalue=1)
scale_joint_3.grid(row=6, column=1, padx=5, pady=5)
# end laout joint 3

# laout joint 3
label_joint_4 = ttk.Label(root, text='joint 4')
label_joint_4.grid(row=7, column=0, padx=5, pady=5)

btn_add4 = Button(root, text="add", padx=5, pady=5)
btn_add4.grid(row=8, column=0, padx=5, pady=5)

btn_reduce4 = Button(root, text="reduce", padx=5, pady=5)
btn_reduce4.grid(row=8, column=2, padx=5, pady=5)

scale_joint_4 = Scale(root, orient=HORIZONTAL, from_=0,
                      to=180, repeatdelay=5, resolution=0.5, showvalue=1)
scale_joint_4.grid(row=8, column=1, padx=5, pady=5)
# end laout joint 3

root.mainloop()
