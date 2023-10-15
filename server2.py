import socket

host = "localhost" 
port = 55555  

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Server listening on {host}:{port}...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    data = client_socket.recv(1024).decode()  # Receive data from the client
    print("Received data:", data)
    capitalized_data = data.upper()  # Capitalize the received data
    print("Capitalized data:", capitalized_data)
    client_socket.send(capitalized_data.encode())  # Send the capitalized data back to the client
    print("Sent data back to the client")
    client_socket.close()   # Close the connection with the client
    print("Connection closed\n")