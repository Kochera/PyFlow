from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.serialization import PublicFormat, Encoding, load_der_public_key
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
	server_private_key = key_gen_params.generate_private_key()

	#generate public key and serialize to send (encode as DER)
	server_public_key = server_private_key.public_key().public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)

	return server_private_key, server_public_key

def do_exchange(server_private_key, server_public_key):
	#define exchange on local host on high port number
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

		#send the server public key to the client
		clientsocket.send(len(server_public_key).to_bytes(2, "big") + server_public_key)

		#recieve the client's public key
		length_of_msg = clientsocket.recv(2)
		client_public_key = clientsocket.recv(int.from_bytes(length_of_msg, "big"))

		print("Got client public key: " + str(client_public_key))

		#decerialize the clients key after transmission, so it is usable to generate shared key
		client_public_key = load_der_public_key(client_public_key, default_backend())

		#close the connection
		clientsocket.close()
		break

	shared_key = server_private_key.exchange(client_public_key)


	return shared_key

#run all functions in main method 
def main():
	p,g = get_parameters()

	priv, pub = generate_keys(p,g)

	shared_key = do_exchange(priv, pub)

	print("Shared_Key: ", shared_key)

main()
