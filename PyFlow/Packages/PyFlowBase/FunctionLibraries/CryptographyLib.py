from PyFlow.Core import(
    FunctionLibraryBase,
    IMPLEMENT_NODE
)
from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
import socket
import random
from Cryptodome.Util import number
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.serialization import PublicFormat, Encoding, load_der_public_key, load_der_private_key, PrivateFormat
from codecs import encode
from cryptography.hazmat.primitives.ciphers.aead import AESCCM
import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
import time



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
    @IMPLEMENT_NODE(returns=("StringPin", "", {PinSpecifires.CONSTRAINT: "1", PinSpecifires.SUPPORTED_DATA_TYPES: ["StringPin"]}), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Hashing', NodeMeta.KEYWORDS: []})
    def SHA_256(inp=('StringPin', "")):
        derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data',
        backend = default_backend()
        ).derive(revert_to_bytes(inp))

        return derived_key


    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", "", {PinSpecifires.CONSTRAINT: "1", PinSpecifires.SUPPORTED_DATA_TYPES: ["StringPin"]}), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Hashing', NodeMeta.KEYWORDS: []})
    def SHA_384(inp=('StringPin', "")):
        derived_key = HKDF(
        algorithm=hashes.SHA384(),
        length=32,
        salt=None,
        info=b'handshake data',
        backend = default_backend()
        ).derive(revert_to_bytes(inp))

        return derived_key

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", "", {PinSpecifires.CONSTRAINT: "1", PinSpecifires.SUPPORTED_DATA_TYPES: ["StringPin"]}), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Hashing', NodeMeta.KEYWORDS: []})
    def SHA_512(inp=('StringPin', "")):
        derived_key = HKDF(
        algorithm=hashes.SHA512(),
        length=32,
        salt=None,
        info=b'handshake data',
        backend = default_backend()
        ).derive(revert_to_bytes(inp))

        return derived_key

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
    @IMPLEMENT_NODE(returns=("FloatPin", 0), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def get_time():
        start = time.time()
        return start

    @staticmethod
    @IMPLEMENT_NODE(returns=("IntPin", 0, {PinSpecifires.CONSTRAINT: "1", PinSpecifires.SUPPORTED_DATA_TYPES: ["StringPin"]}), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic_Primitives', NodeMeta.KEYWORDS: []})
    def PrimitiveRoot(inp=('IntPin', 0)):
        return findPrimitive(inp)

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'RSA', NodeMeta.KEYWORDS: []})
    def RSAPublicKey():
        return RSApublic_key

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'RSA', NodeMeta.KEYWORDS: []})
    def GetMessageFromeSignature(signature=('StringPin', "")):
        info_list = signature.split("&&&&&&&")
        message = info_list[1]
        return str(message)

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""),nodeType= NodeTypes.Callable, meta={NodeMeta.CATEGORY: 'RSA', NodeMeta.KEYWORDS: []})
    def RSA_sign(message=('StringPin', "")):
        data = revert_to_bytes(message)
        signature = RSAprivate_key.sign(
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return str(signature)+ "&&&&&&&" + str(data)

    @staticmethod
    @IMPLEMENT_NODE(returns=("BoolPin", ""),nodeType= NodeTypes.Callable, meta={NodeMeta.CATEGORY: 'RSA', NodeMeta.KEYWORDS: []})
    def RSA_verify(signature=('StringPin', ""), sent_RSA_public=('StringPin', "")):
        info_list = signature.split('&&&&&&&')
        sign = info_list[0]
        message = info_list[1]
        sign_bytes = revert_to_bytes(sign)
        sent_RSA_public_bytes = revert_to_bytes(sent_RSA_public)
        pub = load_der_public_key(sent_RSA_public_bytes, default_backend())
        data = revert_to_bytes(message)
        try:
            pub.verify(
                sign_bytes,
                data,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except:
            return False


    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""),nodeType= NodeTypes.Callable, meta={NodeMeta.CATEGORY: 'AES', NodeMeta.KEYWORDS: []})
    def AESccm_Encrypt(key=('StringPin', default_AES), dataIn=('StringPin', "")):
        key = revert_to_bytes(key)
        aad = b"Associated Data"

        aesccm = AESCCM(key)
        nonce = os.urandom(13)
        data_bytes = bytes(dataIn, 'utf-8')
        ct = aesccm.encrypt(nonce, data_bytes, aad)
        
        return str(ct)+"&&&&"+str(nonce)+"&&&&"+str(aad)

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'AES', NodeMeta.KEYWORDS: []})
    def AESccm_Decrypt(key=('StringPin', default_AES), token=('StringPin', "")):
        key = revert_to_bytes(key)

        aesccm = AESCCM(key)
        list_token = token.split('&&&&')
        ct = revert_to_bytes(list_token[0])
        nonce = revert_to_bytes(list_token[1])
        aad = revert_to_bytes(list_token[2])



        return str(aesccm.decrypt(nonce,ct,aad))

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Communication', NodeMeta.KEYWORDS: []})
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
    @IMPLEMENT_NODE(returns=("StringPin", ""), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Communication', NodeMeta.KEYWORDS: []})
    def ServerListen(host=('StringPin', socket.gethostname())):
        #host = socket.gethostname()   # get local machine name
        port = 8080  # Make sure it's within the > 1024 $$ <65535 range
  
        s = socket.socket()
        s.bind((host, port))
  
        s.listen(1)
        client_socket, addr = s.accept()
        data = client_socket.recv(8192).decode('utf-8')

        client_socket.close()
        return data


    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Diffie-Building-Blocks', NodeMeta.KEYWORDS: []})
    def PublicKey():
    	return public_key

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Diffie-Building-Blocks', NodeMeta.KEYWORDS: []})
    def Exchange(sent_public_key=('StringPin', "")):
        key= revert_to_bytes(sent_public_key)

        #sent_public_key = sent_public_key[2:len(sent_public_key)-1]

        #key = bytes(sent_public_key, encoding='utf-8')
        
        #key=key.decode('unicode-escape').encode('ISO-8859-1')


        pub = load_der_public_key(key, default_backend())

        shared_key = private_key.exchange(pub)

        return shared_key
