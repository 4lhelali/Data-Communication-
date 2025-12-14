import socket
from methods import parity_bit, parity_2d, crc16, hamming_code, internet_checksum

def generate(text, method):
    if method == "PARITY":
        return parity_bit(text)
    if method == "2DPARITY":
        return parity_2d(text)
    if method == "CRC16":
        return crc16(text)
    if method == "HAMMING":
        return hamming_code(text)
    if method == "CHECKSUM":
        return internet_checksum(text)

text = input("Enter text: ")
method = input("Choose method (PARITY, 2DPARITY, CRC16, HAMMING, CHECKSUM): ").upper()

control = generate(text, method)
packet = f"{text}|{method}|{control}"

client = socket.socket()
client.connect(("localhost", 5000))
client.send(packet.encode())
client.close()

print("Sent:", packet)
