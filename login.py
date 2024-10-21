# Importando a classe 'Pai' para fazer a herança
from janela import Janela
# Import da biblioteca de criação de GUI
import tkinter as tk
from tkinter import messagebox as msg
from financas import telaFinancas

class Tela_login(Janela):
        
    def __init__(self, nome, titulo):
        super().__init__(nome, titulo)


    def criar_login(self):
            
        #Criando a função de validação
        def valida_senha():
                    
                nome = usuario.get()
                psw =  senha.get()
                    
                if nome == 'admim' and psw == '123':

                    msg.showinfo('Logando', 'Login realizado com sucesso!!')

                    #comando para fechar a janela atual por completo
                    self.janela.destroy()
                       
                    # Criando uma nova janela
                    finacas = telaFinancas('Conta corrente', 'Saldo', nome, 0)
                    finacas.criarFinancas()              
                else:
                    usuario.config(highlightbackground='red', highlightthickness=2, highlightcolor='red')
                    senha.config(highlightbackground='red', highlightthickness=2, highlightcolor='red')
                    msg.showerror('Ops!', 'Verifique usuário ou senha incorretos!!')
                        
        self.criar_janela()
        # Criando titulo da tela
        self.frameCima(30,'#4169e1')
        texto = tk.Label(self.frame_superior ,text=f'{self.titulo}', font=('arial 20'), foreground='#e5e4fb', bg="#4169e1")
        texto.pack(pady=20)
            
        # Criando inputs de login
        self.frameBaixo(370,None)
        lb_usuario = tk.Label(self.frame_inferior, text='Digite o nome:*', font=('arial 8'), width=80, anchor='nw')
        lb_usuario.pack(pady=10, padx=10)
        usuario = tk.Entry(self.frame_inferior, width=80)
        usuario.pack(pady=10, padx=10)
        

        lb_senha = tk.Label(self.frame_inferior, text='Digite a senha:*', font=('arial 8'), width=80, anchor='nw')
        lb_senha.pack(pady=10, padx=10)
        senha = tk.Entry(self.frame_inferior, show='*', width=80)
        senha.pack(pady=10,padx=10)

        # Criando o botão de validação
        botao = tk.Button(self.frame_inferior, text="LOGAR", command=valida_senha, background='#2a356a', fg='white', padx=20, pady=10,borderwidth=0, relief='flat')
        botao.pack(padx=10, pady=10)

        self.exibir_janela()





