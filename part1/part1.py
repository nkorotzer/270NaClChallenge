def xor_bytes(ba1, ba2):
    return bytes(byte_a ^ byte_b for byte_a, byte_b in zip(ba1, ba2))

def main():
    with open('part1.ciphertext.bin','rb') as ciphertextFile, open('part1.otp.bin','rb') as otpFile:
        ct = ciphertextFile.read()
        #print(len(ct))
        
        otp = otpFile.read()
        #print(len(otp))
        
        result = xor_bytes(ct, otp)
        print(result)
	
	
if __name__ == "__main__":
	main()