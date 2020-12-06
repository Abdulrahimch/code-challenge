import random
import string

LETTERS = "".join(set(string.ascii_lowercase))

def generate_word():
    word = random.choice(LETTERS)
    return word


