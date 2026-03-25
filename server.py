import socket

HOST = '0.0.0.0'   # listen on all interfaces (works for both localhost and LAN)
PORT = 65432

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on port {PORT} ...")

        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    print("Client disconnected.")
                    break
                print(f"Received: {data.decode()}")

if __name__ == "__main__":
    main()
