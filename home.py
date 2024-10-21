import tkinter as tk
from janela import Janela

class Home(Janela):
    def __init__(self, nome, titulo, usuario, saldo):
        super().__init__(nome, titulo)
        self.usuario = usuario
        self.saldo = saldo

    def criarHome(self):
        self.criar_janela()
        self.frameCima(30,'#4169e1')
        lTitulo = tk.Label(self.frame_superior,text='Menu Principal',bg='#4169e1',font=('Arial 15'),foreground='white')
        lTitulo.pack(padx=20)
        lNome = tk.Label(self.janela,text=f'Nome: {self.usuario}',anchor="nw", width=80)
        lNome.pack(padx=20, pady=20)
        lSaldo = tk.Label(self.janela,text=f'Saldo: {self.saldo}',anchor="nw", width=80)
        lSaldo.pack(padx=20, pady=20)



        self.exibir_janela()



app = Home("Home","Menu Principal","Jandherson",10.50)
app.criarHome()

