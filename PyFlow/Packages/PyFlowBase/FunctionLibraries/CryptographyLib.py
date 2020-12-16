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
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.serialization import PublicFormat, Encoding, load_der_public_key, load_der_private_key, PrivateFormat

# def prime(N):
#     q = number.getPrime(N)
#     return q

# def getq(q):
#     p = (2*q) + 1
#     return p

# import random
 
# def rabin(n):
#     """
#     Miller-Rabin primality test.
 
#     A return value of False means n is certainly not prime. A return value of
#     True means n is very likely a prime.
#     """
#     if n!=int(n):
#         return False
#     n=int(n)
#     #Miller-Rabin test for prime
#     if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
#         return False
 
#     if n==2 or n==3 or n==5 or n==7:
#         return True
#     s = 0
#     d = n-1
#     while d%2==0:
#         d>>=1
#         s+=1
#     assert(2**s * d == n-1)
 
#     def trial_composite(a):
#         if pow(a, d, n) == 1:
#             return False
#         for i in range(s):
#             if pow(a, 2**i * d, n) == n-1:
#                 return False
#         return True  
 
#     for i in range(8):#number of trials 
#         a = random.randrange(2, n)
#         if trial_composite(a):
#             return False
 
#     return True

def get_parameters():
	# p = 0
	# g = 0 
	# file = ''
	# try:
	# 	file = open("../../../parameters.txt", "r")
	# 	parameters = file.read()
	# 	file.close()
	# 	parameters= parameters.split()
	# 	p = parameters[0]
	# 	g = parameters[1]

	# except:
	# 	print("file not found")

	p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF


	g = 2
	return p,g

def generate_keys(p,g):
	diffie_nums = dh.DHParameterNumbers(p,g)
	key_gen_params = diffie_nums.parameters(default_backend())

#generate private key
	private_key     = key_gen_params.generate_private_key()

#generate public key and serialize to send (encode as DER)
	public_key = private_key.public_key().public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)

	return private_key,public_key


p,g = get_parameters()
private_key, public_key = generate_keys(p,g)



    	
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
        # port = 8080  # Make sure it's within the > 1024 $$ <65535 range
  		
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


    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def PublicKey():

    	return public_key
        #host = socket.gethostname()  # get local machine name

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def DiffieHellman(sent_public_key=('StringPin', "")):

    	#print("printing the public key: ", sent_public_key)

    	sent_public_key = sent_public_key[2:len(sent_public_key)-1]
    	key = bytes(sent_public_key, encoding='utf-8')

    	key=key.decode('unicode-escape').encode('ISO-8859-1')



    	#print("helloooooo")

    	pub = load_der_public_key(key, default_backend())

    	print("printing the key after loading it: ", pub)
    	print(pub)
    	shared_key = private_key.exchange(pub)

    	print("checking this out mofo")

    	print(shared_key)

    	return shared_key
        #host = socket.gethostname()  # get local machine name
