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
	# realtive character frequency
	freq = {
		'a' : 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 13, 
		'f' : 2.2, 'g': 2, 'h': 6.1, 'i': 7, 'j': 0.15, 
		'k': 0.77, 'l': 4, 'm': 2.4, 'n': 6.7, 'o': 7.5,
		'p': 1.9, 'q': 0.095, 'r':6, 's': 6.3, 't': 9.1, 
		'u': 2.8, 'v': 0.98, 'w': 2.4, 'x': 0.15, 'y': 2, 
		'z': 0.074
	} 
	score = 0
	for ch in message:
		if ch in string.ascii_letters:
			score += freq[ch.lower()]

	return score

def getMessageWithHighCharCount(messages, n):
	return sorted(messages.items(), key=lambda x: x[1][1])[-n:]

if __name__ == "__main__":
	input = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
	input2 = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

	messages = singleByteXOR(hexToBytes(input))

	