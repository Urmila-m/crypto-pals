import random
import os
import math

from Crypto.Cipher import AES
from Crypto.Util import Padding

from challenge1 import base64ToBytes
from challenge11 import detectEncryptionMode, KEY_SIZE

KEY_SIZE = 16
AES_Key = os.urandom(KEY_SIZE)

# this function is available to us, if we provide it a string, it will encrypt it for us(similar to password managers)
# we do not know the internal implementation. but because we are learning, it will be easier if we know whats happening.
# these functions are more complex than this, but we are taking this example for simplicity.
def encryption_oracle(plainText):
	plainText = plainText + base64ToBytes('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')

	cipher = AES.new(AES_Key, AES.MODE_ECB)
	return cipher.encrypt(Padding.pad(plainText, 16))

def find_block_size(encryption_function=encryption_oracle):
	# it will only be able to find the block size if the block size is smaller than 40(worst case scenario)
	lengths = [len(encryption_function(b'a'*i)) for i in range(1, 40+1)]

	# if blocksize is N, then the len(encryption...) will be same for N elements as oracle adds padding to make the ciphertext a multiple of block size
	# for next N elements, the length will be k+N : k is length of previous N elements(also multiple of N)
	sorted_unique_lengths = sorted(set(lengths))

	# block_size(N) = (k+N) - k
	# difference between any two consecutive elements in sorted_unique_list gives the block size
	block_size = sorted_unique_lengths[1] - sorted_unique_lengths[0] 
	return block_size

# we are not exposed to the random bytes that encryption_oracle appends to the given plain text
# this function finds those random bytes
def decrypt_AES_ECB(block_size, ct_length):
	no_of_blocks = math.ceil(ct_length/block_size)
	plain_text = b''
	for k in range(no_of_blocks*block_size, 0, -1):
		byte_n = encryption_oracle(b'a'*(k - 1))
		all_possibilities = [encryption_oracle(b'a'*(k - 1)+plain_text+bytes([i])) for i in range(256)]
		for i, possibility in enumerate(all_possibilities):
			if(byte_n[:no_of_blocks*block_size] == possibility[:no_of_blocks*block_size]):
				try:
					req_chr = bytes([i]).decode('ascii')
					plain_text += bytes([i])
					break
				except:
					return plain_text
	return plain_text

def main():
	block_size = find_block_size()
	print(f"Block size: {block_size}")
	encryption_mode = detectEncryptionMode(encryption_oracle(b'a'*(2*block_size)), block_size)
	print(f"Encryption mode: {encryption_mode}")
	print(decrypt_AES_ECB(block_size, len(encryption_oracle(b''))))

if __name__=="__main__":
	main()




