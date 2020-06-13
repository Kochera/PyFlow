from PyFlow.Core import(
    FunctionLibraryBase,
    IMPLEMENT_NODE
)
from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
import hashlib
from cryptography.fernet import Fernet
    
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