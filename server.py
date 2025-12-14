import socket
import random
from errors.bitflip import bit_flip
from errors.delete import delete_char
from errors.insert import insert_char
from errors.swap import swap_chars
from errors.burst import burst_error

ERROR_FUNCS = [
    bit_flip,
    delete_char,
    insert_char,
    swap_chars,
    burst_error
]

# Socket 1: Receive from Client 1
server1 = socket.socket()
server1.bind(("localhost", 5000))
server1.listen()

print("[SERVER] Waiting for client1...")
conn1, _ = server1.accept()
packet = conn1.recv(2048).decode()
conn1.close()

data, method, control = packet.split("|")

# Apply random error
error_func = random.choice(ERROR_FUNCS)
corrupted_data = error_func(data)

new_packet = f"{corrupted_data}|{method}|{control}"
print("[SERVER] Sending to client2:", new_packet)

# Socket 2: Send to Client 2
server2 = socket.socket()
server2.connect(("localhost", 5001))
server2.send(new_packet.encode())
server2.close()
