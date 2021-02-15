# นําเข้าโมดูล
from tkinter import *
# ใช้งานคลาส ttk
from tkinter import ttk
# สร้างเมธอด เพื่อมาคํานวณการแปลงเปลี่ยนฟุตไปเมตร
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048*value*10000.0+0.5)/10000.0)
    except ValueError:
        pass
# การสร้างหน้าต่างหลัก  mian windown  = root
root = Tk()
root.title("Test calculate")
# สร้าง frame
mainfrm = ttk.Frame(root, padding="3 3 12 12")
mainfrm.grid(column=0, row=0, sticky=(N, W, E, S))
mainfrm.columnconfigure(0, weight=1)
mainfrm.rowconfigure(0, weight=1)

# สร้างตัวแปร
feet = StringVar()
meters = StringVar()

# สร้าง widgets ลงไปใน frame
feet_entry = ttk.Entry(mainfrm, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainfrm, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainfrm, text="feet").grid(column=3, row=1, sticky=E)
ttk.Label(mainfrm, text="is equivalent to ").grid(column=1, row=2, sticky=E)
ttk.Label(mainfrm, text="meters").grid(column=3, row=2, sticky=W)
# กําหนดให้โปรแกรมทําการวาด wodgets ต่างๆ ที่อยู่ในเฟรมลงบน grid 
for child in mainfrm.winfo_children():
    child.grid_configure(padx=5, pady=5)
feet_entry.focus()
#ตรวจจับเมื่อผุ้ใช้กดปุ่ม Enter 
root.bind('<Return>', calculate)


root.mainloop()
