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
            else:
                lb_textoFEEDBACK.config(text='Cuidado, não se pode depositar valores nagativos!! ', foreground='red')
                lb_textoFEEDBACK.pack(pady=5)
        
        # Função de Saque
        def sacar():
            valorDoSaque = float(e_valor.get())

            if self.saldoAtual >= valorDoSaque:
                self.saldo = self.saldoAtual
                self.sacar(valorDoSaque)
                self.saldoAtual = self.saldo
                exibirSaldo.config(text=f'Saldo: R$ {self.saldoAtual:.2f}')
            else:
                lb_textoFEEDBACK.config(text='Cuidado, valor do saque está maior que o saldo!! ', foreground='red')
                lb_textoFEEDBACK.pack(pady=5)


        
        

        self.criar_janela()

        #Titulo da página
        l_titulo = tk.Label(self.janela, text=f'{self.titulo}', font=('Arial 14'),anchor='nw', width=60)
        l_titulo.pack(pady=5)
        exibirSaldo = tk.Label(self.janela, text=f'Saldo: R$ {self.saldoAtual:.2f}', font=('Arial 12'),anchor='nw', width=73)
        exibirSaldo.pack(pady=5)
        l_infos = tk.Label(self.janela, text=f'Taxa de saque: R$ 1,00 | Juros do Deposito: 5%', font=('Arial 10'),anchor='nw', width=82)
        l_infos.pack(pady=5)

        #Inputs da função de sacar e depositar
        lb_valor = tk.Label(self.janela, text='Digite um valor*:')
        lb_valor.pack(pady=5)

        e_valor = tk.Entry(self.janela)
        e_valor.pack(pady=5)

        # Botões de seque e deposito
        b_depositar = tk.Button(self.janela, text='DEPOSITAR', command=depositar)
        b_depositar.pack(pady=5)
        
        b_sacar = tk.Button(self.janela, text='SACAR', command=sacar)
        b_sacar.pack(pady=5)

        lb_textoFEEDBACK = tk.Label(self.janela, text='')


        self.exibir_janela()
    
    

# app = telaFinancas('Finanças', 'Deposite ou Saque', 'Admim', 0)
# app.criarFinancas()