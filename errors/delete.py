import random

def delete_char(data):
    if len(data) <= 1:
        return data
    i = random.randint(0, len(data)-1)
    return data[:i] + data[i+1:]
