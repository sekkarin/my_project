from tkinter import *


def Test():
    pass


def btn_():
    x = var_slider.get()
    selec_ = "value ="+str(var_slider.get())
    Label.config(text=selec_)
    x += 1
    scale_value.set(x)


root = Tk()
var_slider = DoubleVar()

btn_add = Button(root, text="ADD", padx=30, pady=30,
                 command=btn_,
                 )
btn_add.pack(anchor=CENTER)
scale_value = Scale(root,
                    orient=HORIZONTAL,
                    from_=1,
                    to=180,
                    resolution=1,
                    variable=var_slider,
                    )
scale_value.pack(anchor=CENTER)
Label = Label(root)
Label.pack()
root.mainloop()
