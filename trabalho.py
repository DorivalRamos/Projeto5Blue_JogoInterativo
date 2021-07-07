from relogio import Relogio
from status import Status
from personagem import Personagem

class Trabalho:

    def __init__(self, trabalho):
        self.__trabalho = trabalho

        if self.__trabalho == '1':  # homeoffice
            self.statusEstaminaRE(6)
            self.statusDinheiroAD(10)
            print(f''' Você escolheu Home Office
                        Seu Status atual é: {Status}''')

        elif trabalho == '2':
            trabalho.presencial()
            print(f''' Você escolheu presencial
                        Seu Status atual é: {Status}''')

    @property
    def statusEstamina(self):
        return self.__estamina

    @statusEstamina.setter
    def statusEstaminaAD(self, estamina):
        self.__estamina += estamina

    @statusEstamina.setter
    def statusEstaminaRE(self, estamina):
        self.__estamina -= estamina

    @property
    def statusDinheiro(self):
        return self.__dinheiro

    @statusDinheiro.setter
    def statusDinheiroAD(self, dinheiro):
        Status.statusDinheiro += dinheiro

    @statusDinheiro.setter
    def statusDinheiroRE(self, dinheiro):
        self.statusDinheiro -= dinheiro

    def homeOffice(self):
        Trabalho.statusDinheiroAD(dinheiro=10)
        Trabalho.statusEstaminaRE(estamina=6)
        Personagem.diaAdd(1)

    def presencial():
        Trabalho.statusDinheiroAD(10)
        Trabalho.statusEstaminaRE(8)
        Personagem.diaAdd(1)

 