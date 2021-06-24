import base64

def hexToBase64(hexValue):
	return bytesToBase64(hexToBytes(hexValue))

def hexToBytes(hexValue):
	return bytes.fromhex(hexValue)

def bytesToBase64(bytesValue):
	# b64encode returns a bytes type, decode() converts it to string type
	return base64.b64encode(bytesValue).decode("UTF-8")

def bytesToHex(bytesValue):
	return bytesValue.hex()

def base64ToBytes(base64Value):
	return base64.b64decode(base64Value)

if __name__ == "__main__":
	print(hexToBase64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))
