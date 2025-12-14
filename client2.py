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

server = socket.socket()
server.bind(("localhost", 5001))
server.listen()

print("[CLIENT2] Waiting for server...")
conn, _ = server.accept()
packet = conn.recv(2048).decode()
conn.close()

data, method, incoming_control = packet.split("|")
computed = generate(data, method)

print("Received Data      :", data)
print("Method             :", method)
print("Incoming Control   :", incoming_control)
print("Computed Control   :", computed)

if incoming_control == computed:
    print("STATUS: DATA CORRECT")
else:
    print("STATUS: DATA CORRUPTED")
