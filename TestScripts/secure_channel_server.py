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
import sys

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
	server_private_key = key_gen_params.generate_private_key()

	#generate public key and serialize to send (encode as DER)
	server_public_key = server_private_key.public_key().public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)

	#print(server_private_key)

	return server_private_key, server_public_key

def rsa_keys():
	RSAprivate_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
	)
	RSApublic_key = RSAprivate_key.public_key().public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)

	return RSAprivate_key, RSApublic_key

def do_exchange(server_private_key, server_public_key):
	#define exchange on local host on high port number
	host = '127.0.0.1'   
	port = 65432

	RSAprivate_key,RSApublic_key = rsa_keys() 

	#TCP    
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))

	s.listen(1)

	while True:

		#accept connection from client
		clientsocket,address = s.accept()
		print(f"Connection from {address} has been established.")

		print("server sending public key: " + str(RSApublic_key))
		clientsocket.send(RSApublic_key)

		public_signed_key = RSAprivate_key.sign(server_public_key, 
			padding.PSS(
				mgf=padding.MGF1(hashes.SHA256()),
				salt_length=padding.PSS.MAX_LENGTH
				),
			hashes.SHA256()
			)

		#send the server public key to the client
		print("server sending signed public key and key: " + str(public_signed_key) + "&&&&&" + str(server_public_key))
		clientsocket.send(public_signed_key + b"&&&&&" + server_public_key)

		#recieve the client's public key

		
		client_rsa_bytes = clientsocket.recv(8192)
		print("recieving clients public key: " + str(client_rsa_bytes))
		client_rsa_key = load_der_public_key(client_rsa_bytes, default_backend())



		client_signed_public_key = clientsocket.recv(8192)
		print("recieving clients signed public key and key: " + str(client_signed_public_key))
		client_signed_public_key = client_signed_public_key.split(b"&&&&&")
		signature= client_signed_public_key[0]
		client_key = client_signed_public_key[1]

		try:
			client_rsa_key.verify(signature, client_key,
				padding.PSS(
					mgf=padding.MGF1(hashes.SHA256()),
					salt_length=padding.PSS.MAX_LENGTH
					),
				hashes.SHA256()
				)
		except:
			exit()

		

		#print("Got client public key: " + str(client_key))

		#deserialize the clients key after transmission, so it is usable to generate shared key
		client_public_key = load_der_public_key(client_key, default_backend())


	#generate the shared key with client's public key and server's private key
		shared_key = server_private_key.exchange(client_public_key)


		derived_key = sha_256(shared_key)

		aes = aesc(derived_key)

		ct = clientsocket.recv(8192)

		print("Got client cipher text: " + str(ct))

		print(type(ct))
		
		cipher = ct.split(b"&&&&")
		print(cipher)

		ciphertext = cipher[0]
		nonce = cipher[1]
		print(nonce)
		aad=bytes(cipher[2])

		message = aes.decrypt(ciphertext,nonce,aad)

		print(message)

		clientsocket.close()
		break

	#generate the shared key with client's public key and server's private key
	


	

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
	aesccm = AESCCM(key)
	return aesccm

def recieve_encrypted_message(key):
	host = '127.0.0.1'   
	port = 65431

	#TCP    
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))

	s.listen(1)

	while True:

		#accept connection from client
		clientsocket,address = s.accept()
		print(f"Connection from {address} has been established.")

		aes= aesc(key)
		
		

		#recieve the client's public key
		
		ct = clientsocket.recv(8192)

		print("Got client cipher text: " + str(ct))

		print(type(ct))
		
		cipher = ct.split(b"&&&&")
		print(cipher)

		ciphertext = cipher[0]
		nonce = cipher[1]
		print(nonce)
		aad=bytes(cipher[2])

		message = aes.decrypt(ciphertext,nonce,aad)

		print(message)

		#deserialize the clients key after transmission, so it is usable to generate shared key
		#message= aes.decrypt()

		#close the connection
		#clientsocket.close()
		break
		

#run all functions in main method 
def main():
	p,g = get_parameters()

	priv, pub = generate_keys(p,g)

	do_exchange(priv, pub)

	#print("Shared_Key: ", shared_key)

	#derived_key = sha_256(shared_key)

	#print("derived_key: ", shared_key)

	#recieve_encrypted_message(derived_key)

main()
