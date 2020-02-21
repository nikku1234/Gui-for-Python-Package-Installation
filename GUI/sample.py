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

		self.gpu_driver_button = Button(master,text="Installation of GPU Drivers(Ubuntu)",command=self.gpu_driver)
		self.gpu_driver_button.pack()

		self.basic_button = Button(master,text="Install Basic Packages",command=self.basic)
		self.basic_button.pack()

		self.conda_button = Button(master,text="Install Conda ",command=self.conda_install)
		self.conda_button.pack()

		self.basic_conda_button = Button(master,text="Install all the conda Packages",command=self.basic_conda)
		self.basic_conda_button.pack()

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

	def gpu_driver(self):
		os.system("ubuntu-drivers devices")
		os.system("sudo add-apt-repository ppa:graphics-drivers/ppa")
		os.system("sudo ubuntu-drivers autoinstall")

	def list1(self):
		os.system("pip install numpy")

	def conda_install(self):
		os.system("cd /tmp")
		os.system("curl -O https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh")
		os.system("bash Anaconda3-5.2.0-Linux-x86_64.sh")
		os.system("conda update conda")
		os.system("conda update anaconda")

	def basic_conda(self):
		with open('conda_requirements.txt') as f:
			lines = [line.rstrip() for line in f]
		#print(lines)
		for i in lines:
			package = i
			os.system("conda install "+package)

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
		os.system("conda create -n tensorflow_env tensorflow")
		os.system("conda activate tensorflow_env")

	def tensorflow_gpu(self):
		os.system("conda create -n tensorflow_gpuenv tensorflow-gpu")
		os.system("conda activate tensorflow_gpuenv")

	def pytorch_cpu(self):
		os.system("conda create -n pytorch python=3.6 numpy=1.13.3 scipy")

	def pytorch_gpu(self):
		os.system("conda install pytorch torchvision cudatoolkit=10.1 -c pytorch")




root = Tk()
my_gui = MyFirstGUI(root)
root.geometry("500x500")
root.mainloop()

