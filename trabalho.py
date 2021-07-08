from relogio import Relogio #importação das classes que serão utlizadas
from status import Status
from personagem import Personagem

class Trabalho:

    def __init__(self, trabalho): # Inicialização da classe trabalho
        self.__trabalho = trabalho

    
    @property #Criação de properties dos métodos privados
    def statusEstamina(self):
        return self.__estamina

    @statusEstamina.setter #Criação da SETTER para adicionar a estamina
    def statusEstaminaAD(self, estamina):
        self.__estamina += estamina

    @statusEstamina.setter #Criação da SETTER para remover a estamina
    def statusEstaminaRE(self, estamina):
        self.__estamina -= estamina

    @property #Criação de properties dos métodos privados
    def statusDinheiro(self):
        return self.__dinheiro

    @statusDinheiro.setter #Criação da SETTER para adicionar dinheiro após o dia de trabalho
    def statusDinheiroAD(self, dinheiro):
        Status.statusDinheiro += dinheiro

    @statusDinheiro.setter #Criação da SETTER para remover dinheiro após eventos aleatórios ou compras de supermercado
    def statusDinheiroRE(self, dinheiro):
        self.statusDinheiro -= dinheiro

    def homeOffice(self):
        Trabalho.statusDinheiroAD(dinheiro=10) # Adiciona dinheiro após um dia de trabalho
        Trabalho.statusEstaminaRE(estamina=6) # Remove estamina após um dia de trabalho
        Personagem.diaAdd(1) # Adiciona um dia após um dia de trabalho

    def presencial():
        Trabalho.statusDinheiroAD(10) # Adiciona dinheiro após um dia de trabalho
        Trabalho.statusEstaminaRE(8) # Remove estamina após um dia de trabalho
        Personagem.diaAdd(1) # Adiciona um dia após um dia de trabalho
 
 