import socket
import random
import time


host = "127.0.0.1"
port = 12345

def reciver():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Receiver: Waiting for sender to connect....")
    client_socket, addr = server_socket.accept()

    print(f"Receiver: Accepted connection from {addr}")

    while True:
        frame = client_socket.recv(1024).decode()
        if frame == "END":
            print("Receiver: Transmission Completed Closing connection...")
            break

        print(f"Receiver : Received {frame}")


        ack = f"ACK-{frame}"
        client_socket.send(ack.encode())
        print(f"Receiver : Sent {ack}")

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    reciver()
