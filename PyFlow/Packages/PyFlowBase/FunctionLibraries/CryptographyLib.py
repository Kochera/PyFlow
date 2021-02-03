from PyFlow.Core import(
    FunctionLibraryBase,
    IMPLEMENT_NODE
)
from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
import hashlib
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
from codecs import encode
from cryptography.hazmat.primitives.ciphers.aead import AESCCM
import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes




def revert_to_bytes(string_item):
    string_item = string_item[2:len(string_item)-1]

    string_item = bytes(string_item, encoding='utf-8')
        
    string_item=string_item.decode('unicode-escape').encode('ISO-8859-1')

    return string_item


def get_parameters():
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



#For Diffie-Hellman Key exchange
p,g = get_parameters()
private_key, public_key = generate_keys(p,g)

#For default AES key if not provided one
default_AES = str(AESCCM.generate_key(bit_length=128))


#For RSA Signature
RSAprivate_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
RSApublic_key = RSAprivate_key.public_key().public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)



    	
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
    @IMPLEMENT_NODE(returns=("StringPin", ""), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def RSAPublicKey():
        return RSApublic_key

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""),nodeType= NodeTypes.Callable, meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def RSA_sign(message=('StringPin', "")):
        data = bytes(message, 'utf-8')
        signature = RSAprivate_key.sign(
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return str(signature)

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""),nodeType= NodeTypes.Callable, meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def RSA_verify(signature=('StringPin', ""), sent_RSA_public=('StringPin', ""), message = ('StringPin', "")):
        signature = revert_to_bytes(signature)
        sent_RSA_public = revert_to_bytes(sent_RSA_public)
        pub = load_der_public_key(sent_RSA_public, default_backend())
        data = bytes(message, 'utf-8')
        try:
            pub.verify(
                signature,
                data,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return "Correct Signature"
        except:
            return "Incorrect Signature"


    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""),nodeType= NodeTypes.Callable, meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def AESccm_Encrypt(key=('StringPin', default_AES), dataIn=('StringPin', "")):
        key = revert_to_bytes(key)
        aad = b"Associated Data"

        aesccm = AESCCM(key)
        nonce = os.urandom(13)
        data_bytes = bytes(dataIn, 'utf-8')
        ct = aesccm.encrypt(nonce, data_bytes, aad)
        
        return str(ct)+","+str(nonce)+","+str(aad)

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def AESccm_Decrypt(key=('StringPin', default_AES), token=('StringPin', "")):
        key = revert_to_bytes(key)

        aesccm = AESCCM(key)
        list_token = token.split(',')
        ct = revert_to_bytes(list_token[0])
        nonce = revert_to_bytes(list_token[1])
        aad = revert_to_bytes(list_token[2])



        return str(aesccm.decrypt(nonce,ct,aad))

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
        data = client_socket.recv(4096).decode('utf-8')

        client_socket.close()
        return data


    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def PublicKey():
    	return public_key

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def Exchange(sent_public_key=('StringPin', "")):
        key= revert_to_bytes(sent_public_key)

        #sent_public_key = sent_public_key[2:len(sent_public_key)-1]

        #key = bytes(sent_public_key, encoding='utf-8')
        
        #key=key.decode('unicode-escape').encode('ISO-8859-1')


        pub = load_der_public_key(key, default_backend())

        shared_key = private_key.exchange(pub)

        return shared_key
