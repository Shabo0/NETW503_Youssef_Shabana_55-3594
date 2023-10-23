import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5605
client_socket.connect(('127.0.0.1', port))

def send_message():
    while True:
        message = input("Enter your message: ")
        client_socket.send(bytes(message, 'utf-8'))

        if message == "CLOSE SOCKET":
            break

def receive_message():
    while True:
        server_msg = client_socket.recv(1024).decode('utf-8')
        print(server_msg)

        if server_msg == "Connection closed.":
            break

print("Client connected.")
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)

send_thread.start()
receive_thread.start()

send_thread.join()
receive_thread.join()

client_socket.close()