import random
from words import word_list


print("\nWelcome to HANGMAN!")
print("-------------------")


def pick_word():
    the_word = random.choice(word_list)
    return the_word.upper()


word = pick_word()


def rules():
    print("\nGreat! Listen up!\n")
    print(
        "\nRULES\n1. Pick a letter.\n2. If the letter is in the word"
        + " you'll see it appear in the missing letters sections.\n3."
        + " If the letter is incorrect it'll appear in the guessed letters"
        + " section.\n4. Be careful, each time you get a letter wrong"
        + " you'll get closer to hanging the man. It'll only take 6 wrong"
        + " moves to kill him, so choose wisely.\n"
    )
    after_rules = True
    while after_rules:
        understand = input("Are you ready to play? Y/N\n").upper()
        if understand == "Y":
            print("\nLet's go!\n")
            play_game(word)
        elif understand == "N":
            print("\nNo problem, lets go back to the main menu.\n")
            main_menu()
        else:
            print("\nYour options are clear, Y or N...\n")


def main_menu():
    before_play = True
    while before_play:
        play_now = input("\nWould you like to play? Y/N\n").upper()
        if play_now == "Y":
            before_rules = True
            while before_rules:
                game_rules = input(
                    "\nWould you like to read the rules? " + "Y/N\n"
                ).upper()
                if game_rules == "Y":
                    rules()
                elif game_rules == "N":
                    play_game(word)
                else:
                    print("\nYour options are Y or N..." + "Try again.")
        elif play_now == "N":
            print("\nThat's too bad, adios!\n")
        else:
            print("\nThat wasn't an option...\n")


def game_over():
    after_play = True
    while after_play:
        play_again = input("\nPlay again? Y/N\n").upper()
        if play_again == "Y":
            print("\nGreat, let's play!\n")
            play_game(word)
        elif play_again == "N":
            print("\nI'll bring you back to the main menu.\n")
            main_menu()
        else:
            print("\nThat isn't a valid choice.")


def print_lives(lives):
    print(f"\nlives = {lives}\n")


def play_game(word):
    word = pick_word()
    letters = "_" * len(word)
    lives = 6
    letters_guessed = []
    correct_letters = []
    guessed = False
    print_lives(lives)
    while not guessed and lives > 0:
        print(f"\n{letters}\n")
        guess = input("\nChoose a letter: \n").upper()
        if guess.isalpha() and len(guess) == 1:
            if guess in letters_guessed:
                print("\nYou already picked that letter\n")
                print_lives(lives)
                print("=========================================")
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
                print_lives(lives)
                print("=========================================")
            elif guess not in word:
                print(f"\n{guess} isn't in the word\n")
                letters_guessed.append(guess)
                lives = lives - 1
                print_lives(lives)
                print("=========================================")
        elif not guess.isalpha() or len(guess) != 1:
            print(
                "\nNope, can't pick that."
                + "You have to choose a single letter."
                + "\nTry again.\n"
            )
            print("=========================================")
    if lives == 0:
        print("\nSorry you lost.\n")
        print(f"\nThe word was {word}.\n")
        game_over()
    if correct_word == correct_letters:
        print(f"\nCongratulations! You guessed the word {word}!.\n")
        game_over()


def main():
    main_menu()


main()
