#Name: Lucas Beasley
#Purpose: Server file for project 2 with RSA implemented

import socket
from Crypto.PublicKey import RSA

#create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#setup server socket on machine
try:
    server_socket.bind(("localhost", 1234))

except socket.error as error:
    print error


#wait for clients
server_socket.listen(1234)

#generate server keys
skey = RSA.generate(2048)
publick = skey.publickey().exportKey('DER')
privatek = skey.exportKey('DER')
privk = RSA.importKey(privatek)




while 1:
    try:
        #accept clients
        client, address = server_socket.accept()

        #receive client public key
        clientkey = client.recv(2048)
        pubckey = RSA.importKey(clientkey)

        #send public key to client
        client.send(publick)

        #receive and decrypt message from client
        recstr = client.recv(2048)
        dstr = privk.decrypt(recstr)
        print dstr

    except Exception as error:
        print error

