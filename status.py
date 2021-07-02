class Status:
    def __init__(self, saldo, estamina):
        self.saldo = saldo
        self.estamina = estamina
        return f'''
        Estamina = {estamina}
        Saldo = $ {saldo}'''