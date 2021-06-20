from challenge3 import *
from challenge2 import *
import sys
import base64
from challenge5 import *
import numpy as np

def hammingDist(byte1, byte2):
	temp = fixedXOR(byte1, byte2)

	# Number of 1's in the XOR of byte1 and byte2 gives the hamming distance
	return bin(int.from_bytes(temp, byteorder=sys.byteorder)).count('1')

def base64ToBytes(base64Value):
	return base64.b64decode(base64Value)

def searchKey(bytesValue):
	hammingDistances = {}
	for i in range(2, 41):
		byte1 = bytesValue[0:i]
		byte2 = bytesValue[i:2*i]
		hammingDistances[i] = hammingDist(byte1, byte2)/i

	return sorted(hammingDistances.items(), key=lambda x: x[1])[0]


if __name__ == "__main__":
	with open("set1/6.txt", "r") as f:
		input = f.read()

	inputBytes = base64ToBytes(input)

	# keySizes = searchKey(inputBytes)
	keySize, distance = searchKey(inputBytes)
	# for keySize, distance in keySizes:
	print(f"\n\n\nkeysize: {keySize}")
	blockList = []
	for i in range(0, len(inputBytes), keySize):
		block = []
		for j in range(i, min(i+keySize, len(inputBytes))):
			block.append(inputBytes[j])

		blockList.append(block)

	if not len(inputBytes)%keySize == 0:
		zeroPadding = [0] * (keySize-len(inputBytes)%keySize)
		blockList[-1].extend(zeroPadding)
	
	transposedBlock = np.transpose(blockList)


	for i in range(keySize):
		print(f"Block: {i}\n")
		singleByteXOR(bytes(transposedBlock[i]), 3)