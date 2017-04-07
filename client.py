#Name: Lucas Beasley
#Purpose: Client file for project 2

import socket

#create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to server
client_socket.connect(("localhost", 12345))
