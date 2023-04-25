import socket
import nacl.secret
import nacl.utils
from nacl.public import PrivateKey, Box
import base64

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
    
    #msg = type + "\r\n" + "Name: " + name + "\r\n" + "PublicKey: " + pkey._public_key.hex() + "\r\n" + "\r\n"
    #print(msg)
    
    msg = type + "\r\n" + "Name: " + name + "\r\n" + "PublicKey: " + base64.b16encode(pkey._public_key).decode('ascii') + "\r\n" + "\r\n"
    print(msg)

    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        s.sendall(msg.encode())
        data = s.recv(1024)
        
    
        print(f"Received {data}")
        
    data_str = data.decode().split('\r\n')
    shafer_pkey = nacl.public.PublicKey(base64.b16decode(data_str[2][11:]))
    ctext = base64.b16decode(data_str[3][12:])
    
    print('ciphertext:\t',ctext)
    
    
    my_box = Box(skey, shafer_pkey)
    ptext = my_box.decrypt(ctext)
    print('plaintext:\t',ptext.decode('ascii'))
    
	
if __name__ == "__main__":
	main()