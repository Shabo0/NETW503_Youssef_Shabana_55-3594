import socket

host = "localhost"  # Change this to your server IP address if needed
port = 55555  # Make sure it matches the server port number

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

input_string = input("Enter a string: ")  # Send the input string to the server
client_socket.send(input_string.encode())
print("Sent data to server")

received_data = client_socket.recv(1024).decode()  # Receive the capitalized data from the server
print("Received data:", received_data)

client_socket.close()  # Close the client socket