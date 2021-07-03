class Dev:  # Criação da classe para personagem principal
    def __init__(self, nome, estamina=12, dinheiro=10):
        self.__nome = nome
        self.__estamina = estamina
        self.__dinheiro = dinheiro

    def __str__(self) -> str:
        return f''' Personagem: {self.__nome}
                    Pontos de estamina: {self.__estamina}
                    Unidades de Dinheiro: {self.__dinheiro}
                '''

    @property
    def statusEstamina(self):
        return self.__estamina

    @statusEstamina.setter
    def statusEstaminaAD(self, estamina):
        self.__estamina += estamina

    @statusEstamina.setter
    def statusEstaminaRE(self, estamina):
        self.__estamina -= estamina
