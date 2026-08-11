import json
import os
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.uix.screenmanager import Screen
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.clock import Clock
from kivymd.uix.boxlayout import MDBoxLayout

def upload():
    if not os.path.exists("data.json"):
        with open("data.json", "w") as file:
            json.dump([], file)
            return []
    with open("data.json", "r") as file:
        return json.load(file)
list_todo = upload()
class Task_sreen(Screen):
    def display(self,dt=None):  
        print("function to display the tasks")
        list_todo = upload()
        layout = self.ids.task          
        layout.clear_widgets()          
        app=MDApp.get_running_app() 
        for index, task in enumerate(list_todo):
            label = MDLabel(
                text=f"{index}: {task}\n",
                halign="center",
                theme_text_color="Primary",
                font_style="H5",
            )
            delete_button = MDFillRoundFlatIconButton(
                icon="delete",
                text="Delete",
                md_bg_color="red",
                on_release=lambda x, idx=index: self.delete(idx),
            )
            card = MDCard(
                size_hint=(None, None),   
                size=(1200, 200),
                spacing=100,
                padding=50,
            )
            button_box = MDBoxLayout(
            orientation="horizontal",
            spacing="10dp",
            size_hint=(None, None),
            size=("220dp", "40dp"),
            pos_hint={"right": 0.98, "y": 0.005},
            )
            card.add_widget(label)
            button_box.add_widget(delete_button)
            card.add_widget(button_box)
            layout.add_widget(card)
    def on_enter(self):   
        Clock.schedule_once(self.display, 0)  

    def delete(self, idx):              
        list_todo.pop(idx)
        with open("data.json", "w") as file:
            json.dump(list_todo, file, indent=4)
        self.display()
class adding_task(Screen):  
    def write(self):
        Task = self.ids.new_task.text
        if Task.strip()=="":
            self.ids.not_empty.text="Task cannot be empty"
        else:
            list_todo.append(Task)
            with open("data.json", "w") as file:
                json.dump(list_todo, file, indent=4)
                self.ids.new_task.text=""
                self.ids.not_empty.text_color="green"
                self.ids.not_empty.text="Task saved succesfully"         
class WindowManager(ScreenManager):
    pass
class Task_manager(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return WindowManager()

    def switch(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
            self.theme_cls.theme_style_switch_animation_duration = 0.8
        else:
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.theme_style_switch_animation_duration = 0.8

if __name__ == "__main__":
    Task_manager().run()