from random import randint
from helpers import *
import os
import sys
os.system('cls' if os.name == 'nt' else 'clear')
def game():

    with open("words.txt") as f:
        words = f.readlines()
        word = words[randint(1,len(words))]
        word = list(word.strip().upper())
        word_len = len(word)

    wrong = 0
    won = False
    output = ["_" for i in range(word_len)]
    letters_used = []
    letters_wrong = []

    while wrong < guesses:
        print(stick_figures[wrong])
        print(" ".join(output) + "\n")
        print("Wrong letters: " + " ".join(letters_wrong))
        print("\n\n")
        guess = input("Enter your guess: ")
        if guess.upper() == "QUIT":
            sys.exit()
        guess = check_guess(guess)
        if guess in letters_used:
            print("That letter is already used")
            continue
        if not guess:
            print("Enter a single letter\n")
            continue
        if guess in word:
            print("Correct! Guesses left:", guesses-wrong)
            for idx, letter in enumerate(word):
                if guess == letter:
                    output[idx] = letter
            if output == word:
                won = True
                print("\n")
                break
        else:
            wrong += 1
            print("Wrong! Guesses left:", guesses-wrong)
            letters_wrong.append(guess)
        letters_used.append(guess)
        print("\n\n")
    return word, won

def main():
    playing = True
    while playing:
        if input("Press enter to play or 'Q' to exit: ").upper() == "Q":
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()
        word, won = game()
        if won: 
            print("You won! The word was:", "".join(word))
        else:
            print("You lost! The word was:", "".join(word))
        play_again = input("Do you want to play again (Y/N): ").upper()
        if play_again == "Y":
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:
            playing = False
            return False
    

        
