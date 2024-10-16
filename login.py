# Importando a classe 'Pai' para fazer a herança
from janela import Janela
# Import da biblioteca de criação de GUI
import tkinter as tk
from tkinter import messagebox as msg

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
                    teste = Janela('Conta corrente', 'Saldo')
                    teste.criar_janela()
                    teste.exibir_janela()              
                else:
                    usuario.config(highlightbackground='red', highlightthickness=2, highlightcolor='red')
                    senha.config(highlightbackground='red', highlightthickness=2, highlightcolor='red')
                    msg.showerror('Ops!', 'Verifique usuário ou senha incorretos!!')
                        
        self.criar_janela()
        # Criando titulo da tela
        texto = tk.Label(self.janela ,text=f'{self.titulo}', font=('arial 20'), bg='#aeb1f1', width=100)
        texto.pack(pady=10)
            
        # Criando inputs de login
        lb_usuario = tk.Label(self.janela, text='Digite o nome:*', font=('arial 8'), width=80, anchor='nw')
        lb_usuario.pack(pady=5)
        usuario = tk.Entry(self.janela, width=80, borderwidth=2)
        usuario.pack(pady=10)
        

        lb_senha = tk.Label(self.janela, text='Digite a senha:*', font=('arial 8'), width=80, anchor='nw')
        lb_senha.pack(pady=5)
        senha = tk.Entry(self.janela, show='*', width=80, borderwidth=2)
        senha.pack(pady=10)

        # Criando o botão de validação
        botao = tk.Button(self.janela, text="fazer login", command=valida_senha, background='#2a356a', fg='white', padx=20, pady=10,borderwidth=0, relief='flat')
        botao.pack(padx=10, pady=10)

        self.exibir_janela()





