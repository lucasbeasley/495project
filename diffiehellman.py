#Name: Lucas Beasley
#Purpose: Diffie Hellman key exchange for project 2
from Crypto.Util import number

#generate shared prime (p)
def getP():
    sharedPrime = number.getPrime(128)
    return sharedPrime

#shared base (g)
def getB():
    return 5

#generate random secret number (r)
def getRando():
    rando = number.getRandomNumber(128)
    return rando
