import socket
import time


host = "127.0.0.1"
port =  12345

def sender():
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sender_socket.bind((host, port))
    print("Connection established with receiver ")

    frames = 5;
    for i in range(1,frames+1):
        frame = f"Frame{i}"
        sender_socket.send()
