from random import randint
from dev import Dev


class Trabalho:

    def __init__(self, trabalho):
        self.__trabalho = trabalho

    def homeOffice(self):  # dinheiro, estamina
        self.__dinheiro += 10  # protegendo o atributo
        self.__estamina -= 6

    def presencial(self):  # dinheiro, estamina
        self.__dinheiro += 10
        self.__estamina -= 8

    def aleatoria(self):  # dinheiro, estamina
        self.__dinheiro = dinheiro
        self.__estamina = estamina

        from random import choice
        eventos = ('Acidente de carro', 'Dor de barriga',
                   'Dappy hour', 'Dor de cabeça', 'Quebrou a perna')
        perde_dia = choice(eventos)

        eventoAleatorio = randint(1, 100)
        if eventoAleatorio > 90:
            if perde_dia == 'acidente de carro':
                self.__dinheiro -= 10
                return f'''Você sofreu um acidente voltando do trabalho. Ficará impossibilitado de trabalhar por 2 dias.
                    Você perdeu 10 unidades de dinheiro'''
                saldo()
            elif perde_dia == 'dor de barriga':
                self.__dinheiro -= 1
                return f'''Você comeu algo estragado. Ficará impossibilitado de trabalhar por 1 dias.
                    Você perdeu 5 unidade de dinheiro'''
                saldo()
            elif perde_dia == 'happy hour':
                opcao = input(
                    'Você recebeu um convite para um happy hour. Deseja ir? [S/N]').upper().strip()[0]
                if opcao == 'S':
                    self.__dinheiro -= 1
                    self.__estamina -= 2
                    return f'''Você exagerou... Chegou tarde em casa e não vai conseguir dormir o número suficiente de horas para recuperar suas energias.'''
                else:
                    return f'Obrigado... fica para uma próxima vez...'
            elif perde_dia == 'dor de cabeça':
                self.__dinheiro -= 1
                return f'''Você acordou com uma baita dor de cabeça e não vai conseguir trabalhar por 1 dia.
                    Você perdeu 1 unidade de dinheiro'''
                saldo()
            elif perde_dia == 'quebrou a perna':
                self.__dinheiro -= 1
                return f'''Você quebrou a perna e não vai conseguir trabalhar por 7 dias.
                    Você perdeu 7 unidades de dinheiro'''
                saldo()
