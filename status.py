class Status:  # Criação da Super classe
    # atributos pertinentes à Super classe
    def __init__(self, dinheiro, estamina, alimento, dia=1):
        self.__dinheiro = dinheiro  # protegendo o atributo
        self.__estamina = estamina  # protegendo o atributo
        self.__alimento = alimento  # protegendo o atributo
        self.__dia = dia  # protegendo o atributo

    @property  # property do atributo dinheiro
    def dinheiro(self):
        return self.__dinheiro

    @property  # property do atributo estamina
    def estamina(self):
        return self.__estamina

    @property  # property do atributo alimento
    def alimento(self):
        return self.__alimento

    @estamina.setter  # Setter para atributo privado
    def estamina(self, valor):
        self.__estamina = valor

    @dinheiro.setter  # Setter para atributo privado
    def dinheiro(self, valor):
        self.__dinheiro = valor

    @alimento.setter  # Setter para atributo privado
    def alimento(self, valor):
        self.__alimento = valor

    @property  # property do atributo dia
    def dia(self):
        return self.__dia

    @dia.setter  # Setter para adiconar dias no decorrer do jogo.
    def dia(self, valor):
        self.__dia = valor
