
from set1.challenge1 import base64ToBytes
from set1.challenge11 import KEY_SIZE

import random
import os
from Crypto.Cipher import AES
from Crypto.Util import Padding

KEY_SIZE = 16

def encryption_oracle(plainText):
	AES_Key = os.urandom(KEY_SIZE)
	print(f"AES key generated: {AES_Key}")

	plainText = plainText + base64ToBytes('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')

	cipher = AES.new(AES_Key, AES.MODE_ECB)
	return cipher.encrypt(Padding.pad(plainText, 16))