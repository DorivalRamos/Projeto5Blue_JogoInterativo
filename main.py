from status import Status  # Importação da Super classe
from relogio import Relogio  # Importação de classe
from personagem import Personagem
# Biblioteca utilizada para simular tempo decorrido para se executar a ação escolhida
from time import sleep
from os import system  # Biblioteca utilizada para limpar a tela
from tqdm import tqdm  # Biblioteca utilizada para a barra de progresso
from rich import print  # Biblioteca para estilizar os prints
import pygame  # Biblioteca utilizada para executar áudio
pygame.mixer.init()  # Função para iniciar a aplicação que executa o áudio
pygame.mixer.music.load("musica.mp3")  # carregamento do arquivo mp3
# Função importada da biblioteca Pygame para tocar música de fundo do jogo
pygame.mixer.music.play()

if(__name__ == "__main__"):  # O programa só irá funcionar se estiver na main
    system('cls')  # Função de limpeza da tela
    relogio = Relogio()  # Instanciação do objeto Relógio
    # Instanciação do objeto personagem com input
    personagem = Personagem(input("Qual o nome do seu personagem: "))
    cafe_da_manha = False

    while True:  # Laço de repetição para as ações do personagem
        # Print com menu de ações
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
                    7 - Dormir
                    99 - Sair do jogo
                    {'-='*30}''')

        opcao = input("Escolha sua ação:")
        sleep(2)
        system('cls')
        if(opcao == "1"):
            if(personagem.alimento > 0):
                print(f'[cyan]preparando café')
                for i in tqdm(range(150)):  # função para exibir barra de progresso decorativa
                    sleep(0.001)
                print()
                print('Agora que você já tomou café, vamos para o próximo passo: ')
                sleep(4)
                # Utilização da classe para debitar valores
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
                # Função que "chama" a possibilidade de ocorrer um evento aleatório
                personagem.aleatorios()
                relogio.avancaTempo(600)

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
                relogio.avancaTempo(480)
                # personagem.diaAdd(1)
                relogio = Relogio()
            else:
                print(
                    '[red]Você não tem descansado bastante. Selecione a opção [7] para recuperar sua energia.')
                sleep(4)
                continue
        elif (opcao == "6"):
            if personagem.estamina >= 5 and personagem.dinheiro >= 5: # condicional de verificação para ver se o personagem tem dinheiro e energia
                print("-=-=-")
                print("Você optou por tirar o dia para estudos...")
                print(f'[cyan]estudando...')
                for i in tqdm(range(900)):
                    sleep(0.001)
                sleep(2)
                personagem.estaminaAD(5) 
                personagem.dinheiroRE(5)
                relogio.avancaTempo(360)
                relogio = Relogio()
            else:
                print('Você não possui dinheiro ou estamina para poder tirar o dia de estudos. Acesse a opção [7] para recarregar seus atributos.')
        elif (opcao == "7"):  # Caso o personagem esteja sem energias ele é obrigado a utilizar esta ação
            print(
                f'[cyan]Depois de uma boa noite de sono você já está pronto para recomeçar sua jornada !!!')
            for i in tqdm(range(900)):
                sleep(0.001)
            sleep(2)
            personagem.estaminaAD(10)
            personagem.dinheiroRE(1)
            personagem.diaAdd(1)
            print(f'[cyan]dormindo !!!')
            relogio = Relogio()
            print("-=-=-")
        elif(opcao == "99"):  # opção de encerrar o programa
            break
        else:
            print("Opção inválida!")
            relogio.avancaTempo(5)
