# Importação da biblioteca de criação de GUI
import tkinter as tk

class Janela:
    def __init__(self, nome, titulo):
        self.nome = nome
        self.titulo = titulo
        self.janela = None
        self.frame_superior = None
        self.frame_inferior = None
        self.frame_esquerdo = None
        self.frame_direito = None
    
    def criar_janela(self):
        # criando janela
        self.janela = tk.Tk()
        self.janela.geometry('700x350')
        self.janela.resizable(False, False)
        self.janela.title(f'{self.nome}')
        #Favicon da janela
        favicon = tk.PhotoImage(file='img\\logos\\favicon.png')
        self.janela.iconphoto(False,favicon)

    def frameCima(self, altura, corFundo):
        self.frame_superior = tk.Frame(self.janela, bg=corFundo, height=altura)
        self.frame_superior.pack(side='top', fill='x')  

    def frameBaixo(self,altura, corFundo):
        self.frame_inferior = tk.Frame(self.janela, height=altura, bg=corFundo)
        self.frame_inferior.pack(side='top', fill='x')

    def frameEsquerdo(self,largura,altura, corFundo): 
        self.frame_esquerdo = tk.Frame(self.janela, width=largura, bg=corFundo, height=altura)
        self.frame_esquerdo.pack(side='left', fill='x')

    def frameDireito(self,largura,altura, corFundo): 
        self.frame_direito = tk.Frame(self.janela, width=largura, bg=corFundo, height=altura)
        self.frame_direito.pack(side='left', fill='x')

    def exibir_janela(self):
        # exibindo a janela
        self.janela.mainloop()



        

