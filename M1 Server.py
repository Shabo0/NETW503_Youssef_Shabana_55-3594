import socket
import threading

PORT = 5605
ADDR = ('127.0.0.1', PORT)

def handle_client(client_socket, addr):
    print("[NEW CONNECTION] " + str(addr) + " connected.")
    while True:
        message = client_socket.recv(1024).decode('utf-8')

        if message == "CLOSE SOCKET":
            client_socket.send("Connection closed.".encode('utf-8'))
            client_socket.close()
            print("[CONNECTION CLOSED] " + str(addr) + " disconnected.")
            break

        capitalized_message = message.upper()
        client_socket.send(capitalized_message.encode('utf-8'))

def main():
    print("Server is starting...")
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()
        
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == "__main__":
    main()