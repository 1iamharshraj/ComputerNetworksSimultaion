import socket
import time

host = "127.0.0.1"
port =  12345

def receiver():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((host,port))
    server_socket.listen(5)

    client_socket, addr = server_socket.accept()

    while True:
        frame = client_socket.recv(1024).decode()

        if(frame == "END"):
            print("Received all the frames")
            break


        print(f"recieved frame: {frame}")

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    receiver()

