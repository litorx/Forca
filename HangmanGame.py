import random
import time

def playAgain():
    play()

def play():
    c = 's'
    print("""
            ----------- MENU -----------
            |   Enter 1 to play          |
            |   Enter 2 to exit          |
            |   Enter 3 for a fact       |
            ----------------------------
        """)
    Entered = input()
    if Entered not in ('1', '2', '3'): #Out of options
        print("\x1b[2J\x1b[1;1H")
        print("This option does not exist")
        play()

    while True:
        if Entered == "1":
            c = 's'
            while c == 's':     #While it is S, select another word from the list
                wordList = ["patricia","chico","alexandre","simone","sergio","bruno","alberto","junior","julia","luciana"]
                Chosen = random.choice(wordList)
                print("\x1b[2J\x1b[1;1H")
                print("                         Guess the teacher's name")
                long = len(Chosen)
                print(f"                The word has {long} characters only lowercase")
                print("                              ", long*"_ ")
                print("""
                    ------------- OPTIONS --------------
                    |   Press enter to continue       |
                    |   Type s to change the word      |
                    |   Enter 1 to exit                 |
                    -----------------------------------
                """)
                c = input("")

                if c == '1':
                    print("\x1b[2J\x1b[1;1H")
                    print("""
                        You exited the game
                    """)
                    exit()

            error = 0
            correct = 0
            points = long * "_"
            won = False
            start_time = time.time()   #  When exiting the while loop, start timer
            print("\x1b[2J\x1b[1;1H")
            print("You have 1 minute")
            while True:
                if error != 6 :
                    print(f"Type 1 to stop")
                    print(f"Type a letter: {points}")
                    letter = input("")
                if letter in points:
                    print("You have already typed this letter before. Please try again.")
                    continue
                if letter == '1':
                    print("\x1b[2J\x1b[1;1H")
                    print("You stopped the game")
                    play()

                end_time = time.time() - start_time 
                if end_time >= 60:  #End in 60 seconds
                    print("\x1b[2J\x1b[1;1H")
                    print("Time's up!")
                    play()
                if letter in Chosen and letter != "":
                    for i in range(len(Chosen))  :#Will check if the entered letter is within the chosen word, enters, checks the position of i, exits and goes on until the word ends
                        if Chosen[i] == letter:     
                            points = points[:i] + letter + points[i + 1:]    # If it is found, replace it with the place it was found and continue checking
                            correct  = correct + 1  #If it finds the correct one, it increases the correct ones for each found
                    print("\x1b[2J\x1b[1;1H")
                    print(f"""
                        You got it right
                        {points}
                    """)

                    if points == Chosen:     #If the length of points is equal to the word, he wins
                        won = True
                        break
                
                elif letter != '1' and letter not in Chosen:   #Checks if it is wrong
                        error  = error + 1
                        
                        if error == 1:
                            print("\x1b[2J\x1b[1;1H")
                            print("""
                                You got it wrong
                                    |
                                    O
                                   /|\ 
                                   / 
                        You have 5 more chances 
                            """)
                        elif error == 2:
                            print("\x1b[2J\x1b[1;1H")
                            print("""
                                You got it wrong
                                    |
                                    O
                                   /|\ 

                        You have 4 more chances  
                            """)
                        elif error == 3:
                            print("\x1b[2J\x1b[1;1H")
                            print("""
                                You got it wrong
                                    |
                                    O
                                   /| 

                        You have 3 more chances
                            """)
                        elif error == 4:
                            print("\x1b[2J\x1b[1;1H")
                            print("""
                                You got it wrong
                                    |
                                    O
                                    |

                        You have 2 more chances
                            """)
                        elif error == 5:
                            print("\x1b[2J\x1b[1;1H")
                            print("""
                                You got it wrong
                                    |
                                    O


                        You have 1 more chance
                            """)
                        elif error == 6:     #If the number of errors is equal to 6, lose
                            print("\x1b[2J\x1b[1;1H")
                            print("""
                                --------- You lost -----------
                                |   Enter 1 to play again     |
                                |   Enter 2 to exit           |
                                ----------------------------------
                            """)
                            new = input("")
                            if new == '1':
                                print("\x1b[2J\x1b[1;1H")
                                playAgain()
                            elif new == '2':
                                print("\x1b[2J\x1b[1;1H")
                                print("You closed the game")
                                exit()
                            else:
                                print("\x1b[2J\x1b[1;1H")
                                print("""
                                This option does not exist
                                """)
                                break

            if won:
                print("\x1b[2J\x1b[1;1H")
                print(f"""
                     -------- Congratulations! You won!  --------
                    |               The name was                |
                                     {Chosen}
                                                     
                    |   Enter 1 to play again                   |
                    |   Enter 2 to exit                         |
                     -----------------------------------------
                """)
                new = input("")
                if new == '1':
                    print("\x1b[2J\x1b[1;1H")
                    play()
                elif new == '2':
                    print("\x1b[2J\x1b[1;1H")
                    print("""
                    You closed the game
                    """)
                    exit()
                else:
                    print("\x1b[2J\x1b[1;1H")
                    print("""
                    This option does not exist
                    """)
                    break

        elif Entered == "2":
            print("\x1b[2J\x1b[1;1H")
            print("""
                You closed the game
            """)
            break

        elif Entered == "3":
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
        
play() 
