#encryption function wrappers for ease of use

from dotenv import load_dotenv
import rsa
import os
import keys

#get keys

load_dotenv()

ENCRYPTION_KEY = rsa.PublicKey(int(os.getenv('ENCRYPT0')), int(os.getenv('ENCRYPT1')))
DECRYPTION_KEY = rsa.PrivateKey(int(os.getenv('DECRYPT0')), int(os.getenv('DECRYPT1')), int(os.getenv('DECRYPT2')), int(os.getenv('DECRYPT3')), int(os.getenv('DECRYPT4')))

def encrypt(data:str)->str:
    """encrypt a string using a globally defined public key"""
    return rsa.encrypt(data.encode(), ENCRYPTION_KEY)

def decrypt(data:str)->str:
    """decrypt a string using a private key"""
    return rsa.decrypt(data, DECRYPTION_KEY).decode()

#test
test_string = "uiribreiubgiuergui"
print(test_string)
test_string = encrypt(test_string)
print(test_string)
test_string = decrypt(test_string)
print(test_string)
