class Trabalho:
    def __init__(self, trabalho):
        self.trabalho = trabalho
    
    def homeOffice(self, dinheiro, estamina):
        self.__dinheiro += 10 #protegendo o atributo
        self.__estamina -= 6

    def presencial(self, dinheiro, estamina):
        self.__dinheiro += 10
        self.__estamina -= 8

    def aleatoria(self, dinheiro, estamina):
        self.__dinheiro = dinheiro
        self.__estamina = estamina
        from random import choice
        eventos = ('acidente de carro', 'dor de barriga', 'happy hour', 'dor de cabeça', 'quebrou a perna')
        perde_dia = choice(eventos)
        if perde_dia == 'acidente de carro':
            dinheiro -= 2
            return f'''Você sofreu um acidente voltando do trabalho. Ficará impossibilitado de trabalhar por 2 dias.
                Você perdeu 2 unidades de dinheiro'''
            saldo()
        elif perde_dia == 'dor de barriga':
            dinheiro -= 1
            return f'''Você comeu algo estragado. Ficará impossibilitado de trabalhar por 1 dias.
                Você perdeu 1 unidade de dinheiro'''
            saldo()
        elif perde_dia == 'happy hour':
            opcao = input('Você recebeu um convite para um happy hour. Deseja ir? [S/N]').upper().strip()[0]
            if opcao == 'S':
                dinheiro -= 1
                estamina -= 2
                return f'''Você exagerou... Chegou tarde em casa e não vai conseguir dormir o número suficiente de horas para recuperar suas energias.'''
            else:
                return f'Obrigado... fica para uma próxima vez...'
        elif perde_dia == 'dor de cabeça':
            dinheiro -= 1
            return f'''Você acordou com uma baita dor de cabeça e não vai conseguir trabalhar por 1 dia.
                Você perdeu 1 unidade de dinheiro'''
            saldo()
        elif perde_dia == 'quebrou a perna':
            dinheiro -= 1
            return f'''Você quebrou a perna e não vai conseguir trabalhar por 7 dias.
                Você perdeu 7 unidades de dinheiro'''
            saldo()
        