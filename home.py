import tkinter as tk
from janela import Janela

class Home(Janela):
    def __init__(self, nome, titulo):
        super().__init__(nome, titulo)

    def criarHome(self):
        self.criar_janela()
        self.frameCima(30,'#4169e1')
        lTitulo = tk.Label(self.frame_superior,text='Menu Principal',bg='#4169e1',font=('Arial 15'),foreground='white')
        lTitulo.pack(padx=20)
        self.exibir_janela()


app = Home("Home","Menu Principal")
app.criarHome()

