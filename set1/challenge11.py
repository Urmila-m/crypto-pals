from challenge10 import *
import os
import random
from Crypto.Cipher import AES
from Crypto.Util import Padding

KEY_SIZE = 16

def encryption_oracle(plainText):
	AES_Key = os.urandom(KEY_SIZE)
	print(f"AES key generated: {AES_Key}")

	noOfBytesToAppend = random.randint(5, 10)
	randomBytesToAppend = os.urandom(noOfBytesToAppend)
	print(f"Random appending bytes: {randomBytesToAppend}")
	plainText = randomBytesToAppend + plainText + randomBytesToAppend

	modes = { 0: 'ECB', 1: 'CBC'}
	selectedMode = modes[random.randint(0, 1)]
	print(f"Selected mode: {selectedMode}")

	if selectedMode == 'ECB':
		cipher = AES.new(AES_Key, AES.MODE_ECB)
		return cipher.encrypt(Padding.pad(plainText, BLOCK_SIZE))
	else:
		initialVector = os.urandom(KEY_SIZE)
		return AES_CBC_encrypt(plainText, initialVector, AES_Key)

def detectEncryptionMode(cipherText):
	blocks = []
	for i in range(0, len(cipherText), BLOCK_SIZE):
		blocks.append(cipherText[i:i+BLOCK_SIZE])
	
	if len(blocks) != len(set(blocks)):
		return 'ECB'

	else:
		return 'CBC'

if __name__ == "__main__":
	
	plainText = b'a' * 60

	cipherText = encryption_oracle(plainText)
	print(detectEncryptionMode(cipherText))
	




