def crc16(data):
    poly = 0x1021
    crc = 0xFFFF

    for c in data.encode():
        crc ^= c << 8
        for _ in range(8):
            crc = (crc << 1) ^ poly if crc & 0x8000 else crc << 1
            crc &= 0xFFFF

    return f"{crc:04X}"
