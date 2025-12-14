import random
import string

def burst_error(data):
    length = random.randint(3, 8)
    if len(data) < length:
        return data

    start = random.randint(0, len(data) - length)
    burst = ''.join(random.choice(string.ascii_letters) for _ in range(length))

    return data[:start] + burst + data[start+length:]
