guesses = 7

stick_figures = [
"\n_______\n\
 | /\n\
 |/\n\
 |\n\
 |\n\
----\n",

"\n_______\n\
 | /  |\n\
 |/\n\
 |\n\
 |\n\
----\n",

"\n_______\n\
 | /  |\n\
 |/   O\n\
 |\n\
 |\n\
----\n",

"\n_______\n\
 | /  |\n\
 |/   O\n\
 |    |\n\
 |\n\
----\n",

"\n_______\n\
 | /  |\n\
 |/   O\n\
 |   -|\n\
 | \n\
----\n",

 "\n_______\n\
 | /  |\n\
 |/   O\n\
 |   -|-\n\
 |\n\
----\n",

 "\n_______\n\
 | /  |\n\
 |/   O\n\
 |   -|-\n\
 |   / \n\
----\n",

 "\n_______\n\
 | /  |\n\
 |/   O\n\
 |   -|-\n\
 |   / \ \n\
----\n"
]

def check_guess(guess):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    guess = guess.strip().upper()
    if len(guess) != 1:
        return False
    if guess not in alphabet:
        return False
    return guess