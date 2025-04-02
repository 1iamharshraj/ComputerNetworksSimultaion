import socket
import time

host = "127.0.0.1"
port = 12345

def sender():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host,port))
    print("Sender : Connected to receiver.")

    frames = 5
    for i in range(1,frames+1):
        frame = f"frame-{i}"
        print(f"sending frame: {frame}")

        client_socket.send(frame.encode())

        ack = client_socket.recv(1024).decode()
        print(f"Receiver : {ack}")

        time.sleep(1)

    client_socket.send("END".encode())
    print("sender: transmission complete. Closing the connection")
    client_socket.close()

if __name__ == "__main__":
    sender()


