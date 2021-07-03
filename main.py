from dev import Dev
from trabalho import Trabalho
from status import Status

if __name__ == '__main__':
    dia = 1
    #dev = Dev()
    #trabalho = Trabalho()
    status = Status()
    alimentacao = False
    dev = Dev(input('Informe seu nome: '))
    print('''
        {dev}, vamos conhecer a rotina de um Dev
        ''')
    while True:
        print('===============================================================')
        print(f'Vamos começar nossa jornada do dia-a-dia de um dev. Dia {dia}')   
        print(f'''Você começa seu dia com: 
        {status}
        ''')  
        trabalho = input('Você deseja trabalhar hoje Home Office ou Presencial? [ 1 - Home Office / 2 - Presencial ] ' )
           
        if trabalho == '1':
            Trabalho.homeOffice()
            print('Você escolheu Home Office')
            print('Seu satus atual é: {Status}')
            break
        elif trabalho == '2':
            Trabalho.presencial()
            print('Você escolheu Presencial')
            print('Seu satus atual é: {Status}')
            break
            

        