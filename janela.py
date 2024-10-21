# Importação da biblioteca de criação de GUI
import tkinter as tk

class Janela:
    def __init__(self, nome, titulo):
        self.nome = nome
        self.titulo = titulo
        self.janela = None
        self.frame_superior = None
        self.frame_inferior = None
    
    def criar_janela(self):
        # criando janela
        self.janela = tk.Tk()
        self.janela.geometry('700x350')
        self.janela.resizable(False, False)
        self.janela.title(f'{self.nome}')

    def frameCima(self, altura, corFundo):
        self.frame_superior = tk.Frame(self.janela, bg=corFundo, height=altura)
        self.frame_superior.pack(side='top', fill='x')  

    def frameBaixo(self,altura, corFundo):
        self.frame_inferior = tk.Frame(self.janela, height=altura, bg=corFundo)
        self.frame_inferior.pack(side='top', fill='x')   
       

    def exibir_janela(self):
        # exibindo a janela
        self.janela.mainloop()



        

