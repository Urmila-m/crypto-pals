import os
import random
import math
from Crypto.Util import Padding
from Crypto.Cipher import AES
from challenge1 import base64ToBytes
from challenge12 import find_block_size

AES_key = os.urandom(16)
noOfBytesToAppend = random.randint(5, 10)
randomBytesToAppend = os.urandom(noOfBytesToAppend)


def encryption_oracle(plainText):
    plainText = randomBytesToAppend + plainText + base64ToBytes(
        'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
    cipher = AES.new(AES_key, AES.MODE_ECB)
    return cipher.encrypt(Padding.pad(plainText, 16))


def find_random_byte_size(blocksize):
    prev_encrypted = b''
    for i in range(1, blocksize + 1):
        input = b'a' * i
        if not len(prev_encrypted) == 0:
            if prev_encrypted[:blocksize] == encryption_oracle(input)[:blocksize]:
                return blocksize - (i - 1)

        prev_encrypted = encryption_oracle(input)

    return None


def decrypt_AES_ECB(block_size, ct_length, random_byte_size):
    no_of_blocks = math.ceil(ct_length / block_size)
    plain_text = b''
    for k in range(no_of_blocks * block_size, 0, -1):
        byte_n = encryption_oracle(b'a' * (k - random_byte_size - 1))
        all_possibilities = [encryption_oracle(b'a' * (k - random_byte_size - 1) + plain_text + bytes([i])) for i in
                         range(256)]
        for i, possibility in enumerate(all_possibilities):
            if byte_n[:no_of_blocks * block_size] == possibility[:no_of_blocks * block_size]:
                try:
                    req_chr = bytes([i]).decode('ascii')
                    plain_text += bytes([i])
                    break
                except:
                    return plain_text

    return plain_text


def main():
    block_size = find_block_size(encryption_oracle)
    print(decrypt_AES_ECB(block_size, len(encryption_oracle(b'')), find_random_byte_size(block_size)))


if (__name__ == "__main__"):
    main()
