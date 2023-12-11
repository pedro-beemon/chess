# Echo client program
import socket

HOST = 'localhost'  # The remote host
PORT = 50007  # The same port as used by the server


def send_move(move: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(move.encode())
        data = s.recv(1024)
    print('Received', repr(data))
