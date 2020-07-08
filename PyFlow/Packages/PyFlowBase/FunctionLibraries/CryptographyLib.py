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
from Cryptodome.Util import number
from decimal import Decimal

def prime(N):
    q = number.getPrime(N)
    return q

def getq(q):
    p = (2*q) + 1
    return p

import random
 
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

class CryptographyLib(FunctionLibraryBase):
    '''Cryptographic Primitives'''

    def __init__(self, packageName):
        super(CryptographyLib, self).__init__(packageName)
    
    @staticmethod
    @IMPLEMENT_NODE(returns=("IntPin", 0), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def generateLargePrime(k=('IntPin', 0)):
        return number.getPrime(k)

    @staticmethod
    @IMPLEMENT_NODE(returns=('IntPin', 0.0), meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def power(x=('IntPin', 0.0), y=('IntPin', 0.0), result=(REF, ('BoolPin', False))):
        '''Return `x` raised to the power `y`.'''
        try:
            result(True)
            return int(math.pow(x, y))
        except:
            result(False)
            return -1


    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", "", {PinSpecifires.CONSTRAINT: "1", PinSpecifires.SUPPORTED_DATA_TYPES: ["StringPin"]}), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def SHA256(inp=('StringPin', "")):
        return hashlib.sha256(inp.encode()).hexdigest()


    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", 0), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def findpq(n=('IntPin', 0)):
        done = False
        while not done:
            p = prime(n)
            q = getq(p)
            if(rabin(q)):
                done = True

        stringVersion = str(p) + "," + str(q)
        return stringVersion

    @staticmethod
    @IMPLEMENT_NODE(returns=("IntPin", 0), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def getItem(item=('StringPin', ""), index=('IntPin', 0)):
        listItems= item.split(',')
        return int(listItems[index])


    @staticmethod
    @IMPLEMENT_NODE(returns=("IntPin", 0), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def generateLargePrime(k=('IntPin', 0)):
        return number.getPrime(k)

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