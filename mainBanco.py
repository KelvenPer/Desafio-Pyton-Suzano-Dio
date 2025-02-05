class Banco:
    def __init__(self):
        self.saldo = 0
        self.limite_saque_diario = 1500
        self.saques_realizados = 0
        self.depositos_realizados = 0
        self.movimentacoes = []
    
    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido!")
        elif self.saldo < valor:
            print("Saldo insuficiente!")
        elif self.saques_realizados + valor > self.limite_saque_diario:
            print("Você atingiu o limite de saque diário!")
        else:
            self.saldo -= valor
            self.saques_realizados += valor
            self.movimentacoes.append(f"Saque: -R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {self.saldo:.2f}")
    
    def depositar(self, valor):
        if valor <= 0:
            print("Valor de depósito inválido!")
        elif self.depositos_realizados >= 3:
            print("Você chegou no limite de depósito diário!")
        elif valor > 500:
            print("O limite por depósito é de R$ 500,00!")
        else:
            self.saldo += valor
            self.depositos_realizados += 1
            self.movimentacoes.append(f"Depósito: +R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {self.saldo:.2f}")
    
    def extrato(self):
        print("\n=== EXTRATO ===")
        if not self.movimentacoes:
            print("Nenhuma movimentação realizada hoje.")
        else:
            for movimento in self.movimentacoes:
                print(movimento)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("================\n")
    
    def menu(self):
        while True:
            print("\n1 - Sacar\n2 - Depositar\n3 - Extrato\n4 - Sair")
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                valor = float(input("Informe o valor do saque: R$ "))
                self.sacar(valor)
            elif opcao == "2":
                valor = float(input("Informe o valor do depósito: R$ "))
                self.depositar(valor)
            elif opcao == "3":
                self.extrato()
            elif opcao == "4":
                print("Obrigado por utilizar nosso sistema bancário!")
                break
            else:
                print("Opção inválida! Escolha uma opção válida.")

banco = Banco()
banco.menu()
