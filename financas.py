import tkinter as tk
from ContaCorrente import ContaCorrente
from janela import Janela


class telaFinancas(Janela,ContaCorrente):
    def __init__(self, nome, titulo, usuario, saldoAtual):
        super().__init__(nome, titulo)
        self.usuario = usuario
        self.saldoAtual = saldoAtual
    
    def criarFinancas(self):

        # Função de Deposito
        def depositar():
            novoSaldo = float(e_valor.get())
            if novoSaldo > 0:
                self.saldo = 0
                self.depositar(novoSaldo)
                self.aplicar_juros(5)
                self.saldoAtual += self.saldo
                exibirSaldo.config(text=f'Saldo: R$ {self.saldoAtual:.2f}')
                lb_textoFEEDBACK.config(text='Deposito Realizado com sucesso!!!!', foreground='green')
                lb_textoFEEDBACK.pack(pady=5)
                lb_textoFEEDBACK.place(x=10, y=150)
            else:
                lb_textoFEEDBACK.config(text='Cuidado, não se pode depositar valores nagativos!! ', foreground='red')
                lb_textoFEEDBACK.pack(pady=5)
                lb_textoFEEDBACK.place(x=10, y=150)
        
        # Função de Saque
        def sacar():
            valorDoSaque = float(e_valor.get())

            if valorDoSaque < 0:
                lb_textoFEEDBACK.config(text='Cuidado, valor do saque não pode ser negativo!! ', foreground='red')
                lb_textoFEEDBACK.pack(pady=5)
                lb_textoFEEDBACK.place(x=10, y=150)
            elif self.saldoAtual >= valorDoSaque+1:
                self.saldo = self.saldoAtual
                self.sacar(valorDoSaque)
                self.saldoAtual = self.saldo
                exibirSaldo.config(text=f'Saldo: R$ {self.saldoAtual:.2f}')
                lb_textoFEEDBACK.config(text='Saque realizado com sucesso!! ', foreground='green')
                lb_textoFEEDBACK.pack(pady=5)
                lb_textoFEEDBACK.place(x=10, y=150)

            else:
                lb_textoFEEDBACK.config(text='Cuidado, valor do saque está maior que o saldo!! ', foreground='red')
                lb_textoFEEDBACK.pack(pady=5)
                lb_textoFEEDBACK.place(x=10, y=150)
            
        def voltarHome():
            from home import Home
            self.janela.destroy()
            home = Home('Página principal', 'Menu Principal',self.usuario, self.saldoAtual)
            home.criarHome()


        
        

        self.criar_janela()
        self.frameCima(20,'#fcff52')
        #Titulo da página        
        l_titulo = tk.Label(self.frame_superior, text=f'{self.titulo}', font=('Arial 14 bold'),anchor='nw', width=55, fg='#4169e1', bg='#fcff52')
        l_titulo.pack(pady=5)

        self.frameEsquerdo(350, 380, None)
        # Informações sobre o deposito e saque
        l_infos = tk.Label(self.frame_esquerdo, text=f'Taxa de saque: R$ 1,00 | Juros do Deposito: 5%', font=('Arial 10'),anchor='nw')
        l_infos.pack(pady=5, padx=10)
        l_infos.place(x=10, y=10)

        # Saldo do usuário
        exibirSaldo = tk.Label(self.frame_esquerdo, text=f'Saldo: R$ {self.saldoAtual:.2f}', font=('Arial 12'),anchor='nw')
        exibirSaldo.pack(pady=5, padx=10)
        exibirSaldo.place(x=10, y=50)

        # Imgem ilustrativa
        
        caraComMoeda = tk.PhotoImage(file='img\\caracommoeda.png')

        largura_desejada = 340  
        altura_desejada = 280   

        
        largura_original = caraComMoeda.width()
        altura_original = caraComMoeda.height()

        
        escala_x = int(largura_original / largura_desejada)
        escala_y = int(altura_original / altura_desejada)

        img_novoTamanho = caraComMoeda.subsample(escala_x, escala_y)

        l_imgIlustrativa = tk.Label(self.frame_esquerdo, image=img_novoTamanho)
        l_imgIlustrativa.pack(padx=20)
        l_imgIlustrativa.place(x=-50, y=75)



        self.frameDireito(350, 380, None)
        self.frame_direito.pack(expand=True)

        #Inputs da função de sacar e depositar
        lb_valor = tk.Label(self.frame_direito, text='Valor do saque ou deposito:', font=('Arial', 12))
        lb_valor.pack(pady=5)
        lb_valor.place(x=10, y=40)

        e_valor = tk.Entry(self.frame_direito, width=45, font=('Arial', 10))
        e_valor.pack(pady=5,padx=10)
        e_valor.place(x=10, y=70)

        # Botões de seque e deposito
        b_depositar = tk.Button(self.frame_direito, text='DEPOSITAR', command=depositar, font=('Arial', 10, 'bold'), bg='#23ff55', fg='#204f22', borderwidth=0, padx=10, pady=5 )
        b_depositar.pack(pady=15)
        b_depositar.place(x=80, y=100)
        
        b_sacar = tk.Button(self.frame_direito, text='SACAR', command=sacar,font=('Arial', 10, 'bold'), bg='#ff2363', fg='#2b1315', borderwidth=0, padx=10, pady=5)
        b_sacar.pack(pady=15)
        b_sacar.place(x=200, y=100)

        # Feedback da ação
        lb_textoFEEDBACK = tk.Label(self.frame_direito, font=('Arial', 10, 'bold'))
        
        lb_textoFEEDBACK.place_forget()
        


        b_voltar = tk.Button(self.frame_esquerdo, text='VOLTAR', font=('Arial', 10, 'bold'), command=voltarHome, borderwidth=0, fg='#fcff52', bg='#4169e1', pady=5, padx=20)
        b_voltar.pack(pady=5)
        b_voltar.place(x=10, y=320)


        self.exibir_janela()
    
    

app = telaFinancas('Finanças', 'Deposite ou Saque', 'Admim', 0)
app.criarFinancas()