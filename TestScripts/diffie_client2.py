from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.serialization import PublicFormat, Encoding, load_der_public_key
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
import socket
import time
#grab published group parameters that can be used to generate diffie parameters! Grabbing from 
#a file to simulate the way these will be grabbed in pyflow. Might need to change later to a method 
#in another python file that returns variables to both client and server. 
def get_parameters():
	p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF

	g = 2

	return p,g

def generate_keys(p,g):
	diffie_nums = dh.DHParameterNumbers(p,g)
	key_gen_params = diffie_nums.parameters(default_backend())

	#generate private key
	client_private_key     = key_gen_params.generate_private_key()

	#generate public key and serialize to send (encode as DER)
	client_public_key = client_private_key.public_key().public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)

	#print(client_private_key)

	return client_private_key,client_public_key

def rsa_keys():
	RSAprivate_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
	)
	RSApublic_key = RSAprivate_key.public_key().public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)

	return RSAprivate_key, RSApublic_key


def do_exchange(client_private_key, client_public_key, RSAprivate_key, RSApublic_key):
	#define exchange on local host on high port number
	host = '127.0.0.1' 
	port = 65432 

	#RSAprivate_key,RSApublic_key = rsa_keys()  

	#tcp
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#connect to server
	s.connect((host, port))

	
	server_rsa_bytes= s.recv(8192)
	server_rsa_key = load_der_public_key(server_rsa_bytes, default_backend())
	
	#recieve the severs's public key
	
	server_signed_public_key = s.recv(8192)
	server_signed_public_key = server_signed_public_key.split(b"&&&&&")
	signature= server_signed_public_key[0]
	server_key = server_signed_public_key[1]
	#server_key_deserialized = load_der_public_key(server_key, default_backend())

	try:
		server_rsa_key.verify(signature, server_key,
			padding.PSS(
				mgf=padding.MGF1(hashes.SHA256()),
				salt_length=padding.PSS.MAX_LENGTH
				),
			hashes.SHA256()
			)
	except:
		exit()



	#print("Got server public key: " + str(server_public_key))
	

	s.send(RSApublic_key)

	public_signed_key = RSAprivate_key.sign(client_public_key, 
			padding.PSS(
				mgf=padding.MGF1(hashes.SHA256()),
				salt_length=padding.PSS.MAX_LENGTH
				),
			hashes.SHA256()
			)

	s.send(public_signed_key + b"&&&&&" + client_public_key)
	
	#deserialize the server's key after transmission, so it is usable to generate shared key
	server_public_key = load_der_public_key(server_key, default_backend())

	#send the client public key to the server
	#s.send(len(client_public_key).to_bytes(2, "big") + client_public_key)


	#generate the shared key with server's public key and clients's private key
	shared_key = client_private_key.exchange(server_public_key)

	return shared_key


def main():
	p,g = get_parameters()

	priv, pub = generate_keys(p,g)
	RSApriv_key,RSApub_key = rsa_keys()
	count = 0

	time_start= time.time()
	for i in range(1000):
		try:
			shared_key = do_exchange(priv, pub, RSApriv_key, RSApub_key)
			time.sleep(0.01)
			print(shared_key)
		except:
			print('error found')
			count +=1
	time_end = time.time()

	print(time_end-time_start)
	print(count)


main()
