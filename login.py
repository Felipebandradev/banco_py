from janela import Janela
import tkinter as tk

class Tela_login(Janela):
        
        def __init__(self, nome, titulo):
            super().__init__(nome, titulo)

             

        def criar_login(self):
            
            #Criando a função de validação
            def valida_senha():
                    
                    nome = usuario.get()
                    psw =  senha.get()
                    
                    if nome == 'admim' and psw == '123':
                        #comando para fechar a janela atual por completo
                        self.janela.destroy()
                       
                        # Criando uma nova janela
                        teste = Janela('Conta corrente', 'Saldo')
                        teste.criar_janela()
                        teste.exibir_janela()
                        
                    else:
                        print('Senha ou login incorretos')
                        
            self.criar_janela()
            
            # Criando inputs de login
            usuario = tk.Entry(self.janela)
            usuario.pack(padx=10, pady=10)

            senha = tk.Entry(self.janela, show='*')
            senha.pack(padx=10, pady=10)

            # Criando o botão de validação
            botao = tk.Button(self.janela, text=f"{self.titulo}", command=valida_senha)
            botao.pack(padx=10, pady=10)

            self.exibir_janela()





