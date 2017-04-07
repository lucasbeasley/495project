#Name: Lucas Beasley
#Purpose: Client file for project 2 with RSA implemented

import socket
import time
from Crypto.PublicKey import RSA

#create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to server
client_socket.connect(("localhost", 1234))

#generate client keys
ckey = RSA.generate(2048)
publick = ckey.publickey().exportKey('DER')
privatek = ckey.exportKey('DER')

#send public key to server
client_socket.send(publick)

#receive server public key
serverkey = client_socket.recv(2048)
pubskey = RSA.importKey(serverkey)



#send words to server
inputfile = open('10000words.txt', 'r')
for word in inputfile.readlines():
    estr = pubskey.encrypt(word.rstrip(), 32)[0]
    client_socket.send(estr)
    print client_socket.recv(2048)

