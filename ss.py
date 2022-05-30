import time
import hashlib
import sys
user_hash =input("enter hash: ")


file=open('pass.txt','r')

lines = file.readlines()
for password in lines:
    x = hashlib.md5(password.strip().encode()).hexdigest()
    if x == user_hash:
        print(password)
        sys.exit()
print("cant find the password")
