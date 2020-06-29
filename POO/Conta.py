class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)


    @property #não precisa get_saldo, por conta do property
    # Chamada: from Conta import conta
    #conta = conta()
    #conta.saldo
    #isso retorna o saldo
    def saldo(self):
        return self.__saldo

    @property
    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    # não precisa set_limite, por conta do setter
    # Chamada: from Conta import conta
    # conta = conta()
    # conta.limite = 100.0
    # isso atribui 100.0 ao limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # o staticmethod faz com que codigo_banco exista independente da class ser iniciada ou não.
    # Chamada: from Conta import conta
    # conta.codigo_banco, isso dará certo, se não tivesse o staticmothod não iria dar certo, pois não houve a chamada
    # da class (conta = conta())
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}