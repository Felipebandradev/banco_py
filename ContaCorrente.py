class ContaCorrente:
    TAXA_SAQUE = 1.0  # Taxa fixa de R$ 1,00 por saque

    def __init__(self):
        # """Inicializa a conta com saldo zero."""
        self.saldo = 0.0
        self.conta = None  # Você pode inicializar com um número de conta, se necessário

    def sacar(self, valor):
        # """Saca um valor da conta, aplicando a taxa de saque."""
        if self.saldo >= valor + self.TAXA_SAQUE:
            self.saldo -= (valor + self.TAXA_SAQUE)
        else:
            raise ValueError("Saldo insuficiente para sacar.")

    def depositar(self, valor):
        # """Deposita um valor na conta."""
        if valor > 0:
            self.saldo += valor
        else:
            raise ValueError("O valor do depósito deve ser positivo.")

    def ver_saldo(self):
        # """Exibe o saldo atual da conta."""
        print(f"Saldo = {self.saldo:.2f}")

    def aplicar_juros(self, taxa):
        # """Aplica uma taxa de juros ao saldo da conta."""
        if taxa < 0:
            raise ValueError("A taxa de juros não pode ser negativa.")
        self.saldo += self.saldo * taxa / 100

# Simulação de uso
# conta = ContaCorrente()
# conta.depositar(100)  # Depositar R$ 100
# conta.sacar(50)       # Sacar R$ 50 + taxa de R$ 1
# conta.ver_saldo()     # Ver saldo
# conta.aplicar_juros(5)  # Aplicar 5% de juros
# conta.ver_saldo()     # Ver saldo novamente após os juros