from collections import Counter
import sys

def is_PKCS_padding_valid(padded_text):
    if(len(padded_text) % 16 != 0):
        return (False, None)

    last_byte = padded_text[-1]
    if(last_byte < 16):
        for ch in padded_text[-last_byte:]:
            if(ch != last_byte):
                return (False, None)
        
        if(len(padded_text[-last_byte:]) != last_byte):
            return (False, None)
        
        return (True, last_byte)
    else:
        return (True, 0)

def remove_padding(padded_text):
    isPaddingValid, padding = is_PKCS_padding_valid(padded_text)
    if(isPaddingValid): 
        return padded_text[: -padding] if padding != 0  else padded_text
    else:
        raise Exception("Invalid padding")

def main():
    print(remove_padding(b"ICE ICE BABY\x04\x04\x04\x04"))
    print(remove_padding(b"ICE ICE BABY\x01\x02\x03\x04"))
    print(remove_padding(b"ICE ICE BABY\x05\x05\x05\x05"))
   
if __name__ == "__main__":
    main()




