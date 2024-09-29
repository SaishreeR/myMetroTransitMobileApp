from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from kivymd.uix.screen import MDScreen

class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()


class BaseScreen(MDScreen):
    ...


KV = '''
<BaseMDNavigationItem>

    MDNavigationItemIcon:
        icon: root.icon

    MDNavigationItemLabel:
        text: root.text


<BaseScreen>

    MDLabel:
        text: root.name
        halign: "center"


MDBoxLayout:
    orientation: "vertical"
    md_bg_color: self.theme_cls.backgroundColor

    MDScreenManager:
        id: screen_manager

        BaseScreen:
            name: "Home"

        BaseScreen:
            name: "My Tickets"
        
        BaseScreen:
            name: "About"


    MDNavigationBar:
        on_switch_tabs: app.on_switch_tabs(*args)

        BaseMDNavigationItem
            icon: "home"
            text: "Home"
            active: True

        BaseMDNavigationItem
            icon: "ticket"
            text: "My Tickets"
            
        BaseMDNavigationItem
            icon: "group"
            text: "About"
'''


class myMetroTransitApp(MDApp):
    def build(self):
        return Builder.load_file('main.kv')


myMetroTransitApp().run()