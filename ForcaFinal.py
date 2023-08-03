import random
import time
def jogarDenovo():
    jogar()
def jogar():
    c = 's'
    print("""
            ----------- MENU -----------
            |   Digite 1 para jogar      |
            |   Digite 2 para sair       |
            |   Digite 3 para um fato    |
            ----------------------------
        """)
    Digitado = input()
    if Digitado not in ('1', '2', '3'): #Fora das opções
        print("\x1b[2J\x1b[1;1H")
        print("Essa opção não existe")
        jogar()

    while True:
        if Digitado == "1":
            c = 's'
            while c == 's':     #Enquanto for S, sortear outra palavra da lista
                listaForca = ["patricia","chico","alexandre","simone","sergio","bruno","alberto","junior","julia","luciana"]
                Sorte = random.choice(listaForca)
                print("\x1b[2J\x1b[1;1H")
                print("                         Adivinhe o nome do professor")
                long = len(Sorte)
                print(f"                A palavra tem {long} caracteres apenas minusculos")
                print("                              ", long*"_ ")
                print("""
                    ------------- OPÇÕES --------------
                    |   Aperte enter para continuar     |
                    |   Digite s  para trocar a palavra |
                    |   Digite 1 para sair              |
                    -----------------------------------
                """)
                c = input("")

                if c == '1':
                    print("\x1b[2J\x1b[1;1H")
                    print("""
                        Você saiu do jogo
                    """)
                    exit()

            erro = 0
            certo = 0
            pontos = long * "_"
            ganhou = False
            comeca_time = time.time()   #  Quando sair do while iniciar timer
            print("\x1b[2J\x1b[1;1H")
            print("Você tem 1 minuto")
            while True:
                if erro != 6 :
                    print(f"Digite 1 para parar")
                    print(f"Digite uma letra: {pontos}")
                    letra = input("")
                if letra in pontos:
                    print("Você já digitou essa letra antes. Por favor, tente novamente.")
                    continue
                if letra == '1':
                    print("\x1b[2J\x1b[1;1H")
                    print("Você parou o jogo")
                    jogar()

                acaba_time = time.time() - comeca_time 
                if acaba_time >= 60:  #Acabar em 60 segundos
                    print("\x1b[2J\x1b[1;1H")
                    print("O tempo acabou!")
                    jogar()
                if letra in Sorte and letra != "":
                    for i in range(len(Sorte))  :#Vai verificar se a letra digitada esta dentro da palavra sorteada, entra, verifica a posicao do i, sai e vai indo ate acabar a palavra
                        if Sorte[i] == letra:     
                            pontos = pontos[:i] + letra + pontos[i + 1:]    # Se ela é encontrada, troca pelo lugar que ela foi encontrada e continua verificando
                            certo  = certo + 1  #Se achar a certa, aumenta os certos para cada achada
                    print("\x1b[2J\x1b[1;1H")
                    print(f"""
                        Você acertou
                        {pontos}
                    """)

                    if pontos == Sorte:     #Se a o tamanho de pontos for igual a da palavra, ele ganha
                        ganhou = True
                        break
                
                elif letra != '1' and letra not in Sorte:   #Verifica se esta errado
                        erro  = erro + 1
                        
                        if erro == 1:
                            print("\x1b[2J\x1b[1;1H")
                            print("""
                                Você errou
                                    |
                                    O
                                   /|\ 
                                   / 
                        Você tem mais 5 chances 
                            """)
                        elif erro == 2:
                            print("\x1b[2J\x1b[1;1H")
                            print("""
                                Você errou
                                    |
                                    O
                                   /|\ 

                        Você tem mais 4 chances  
                            """)
                        elif erro == 3:
                            print("\x1b[2J\x1b[1;1H")
                            print("""
                                Você errou
                                    |
                                    O
                                   /| 

                        Você tem mais 3 chances
                            """)
                        elif erro == 4:
                            print("\x1b[2J\x1b[1;1H")
                            print("""
                                Você errou
                                    |
                                    O
                                    |

                        Você tem mais 2 chances
                            """)
                        elif erro == 5:
                            print("\x1b[2J\x1b[1;1H")
                            print("""
                                Você errou
                                    |
                                    O


                        Você tem mais 1 chance
                            """)
                        elif erro == 6:     #Se a quantidade de erros for igual a 6, perde
                            print("\x1b[2J\x1b[1;1H")
                            print("""
                                --------- Você perdeu -----------
                                |   Digite 1  para jogar de novo    |
                                |   Digite 2 para sair              |
                                ----------------------------------
                            """)
                            novo = input("")
                            if novo == '1':
                                print("\x1b[2J\x1b[1;1H")
                                jogarDenovo()
                            elif novo == '2':
                                print("\x1b[2J\x1b[1;1H")
                                print("Você encerrou o jogo")
                                exit()
                            else:
                                print("\x1b[2J\x1b[1;1H")
                                print("""
                                Essa opção não existe
                                """)
                                break

            if ganhou:
                print("\x1b[2J\x1b[1;1H")
                print(f"""
                     -------- Parabéns! Você ganhou!  --------
                    |               O nome era                |
                                     {Sorte}
                                                     
                    |   Digite 1 para jogar de novo           |
                    |   Digite 2 para sair                    |
                     -----------------------------------------
                """)
                novo = input("")
                if novo == '1':
                    print("\x1b[2J\x1b[1;1H")
                    jogar()
                elif novo == '2':
                    print("\x1b[2J\x1b[1;1H")
                    print("""
                    Você encerrou o jogo
                    """)
                    exit()
                else:
                    print("\x1b[2J\x1b[1;1H")
                    print("""
                    Essa opção não existe
                    """)
                    break

        elif Digitado == "2":
            print("\x1b[2J\x1b[1;1H")
            print("""
                Você fechou o jogo
            """)
            break

        elif Digitado == "3":
            print("\x1b[2J\x1b[1;1H")
            print("""  
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣧⣀⣼⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄                                             ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣧⣀⣼⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⣠⣾⣿⣷⡀⠄⠄⠄⠄⠄⣤⣶⣿⣿⣿⣦⣄⠄⠄⠄⠄⠄⣠⣾⣿⣷⣄⠄                                             ⠄⣠⣾⣿⣷⡀⠄⠄⠄⠄⠄⣤⣶⣿⣿⣿⣦⣄⠄⠄⠄⠄⠄⣠⣾⣿⣷⣄⠄
⠺⣿⣿⣿⣿⣿⣦⡀⠄⠄⠄⠿⢿⣿⣿⣿⡿⠟⠄⠄⠄⢀⣼⣾⣿⣿⣿⡿⠇                                             ⠺⣿⣿⣿⣿⣿⣦⡀⠄⠄⠄⠿⢿⣿⣿⣿⡿⠟⠄⠄⠄⢀⣼⣾⣿⣿⣿⡿⠇
⠄⠈⠻⢿⣿⣿⢛⡇⠄⠄⢀⣠⡤⣖⣗⣷⠤⣄⣀⠄⠄⣸⠛⣿⣿⡿⠋⠄⠄                                             ⠄⠈⠻⢿⣿⣿⢛⡇⠄⠄⢀⣠⡤⣖⣗⣷⠤⣄⣀⠄⠄⣸⠛⣿⣿⡿⠋⠄⠄
⠄⠄⠄⠄⠙⠛⠛⢗⡴⣛⠭⣖⢂⠏⡟⢹⠖⢖⠭⡓⢤⡛⠛⠛⠉⠄⠄⠄⠄                                             ⠄⠄⠄⠄⠙⠛⠛⢗⡴⣛⠭⣖⢂⠏⡟⢹⠖⢖⠭⡓⢤⡛⠛⠛⠉⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⡴⣫⢞⢈⡳⠛⠈⠉⠉⠉⠙⠺⢦⡿⠢⡙⣆⠄⠄⠄⠄⠄⠄⠀⠀⠀⠀⠀⠀          ⢀⣠⣤⣶⣶⣶⣶⣶⣤⣄⡀                  ⠄⠄⠄⠄⠄⠄⡴⣫⢞⢈⡳⠛⠈⠉⠉⠉⠙⠺⢦⡿⠢⡙⣆⠄⠄⠄⠄⠄⠄                                                                    
⠄⠄⠄⠄⠄⡾⣱⠉⡲⣏⢀⡠⠴⢶⣟⣓⡤⠔⣚⠑⣖⢛⡌⣧⠄⠄⠄⠄⠄              ⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀             ⠄⠄⠄⠄⠄⡾⣱⠉⡲⣏⢀⡠⠴⢶⣟⣓⡤⠔⣚⠑⣖⢛⡌⣧⠄⠄⠄⠄⠄                                                                 
⠄⠄⠄⠄⢸⢧⣇⢬⠃⠐⢵⣏⣛⠸⢷⣶⣚⡭⠾⠄⠘⣑⣺⢸⡄⠄⠄⠄⠄           ⣠⣴⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣵⣄           ⠄⠄⠄⠄⢸⢧⣇⢬⠃⠐⢵⣏⣛⠸⢷⣶⣚⡭⠾⠄⠘⣑⣺⢸⡄⠄⠄⠄⠄                                                     
⠄⠄⠄⠨⣯⣿⣙⣨⠄⠄⠣⠩⢖⣫⠭⠭⡵⣚⣭⢅⠄⡷⢶⣿⣽⠄⠄⠄⠄         ⢾⣻⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⡀          ⠄⠄⠄⠨⣯⣿⣙⣨⠄⠄⠣⠩⢖⣫⠭⠭⡵⣚⣭⢅⠄⡷⢶⣿⣽⠄⠄⠄⠄                                  
⠄⠄⠄⠈⠹⡝⣿⡿⡀⠄⠈⣋⡭⢖⣫⡭⣞⡽⢖⣫⢤⣉⣹⢹⠏⠄⠄⠄⠄        ⠸⣽⣻⠃⣿⡿⠋⣉⠛⣿⣿⣿⣿⣿⣿⣿⣿⣏⡟⠉⡉⢻⣿⡌⣿⣳⡥          ⠄⠄⠄⠈⠹⡝⣿⡿⡀⠄⠈⣋⡭⢖⣫⡭⣞⡽⢖⣫⢤⣉⣹⢹⠏⠄⠄⠄⠄                           
⠄⣦⡀⠄⠄⢳⡱⣥⡶⢄⠄⠸⡚⠁⢰⣛⡭⠖⠉⡠⠳⣭⢇⡟⠄⠄⢀⣴⠄        ⢜⣳⡟⢸⣿⣷⣄⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⣠⣼⣿⣇⢸⢧⢣          ⠄⣦⡀⠄⠄⢳⡱⣥⡶⢄⠄⠸⡚⠁⢰⣛⡭⠖⠉⡠⠳⣭⢇⡟⠄⠄⢀⣴⠄                                                             
⢰⣿⢷⣤⡀⠈⠳⣝⢤⣾⠶⣤⣕⣀⠄⣀⣀⣤⠚⣷⡶⣣⠞⠄⢀⣴⢿⣿⠄       ⠨⢳⠇ ⣸⣿⣿⢿⣿⣿⣿⣿⡿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡟⢆          ⢰⣿⢷⣤⡀⠈⠳⣝⢤⣾⠶⣤⣕⣀⠄⣀⣀⣤⠚⣷⡶⣣⠞⠄⢀⣴⢿⣿⠄                              
⠄⣿⢞⣷⡀⠄⢀⠜⠲⣍⡲⠿⣢⣰⣩⣠⡃⠿⣛⡡⠞⠥⡀⠄⣠⣟⡶⡿⠄⠀       ⠈⠀  ⣾⣿⣿⣼⣿⣿⣿⣿⡀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣽⣿⣿⠐⠈          ⠄⣿⢞⣷⡀⠄⢀⠜⠲⣍⡲⠿⣢⣰⣩⣠⡃⠿⣛⡡⠞⠥⡀⠄⣠⣟⡶⡿⠄                             
⠄⠄⠈⢫⡻⣶⡟⠁⠄⠄⠉⠑⠒⣗⣟⡗⠒⠛⠉⠄⠄⠄⢨⣶⣯⠞⠄⠁⠄         ⢀⣀⣼⣷⣭⣛⣯⡝⠿⢿⣛⣋⣤⣤⣀⣉⣛⣻⡿⢟⣵⣟⣯⣶⣿⣄⡀         ⠄⠄⠈⢫⡻⣶⡟⠁⠄⠄⠉⠑⠒⣗⣟⡗⠒⠛⠉⠄⠄⠄⢨⣶⣯⠞⠄⠁⠄
⠄⠄⠄⡠⠻⢮⡻⣦⣄⡀⠄⠄⣀⣥⣥⣥⡀⠄⠄⣀⣠⡶⣿⡿⠛⢆⠄⠄⠄⠀      ⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣾⣶⣶⣴⣾⣿⣿⣿⣿⣿⣿⢿⣿⣿⣧         ⠄⠄⠄⡠⠻⢮⡻⣦⣄⡀⠄⠄⣀⣥⣥⣥⡀⠄⠄⣀⣠⡶⣿⡿⠛⢆⠄⠄⠄                                             
⠄⠄⠾⠉⠄⠄⠙⠿⣽⣟⣿⣿⡿⠟⢹⣿⣿⣿⣟⣿⣽⠞⠋⠄⠄⠄⠑⠄⠄       ⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⡿         ⠄⠄⠾⠉⠄⠄⠙⠿⣽⣟⣿⣿⡿⠟⢹⣿⣿⣿⣟⣿⣽⠞⠋⠄⠄⠄⠑⠄⠄             

                                    O CORINTHIANS É O MAIOR DO BRASIL
                            """)
            
            exit()
        
jogar()