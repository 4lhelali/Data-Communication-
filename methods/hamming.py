def hamming_encode(bits):
    d = list(map(int, bits))
    p1 = d[0] ^ d[1] ^ d[3]
    p2 = d[0] ^ d[2] ^ d[3]
    p4 = d[1] ^ d[2] ^ d[3]
    return f"{p1}{p2}{d[0]}{p4}{d[1]}{d[2]}{d[3]}"

def hamming_decode(bits):
    b = list(map(int, bits))
    p1 = b[0] ^ b[2] ^ b[4] ^ b[6]
    p2 = b[1] ^ b[2] ^ b[5] ^ b[6]
    p4 = b[3] ^ b[4] ^ b[5] ^ b[6]
    error_pos = p1 * 1 + p2 * 2 + p4 * 4

    if error_pos:
        b[error_pos - 1] ^= 1

    return f"{b[2]}{b[4]}{b[5]}{b[6]}", error_pos != 0

def hamming_code(text):
    encoded = ""
    for c in text:
        bits = f"{ord(c):08b}"
        encoded += hamming_encode(bits[:4])
        encoded += hamming_encode(bits[4:])
    return encoded

def hamming_decode_text(encoded):
    decoded = ""
    corrected = False
    for i in range(0, len(encoded), 14):
        b1, e1 = hamming_decode(encoded[i:i+7])
        b2, e2 = hamming_decode(encoded[i+7:i+14])
        decoded += chr(int(b1 + b2, 2))
        corrected |= e1 or e2
    return decoded, corrected
