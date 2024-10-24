import tkinter as tk
from tkinter import messagebox as msg
from janela import Janela


class Home(Janela):
    def __init__(self, nome, titulo, usuario, saldo):
        super().__init__(nome, titulo)
        self.usuario = usuario
        self.saldo = saldo
        self.imgPix = None

    def criarHome(self):

        def deslogar():
            from login import Tela_login

            confirmaLogout = msg.askyesno('Deslogar', 'Você deseja mesmo deslogar? ')
            
            if confirmaLogout:
                
                self.janela.destroy()
                voltar_login = Tela_login('Login', 'Acessar conta', self.saldo)
                voltar_login.criar_login()
            else:
                msg.showinfo('Cancelando', 'Deslogar cancelado!!')

        def financas():
            self.janela.destroy()
            from financas import telaFinancas
            financas = telaFinancas('Finanças', 'Deposite ou Saque', self.usuario, self.saldo)
            financas.criarFinancas()

        def gerarQrcode():
            self.imgPix = tk.PhotoImage(file='img\\qrcodes\\qrcodeLucas.png')
            l_imgPix.config(image=self.imgPix, bg='#4169e1')
            l_imgPix.pack(expand=True, padx=20)
            l_imgPix.place(x=10, y=100)
           

            

        self.criar_janela()
        self.frameCima(30,'#4169e1')
        
        #Titulo da página
        lTitulo = tk.Label(self.frame_superior,text=f'{self.titulo}',bg='#4169e1',font=('Arial 15'),foreground='white')
        lTitulo.pack(padx=20)

        fotoUsuario = tk.PhotoImage(file='img\\user-icon.png')
       
        largura_desejada = 50  
        altura_desejada = 50   

        
        largura_original = fotoUsuario.width()
        altura_original = fotoUsuario.height()

        
        escala_x = int(largura_original / largura_desejada)
        escala_y = int(altura_original / altura_desejada)

        self.frameEsquerdo(350, 370, None)
        
        # Foto de perfil do usuário
        img_redimensionada = fotoUsuario.subsample(escala_x, escala_y)
        lMostrarImg = tk.Label(self.frame_esquerdo, image=img_redimensionada,  anchor='nw')
        lMostrarImg.pack(pady=10)
        lMostrarImg.place(x=10, y=20)
        
        # Nome e Saldo do Usuário
        lNome = tk.Label(self.frame_esquerdo,text=f'Nome: {self.usuario}',anchor="nw", width=40, font=('Arial', 10))
        lNome.pack(padx=10, pady=10)
        lNome.place(x=80, y=20)
        lSaldo = tk.Label(self.frame_esquerdo,text=f'Saldo: R$ {self.saldo:.2f}',anchor="nw", width=40, font=('Arial', 10))
        lSaldo.pack(padx=10, pady=20)
        lSaldo.place(x=80, y=40)

        # Botão para deslogar
        b_deslogar = tk.Button(self.frame_esquerdo, text='DESLOGAR',font=('Arial', 8,'bold'), command=deslogar, bg='#7a1b0c', fg='white', borderwidth=0, pady=10, padx=20)
        b_deslogar.pack(padx=10, pady=10)
        b_deslogar.place(x=10, y=100)


        self.frameDireito(350, 370, None)

        # Titulo do gerenciamento de conta
        t_gconta = tk.Label(self.frame_direito, text='Como quer gerenciar seu saldo:', width=50, anchor='nw', font=('Arial', 12))
        t_gconta.pack(padx=10, pady=10)

        # Botão para gerar o qrcode do pix
        b_gerarpix = tk.Button(self.frame_direito, text='PIX', command=gerarQrcode, anchor='nw', font=('Arial', 8, 'bold'),  bg='#227740', foreground='white', borderwidth=0, padx=10, pady=10)
        b_gerarpix.pack(padx=10, pady=10)
        b_gerarpix.place(x=10, y=50)

        # Botão para ir para página de finanças
        b_irFinancas = tk.Button(self.frame_direito, text='FINANÇAS', font=('Arial', 8, 'bold'), fg='#4169e1',command=financas, bg='#fcff52', padx=20, pady=10, borderwidth=0)
        b_irFinancas.pack(padx=10, pady=10)
        b_irFinancas.place(x=80, y=50)

        # label para mostrar o pix
        l_imgPix = tk.Label(self.frame_direito)
        l_imgPix.pack_forget()
        

        
        self.exibir_janela()



