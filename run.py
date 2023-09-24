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
