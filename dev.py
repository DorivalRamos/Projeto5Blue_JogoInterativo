class Dev: #Criação da classe para personagem principal
    def __init__(self, nome, estamina = 12, dinheiro = 10):
        self.nome = nome
        self.__estamina = estamina
        self.__dinheiro = dinheiro
        