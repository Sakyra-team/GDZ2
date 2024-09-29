from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

from text import*

class Main(Screen):
    def __init__(self,name="main"):
        super().__init__(name=name)
        math_layout = BoxLayout(orientation="vertical", padding=30)
        math_alg_btn = Button(text=text_alg)
        math_gem_btn = Button(text=text_gem)
        math_vis_btn = Button(text=text_vis)
        math_fiz_btn = Button(text=text_fiz)
        math_layout.add_widget(math_alg_btn)
        math_layout.add_widget(math_gem_btn)
        math_layout.add_widget(math_vis_btn)
        math_layout.add_widget(math_fiz_btn)
        self.math_popup = Popup(title="Математическое ГДЗ",content=math_layout)


        main_layout = BoxLayout(orientation="vertical")
        main_label = Label(text=text1)
        button_math = Button(text="Математические предметы", size_hint_y=0.2, size_hint_x=0.8, center_x=True)
        button_lang = Button(text="Языковые предметы", size_hint_y=0.2, size_hint_x=0.8)
        button_life = Button(text="Жизненые предметы", size_hint_y=0.2, size_hint_x=0.8)
        button_pk = Button(text="Компьютерные предметы", size_hint_y=0.2, size_hint_x=0.8)

        button_math.pos_hint = {'center_x':0.5}
        button_lang.pos_hint = {'center_x':0.5}
        button_life.pos_hint = {'center_x':0.5}
        button_pk.pos_hint = {'center_x':0.5}

        button_math.on_press = self.buttoner



        main_layout.add_widget(main_label)
        main_layout.add_widget(button_math)
        main_layout.add_widget(button_lang)
        main_layout.add_widget(button_life)
        main_layout.add_widget(button_pk )
        self.add_widget(main_layout)
    def buttoner(self):
        self.math_popup.dismiss
        self.math_popup.open()




class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Main())
        return sm
    
app = MyApp()
if __name__=="__main__":
    app.run()
