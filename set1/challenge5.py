from challenge1 import *
from challenge2 import *


def repeatingKeyXOR(bytesValue, key):
	inputLength = len(bytesValue)
	XORSecondOperator = generateXOROperator(key, inputLength)
	return fixedXOR(bytesValue, XORSecondOperator)

def generateXOROperator(key, totalLength):
	effectiveLength = (int)(totalLength/len(key))
	XOROperater = key * effectiveLength
	if not totalLength % len(key) == 0:
		XOROperater += key[: totalLength % len(key)]
	return XOROperater

if __name__ == "__main__":
	input = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

	print(bytesToHex(repeatingKeyXOR(input.encode(), 'ICE'.encode())))