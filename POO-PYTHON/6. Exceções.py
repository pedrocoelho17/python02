import os

os.system("cls||clear")

class SaladoInsuficienteError(Exception):
    pass

class ValorNegativoError(Exception):
    pass

class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 0 # Atributo protegido.

    @property
    def saldo(self):
        return self._saldo

    def sacar(self) -> str:
        valor_saque = float(input("Digite o valor que deseja sacar: "))   
        
        try: 
            self.__verificar_sacar(valor_saque)
            self.__verificar_valor_negativo(valor_saque)
        except SaladoInsuficienteError as erro:
            return f"Erro: {erro}"
        
        return f"Saque realizado com sucesso"
        
    
    def __verificar_sacar(self, valor) -> None: # Método privado.
        if valor > self._saldo:
            raise SaladoInsuficienteError("Saldo Insuficiente.")
        self._saldo -= valor
        
    def __verificar_valor_negativo(self, valor):
        if valor < 0:
            raise ValorNegativoError("Valor negativo.")
        
        

    def depositar(self, valor):
        self.saldo += valor
        return self._saldo

class ContaCorrente(Conta):
    pass


class ContaPoupanca(Conta):
    pass

# Instanciando classe.
conta_corrente = ContaCorrente(32323, 1111)
conta_poupanca = ContaPoupanca (2000, 3223)

print(f"Número da conta: {conta_corrente.numero_conta}")
print(f"Saldo: {conta_corrente.saldo}")


# Sacar com saldo insuficiente.
print("Conta corrente")
print(conta_corrente.sacar())
print(f"Saldo: {conta_corrente.saldo}")
