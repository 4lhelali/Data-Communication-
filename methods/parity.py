def parity_bit(text):
    bits = "".join(f"{ord(c):08b}" for c in text)
    return str(bits.count("1") % 2)
