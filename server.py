#Name: Lucas Beasley
#Purpose: Server file for project 2

import socket
import sys

#create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#setup server socket on machine
try:
    server_socket.bind(("localhost", 12345))
#catch
except socket.error as error:
    print error
    sys.exit()

#wait for clients
server_socket.listen(12345)

