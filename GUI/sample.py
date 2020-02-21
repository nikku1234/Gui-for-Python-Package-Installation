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

		self.basic_button = Button(master,text="Install Basic Packages",command=self.basic)
		self.basic_button.pack()

		self.tensorflow_cpu_button = Button(master,text="Install Tensorflow Cpu Packages",command=self.tensorflow_cpu)
		self.tensorflow_cpu_button.pack()

		self.tensorflow_gpu_button = Button(master,text="Install Tensorflow Gpu Packages",command=self.tensorflow_gpu)
		self.tensorflow_gpu_button.pack()

		self.pytorch_cpu_button = Button(master,text="Install PyTorch Cpu Packages",command=self.pytorch_cpu)
		self.pytorch_cpu_button.pack()

		self.pytorch_gpu_button = Button(master,text="Install Pytorch Gpu Packages",command=self.pytorch_gpu)
		self.pytorch_gpu_button.pack()

		self.close_button = Button(master,text="Close",command=master.quit)
		self.close_button.pack()

	def greet(self):
		print("Greetings!")

	def action(self):
		os.system("echo 'hello world'")

	def list1(self):
		os.system("pip install numpy")

	def basic(self):
		with open('basic_requirements.txt') as f:
			lines = [line.rstrip() for line in f]
		#print(lines)
		for i in lines:
			package = i
			os.system("pip install "+package)
			os.system("pip install pip-review")
			os.system("pip-review --local --interactive")

    

	def tensorflow_cpu(self):
		print("Greetings!")

	def tensorflow_gpu(self):
		print("Greetings!")

	def pytorch_cpu(self):
		print("Greetings!")

	def pytorch_gpu(self):
		print("Greetings!")




root = Tk()
my_gui = MyFirstGUI(root)
root.geometry("500x500")
root.mainloop()

