import socket
import time

host = "127.0.0.1"
port = 12345
def sender():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print("sender: connected to reciever")

    frames = 5
    for i in range(1,frames+1):
        frame = f"frame{i}"
        print(f"sender: sending {frame}")
        client.send(frame.encode())

        try:
            client.settimeout(3)
            ack = client.recv(1024).decode()
            print(f"sender: received {ack}")
            if ack == f"ACK-{frame}":
                print(f"Sender: Received acknowlege{ack}")
                break
            else:
                print(f"Sender: Received corrupt acknowlege{ack}")

        except socket.timeout:
            print(f"Sender: Timed out")

        time.sleep(1)
    client.send("END".encode())
    print("Sender: transmission completed")
    client.close()


if __name__ == "__main__":
    sender()
