import socket
import time
import random

host = "127.0.0.1"
port = 12345

def reciever():

    server_socker = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socker.bind((host,port))
    server_socker.listen(1)

    print("Reciever: Waiting for a connection")
    conn, addr = server_socker.accept()
    print("Connected by", addr)

    expected_frame = 1

    while True:
        frame = conn.recv(1024).decode()
        if frame == "END":
            print("Transmission is completed")
            break

        print(f"Reciever: received {frame}")

        if random.random() > 0.3:
            print(f"Reciever: Frame {frame} lost !")
            continue

        if random.random() > 0.2:
            corrupted_ack = "ACK-Corrupt"
            conn.send(corrupted_ack.encode())
            print(f"Reciever: sent corrupted ACK: {corrupted_ack} !")
            continue

        ack = f"ACK-{frame}"
        conn.send(ack.encode())
        print(f"Reciever: sent ACK: {ack} !")
        expected_frame +=1

    conn.close()
    server_socker.close()


if __name__ == "__main__":
    reciever()
