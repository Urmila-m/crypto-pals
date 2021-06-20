
from challenge1 import *
from challenge3 import *


allLineMessages = {}

with open("set1/4.txt", "r") as f:
	line = 0
	for input in f.readlines():
		line += 1
		allLineMessages[line] = singleByteXOR(hexToBytes(input), 3)

# line 171, using singleByte 5, the encoded message: Now that the party is jumping