from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MeuLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.label = Label(text="Olá, Mundo!")
        self.botao = Button(text="Clique aqui")
        self.botao.bind(on_press=self.mudar_texto)
        self.add_widget(self.label)
        self.add_widget(self.botao)

    def mudar_texto(self, instance):
        self.label.text = "Você clicou no botão!"

class MeuApp(App):
    def build(self):
        return MeuLayout()

if __name__ == '__main__':
    MeuApp().run()
