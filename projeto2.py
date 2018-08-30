class Conta:
    def __init__(self, numero, cpf, taxa = 0.01, saldo = 0):
        self.numero    = numero 
        self.cpf       = cpf 
        self.taxa      = taxa 
        self.saldo     = saldo
    def imprimir_saldo(self):
        print("Seu saldo é: %.2f" % self.saldo)
    def depositar(self, valor): 
        self.saldo += valor
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.saldo -= valor * self.taxa
