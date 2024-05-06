#generates ney encryption/decryption keys to be stored in env file

import rsa
import os

#generate keys
public_key, private_key = rsa.newkeys(512)

os.environ["ENCRYPTION_KEY"] = public_key
os.environ["DECRYPTION_KEY"] = private_key

print(f"public key = {public_key}")
print(f"private key = {private_key}")
