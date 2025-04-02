import socket
import random
import time

WINDOW_SIZE = 4  # Maximum window size
buffer = {}

def receiver():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Receiver (SR): Waiting for sender to connect...")
    conn, addr = server_socket.accept()
    print(f"Receiver (SR): Connected to {addr}")

    expected_frame = 1

    while True:
        frame = conn.recv(1024).decode()
        if frame == "END":
            print("Receiver (SR): Transmission complete. Closing connection.")
            break

        print(f"Receiver (SR): Received {frame}")

        # Simulate packet loss
        if random.random() < 0.3:
            print(f"Receiver (SR): Frame {frame} lost! No ACK sent.")
            continue

        frame_number = int(frame.split("-")[1])

        # Store received frames
        buffer[frame_number] = frame

        # Send ACK for received frame
        ack = f"ACK-{frame_number}"
        conn.send(ack.encode())
        print(f"Receiver (SR): Sent {ack}")

        # Deliver frames in order
        while expected_frame in buffer:
            print(f"Receiver (SR): Delivered {buffer[expected_frame]}")
            del buffer[expected_frame]
            expected_frame += 1

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    receiver()
