import random
import string
import hashlib
import datetime

print("Welcome to ssc! Generating ssc certificate now... (unsigned)")

characters = string.ascii_letters + string.digits
ssc = ''.join(random.choices(characters, k=12))

print(ssc)

sign = input("Would you like to sign your certificate? (y/n) \n")

if sign == "y":
    print("Please enter your signer's key:")
    key = input()

    signssc = ssc + key + str(datetime.datetime.now())

    string_bytes = signssc.encode()

    hash_object = hashlib.sha256()
    hash_object.update(string_bytes)

    signedssc = hash_object.hexdigest()
    
    print(f"unhashed: {signssc} hashed: {signedssc}")

elif sign == "n":
    exit()