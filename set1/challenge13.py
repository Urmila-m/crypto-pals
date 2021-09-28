import os
from Crypto.Cipher import AES
from Crypto.Util import Padding
from random import randint

AES_key = os.urandom(16)
cipher = AES.new(AES_key, AES.MODE_ECB)

def key_value_parser(input_str):
    all_pairs = input_str.decode().split("&")
    parsed_dict = {}
    for key_value in all_pairs:
        temp_list = key_value.split("=")
        key = temp_list[0]
        value = temp_list[1]
        parsed_dict[key] = value

    return parsed_dict

def profile_for(email_str):
    if("&" in email_str):
        email_str = email_str.split("&")[0]
    return {
        "email": email_str,
        "uid": randint(1, 50),
        "role": "user"
    }

def encode_profile(email_profile):
    key_value_list = []
    for item in email_profile.items():
        key_value_list.append("=".join([str(x) for x in item]))

    return "&".join(key_value_list)

def encrypt(encoded_profile):
    return cipher.encrypt(Padding.pad(encoded_profile.encode(), 16))

def decrypt_and_parse(encrypted_encoded_profile):
    return key_value_parser(Padding.unpad(cipher.decrypt(encrypted_encoded_profile), 16))

# goes to attacker
encrypted_encoded_profile = encrypt(encode_profile(profile_for("iamzombie@gmail.com")))

actual_input_str = decrypt_and_parse(encrypted_encoded_profile)

print(actual_input_str)

