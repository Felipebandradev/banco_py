# Importando a classe 'Pai' para fazer a herança
from janela import Janela
# Import da biblioteca de criação de GUI
import tkinter as tk
from tkinter import messagebox as msg
from home import Home

class Tela_login(Janela):
        
    def __init__(self, nome, titulo,saldo):
        super().__init__(nome, titulo)
        self.saldo = saldo


    def criar_login(self):
            
        #Criando a função de validação
        def valida_senha():
                    
                nome = usuario.get()
                psw =  senha.get()
                    
                if nome == 'Admim' and psw == 'admim123':

                    msg.showinfo('Logando', 'Login realizado com sucesso!!')

                    #comando para fechar a janela atual por completo
                    self.janela.destroy()
                       
                    # Criando uma nova janela
                    telaHome = Home('Página principal', 'Menu Principal', nome, self.saldo)
                    telaHome.criarHome()              
                else:
                    usuario.config(highlightbackground='red', highlightthickness=2, highlightcolor='red')
                    senha.config(highlightbackground='red', highlightthickness=2, highlightcolor='red')
                    msg.showerror('Ops!', 'Verifique usuário ou senha incorretos!!')
                        
        self.criar_janela()
        # Criando titulo da tela
        self.frameCima(20,'#4169e1')
        texto = tk.Label(self.frame_superior ,text=f'{self.titulo}', font=('arial 20'), foreground='#e5e4fb', bg="#4169e1")
        texto.pack(pady=10)

        #Imagem de Ilustrativa
        logo = tk.PhotoImage(file='img\\logos\\logobgclaroNome.png')

        # Redimensionar a imagem usando o método .subsample() ou .zoom()
        largura_desejada = 350  # Largura que você quer
        altura_desejada = 250   # Altura que você quer

        # Dimensões originais da imagem
        largura_original = logo.width()
        altura_original = logo.height()

        # Calcular a escala proporcional
        escala_x = int(largura_original / largura_desejada)
        escala_y = int(altura_original / altura_desejada)

        # Redimensionar a imagem proporcionalmente
        img_redimensionada = logo.subsample(escala_x, escala_y)
        self.frameEsquerdo(350,320,None)
        l_img = tk.Label(self.frame_esquerdo, image=img_redimensionada, width=300)
        l_img.pack(expand=True, padx=20)

            
        # Criando inputs de login
        self.frameDireito(350,None,None)
        lb_usuario = tk.Label(self.frame_direito, text='Digite o nome:*', font=('arial 8'), width=80, anchor='nw')
        lb_usuario.pack(pady=10, padx=20)
        usuario = tk.Entry(self.frame_direito, width=80)
        usuario.pack(pady=10, padx=20)
        

        lb_senha = tk.Label(self.frame_direito, text='Digite a senha:*', font=('arial 8'), width=80, anchor='nw')
        lb_senha.pack(pady=10, padx=20)
        senha = tk.Entry(self.frame_direito, show='*', width=80)
        senha.pack(pady=10,padx=20)

        # Criando o botão de validação
        botao = tk.Button(self.frame_direito, text="LOGAR", command=valida_senha, background='#334690', fg='white', padx=20, pady=10,borderwidth=0, relief='flat')
        botao.pack(padx=20, pady=20)

        self.exibir_janela()





