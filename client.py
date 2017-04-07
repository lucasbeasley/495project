#Name: Lucas Beasley
#Purpose: Client file for project 2

import socket
import diffiehellman
import pyDes

#create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to server
client_socket.connect(("localhost", 1234))

#generate client key
#get base, prime, and a random number for client
base = diffiehellman.getB()
prime = diffiehellman.getP()
crand = diffiehellman.getRando()

#client secret = g^r mod p
csec = pow(base, crand, prime)

#send base, prime, and csec to server
sentstr = str(base) + " " + str(prime) + " " + str(csec)
client_socket.send(sentstr)

#receive server secret
serverstr = client_socket.recv(2048)

#compute server's secret
ssec = pow(long(serverstr), long(crand), long(prime))

#send string using DES
binstr = "{0:b}".format(ssec)
binstr = binstr[:64]
deskey = int(binstr, 2)
des = pyDes.des(str(deskey)[:8], padmode= pyDes.PAD_PKCS5)
estr = des.encrypt("Network Security")
client_socket.send(estr)


