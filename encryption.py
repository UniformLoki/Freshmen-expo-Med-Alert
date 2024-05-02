import pycryptodome
from Crypto.random import get_random_bytes

key = get_random_bytes(128)

print(key)