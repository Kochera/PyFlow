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
	client_private_key     = key_gen_params.generate_private_key()

	#generate public key and serialize to send (encode as DER)
	client_public_key = client_private_key.public_key().public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)

	return client_private_key,client_public_key


def do_exchange(client_private_key, client_public_key):
	#define exchange on local host on high port number
	host = '127.0.0.1' 
	port = 65432   

	#tcp
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#connect to server
	s.connect((host, port))
	
	#recieve the severs's public key
	length_of_msg = s.recv(2)
	server_public_key = s.recv(int.from_bytes(length_of_msg, "big"))

	print("Got server public key: " + str(server_public_key))
	
	#deserialize the server's key after transmission, so it is usable to generate shared key
	server_public_key = load_der_public_key(server_public_key, default_backend())

	#send the client public key to the server
	s.send(len(client_public_key).to_bytes(2, "big") + client_public_key)


	#generate the shared key with server's public key and clients's private key
	shared_key = client_private_key.exchange(server_public_key)

	return shared_key

def main():
	p,g = get_parameters()

	priv, pub = generate_keys(p,g)

	shared_key = do_exchange(priv, pub)

	print("Shared_Key: ", shared_key)

main()


