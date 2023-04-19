import socket
import nacl.secret
import nacl.utils
from nacl.public import PrivateKey, Box

###CRYPTO 1.0 REQUEST\r\n
###Name: Your Name\r\n
###PublicKey: <Base16 string of your public key>\r\n
###\r\n


def main():
    HOST = "cyberlab.pacific.edu"
    PORT = 12001
    
    type = "CRYPTO 1.0 REQUEST"
    name = "Nick Korotzer"
    skey = PrivateKey.generate()
    pkey = skey.public_key
    
    msg = type + "\r\n" + "Name: " + name + "\r\n" + "PublicKey: " + pkey._public_key.hex() + "\r\n" + "\r\n"
    
    while(True):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST,PORT))
            s.sendall(msg.encode())
            data = s.recv(1024)
            
        
            print(f"Received {data}")
	
if __name__ == "__main__":
	main()