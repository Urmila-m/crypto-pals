from challenge1 import *
from challenge2 import *
import string

def generateXORBytes(length):
	XORBytesList = {}
	for i in range(256):
		singleByte = bytes([i])
		XORByte = singleByte * length
		XORBytesList[chr(i)] = XORByte

	return XORBytesList

def singleByteXOR(bytesValue, n=3):
	messages = {}
	for ch, XORByte in generateXORBytes(len(bytesValue)).items():
		message = fixedXOR(bytesValue, XORByte)
		try:
			message = message.decode('ascii')
			messages[ch] = (message, getCharacterFrequency(message))
		except:
			# message contains non-ASCII characters
			pass
	
	for key, value in getMessageWithHighCharCount(messages, n):
		if not len(value) == 0:
			print(f"\n{key}:")
			for msg in value:
				print(msg)

	return messages

def getCharacterFrequency(message):
	score = 0
	for ch in message:
		if ch in string.ascii_letters:
			score += 1

	return score

def getMessageWithHighCharCount(messages, n):
	return sorted(messages.items(), key=lambda x: x[1][1])[-n:]

if __name__ == "__main__":
	input = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
	input2 = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

	messages = singleByteXOR(hexToBytes(input))

	