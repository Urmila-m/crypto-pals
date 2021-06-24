from Crypto.Cipher import AES
from challenge1 import *
from collections import Counter

cipher = AES.new(b'YELLOW SUBMARINE', AES.MODE_ECB)

with open("set1/8.txt", "r") as f:
	input = f.readlines()

def removeNewLine(message):
	if message[-1:] == "\n":
		return message[:-1]
	return message

cipherText = map(removeNewLine, input)

cipherText = map(hexToBytes, cipherText)

repeatCounts = {}
for cipherT in cipherText:
	repeatCount = 0
	blocks = []
	for i in range(0, len(cipherT), 16):
		block = cipherT[i: i+16]
		blocks.append(block)

	for i in range(len(blocks)):
		for j in range(i + 1, len(blocks)):
			if blocks[i] == blocks[j]:
				repeatCount += 1

	repeatCounts[cipherT] = repeatCount

# any cipher text that has repeatCount greater than 0, might have been encrypted with ECB
print(sorted(repeatCounts.items(), key=lambda x: x[1], reverse=True)[0])