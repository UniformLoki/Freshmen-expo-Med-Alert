#generates ney encryption/decryption keys to be stored in env file

import rsa
import os

#generate keys
public_key, private_key = rsa.newkeys(512)

print(f"public key = {public_key}")
print(f"private key = {private_key}")

print("The keys are a set of comma separated values")
print("copy/paste them in the .env file as ENCRYPT0, ENCRYPT1, DECRYPT0, etc")
