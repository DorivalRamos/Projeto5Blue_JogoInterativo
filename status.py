class Status:
    def __init__(self, dinheiro, estamina, alimento, dia = 1):
        self.__dinheiro = dinheiro  # protegendo o atributo
        self.__estamina = estamina
        self.__alimento = alimento
        self.__dia = dia
            

    @property
    def dinheiro(self):
        return self.__dinheiro

    @property
    def estamina(self):
        return self.__estamina

    @property
    def alimento(self):
        return self.__alimento

    @estamina.setter
    def estamina(self, valor):
        self.__estamina = valor

    @dinheiro.setter
    def dinheiro(self, valor):
        self.__dinheiro = valor

    @alimento.setter
    def alimento(self, valor):
        self.__alimento = valor

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, valor):
        self.__dia = valor