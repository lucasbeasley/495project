#Name: Lucas Beasley
#Purpose: Server file for project 2

import socket
import diffiehellman
import time
import pyDes

#create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#setup server socket on machine
try:
    server_socket.bind(("localhost", 1234))

except socket.error as error:
    print error


#wait for clients
server_socket.listen(1234)


while 1:
    try:
        #accept clients
        client, address = server_socket.accept()

        #receive string
        clientstr = client.recv(2048)

        #unpackage string
        arr = clientstr.split(" ")
        base = arr[0]
        prime = arr[1]
        csec = arr[2]

        #generate random number
        srand = diffiehellman.getRando()

        #server secret = g^r mod p
        ssec = pow(long(base), long(srand), long(prime))

        #send client ssec
        client.send(str(ssec))

        #compute client's secret
        csec = pow(long(csec), long(srand), long(prime))

        #receive string using DES
        binstr = "{0:b}".format(csec)
        binstr = binstr[:64]
        deskey = int(binstr, 2)
        des = pyDes.des(str(deskey)[:8], padmode=pyDes.PAD_PKCS5)
        clientstr = client.recv(2048)
        dstr = des.decrypt(clientstr)

        #print received string
        print dstr

        # receive and decrypt message from client
        while 1:
            recstr = client.recv(2048)
            dstr = des.decrypt(str(recstr))
            print str(dstr)

            # get final time after decryption and pass to client
            end = time.time()
            client.send(str(end))

    except Exception as error:
        print error

