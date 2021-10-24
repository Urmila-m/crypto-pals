import os
from challenge10 import AES_CBC_encrypt, AES_CBC_decrypt
from challenge15 import remove_padding

AES_key = os.urandom(16)
initial_vector = os.urandom(16)

def encrypt(plain_text):
    processed_text = plain_text.replace(";", "%3b")
    processed_text = processed_text.replace("=", "%3d")
    processed_text = "comment1=cooking%20MCs;userdata=" + processed_text + ";comment2=%20like%20a%20pound%20of%20bacon"
    return AES_CBC_encrypt(bytes(processed_text, 'utf-8'), initial_vector, AES_key, 'PKCS')

def decrypt(cipher_text):
    padded_plain_text = AES_CBC_decrypt(cipher_text, initial_vector, AES_key)
    return remove_padding(padded_plain_text)

def check_admin(plain_text):
    if 'admin=true' in plain_text.decode(encoding="unicode_escape").split(";"):
        return True

    return False

def bit_flip_attack():
    # "comment1=cooking%20MCs;userdata=" => length = 32 bytes, i.e. it occupies exactly 2 blocks.
    # "x" * 16 => next block which is going to be completely scrambled, so we do not care what these bytes are.
    # ":admin<true;comment2=..." is the next block whose bits can be flipped by changing the cipher text of the previous block 
    # The last bit of ":" and "<" gets flipped so that we get our required text ";admin=true".
    user_input = "x" * 16 + ":admin<true"
    encrypted = encrypt(user_input)

    # bytes type is immutable in python, so use bytearray type instead
    encrypted_bytearray = bytearray(encrypted)

    # 32 and 38 positions of the "xxxx..." block corresponds to ":" and "<" of the ":admin<true..." block
    # A xor 1 = !(A), A xor 0 = A
    encrypted_bytearray[32] = encrypted_bytearray[32] ^ 1
    encrypted_bytearray[38] = encrypted_bytearray[38] ^ 1
    decrypted = decrypt(bytes(encrypted_bytearray))
    print(f"Decrypted text: {decrypted}")
    print(f"Check admin: {check_admin(decrypted)}")

def main():
    bit_flip_attack()

if __name__ == "__main__":
    main()
    

