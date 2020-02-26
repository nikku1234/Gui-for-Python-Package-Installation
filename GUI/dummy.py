from tkinter import *
import subprocess


root = Tk()
frame = Frame(root,width=1024, height=768)
frame.grid(row=0, column=0)
c = Canvas(frame, bg='blue', width=800, height=600)
c.config(scrollregion=(0, 0, 800, 3000))
sbar = Scrollbar(frame)
sbar.config(command=c.yview)
c.config(yscrollcommand=sbar.set)
sbar.pack(side=RIGHT, fill=Y)
c.pack(side=LEFT, expand=True, fill=BOTH)

String1 = subprocess.check_output('chcp 437 && ping /?', shell=True)
c.create_text(400, 0, anchor=N, fill='orange', font='Times 15', text=String1)
# c.create_text(750, 300, anchor=W, fill='orange', font='Times 28', text='List')

button = Button(root, text="Quit", command=root.destroy)
c.create_window(400, 0, anchor=N, window=button)

mainloop()
