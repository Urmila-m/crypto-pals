from challenge1 import *

def fixedXOR(byte1, byte2):
	# ^ operator is used for bitwise XOR
	# chr() function returns string character from its ASCII value
	# encode converts the string to bytes type
	return "".join([chr(_byte1 ^ _byte2) for _byte1, _byte2 in zip(byte1, byte2)]).encode()

if __name__ == "__main__":
	print(bytesToHex(fixedXOR(hexToBytes("1c0111001f010100061a024b53535009181c"), hexToBytes("686974207468652062756c6c277320657965"))))
