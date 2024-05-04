import rsa

#generate keys
public_key, private_key = rsa.newkeys(512)

#create strings
a_string = "lettuce"
another_string = "35.5"

#encrypt
a_string_encrypted = rsa.encrypt(a_string.encode(), public_key)
another_string_encrypted = rsa.encrypt(another_string.encode(), public_key)

#print
print(a_string)
print(a_string_encrypted)
print()
print(another_string)
print(another_string_encrypted)

print()

#decrypt
decrypted_string = rsa.decrypt(a_string_encrypted, private_key).decode()
print(decrypted_string)
another_decrypted_string = rsa.decrypt(another_string_encrypted, private_key).decode()
print(another_decrypted_string)

