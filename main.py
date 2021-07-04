from dev import Dev
from trabalho import Trabalho
from status import Status
from os import system
from time import sleep
if __name__ == '__main__':
    dia = 1
    dev = Dev(input('Informe o nome do seu Personagem: '))
    print(f'''  
        {'-='*20}
        {dev}, Vamos conhecer a sua rotina como um Dev
        {'-='*20}
        ''')
    sleep(5)
    system('cls')
    while True:
        print(f'''
                                    Dia {dia}
                                'Você começa seu dia com: 
                                    {Status()}
        ''')
        sleep(3)

        trabalho = Trabalho(input(

            '''
            Após Você levantar e fazer sua primeira refeição,
            você deverá escolher qual forma de trabalho?

            Você deseja trabalhar hoje em Home Office ou Presencial? [ 1 - Home Office / 2 - Presencial ] '''))
