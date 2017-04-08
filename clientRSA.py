#Name: Lucas Beasley
#Purpose: Client file for project 2 with RSA implemented

import socket
import time
from Crypto.PublicKey import RSA
from Crypto.Hash import MD5

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

#hash message to send to server and send
stri = MD5.new('Network Security')
estr = pubskey.encrypt(stri.hexdigest(), 32)[0]
client_socket.send(estr)
client_socket.recv(2048)

#set timing
timing = 0

#send words to server
inputfile = open('10000words.txt', 'r')
for word in inputfile.readlines():
    #start timing
    start = time.time()

    #encrypt and receive final time
    estr = pubskey.encrypt(word.rstrip(), 32)[0]
    client_socket.send(estr)
    end = client_socket.recv(2048)

    #calculate total time taken to encrypt/decrypt
    timing = timing + (float(end) - start)

#report final timing
print("Total time taken in seconds: " + str(timing))
