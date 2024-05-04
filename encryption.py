import rsa

#generate keys
PUBLIC_KEY, PRIVATE_KEY = rsa.newkeys(512)

def encrypt(data:str)->str:
    """encrypt a string using a globally defined public key"""
    return rsa.encrypt(data.encode(), PUBLIC_KEY)

def decrypt(data:str)->str:
    """decrypt a string using a private key"""
    return rsa.decrypt(data, PRIVATE_KEY).decode()
