import random
import string

def insert_char(data):
    i = random.randint(0, len(data))
    random_char = random.choice(string.ascii_letters)
    return data[:i] + random_char + data[i:]
