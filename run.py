import random
from words import word_list
from colorama import Fore, Back, Style
def display_hangman(lives):
    
    if lives == 10:
        print( """
""")    
    elif lives == 9:
        print( """
   
    | 
    |              
    |                
    |                 
    |               
    |                   
    |                

""")
    
    elif lives == 8:
        print( """
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 

""")

    elif lives == 7:
        print("""
   _________
    |/   |      
    |    |         
    |                
    |                 
    |               
    |                   
    |___                 

""")
    elif lives == 6:
        print("""
   _________       
    |/   |              
    |   _|_  
    |  /   \ 
    |  \_ _/   
    |                         
    |                       
    |                         
    |                          
    |___                       

""")
    elif lives == 5:
        print("""
   ________               
    |/   |                   
    |   _|_  
    |  /   \ 
    |  \_ _/    
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    

""")
    elif lives == 4:
        print("""
   _________             
    |/   |               
    |   _|_  
    |  /   \ 
    |  \_ _/     
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          

""")
    elif lives == 3:
        print("""
   _________              
    |/   |                     
    |   _|_  
    |  /   \ 
    |  \_ _/     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          

""")
    elif lives == 2:
        print("""
   ________                   
    |/   |                         
    |   _|_  
    |  /   \ 
    |  \_ _/                          
    |   /|\                             
    |    |                          
    |  _/                            
    |                                  
    |___                              

""")
    elif lives == 1:
        print("""
   ________
    |/   |
    |   _|_  
    |  /   \ 
    |  \_ _/   
    |   /|\         
    |    |        
    |  _/ \_       
    |               
    |___           
    
""")
    elif lives == 0:
        print("""
   ________
    |/   |
    |   _|_  
    |  /x x\ 
    |  \_-_/   
    |   /|\         
    |    |        
    |  _/ \_       
    |               
    |___           
    
""")
print(
    Style.NORMAL
    + Fore.RED
    + Back.CYAN
    + """
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                """
)

print(Style.RESET_ALL)


def dashes():
    print(Style.NORMAL + Fore.CYAN
          + "=========================================")
    print(Style.RESET_ALL)


print("\nWelcome to HANGMAN!")


def pick_word():
    the_word = random.choice(word_list)
    return the_word.upper()


word = pick_word()


def main_menu():
    before_play = True
    while before_play:
        print("\nWould you like to play?" + Style.NORMAL + Fore.GREEN)
        play_now = input("Y/N\n" + Style.NORMAL + Fore.GREEN).upper()
        print(Style.RESET_ALL)
        if play_now == "Y":
            dashes()
            before_rules = True
            while before_rules:
                print(
                    "\nWould you like to read the rules? "
                    + Style.NORMAL + Fore.GREEN
                )
                game_rules = input("Y/N\n" + Style.NORMAL + Fore.GREEN).upper()
                print(Style.RESET_ALL)
                if game_rules == "Y":
                    dashes()
                    rules()
                elif game_rules == "N":
                    dashes()
                    print("\nLet's play!\n")
                    play_game(word)
                else:
                    invalid()
                    dashes()
        elif play_now == "N":
            print("\nThat's too bad, adios!\n")
            dashes()
        else:
            invalid()
            dashes()


def rules():
    print("\nGreat! Listen up!\n")
    print(Style.NORMAL + Fore.CYAN + "RULES")
    print(Style.RESET_ALL)
    print(
        "\n1. Pick a letter.\n2. If the letter is in the word"
        + " you'll see it appear in the missing letters sections.\n3."
        + " If the letter is incorrect it'll appear in the guessed letters"
        + " section.\n4. Be careful, each time you get a letter wrong"
        + " you'll get closer to hanging the man. It'll only take 6 wrong"
        + " moves to kill him, so choose wisely.\n"
    )
    after_rules = True
    while after_rules:
        print("\nAre you ready to play?" + Style.NORMAL + Fore.GREEN)
        understand = input("Y/N\n" + Style.NORMAL + Fore.GREEN).upper()
        print(Style.RESET_ALL)
        if understand == "Y":
            dashes()
            print("\nLet's play!\n")
            play_game(word)
        elif understand == "N":
            print("\nNo problem, lets go back to the main menu.\n")
            dashes()
            main_menu()
        else:
            invalid()
            dashes()


def invalid():
    print(Fore.RED + "\nThat isn't a valid option.")
    print(Style.RESET_ALL)


def lives_guesses(lives, letters_guessed):
    if 7 < lives <= 10:
        print("\nlives = " + Fore.GREEN + f"{lives}\n")
    elif 3 < lives <= 7:
        print("\nlives = " + Fore.YELLOW + f"{lives}\n")
    elif lives <= 3:
        print("\nlives = " + Fore.RED + f"{lives}\n")
    print(Style.RESET_ALL)
    print(*letters_guessed)


def play_game(word):
    word = pick_word()
    letters = "_" * len(word)
    lives = 10
    letters_guessed = []
    correct_letters = []
    guessed = False
    lives_guesses(lives, letters_guessed)
    while not guessed and lives > 0:
        print(f"\n{letters}\n")
        guess = input("\nChoose a letter: \n").upper()
        if guess.isalpha() and len(guess) == 1:
            if guess in letters_guessed:
                print("\nYou already picked that letter\n")
                lives_guesses(lives, letters_guessed)
                dashes()
            elif guess in word:
                print(
                    "\nGood choice!"
                    + Fore.GREEN
                    + f" {guess} "
                    + Style.RESET_ALL
                    + "is in the word!\n"
                )
                letters_guessed.append(guess)
                correct_letters.append(guess)
                correct_word = list(letters)
                indices = [i for i, letter in enumerate(word)
                           if letter == guess]
                for index in indices:
                    correct_word[index] = guess
                letters = "".join(correct_word)
                if "_" not in letters:
                    guessed = True
                display_hangman(lives)
                lives_guesses(lives, letters_guessed)
                dashes()
            elif guess not in word:
                print(
                    Fore.RED + f"\n{guess} " + Style.RESET_ALL
                    + "isn't in the word\n"
                )
                letters_guessed.append(guess)
                lives = lives - 1
                display_hangman(lives)
                lives_guesses(lives, letters_guessed)
                dashes()
        elif not guess.isalpha() or len(guess) != 1:
            print(
                "\nNope, can't pick that."
                + "You have to choose a single letter."
                + "\nTry again.\n"
            )
            dashes()
    if lives == 0:
        print(Fore.RED + "\nSorry you lost.\n" + Style.RESET_ALL)
        print("\nThe word was" + Fore.RED + f" {word}.\n")
        dashes()
        game_over()
    else:
        print(Fore.GREEN + "\nCongratulations!" + Style.RESET_ALL)
        print(
            "You guessed the word"
            + Fore.GREEN
            + f" {word} "
            + Style.RESET_ALL
            + "with"
            + Fore.GREEN
            + f" {lives} "
            + Style.RESET_ALL
            + "lives to go!\n"
        )
        dashes()
        game_over()


def game_over():
    after_play = True
    while after_play:
        print("\nPlay again?\n" + Style.NORMAL + Fore.GREEN)
        play_again = input("Y/N\n").upper()
        print(Style.RESET_ALL)
        if play_again == "Y":
            dashes()
            print("\nGreat, let's play!\n")
            play_game(word)
        elif play_again == "N":
            print("\nLet's go you back to the main menu.\n")
            dashes()
            main_menu()
        else:
            invalid()
            dashes()


def main():
    main_menu()


main()

