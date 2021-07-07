from relogio import Relogio
from personagem import Personagem
from random import choice
from random import randint
from time import sleep
from os import system
if(__name__ == "__main__"):  # Pesquisar significado desse if #o programa só roda se tiver na mais
    system('cls')
    #dia = 1
    relogio = Relogio()
    personagem = Personagem(input("Qual o nome do seu personagem: "))
    cafe_da_manha = False

    while True:
        # personagem.diaAdd(1)
        print(f'''  
                    {'-='*30}
                    {personagem.nome}
                    São {(relogio)} do dia {(personagem.dia)}. Já é hora de se arrumar para o trabalho.
                            {personagem}
                    
                    O que fazer:
                    1 - Fazer café da manhã
                    2 - Pedir café da manhã
                    3 - Supermercado
                    4 - Presencial
                    5 - Home Office
                    6 - Estudar
                    7 - Relaxar
                    8 - Recuperar energia
                    99 - Sair do jogo
                    {'-='*30}''')

        opcao = input("Escolha sua ação:")
        sleep(2)
        # system('cls')
        if(opcao == "1"):
            if(personagem.alimento > 0):
                personagem.alimentoRE(1)
                cafe_da_manha = True
                relogio.avancaTempo(20)
            else:
                print("Não há comida em casa.")
                sleep(2)
            relogio.avancaTempo(15)
        elif(opcao == "2"):
            if(personagem.dinheiro >= 3):
                personagem.dinheiroRE(3)
                cafe_da_manha = True
            else:
                print(
                    "O café da manhã custa 3 unidades de dinheiro, você não tem dinheiro suficiente.")
                sleep(2)
            relogio.avancaTempo(5)
        elif(opcao == "3"):
            if(personagem.dinheiro >= 5):
                personagem.alimentoAD(3)
                personagem.dinheiroRE(5)
                relogio.avancaTempo(2)
                print('''
                Você foi ao supermercado
                Alimento + 3
                Dinheiro - 5     
                     ''')
                sleep(2)
            else:
                print("Você não tem dinheiro suficiente.")
                sleep(2)
        elif(opcao == "4"):
            if personagem.estamina >= 10:

                print('Você optou pelo trabalho presencial hoje')
                personagem.estaminaRE(10)
                personagem.dinheiroAD(10)
                personagem.aleatorios()
                personagem.dormir()
                personagem.diaAdd(1)
                relogio.avancaTempo(10)
                relogio = Relogio()

            else:
                print(
                    'Você não tem descansado bastante. Selecione a opção [7] para recuperar sua energia.')
                continue
        elif(opcao == "5"):
            if personagem.estamina >= 8:

                print("-=-=-")
                print("Você optou por fazer Home Office hoje.")
                personagem.estaminaRE(8)
                personagem.dinheiroAD(10)
                relogio.avancaTempo(10)
                personagem.diaAdd(1)
                relogio = Relogio()
            else:
                print(
                    'Você não tem descansado bastante. Selecione a opção [7] para recuperar sua energia.')
                continue
        elif(opcao == "7"):
            if personagem.estamina >= 3 and personagem.estamina >= 3:
                personagem.estaminaRE(3)
                personagem.dinheiroRE(3)

                print(
                    'Você tirou 3 horas do seu dia para poder fazer algo que gosta, seja sair, ler um livro ou ter um hobbie')
        elif (opcao == "8"):
            # personagem.dormir()
            personagem.estaminaAD(10)
            personagem.dinheiroRE(1)
            personagem.dormir()
            print(
                'Depois de uma latinha de Red Bull você já está pronto para começar sua jornada.')
            # personagem.diaAdd(1)
            relogio = Relogio()
            print("-=-=-")
        elif(opcao == "99"):
            break
        else:
            print("Opção inválida!")
            relogio.avancaTempo(5)
