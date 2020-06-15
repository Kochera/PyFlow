from PyFlow.Core import(
    FunctionLibraryBase,
    IMPLEMENT_NODE
)
from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
import hashlib
from cryptography.fernet import Fernet
import socket
import math
from math import sqrt
import random
import sys

def phi(n): 
      
    # Initialize result as n 
    result = n;  
  

    p = 2;  
    while(p * p <= n): 
          
        # Check if p is a  
        # prime factor. 
        if (n % p == 0):  
              
            # If yes, then  
            # update n and result 
            while (n % p == 0): 
                n = int(n / p); 
            result -= int(result / p); 
        p += 1; 
  
    if (n > 1): 
        result -= int(result / n); 
    return result; 



  
# Returns True if n is prime  
def isPrime( n):  
  
    # Corner cases  
    if (n <= 1): 
        return False
    if (n <= 3): 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop  
    if (n % 2 == 0 or n % 3 == 0): 
        return False
    i = 5
    while(i * i <= n): 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
  
def power( x, y, p):  
  
    res = 1 # Initialize result  
  
    x = x % p # Update x if it is more  
              # than or equal to p  
  
    while (y > 0):  
  
        # If y is odd, multiply x with result  
        if (y & 1): 
            res = (res * x) % p  
  
        # y must be even now  
        y = y >> 1 # y = y/2  
        x = (x * x) % p  
  
    return res  
  
# Utility function to store prime 
# factors of a number  
def findPrimefactors(s, n) : 
  
    # Print the number of 2s that divide n  
    while (n % 2 == 0) : 
        s.add(2)  
        n = n // 2
  
    # n must be odd at this po. So we can   
    # skip one element (Note i = i +2)  
    for i in range(3, int(sqrt(n)), 2): 
          
        # While i divides n, print i and divide n  
        while (n % i == 0) : 
  
            s.add(i)  
            n = n // i  
          
    # This condition is to handle the case  
    # when n is a prime number greater than 2  
    if (n > 2) : 
        s.add(n)  
  
# Function to find smallest primitive  
# root of n  
def findPrimitive( n) : 
    s = set()  
  
    # Check if n is prime or not  
    if (isPrime(n) == False):  
        return -1
  
    # Find value of Euler Totient function  
    # of n. Since n is a prime number, the  
    # value of Euler Totient function is n-1  
    # as there are n-1 relatively prime numbers. 
    phi = n - 1
  
    # Find prime factors of phi and store in a set  
    findPrimefactors(s, phi)  
  
    # Check for every number from 2 to phi  
    for r in range(2, phi + 1):  
  
        # Iterate through all prime factors of phi.  
        # and check if we found a power with value 1  
        flag = False
        for it in s:  
  
            # Check if r^((phi)/primefactors) 
            # mod n is 1 or not  
            if (power(r, phi // it, n) == 1):  
  
                flag = True
                break
              
        # If there was no power with value 1.  
        if (flag == False): 
            return r  
  
    # If no primitive root found  
    return -1
  

def is_prime(n, k=128):
    """ Test if a number is prime
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do
        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while int(r) & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(int(a), int(r), int(n))
        if x != 1 and x != n - 1:
            j = 1
            while int(j) < int(s) and x != n - 1:
                x = pow(int(x), 2, int(n))
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True
def generate_prime_candidate(length):
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    p = random.getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p
def generate_prime_number(length):
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in          bits
        return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p

def rabinMiller(n):
    s = n-1
    t = 0
    while((int(s)&1) == 0):
        s = s/2
        t +=1
    k = 0
    while(k<128):
        a = random.randrange(2,n-1)
        #a^s is computationally infeasible.  we need a more intelligent approach
        #v = (a**s)%n
        #python's core math module can do modular exponentiation
        v = pow(int(a),int(s),int(n)) #where values are (num,exp,mod)
        if v != 1:
            i=0
            while v != (n-1):
                if i == t-1:
                    return False
                else:
                    i = i+1
                    v = (v**2)%n
        k+=2
    return True


class CryptographyLib(FunctionLibraryBase):
    '''Cryptographic Primitives'''

    def __init__(self, packageName):
        super(CryptographyLib, self).__init__(packageName)
    
    @staticmethod
    @IMPLEMENT_NODE(returns=("IntPin", 0), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def generateLargePrime(k=('IntPin', 0)):
        return generate_prime_number(k)


    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", "", {PinSpecifires.CONSTRAINT: "1", PinSpecifires.SUPPORTED_DATA_TYPES: ["StringPin"]}), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def SHA256(inp=('StringPin', "")):
        return hashlib.sha256(inp.encode()).hexdigest()

    @staticmethod
    @IMPLEMENT_NODE(returns=("IntPin", 0, {PinSpecifires.CONSTRAINT: "1", PinSpecifires.SUPPORTED_DATA_TYPES: ["StringPin"]}), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def PrimitiveRoot(inp=('IntPin', 0)):
        return findPrimitive(inp)

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", "", {PinSpecifires.CONSTRAINT: "1", PinSpecifires.SUPPORTED_DATA_TYPES: ["StringPin"]}),nodeType= NodeTypes.Callable, meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def KeyGen():
        f = Fernet.generate_key()
        return f.decode("utf-8")

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""),nodeType= NodeTypes.Callable, meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def AES_Encrypt(key=('StringPin', ""), dataIn=('StringPin', "")):
        f = Fernet(key)
        rawb = bytes(dataIn, 'utf-8')
        token = f.encrypt(rawb)
        tokend = token.decode('utf-8')
        return tokend

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def AES_Decrypt(key=('StringPin', ""), token=('StringPin', "")):
        f = Fernet(key)
        tokenb = token.encode('utf-8')
        raw = f.decrypt(tokenb)
        rawd = raw.decode('utf-8')
        return rawd

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def ClientSend(message=('StringPin', ""), host=('StringPin', socket.gethostname())):
        #host = socket.gethostname()  # get local machine name
        port = 8080  # Make sure it's within the > 1024 $$ <65535 range
  
        s = socket.socket()
        s.connect((host, port))
        message = message.encode('utf-8')
        s.send(message)

        s.close()
        return "Sent"

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def ServerListen(host=('StringPin', socket.gethostname())):
        #host = socket.gethostname()   # get local machine name
        port = 8080  # Make sure it's within the > 1024 $$ <65535 range
  
        s = socket.socket()
        s.bind((host, port))
  
        s.listen(1)
        client_socket, addr = s.accept()
        data = client_socket.recv(1024).decode('utf-8')

        client_socket.close()
        return data