import socket
from threading import Thread

def client_handler(client_socket):
    while True:
        data = client_socket.recv(1024)

        if not data:
            break

        message = data.decode('utf-8')

        print(f"Received message: {message}")

        response = "Server received your message: " + message
        client_socket.sendall(response.encode('utf-8'))
    
    client_socket.close()

def main():
    host = '127.0.0.1'
    port =  1024       #(non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print(f"server listening on {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            
            print(f"Accepted connection from {client_address}")

            client_thread = Thread(target = client_handler, args=(client_socket,))
            client_thread.start()


if __name__ == '__main__':
    main()