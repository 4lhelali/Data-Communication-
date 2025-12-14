import random

def bit_flip(data):
    bits = list("".join(f"{ord(c):08b}" for c in data))
    i = random.randint(0, len(bits)-1)
    bits[i] = '0' if bits[i] == '1' else '1'

    chars = [
        chr(int("".join(bits[j:j+8]), 2))
        for j in range(0, len(bits), 8)
    ]
    return "".join(chars)
