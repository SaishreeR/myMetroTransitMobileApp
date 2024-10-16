from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import ScreenManager
Window.size = (350, 580)

class MyMMTApp(MDApp):
    
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("app-splash.kv"))
        screen_manager.add_widget(Builder.load_file("app-login.kv"))
        screen_manager.add_widget(Builder.load_file("app-home.kv"))
        return screen_manager
    
    def on_start(self):
        Clock.schedule_once(self.login, 5)
        
    def login(self, *args):
        screen_manager.current = "app-login"
        
    def homes(self, *args):
        screen_manager.current = "app-home"
            
if __name__ == "__main__":
    MyMMTApp().run()

