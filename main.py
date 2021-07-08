from relogio import Relogio
from personagem import Personagem
from random import choice
from random import randint
from time import sleep
from os import system
from tqdm import tqdm  # Biblioteca utilizada para a barra de progresso
from rich import print
import pygame  # Biblioteca utilizada para executar áudio
pygame.mixer.init()  # Função para iniciar a aplicação que executa o áudio
pygame.mixer.music.load("musica.mp3")  # carregamento do arquivo mp3
pygame.mixer.music.play()  # Após votar toca o áudio a vinheta de urna eletrônica

if(__name__ == "__main__"):  # Pesquisar significado desse if #o programa só roda se tiver na main
    system('cls')
    #dia = 1
    relogio = Relogio()
    personagem = Personagem(input("Qual o nome do seu personagem: "))
    cafe_da_manha = False

    while True:
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
                    7 - Recuperar energia
                    99 - Sair do jogo
                    {'-='*30}''')

        opcao = input("Escolha sua ação:")
        sleep(2)
        system('cls')
        if(opcao == "1"):
            if(personagem.alimento > 0):
                print(f'[cyan]preparando café')
                for i in tqdm(range(150)):
                    sleep(0.001)
                print()
                print('Agora que você já tomou café, vamos para o próximo passo: ')
                sleep(4)
                personagem.alimentoRE(3)
                cafe_da_manha = True
                relogio.avancaTempo(20)
            else:
                print("Não há comida em casa.")
                sleep(4)
            relogio.avancaTempo(15)
        elif(opcao == "2"):
            if(personagem.dinheiro >= 3):
                print(f'[cyan]pedindo café por aplicativo...Guilherme')
                for i in tqdm(range(90)):
                    sleep(0.001)
                print()
                print('Agora que você já tomou café, vamos para o próximo passo: ')
                sleep(4)
                personagem.dinheiroRE(3)
                cafe_da_manha = True
            else:
                print(
                    "O café da manhã custa 3 unidades de dinheiro, você não tem dinheiro suficiente.")
                sleep(2)
            relogio.avancaTempo(5)
        elif(opcao == "3"):
            if(personagem.dinheiro >= 5):
                print(f'[cyan]indo ao supermercado...')
                for i in tqdm(range(150)):
                    sleep(0.001)
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
                print(f'[cyan]trabalhando...')
                for i in tqdm(range(900)):
                    sleep(0.001)
                personagem.estaminaRE(10)
                personagem.dinheiroAD(10)
                personagem.aleatorios()
                relogio.avancaTempo(10)
                personagem.diaAdd(1)
                relogio = Relogio()

            else:
                print(
                    '[red]Você não tem descansado bastante. Selecione a opção [7] para recuperar sua energia.')
                sleep(5)
                continue
        elif(opcao == "5"):
            if personagem.estamina >= 8:

                print("-=-=-")
                print("Você optou por fazer Home Office hoje.")
                print(f'[cyan]trabalhando...')
                for i in tqdm(range(900)):
                    sleep(0.001)
                sleep(2)
                personagem.estaminaRE(8)
                personagem.dinheiroAD(10)
                relogio.avancaTempo(10)
                personagem.diaAdd(1)
                relogio = Relogio()
            else:
                print(
                    'Você não tem descansado bastante. Selecione a opção [7] para recuperar sua energia.')
                sleep(4)
                continue
        elif (opcao == "6"):
            print("-=-=-")
            print("Você optou por tirar o dia para estudos...")
            print(f'[cyan]estudando...')
            for i in tqdm(range(900)):
                sleep(0.001)
            sleep(2)
            personagem.diaAdd(1)
            personagem.estaminaAD(5)
            personagem.dinheiroRE(5)
            relogio = Relogio()
        elif (opcao == "7"):
            # personagem.dormir()
            print(f'[cyan]renovando as energias !!!')
            for i in tqdm(range(900)):
                sleep(0.001)
            sleep(2)
            personagem.estaminaAD(10)
            personagem.dinheiroRE(1)
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
