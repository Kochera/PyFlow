from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.serialization import PublicFormat, Encoding, load_der_public_key
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
import os
from cryptography.hazmat.primitives.ciphers.aead import AESCCM
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
import socket

#grab published group parameters that can be used to generate diffie parameters! Grabbing from 
#a file to simulate the way these will be grabbed in pyflow. Might need to change later to a method 
#in another python file that returns variables to both client and server. 
def get_parameters():
	p = 0
	g = 0 
	file = ''
	try:
		file = open("parameters.txt","r")
		parameters = file.read()
		file.close()
		parameters = parameters.split()
		p = parameters[0]
		g = parameters[1]

	except:
	    print("file not found")

	p = int(p, 16)
	g = int(g)

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


def do_exchange(client_private_key, client_public_key):
	#define exchange on local host on high port number
	host = '127.0.0.1' 
	port = 65432 

	RSAprivate_key,RSApublic_key = rsa_keys()  

	#tcp
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#connect to server
	s.connect((host, port))

	
	server_rsa_bytes= s.recv(8192)
	print("recieving servers public key: " + str(server_rsa_bytes))
	server_rsa_key = load_der_public_key(server_rsa_bytes, default_backend())
	
	#recieve the severs's public key
	
	server_signed_public_key = s.recv(8192)
	server_signed_public_key = server_signed_public_key.split(b"&&&&&")
	print("recieving servers signed public key and key: " +str(server_signed_public_key))
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
	
	print("client sending public key: " + str(RSApublic_key))
	s.send(RSApublic_key)

	public_signed_key = RSAprivate_key.sign(client_public_key, 
			padding.PSS(
				mgf=padding.MGF1(hashes.SHA256()),
				salt_length=padding.PSS.MAX_LENGTH
				),
			hashes.SHA256()
			)

	print("client sending signed public key and key: " + str(public_signed_key) + "&&&&&" + str(client_public_key))
	s.send(public_signed_key + b"&&&&&" + client_public_key)
	
	#deserialize the server's key after transmission, so it is usable to generate shared key
	server_public_key = load_der_public_key(server_key, default_backend())

	#send the client public key to the server
	#s.send(len(client_public_key).to_bytes(2, "big") + client_public_key)


	#generate the shared key with server's public key and clients's private key
	shared_key = client_private_key.exchange(server_public_key)

	derived_key = sha_256(shared_key)

	aes=aesc(derived_key)

	aad=b"Associated data"
	nonce = os.urandom(13)
	print()
	print("nonce: " + str(nonce))
	message= b"hello world"
	ct = aes.encrypt(nonce, message, aad)
	#send the client public key to the server
	s.send(nonce + b"&&&&" + ct + b"&&&&" + aad)

	#return shared_key


def sha_256(key):
	derived_key = HKDF(
		algorithm=hashes.SHA256(),
		length=32,
		salt=None,
		info=b'handshake data',
		backend = default_backend()
		).derive(key)
	return derived_key

def aesc(key):
	aesccm=AESCCM(key)
	return aesccm


def send_encrypted_message(key):
	#define exchange on local host on high port number
	host = '127.0.0.1' 
	port = 65431

	#tcp
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#connect to server
	booli = True
	while booli == True:
		try:
			s.connect((host, port))
			booli = False
		except:
			print("host not set up yet")

	
	#recieve the private key
	#private_key = s.recv(8192)

	#print("got the private key!!!" + str(private_key))

	aes=aesc(key)

	aad=b"Associated data"
	nonce = os.urandom(13)
	print()
	print("nonce: " + str(nonce))
	message= b"hello world"
	ct = aes.encrypt(nonce, message, aad)
	#send the client public key to the server
	s.send(nonce + b"&&&&" + ct + b"&&&&" + aad)


	#generate the shared key with server's public key and clients's private key
	s.close()


def main():
	p,g = get_parameters()

	priv, pub = generate_keys(p,g)

	do_exchange(priv, pub)

	
	#print("Shared_Key: ", shared_key)
	#derived_key = sha_256(shared_key)

	#print("derived key: ", derived_key)

	#send_encrypted_message(derived_key)

main()


