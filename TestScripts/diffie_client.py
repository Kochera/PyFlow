import hashlib
from cryptography.fernet import Fernet
import math
from math import sqrt
import random
import sys
from Cryptodome.Util import number
import socket


#this should be get x but i use x later in the program and it was confusing
def getZ(p):
    z = random.randint(0,p+1)
    return z
#create the generator
def getG(z,p):
    g = (z*z) % p
    return g
#generate N bit prime
def getQ(N):
    q = number.getPrime(N);
    return q
#generate p from q
def getP(q):
    p = (2*q) + 1
    return p
#get two prime numbers
def getPandQ():
    q = 0
    p = 0
    r = False

    while(r == False):
        q = getQ(2048)
        p = getP(q)
        r = rabin(p)
    
    return p,q
    

#prime test taken from an online resource  
def rabin(n):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n!=int(n):
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
 
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
 
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(8):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True 

#a function that either generates the new primes or takes existing primes 
#from a file for use 
def openPrimes(newPrime):
    p = 0
    q = 0
    primes = 0
    prime_file = ''
    if newPrime == False:
        try:
            prime_file= open("primes.txt","r")
            primes = prime_file.read()
            prime_file.close()
            primes = primes.split()
            p = primes[0]
            q = primes[1]
        except:
            print("creating primes")
            prime_file = open("primes.txt","w")
            p,q = getPandQ()
            prime_file.write(str(p))
            prime_file.write(" ")
            prime_file.write(str(q))
            prime_file.close()


    else:
        print("creating primes")
        prime_file = open("primes.txt","w")
        p,q = getPandQ()
        prime_file.write(str(p))
        prime_file.write(" ")
        prime_file.write(str(q))
        prime_file.close()
    return p,q


def client_send():
    server_calc = 0
    sock = socket.socket()

# Connect the socket to the port where the server is listening
    host = '127.0.0.1'   #local lost
    port = 65432   
    sock.connect(host,port)

    try:

        # Send data
        number,secret = calculate_client_secret(p,q)
        
        print('sending {!r}'.format(message))
        sock.sendall(number)

        data = sock.recv(2048)
        server_calc = data

    finally:
        print('closing socket')
        sock.close()

    return  server_calc, secret

def calculate_client_secret(p,q):
    
    z = getZ(p)
    g = getG(z,p)

    client_secret_number = random.randint(0,1001)

    client_send= (g**client_secret_number)%p

    return client_send, client_secret_number

def calculate_shared(server_calc, number,p):
    shared_secret = (server_calc**number)%p
    return shared_secret;
    


p,q = openPrimes(False)
doDiffie(int(p),int(q))