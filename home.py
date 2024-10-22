import tkinter as tk
from tkinter import messagebox as msg
from janela import Janela


class Home(Janela):
    def __init__(self, nome, titulo, usuario, saldo):
        super().__init__(nome, titulo)
        self.usuario = usuario
        self.saldo = saldo

    def criarHome(self):

        def deslogar():
            from login import Tela_login

            confirmaLogout = msg.askyesno('Deslogar', 'Você deseja mesmo deslogar? ')
            
            if confirmaLogout:
                self.janela.destroy()
                home = Tela_login('Login', 'Acessar conta', self.saldo)
                home.criar_login()
            else:
                msg.showinfo('Cancelando', 'Deslogar cancelado!!')

        def financas():
            from financas import telaFinancas
            self.janela.destroy()
            financas = telaFinancas('Finanças', 'Deposite ou Saque', self.usuario, self.saldo)
            financas.criarFinancas()


        self.criar_janela()
        self.frameCima(30,'#4169e1')
        lTitulo = tk.Label(self.frame_superior,text='Menu Principal',bg='#4169e1',font=('Arial 15'),foreground='white')
        lTitulo.pack(padx=20)

        fotoUsuario = tk.PhotoImage(file='img\\user-icon.png')
       
        largura_desejada = 50  
        altura_desejada = 50   

        
        largura_original = fotoUsuario.width()
        altura_original = fotoUsuario.height()

        
        escala_x = int(largura_original / largura_desejada)
        escala_y = int(altura_original / altura_desejada)

        
        img_redimensionada = fotoUsuario.subsample(escala_x, escala_y)
        lMostrarImg = tk.Label(self.janela, image=img_redimensionada)
        lMostrarImg.pack(pady=10)
        
        lNome = tk.Label(self.janela,text=f'Nome: {self.usuario}',anchor="nw", width=80)
        lNome.pack(padx=20, pady=20)
        lSaldo = tk.Label(self.janela,text=f'Saldo: {self.saldo}',anchor="nw", width=80)
        lSaldo.pack(padx=20, pady=20)
        
        b_irFinancas = tk.Button(self.janela, text='FINANÇAS', command=financas)
        b_irFinancas.pack(padx=20, pady=10)
        b_deslogar = tk.Button(self.janela, text='DESLOGAR', command=deslogar)
        b_deslogar.pack(padx=20, pady=10)


        self.exibir_janela()



app = Home("Home","Menu Principal","Padrão",10.50)
app.criarHome()

