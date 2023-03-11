#!/bin/python

import secrets
import string

letters = string.ascii_letters
digits = string.digits
specials = string.punctuation
alphabet = letters + specials + digits
pwd_lenght = int(input("Longueur du mot de passe: "))
pwd = ''
for i in range(pwd_lenght):
    pwd +=''.join(secrets.choice(alphabet))

while True:
    pwd = ''
    for i in range(pwd_lenght):
        pwd +=''.join(secrets.choice(alphabet))
    if (sum(char in specials for char in pwd) >=3 and sum(char in digits for char in pwd) >=2):
        break

print("Password: {}".format(pwd))