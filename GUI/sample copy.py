# Written by Nikhil Ramesh on 22-Feb-2019
# Last update on 24-Feb-2019


import Tkinter as tk
import os
import subprocess
from tkinter import Tk, Label, Button


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        def show(self):
            self.lift()


class Page1(Page):
    def __init__(self, master,*args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 1")
        label.pack(side="top", fill="both", expand=True)
        self.master = master
        # master.title("Python Package GUI Installation")

        self.label = Label(master, text="This is the first GUI try, BETA")
        self.label.pack()

        self.greet_button = Button(
            master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.action_button = Button(
            master, text="Action", command=self.action)
        self.action_button.pack()

        self.list_button = Button(
            master, text="List Directories", command=self.list1)
        self.list_button.pack()

        self.gpu_driver_button = Button(
            master, text="Installation of GPU Drivers(Ubuntu)", command=self.gpu_driver)
        self.gpu_driver_button.pack()

        self.basic_button = Button(
            master, text="Install Basic Packages", command=self.basic)
        self.basic_button.pack()

        self.update_all_button = Button(
            master, text="Update all the Packages Installed", command=self.update_all)
        self.update_all_button.pack()

        self.conda_button = Button(
            master, text="Install Conda ", command=self.conda_install)
        self.conda_button.pack()

        self.basic_conda_button = Button(
            master, text="Install all the conda Packages", command=self.basic_conda)
        self.basic_conda_button.pack()

        self.tensorflow_cpu_button = Button(
            master, text="Install Tensorflow Cpu Packages", command=self.tensorflow_cpu)
        self.tensorflow_cpu_button.pack()

        self.tensorflow_gpu_button = Button(
            master, text="Install Tensorflow Gpu Packages", command=self.tensorflow_gpu)
        self.tensorflow_gpu_button.pack()

        self.pytorch_cpu_button = Button(
            master, text="Install PyTorch Cpu Packages", command=self.pytorch_cpu)
        self.pytorch_cpu_button.pack()

        self.pytorch_gpu_button = Button(
            master, text="Install Pytorch Gpu Packages", command=self.pytorch_gpu)
        self.pytorch_gpu_button.pack()

        self.all_clear_button = Button(
            master, text="Clear all the Packages", command=self.all_clear)
        self.all_clear_button.pack()

        self.close_button = Button(
            master, text="Close", command=master.quit)
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

        def update_all(self):
            os.system("pip install yolk3k")
            os.system("yolk --upgrade")

        def conda_install(self):
            os.system("cd /tmp")
            os.system(
                "curl -O https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh")
            os.system("bash Anaconda3-5.2.0-Linux-x86_64.sh")
            os.system("conda update conda")
            os.system("conda update anaconda")

        def basic_conda(self):
            with open('conda_requirements.txt') as f:
                lines = [line.rstrip() for line in f]
            # print(lines)
            for i in lines:
                package = i
                os.system("conda install " + package)

        def basic(self):
            with open('basic_requirements.txt') as f:
                lines = [line.rstrip() for line in f]
            # print(lines)
            for i in lines:
                package = i
                os.system("pip install " + package)
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
            os.system(
                "conda install pytorch torchvision cudatoolkit=10.1 -c pytorch")

        def all_clear(self):
            os.system("pip freeze | xargs pip uninstall -y")

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("500x500")
    root.mainloop()
                # root = Tk()
                # my_gui = MyFirstGUI(root)
                # root.geometry("500x500")
                # root.mainloop()
