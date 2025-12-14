def internet_checksum(data):
    data = data.encode()
    if len(data) % 2:
        data += b'\x00'

    checksum = 0
    for i in range(0, len(data), 2):
        word = (data[i] << 8) + data[i+1]
        checksum = (checksum + word) & 0xFFFF

    return f"{(~checksum) & 0xFFFF:04X}"
