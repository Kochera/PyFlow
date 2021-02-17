import os
from cryptography.hazmat.primitives.ciphers.aead import AESCCM
import socket

def aesc():
	key = AESCCM.generate_key(bit_length=256)
	aesccm = AESCCM(key)
	return aesccm, key

def recieve_encrypted_message():
	host = '127.0.0.1'   
	port = 65432

	#TCP    
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))

	s.listen(1)

	while True:

		#accept connection from client
		clientsocket,address = s.accept()
		print(f"Connection from {address} has been established.")

		aes,key= aesc()
		
		clientsocket.send(key)

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

recieve_encrypted_message()		
