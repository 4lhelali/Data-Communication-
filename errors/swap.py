import random

def swap_chars(data):
    if len(data) < 2:
        return data
    i = random.randint(0, len(data)-2)
    return data[:i] + data[i+1] + data[i] + data[i+2:]
