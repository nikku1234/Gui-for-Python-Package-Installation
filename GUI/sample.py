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



root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

