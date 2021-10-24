from Crypto.Cipher import AES
from challenge1 import *

BLOCK_SIZE = 16

def fixedXOR(byte1, byte2):
	xorResult = []
	for b1, b2 in zip(byte1, byte2):
		xorResult.append(b1^b2)
	
	return bytes(xorResult)

def AES_CBC_block_encrypt(block, nonce, key, padding):
	if(len(block) != len(nonce)):
		padding = bytes([len(nonce) - len(block)]) if padding != b'\x00' else padding
		block = block + (len(nonce) - len(block)) * padding

	processedBlock = fixedXOR(block, nonce)
	cipher = AES.new(key, AES.MODE_ECB)
	return cipher.encrypt(processedBlock)

def AES_CBC_encrypt(plainText, initialVector, key, padding=b'\x00'):
	cipherText = b""
	nonce = initialVector
	for i in range(0, len(plainText), BLOCK_SIZE):
		block = plainText[i:i+BLOCK_SIZE]
		nonce = AES_CBC_block_encrypt(block, nonce, key, padding)
		cipherText += nonce
	return cipherText

def AES_CBC_block_decrypt(cipherBlock, nonce, key):
	cipher = AES.new(key, AES.MODE_ECB)
	processedPlainBlock = cipher.decrypt(cipherBlock)
	return fixedXOR(processedPlainBlock, nonce)

def AES_CBC_decrypt(cipherText, initialVector, key):
	plainText = b''
	nonce = initialVector
	for i in range(0, len(cipherText), BLOCK_SIZE):
		cipherBlock = cipherText[i: i+BLOCK_SIZE]
		if(len(cipherBlock) == BLOCK_SIZE):
			plainText += AES_CBC_block_decrypt(cipherBlock, nonce, key)
		nonce = cipherBlock
	return plainText

if __name__ == "__main__":
	with open("10.txt", "r") as f:
		input = f.read()

	cipherText = base64ToBytes(input)
	print(AES_CBC_decrypt(cipherText, b'\x00'*16, b'YELLOW SUBMARINE').decode())
	
	# with open("set1/alice.txt", "r") as f:
	# 	input = f.read()

	# cipherText = AES_CBC_encrypt(input.encode(), b'\x00'*16, b'YELLOW SUBMARINE')
	# print(cipherText)

	# plainText = AES_CBC_decrypt(cipherText, b'\x00'*16, b'YELLOW SUBMARINE')
	# print(plainText)


	