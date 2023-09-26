import random
from words import word_list
from colorama import Fore, Back, Style


import pyfiglet

ASCII_art_1 = pyfiglet.figlet_format("HANGMAN")
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
dashes()


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
            before_rules = True
            while before_rules:
                dashes()
                print("\nWould you like to read the rules? " + Style.NORMAL + Fore.GREEN)
                game_rules = input("Y/N\n" + Style.NORMAL + Fore.GREEN).upper()
                print(Style.RESET_ALL)
                if game_rules == "Y":
                    rules()
                elif game_rules == "N":
                    dashes()
                    print(+"\nLet's play!\n")
                    play_game(word)
                else:
                    invalid()
                    
        elif play_now == "N":
            print("\nThat's too bad, adios!\n")
            dashes()
        else:
            invalid()


def rules():
    dashes()
    print("\nGreat! Listen up!\n")
    print(Style.NORMAL + Fore.RED + Back.CYAN + "RULES")
    print(Style.RESET_ALL)
    print("\n1. Pick a letter.\n2. If the letter is in the word"
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


def invalid():
    print(Fore.RED + "\nThat isn't a valid option.")
    print(Style.RESET_ALL)
    dashes()


def lives_guesses(lives, letters_guessed):
    print(f"\nlives = {lives}\n")
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
                print(f"\nGood choice! {guess} is in the word!\n")
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
                print(f"\n{guess} isn't in the word\n")
                letters_guessed.append(guess)
                lives = lives - 1
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
        print("\nSorry you lost.\n")
        print(f"\nThe word was {word}.\n")
        game_over()
    else:
        print(
            "\nCongratulations!"
            + f"You guessed the word {word} with {lives} lives to go!\n"
        )
        game_over()


def game_over():
    after_play = True
    while after_play:
        play_again = input("\nPlay again? Y/N\n").upper()
        if play_again == "Y":
            print("\nGreat, let's play!\n")
            dashes()
            play_game(word)
        elif play_again == "N":
            print("\nLet's go you back to the main menu.\n")
            dashes()
            main_menu()
        else:
            print("\nThat isn't a valid option.\n")
            dashes()


def main():
    main_menu()


main()
