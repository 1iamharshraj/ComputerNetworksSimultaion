import socket
import random
import time

WINDOW_SIZE = 4  # Maximum window size

def receiver():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Receiver (GBN): Waiting for sender to connect...")
    conn, addr = server_socket.accept()
    print(f"Receiver (GBN): Connected to {addr}")

    expected_frame = 1

    while True:
        frame = conn.recv(1024).decode()
        if frame == "END":
            print("Receiver (GBN): Transmission complete. Closing connection.")
            break

        print(f"Receiver (GBN): Received {frame}")

        # Simulate packet loss
        if random.random() < 0.3:
            print(f"Receiver (GBN): Frame {frame} lost! No ACK sent.")
            continue

        frame_number = int(frame.split("-")[1])
        if frame_number == expected_frame:
            ack = f"ACK-{frame}"
            conn.send(ack.encode())
            print(f"Receiver (GBN): Sent {ack}")
            expected_frame += 1  # Move to next expected frame
        else:
            print(f"Receiver (GBN): Out-of-order frame received. Discarding!")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    receiver()
