def parity_2d(text):
    bits = [f"{ord(c):08b}" for c in text]

    row_parity = []
    col_parity = [0] * 8

    for row in bits:
        row_parity.append(str(row.count("1") % 2))
        for i, bit in enumerate(row):
            col_parity[i] ^= int(bit)

    return "".join(row_parity) + "".join(str(b) for b in col_parity)

