class Status:
    def __init__(self, dinheiro, estamina):
        self.__dinheiro = dinheiro #protegendo o atributo
        self.__estamina = estamina
        return f'''
        Estamina = {estamina}
        Saldo = $ {dinheiro}'''