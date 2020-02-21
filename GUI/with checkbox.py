from tkinter import Tk,Label,Button
import os
import subprocess

class MyFirstGUI:
	def __init__(self,master):
		self.master = master
		master.title("A Simple GUI")

		self.label = Label(master,text="This is the first GUI try")
		self.label.pack()

		self.greet_button = Button(master,text="Greet",command=self.greet)
		self.greet_button.pack()

		self.action_button = Button(master,text="Action",command=self.action)
		self.action_button.pack()

		self.list_button = Button(master,text="List Directories",command=self.list1)
		self.list_button.pack()

		self.close_button = Button(master,text="Close",command=master.quit)
		self.close_button.pack()

	def greet(self):
		print("Greetings!")

	def action(self):
		os.system("echo 'hello world'")

	def list1(self):
		os.system("pip install numpy")

		

class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)


if __name__ == '__main__':
   root = Tk()
   lng = Checkbar(root, ['Python', 'Ruby', 'Perl', 'C++'])
   tgl = Checkbar(root, ['English','German'])
   lng.pack(side=TOP,  fill=X)
   tgl.pack(side=LEFT)
   lng.config(relief=GROOVE, bd=2)

   def allstates(): 
      print(list(lng.state()), list(tgl.state()))
   Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
   Button(root, text='Peek', command=allstates).pack(side=RIGHT)
   root.mainloop()
   #root = Tk()
   #my_gui = MyFirstGUI(root)
   #root.mainloop()

