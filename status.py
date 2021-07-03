class Status:
    def __init__(self, dinheiro = 10, estamina = 12, alimento = 3):
        self.__dinheiro = dinheiro #protegendo o atributo
        self.__estamina = estamina
        self.__alimento = alimento
        # return f'''
        # Estamina = {estamina}
        # Saldo = $ {dinheiro}'''