import socket

def udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('127.0.0.1', 12345))

    print("UDP server listening on port 12345")

    data, addr = server.recvfrom(1024)

    print(f"received from {addr}: {data.decode()}")

    server.sendto("hello from UDP server!".encode(), addr)

    server.close()

udp_server()