# Importação da biblioteca de criação de GUI
import tkinter as tk

class Janela:
    def __init__(self, nome, titulo):
        self.nome = nome
        self.titulo = titulo
        self.janela = None
    
    def criar_janela(self):
        # criando janela
        self.janela = tk.Tk()
        self.janela.geometry('700x350')
        self.janela.resizable(False, False)
        self.janela.title(f'{self.nome}')
       

    def exibir_janela(self):
        # exibindo a janela
        self.janela.mainloop()



        

