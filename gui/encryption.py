import rsa
import os
from dotenv import load_dotenv

load_dotenv()

#get keys from .env file
PUBLIC_KEY = rsa.PublicKey(int(os.getenv('ENCRYPT0')), int(os.getenv('ENCRYPT1')))
PRIVATE_KEY = rsa.PrivateKey(int(os.getenv('DECRYPT0')), int(os.getenv('DECRYPT1')), int(os.getenv('DECRYPT2')), int(os.getenv('DECRYPT3')), int(os.getenv('DECRYPT4')))


def encrypt(data:str)->str:
    """encrypt a string using a globally defined public key"""
    return rsa.encrypt(data.encode(), PUBLIC_KEY)

def decrypt(data:str)->str:
    """decrypt a string using a private key"""
    return rsa.decrypt(data, PRIVATE_KEY).decode()
