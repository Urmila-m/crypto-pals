from Crypto.Cipher import AES
from challenge1 import *

key = b'YELLOW SUBMARINE'
cipher = AES.new(key, AES.MODE_ECB)

# initialization vector, not required in ECB mode->Electric Code Book Mode
# nonce = cipher.nonce

with open("set1/7.txt", "r") as f:
	input = f.read()

cipherText = base64ToBytes(input)
# the cipher should have length as a multiple of 16(AES-128), if not, add padding Crypto.Util.Padding
plainText = cipher.decrypt(cipherText)
print(plainText.decode())

