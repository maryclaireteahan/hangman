import random
from words import word_list
from colorama import Fore, Back, Style

print(
    Style.NORMAL
    + Fore.RED
    + Back.CYAN
    + """
|                                                                            |
|                                                                            |
|     ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗       |
|     ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║       |
|     ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║       |
|     ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║       |
|     ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║       |
|     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝       |
|                                                                            |
|                                                                            |
"""
)

print(Style.RESET_ALL)
print(" \nWelcome to HANGMAN!")
print(Fore.CYAN + "---------------------"
      + Style.RESET_ALL)


def pick_word():
    """
    Picks a random word from words.py file and
    returns then in uppercase.
    """
    the_word = random.choice(word_list)
    return the_word.upper()


word = pick_word()


def main_menu():
    """
    Asks player if they would like to play the game.
    If no the programme says goodbye.
    If yes they are asked if they need to see the rules.
    If yes the rules function is called.
    If no the play_game function is called and user starts the game.
    """
    before_play = True
    while before_play:
        print(" \nWould you like to play?" + Style.NORMAL + Fore.GREEN)
        play_now = input(" Y/N\n" + Style.NORMAL + Fore.GREEN).upper()
        print(Style.RESET_ALL)
        if play_now == "Y":
            dashes()
            before_rules = True
            while before_rules:
                print(
                    " \nWould you like to read the rules? "
                    + Style.NORMAL + Fore.GREEN
                )
                game_rules = input(" Y/N\n"
                                   + Style.NORMAL + Fore.GREEN).upper()
                print(Style.RESET_ALL)
                if game_rules == "Y":
                    dashes()
                    rules()
                elif game_rules == "N":
                    dashes()
                    print(" \nLet's play!\n")
                    play_game(word)
                else:
                    invalid()
                    dashes()
        elif play_now == "N":
            print(" \nThat's too bad, adios!\n")
            dashes()
        else:
            invalid()
            dashes()


def rules():
    """
    Rules for the game are presented.
    User is asked if they are ready to start the game.
    If yes the play_game function is called and the game begins.
    If no the user is brought back to the main_menu function.
    """
    print(" \nGreat! Listen up!\n")
    print(Style.NORMAL + Fore.CYAN + "RULES")
    print(Style.RESET_ALL)
    print(
        "\n1. Pick a letter."
        + "\n2. If the letter is in the word "
        + "you'll see it appear in the missing letters sections."
        + "\n3. If the letter is incorrect it'll appear "
        + "in the guessed letters section."
        + "\n4. Be careful, each time you get a letter wrong "
        + "you'll get closer to hanging the man."
        + "It'll only take 10 wrong moves to kill him, "
        + "so choose wisely.\n"
    )
    after_rules = True
    while after_rules:
        print("\nAre you ready to play?" + Style.NORMAL + Fore.GREEN)
        ready = input("Y/N\n" + Style.NORMAL + Fore.GREEN).upper()
        print(Style.RESET_ALL)
        if ready == "Y":
            dashes()
            print("\nLet's play!\n")
            play_game(word)
        elif ready == "N":
            print("\nNo problem, lets go back to the main menu.\n")
            dashes()
            main_menu()
        else:
            invalid()
            dashes()


def play_game(word):
    """
    A random word is selected from the pick_word function.
    User is promted to guess a letter.

    If the letter is in the word the user will get a message to say so and the
    letter will appear in the correct letter and used letter section.

    If the letter is not in the word the user
    will get a message to say so and the
    letter will appear in the used letter section.

    Each time a wrong letter is chosen the lives decrease by 1 and the hangman
    image progresses to the next stage.

    If the user guesses all correct letters they will get a message to saying
    so and how many lives they had left.

    If thr user has 0 lives before the find all the correct
    letters they will get a message to say so.

    The hangman will also be fully dead.
    """
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
                display_hangman(lives)
                print("Good choice!"
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
                lives_guesses(lives, letters_guessed)
                dashes()
            elif guess not in word:
                display_hangman(lives)
                print(
                    Fore.RED + f"{guess} " + Style.RESET_ALL
                    + "isn't in the word\n"
                )
                letters_guessed.append(guess)
                lives = lives - 1
                lives_guesses(lives, letters_guessed)
                dashes()
        elif not guess.isalpha() or len(guess) != 1:
            print(
                Fore.RED + 
                "\nNope, can't pick that."
                + "You have to choose a single letter."
                + "\nTry again.\n"
                + Style.RESET_ALL
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
    """
    When the game is over the user is given the option to
    either play again by selectin Y or returning to the main_menu
    function by selecting N.
    """
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


def dashes():
    """
    Used as dividers between each go in the game.
    """
    print(Style.NORMAL + Fore.CYAN
          + "----------------------------------------")
    print(Style.RESET_ALL)


def invalid():
    """
    If the customer selects an invalid key this
    message will display.
    """
    print(Fore.RED + "\nThat isn't a valid option.")
    print(Style.RESET_ALL)


def lives_guesses(lives, letters_guessed):
    """
    Lives decrease by 1 for each wrong letter. Different colors for
    0-3, 4-7 and 8-10.
    Function also prints the letters that have been guessed so far.
    """
    if 7 < lives <= 10:
        print("\nlives = " + Fore.GREEN + f"{lives}\n")
    elif 3 < lives <= 7:
        print("\nlives = " + Fore.YELLOW + f"{lives}\n")
    elif lives <= 3:
        print("\nlives = " + Fore.RED + f"{lives}\n")
    print(Style.RESET_ALL)
    print(*letters_guessed)


def display_hangman(lives):
    """
    Tha hangman that gets displayed each time a letter is guessed.
    When a letter is incorrect the next stage of the image is shown.
    """
    if lives == 10:
        print("""
""")
    elif lives == 9:
        print("""

    |
    |
    |
    |
    |
    |
    |

""")
    elif lives == 8:
        print("""
   _________
    |/
    |
    |
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
    |
    |
    |___

""")
    elif lives == 6:
        print("""
   _________
    |/   |
    |   _|_
    |  |   |
    |  |_ _|
    |
    |
    |
    |
    |___

""")
    elif lives == 5:
        print("""
   _________
    |/   |
    |   _|_
    |  |   |
    |  |_ _|
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
    |  |   |
    |  |_ _|
    | ---|
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
    |  |   |
    |  |_ _|
    | ---|---
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
    |  |   |
    |  |_ _|
    | ---|---
    |   _|
    |   |
    |   |
    |___

""")
    elif lives == 1:
        print("""
   ________
    |/   |
    |   _|_
    |  |   |
    |  |_ _|
    | ---|---
    |   _|_
    |   | |
    |   | |
    |___

""")
    elif lives == 0:
        print("""
   ________
    |/   |
    |   _|_
    |  |x x|
    |  |_-_|
    | ---|---
    |   _|_
    |   | |
    |   | |
    |___

""")


def main():
    """
    Run all programme functions.
    """
    main_menu()


main()
