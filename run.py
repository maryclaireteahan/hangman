import random
from words import word_list


print("\nWelcome to HANGMAN!")
print("-------------------")

def pick_word():
    word = random.choice(word_list)
    return word.upper()

word = pick_word()
