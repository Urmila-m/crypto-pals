from collections import Counter

def is_PKCS_padding_valid(padded_text):
    raw_string = padded_text.encode('unicode_escape').decode()
    all_padding = raw_string.split(r'\x')[1:]
    counter = Counter(all_padding)
    if(len(counter) != 1):
        return (False, None)
    else:
        padding = int(str(list(dict(counter).items())[0][0]), 16)
        count = list(dict(counter).items())[0][1]
        if(count == padding):
            return (True, count)
        return (False, None)

def remove_padding(padded_text):
    isPaddingValid, padding = is_PKCS_padding_valid(padded_text)
    if(isPaddingValid): 
        return padded_text[: -padding]
    else:
        raise Exception("Invalid padding")

def main():
    print(remove_padding("ICE ICE BABY\x04\x04\x04\x04"))
    print(remove_padding("ICE ICE BABY\x05\x05\x05\x05"))
    print(remove_padding("ICE ICE BABY\x01\x02\x03\x04"))
   
if __name__ == "__main__":
    main()




