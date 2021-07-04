from status import Status
from dev import Dev

dev = Dev


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

    def presencial():
        Trabalho.statusDinheiroAD(10)
        Trabalho.statusEstaminaRE(8)

    def aleatoria(self):
        from random import choice, randint

        eventos = ('Acidente de carro', 'Dor de barriga',
                   'Dappy hour', 'Dor de cabeça', 'Quebrou a perna')
        perde_dia = choice(eventos)

        eventoAleatorio = randint(1, 100)
        if eventoAleatorio > 90:
            if perde_dia == 'acidente de carro':
                dev.statusDinheiroRE(10)
                return f'''Você sofreu um acidente voltando do trabalho. Ficará impossibilitado de trabalhar por 2 dias.
                    Você perdeu 10 unidades de dinheiro'''
                saldo()
            elif perde_dia == 'dor de barriga':
                dev.statusDinheiroRE(1)
                return f'''Você comeu algo estragado. Ficará impossibilitado de trabalhar por 1 dias.
                    Você perdeu 5 unidade de dinheiro'''
                saldo()
            elif perde_dia == 'happy hour':
                opcao = input(
                    'Você recebeu um convite para um happy hour. Deseja ir? [S/N]').upper().strip()[0]
                if opcao == 'S':
                    dev.statusDinheiroRE(1)
                    dev.statusEstaminaRE(2)
                    return f'''Você exagerou... Chegou tarde em casa e não vai conseguir dormir o número suficiente de horas para recuperar suas energias.'''
                else:
                    return f'Obrigado... fica para uma próxima vez...'
            elif perde_dia == 'dor de cabeça':
                dev.statusDinheiroRE(1)
                return f'''Você acordou com uma baita dor de cabeça e não vai conseguir trabalhar por 1 dia.
                    Você perdeu 1 unidade de dinheiro'''
                saldo()
            elif perde_dia == 'quebrou a perna':
                dev.statusDinheiroRE(1)
                return f'''Você quebrou a perna e não vai conseguir trabalhar por 7 dias.
                    Você perdeu 7 unidades de dinheiro'''
                saldo()
