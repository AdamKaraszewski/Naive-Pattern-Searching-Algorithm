import random

def generate_string(alphabet, letters_number):
    return ''.join(random.choice(alphabet) for _ in range(letters_number))