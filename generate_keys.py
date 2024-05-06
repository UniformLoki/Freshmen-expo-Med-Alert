import rsa

#generate keys
public_key, private_key = rsa.newkeys(512)

print(f"public key = {public_key}")
print(f"private key = {private_key}")
