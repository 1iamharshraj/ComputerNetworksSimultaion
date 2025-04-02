import socket
import time

WINDOW_SIZE = 4  # Maximum window size
sent_frames = {}

def sender():
    host = "127.0.0.1"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Sender (SR): Connected to receiver.")

    frames = 10  # Total number of frames
    base = 1
    next_frame = 1

    while base <= frames:
        # Send frames within window
        while next_frame < base + WINDOW_SIZE and next_frame <= frames:
            frame = f"Frame-{next_frame}"
            print(f"Sender (SR): Sending {frame}")
            client_socket.send(frame.encode())
            sent_frames[next_frame] = frame
            next_frame += 1

        # Wait for acknowledgment
        try:
            client_socket.settimeout(3)
            ack = client_socket.recv(1024).decode()
            ack_num = int(ack.split("-")[1])

            print(f"Sender (SR): Received {ack}, removing from buffer")
            if ack_num in sent_frames:
                del sent_frames[ack_num]  # Remove acknowledged frame

            # Move base forward if the lowest unacknowledged frame advances
            while base in sent_frames:
                base += 1

        except socket.timeout:
            print("Sender (SR): ACK timeout! Retransmitting missing frames...")
            for frame_number in sent_frames:
                frame = sent_frames[frame_number]
                print(f"Sender (SR): Retransmitting {frame}")
                client_socket.send(frame.encode())

        time.sleep(1)

    client_socket.send("END".encode())
    print("Sender (SR): Transmission complete. Closing connection.")

    client_socket.close()

if __name__ == "__main__":
    sender()
