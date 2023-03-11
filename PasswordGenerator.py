#!/bin/python

import secrets
import string

#generate used characters
letters = string.ascii_letters
digits = string.digits
specials = string.punctuation
alphabet = letters + specials + digits
#choose the lenght of the password
pwd_lenght = int(input("Longueur du mot de passe: "))
#generate password until conditions are matched
while True:
    pwd = ''
    #generate password
    for i in range(pwd_lenght):
        pwd +=''.join(secrets.choice(alphabet))
    #check if there are enought special caracters and digits
    if (sum(char in specials for char in pwd) >=3 and sum(char in digits for char in pwd) >=2):
        break

print("Password: {}".format(pwd))