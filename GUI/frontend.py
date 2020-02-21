from kivy.app import App
 
from kivy.uix.label import Label
from kivy.uix.button import Button
 
class FirstKivy(App):
 
    def build(self):
 
        #return Label(text="Hello Kivy!")
        return Button(text="Welcome to the program")

 
FirstKivy().run()