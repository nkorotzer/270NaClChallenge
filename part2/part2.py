import nacl.secret
import nacl.utils


def main():
	with open('part2.key.bin',"rb") as keyFile, open('part2.ciphertext.bin',"rb") as ctFile:
		key = keyFile.read()
		ct = ctFile.read()

	box = nacl.secret.SecretBox(key)
	pt = box.decrypt(ct)
	print(pt)
	
if __name__ == "__main__":
	main()