from PyFlow.Core import(
    FunctionLibraryBase,
    IMPLEMENT_NODE
)
from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
import hashlib
from cryptography.fernet import Fernet
import socket
    
class CryptographyLib(FunctionLibraryBase):
    '''Cryptographic Primitives'''

    def __init__(self, packageName):
        super(CryptographyLib, self).__init__(packageName)
        
    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", "", {PinSpecifires.CONSTRAINT: "1", PinSpecifires.SUPPORTED_DATA_TYPES: ["StringPin"]}), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic Primitives', NodeMeta.KEYWORDS: []})
    def SHA256(inp=('StringPin', "")):
        return hashlib.sha256(inp.encode()).hexdigest()

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", "", {PinSpecifires.CONSTRAINT: "1", PinSpecifires.SUPPORTED_DATA_TYPES: ["StringPin"]}),nodeType= NodeTypes.Callable, meta={NodeMeta.CATEGORY: 'Cryptographic Primitives', NodeMeta.KEYWORDS: []})
    def KeyGen():
        f = Fernet.generate_key()
        return f.decode("utf-8")

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""),nodeType= NodeTypes.Callable, meta={NodeMeta.CATEGORY: 'Cryptographic Primitives', NodeMeta.KEYWORDS: []})
    def AES_Encrypt(key=('StringPin', ""), dataIn=('StringPin', "")):
        f = Fernet(key)
        rawb = bytes(dataIn, 'utf-8')
        token = f.encrypt(rawb)
        tokend = token.decode('utf-8')
        return tokend

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic Primitives', NodeMeta.KEYWORDS: []})
    def AES_Decrypt(key=('StringPin', ""), token=('StringPin', "")):
        f = Fernet(key)
        tokenb = token.encode('utf-8')
        raw = f.decrypt(tokenb)
        rawd = raw.decode('utf-8')
        return rawd

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic Primitives', NodeMeta.KEYWORDS: []})
    def ClientSend(message=('StringPin', "")):
        host = socket.gethostname()  # get local machine name
        port = 8080  # Make sure it's within the > 1024 $$ <65535 range
  
        s = socket.socket()
        s.connect((host, port))
  
        s.send(message.encode('utf-8'))

        s.close()
        return "Sent"

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""), nodeType= NodeTypes.Callable,meta={NodeMeta.CATEGORY: 'Cryptographic Primitives', NodeMeta.KEYWORDS: []})
    def ServerListen():
        host = socket.gethostname()   # get local machine name
        port = 8080  # Make sure it's within the > 1024 $$ <65535 range
  
        s = socket.socket()
        s.bind((host, port))
  
        s.listen(1)
        client_socket, addr = s.accept()
        data = client_socket.recv(1024).decode('utf-8')

        client_socket.close()
        return data
