import socket
import time

WINDOW_SIZE = 4  # Maximum window size

def sender():
    host = "127.0.0.1"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Sender (GBN): Connected to receiver.")

    frames = 10  # Total number of frames
    base = 1  # First frame in the window
    next_frame = 1

    while base <= frames:
        # Send frames within window
        while next_frame < base + WINDOW_SIZE and next_frame <= frames:
            frame = f"Frame-{next_frame}"
            print(f"Sender (GBN): Sending {frame}")
            client_socket.send(frame.encode())
            next_frame += 1

        # Wait for acknowledgment
        try:
            client_socket.settimeout(3)  # Timeout for ACKs
            ack = client_socket.recv(1024).decode()

            # ✅ Check if ACK is valid before processing
            if not ack.startswith("ACK-"):
                print(f"Sender (GBN): Invalid ACK received '{ack}', ignoring it.")
                continue  # Ignore invalid ACK

            ack_num = int(ack.split("-")[1])  # Extract frame number from ACK
            print(f"Sender (GBN): Received {ack}, moving window forward")
            base = ack_num + 1  # Move window forward

        except socket.timeout:
            print("Sender (GBN): ACK timeout! Retransmitting window...")
            next_frame = base  # Go back and retransmit window

        time.sleep(1)

    client_socket.send("END".encode())
    print("Sender (GBN): Transmission complete. Closing connection.")

    client_socket.close()

if __name__ == "__main__":
    sender()
