import random
from words import word_list


print("\nWelcome to HANGMAN!")
print("-------------------")

def pick_word():
    word = random.choice(word_list)
    return word.upper()

word = pick_word()


def main_menu():
    answer = input("\nWould you like to play? Y/N\n").upper()
    if answer == "Y":
        print("\nGreat! Listen up!\n")
        print("\nRULES\n1. Pick a letter.\n2. If the letter is in the word you'll see it appear in the missing letters sections.\n3. If the letter is incorrect it'll appear in the guessed letters section.\n4. Be careful, each time you get a letter wrong you'll get closer to hanging the man. It'll only take 6 wrong moves to kill him, so choose wisely.\n")
        ready = input("\nAre you ready? Y/N \n").upper()
        if ready == "Y":
            print("\nLet's go!\n")
            play_game(word)
        elif ready == "N":
            print("\nThat's okay but I'll make you read the rules again if you change your mind.\n")
            main_menu()
        else:
            understand = input("Do you understand the rules or not? Y/N\n").upper()
            if understand == "Y":
                print("\nLet's go!\n")
                play_game(word)
            elif understand == "N":
                main_menu()
            else:
                print("\nHave it your way, back to the main menu!\n")
                main_menu()
    elif answer == "N":
        print("\nThat's too bad, adios!\n")
    else:
        print("\nThat wasn't an option...\n")
        main_menu()

def play_game(word):
    letters= "_ " * len(word)
    correct_word = list(word)
    lives = 6
    letters_guessed = []
    correct_letters = []
    guessed = False
    print(f"\nlives = {lives}\n")
    while not guessed and lives > 0:
        print(f"\n{letters}\n")
        guess = input("\nChoose a letter: \n").upper()
        if guess.isalpha() and len(guess) == 1:
            if guess in letters_guessed:
                print("\nYou already picked that letter\n")
                print(f"\nlives = {lives}\n")
                print("=========================================")
            elif guess in word:
                print(f"\nGood choice! {guess} is in the word!\n")
                letters_guessed.append(guess)
                correct_letters.append(guess)
                correct_word = list(letters)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    correct_word[index] = guess
                letters = "".join(correct_word)
                if "_" not in letters:
                    guessed = True
                print(f"\nlives = {lives}\n")
                print("=========================================")
            elif guess not in word:
                print(f"\n{guess} isn't in the word\n")
                letters_guessed.append(guess)
                lives = lives - 1
                print(f"\nlives = {lives}\n")
                print("=========================================")
        elif not guess.isalpha() or len(guess) != 1:
            print("\nNope, can't pick that. You have to choose a single letter.\nTry again.\n")
            print("=========================================")
    if lives == 0:
        print("\nSorry you lost.\n")
        print(f"\nThe word was {word}.\n")
        play_again = input("\nPlay again? Y/N\n")
        if play_again == "Y":
            print("\nGreat, let's play!\n")
            play_game()
        elif play_again == "N":
            print("\nOkay, I'll bring you back to the main menu incase you change your mind.\n")
            main_menu()
        else:
            print("\n I don't know what you're trying to say so I'll just bring you to the main menu.")
            main_menu()
    if correct_word == correct_letters:
        print(f"\nCongratulations! You guessed the word {word}!.\n")
        play_again = input("\nPlay again? Y/N\n")
        if play_again == "Y":
            print("\nGreat, let's play!\n")
            play_game()
        elif play_again == "N":
            print("\nOkay, I'll bring you back to the main menu incase you change your mind.\n")
            main_menu()
        else:
            print("\n I don't know what you're trying to say so I'll just bring you to the main menu.")
            main_menu()

def main():
    main_menu()

main()
