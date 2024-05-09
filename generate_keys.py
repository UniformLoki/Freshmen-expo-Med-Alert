#run this file to generate new encryption/decryption keys and store them in the .env file

import rsa
import os
import dotenv

#generate keys
public_key, private_key = rsa.newkeys(512)

#store keys
env_file = dotenv.find_dotenv()
dotenv.load_dotenv(env_file)

public_key_str = str(public_key)
private_key_str = str(private_key)

public_key_list = public_key_str[10:].strip(")")
public_key_list = str(public_key_list)
public_key_list = public_key_list.split(", ")

private_key_list = private_key_str[11:].strip(")")
private_key_list = str(private_key_list)
private_key_list = private_key_list.split(", ")

os.environ["ENCRYPT0"] = public_key_list[0]
os.environ["ENCRYPT1"] = public_key_list[1]

os.environ["DECRYPT0"] = private_key_list[0]
os.environ["DECRYPT1"] = private_key_list[1]
os.environ["DECRYPT2"] = private_key_list[2]
os.environ["DECRYPT3"] = private_key_list[3]
os.environ["DECRYPT4"] = private_key_list[4]

dotenv.set_key(env_file, "ENCRYPT0", os.environ["ENCRYPT0"])
dotenv.set_key(env_file, "ENCRYPT1", os.environ["ENCRYPT1"])

dotenv.set_key(env_file, "DECRYPT0", os.environ["DECRYPT0"])
dotenv.set_key(env_file, "DECRYPT1", os.environ["DECRYPT1"])
dotenv.set_key(env_file, "DECRYPT2", os.environ["DECRYPT2"])
dotenv.set_key(env_file, "DECRYPT3", os.environ["DECRYPT3"])
dotenv.set_key(env_file, "DECRYPT4", os.environ["DECRYPT4"])

print("New keys have been generated and stored in the .env file.")