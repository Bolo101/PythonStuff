*#!/bin/python

"""Credits: Bolo101

    Password manager in python, data stored in encrypted files created during first launch
"""


import getpass
import secrets
import sys
from cryptography.fernet import Fernet


def save_key(key,file):
    with open(file,'wb') as file:
        file.write(key)

def load_key(file):
    with open(file, 'rb') as file:
        return file.read()

def encrypt_data(data,key):
    return Fernet(key).encrypt(data.encode("utf-8"))

def decrypt_data(data,key):
    return Fernet(key).decrypt(data.decode("utf-8"))

def add_site(register,key):
    site = input("Site to add: ")
    password = getpass.getpass(f"Password for {site}: ")
    register[site] = encrypt_data(password,key)
    print("Password added for {} ! ".format(site))


def remove_site(register):
    site = input("Site to remove: ")
    if site in register:
        del register[site]
        print("Data deleted")
    else:
        print("Not in the database")

def read_site(register,key):
    site = input("Site: ")
    if site in register:
        password_encrypted = register[site]
        passworden = decrypt_data(password_encrypted, key)
        password = passworden.decode("utf-8")
        print(f"{site}: {password}")
    else :
        print("Not in database") 

def modify_site(register,key):
    site = input("Site to modify: ")
    if site in register:
        password = getpass.getpass("New password: ")
        register[site] = encrypt_data(password,key)
        print("Password changed for {}".format(site))
        


def check_safety(locker_file,key):
    with open(locker_file,'rb') as file:
        checking = getpass.getpass("Security input: ")
        pas = file.read()
        decrypted_pas = decrypt_data(pas,key)
        decrypted_pas = decrypted_pas.decode()
        if checking == decrypted_pas:
            return True
        else :
            return False
        
def constructSecurity(locker_file,key):
    with open(locker_file,'wb') as file:
        while True:
            yourPassword = getpass.getpass("Enter password: ")
            confirmation = getpass.getpass("Confirm password: ")
            if yourPassword == confirmation:
                text = encrypt_data(yourPassword,key)
                file.write(text)
                break
            else:
                print("Unmatched passwords. Please try again")

def kind_world():
    liste = ['You are a genius', 'You can do it','Believe in yourself','You are your destiny','Keep it up']
    print(secrets.choice(liste))

def modifyRootPassword(l_file,key):
    confirmation = getpass.getpass("Enter current security input: ")
    
    with open(l_file,'rb') as file:
        c_en_password = file.read()
        c_password = decrypt_data(c_en_password,key).decode()
        file.close()
            
    with open(l_file,'wb') as file: 
        if confirmation == c_password:
            new_password = getpass.getpass("Enter new security input: ")
            new_en_password = encrypt_data(new_password,key)
            file.write(new_en_password)
            file.close()
        else:
            print("Pro")

def displayMenu():
    print("1. Add a site/service credential")
    print("2. Delete a site/service credential")
    print("3. Read a site/service credential")
    print("4. Modify a site/service credential")
    print("5. Get a kind word")
    print("6. Modify password manager security input")
    print("7. Exit")

def subMain(bank,key,data_file,locker_file):
    while True:
        displayMenu()
        choice = input("Option: ")
        if choice =="1":
            add_site(bank,key)
        elif choice == '2':
            remove_site(bank)
        elif choice =='3':
            read_site(bank,key)
        elif choice == '4':
            modify_site(bank,key)
        elif choice == '5':
            kind_world()
        elif choice =='6':
            modifyRootPassword(locker_file,key)
        elif choice == '7':
            data_to_encrypt = str(bank)
            data_encrypted = encrypt_data(data_to_encrypt,key)
            with open(data_file,'wb') as file:
                file.write(data_encrypted)
            print("Data updated ! Enjoy your day and remerber to use strong and unique password to stay safe online")
            sys.exit()
        else:
            print("Try again !")


def main():
    key_file = "key.key"
    data_file = "data_file.dat"
    locker_file = "locker_file.dat"

    try:
        key = load_key(key_file)
    except FileNotFoundError:
        key = Fernet.generate_key()
        save_key(key,key_file)

    try:
        encrypted_data = open(data_file,'rb').read()
        decrypted_data = decrypt_data(encrypted_data,key)
        bank = eval(decrypted_data)
    except (FileNotFoundError,SyntaxError):
        bank = {}

    try:
        if check_safety(locker_file,key):
            subMain(bank,key,data_file,locker_file)
        else:
            print("X YOU SHALL NOT PASS X")
    except FileNotFoundError:
        if len(bank)==0:
            constructSecurity(locker_file,key)
            subMain(bank,key,data_file,locker_file)
        else :
            print("Wrong password. Access denied")

if __name__ =='__main__':
    main()






