import socket
import random
import time

HOST = '127.0.0.1'  # change to server's IP when testing across devices
PORT = 65432

def generate_temperature():
    return round(random.uniform(18.0, 35.0), 1)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")

        while True:
            temp = generate_temperature()
            message = f"Temperature: {temp} C"
            s.sendall(message.encode())
            print(f"Sent: {message}")
            time.sleep(5)

if __name__ == "__main__":
    main()
