import socket

def udp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto("hello from udp client".encode(),('127.0.0.1',12345))

    data, _ = client.recvfrom(1024)
    print(f"server response: {data.decode()}")

    client.close()

udp_client()