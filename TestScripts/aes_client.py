import os
from cryptography.hazmat.primitives.ciphers.aead import AESCCM
import socket


def aesc(key):
	aesccm=AESCCM(key)
	return aesccm


def send_encrypted_message():
	#define exchange on local host on high port number
	host = '127.0.0.1' 
	port = 65432   

	#tcp
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#connect to server
	s.connect((host, port))
	
	#recieve the private key
	private_key = s.recv(8192)

	print("got the private key!!!" + str(private_key))

	aes=aesc(private_key)

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

send_encrypted_message()