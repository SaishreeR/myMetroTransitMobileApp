from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem

Window.size = (350, 580)

class MyMMTApp(MDApp):
    
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("app-splash.kv"))
        screen_manager.add_widget(Builder.load_file("app-login.kv"))
        screen_manager.add_widget(Builder.load_file("app-home.kv"))
        screen_manager.add_widget(Builder.load_file("app-buytickets.kv"))
        screen_manager.add_widget(Builder.load_file("app-departurevision.kv"))
        screen_manager.add_widget(Builder.load_file("app-schedules.kv"))
        screen_manager.add_widget(Builder.load_file("app-njsrewards.kv"))
        screen_manager.add_widget(Builder.load_file("app-rail.kv"))
        return screen_manager
    
    def on_start(self):
        Clock.schedule_once(self.login, 5)
        
    def login(self, *args):
        screen_manager.current = "app-login"
        
    def homes(self, *args):
        screen_manager.current = "app-home"

    def on_switch_tabs(
            self,
            bar: MDNavigationBar,
            item: MDNavigationItem,
            item_icon: str,
            item_text: str,
    ):

        screen_manager.current_screen.ids["myHomeScreen"].current = item_text
            
if __name__ == "__main__":
    MyMMTApp().run()

