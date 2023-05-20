#!/bin/python
import getpass
from cryptography.fernet import Fernet


def generer_cle():
    return Fernet.generate_key()


def sauvegarder_cle(cle, fichier):
    with open(fichier, 'wb') as file:
        file.write(cle)


def charger_cle(fichier):
    with open(fichier, 'rb') as file:
        return file.read()

def verifier_phrase_secrete():
    phrase_secrete = "test"
    tentative = getpass.getpass("Entrez la phrase secrète : ")
    return tentative == phrase_secrete

def crypter_donnees(donnees, cle):
    cipher_suite = Fernet(cle)
    return cipher_suite.encrypt(donnees.encode())


def decrypter_donnees(donnees_cryptees, cle):
    cipher_suite = Fernet(cle)
    return cipher_suite.decrypt(donnees_cryptees).decode()


def ajouter_mot_de_passe(coffre_fort, cle):
    site = input("Entrez le nom du site ou du service : ")
    mot_de_passe = getpass.getpass("Entrez le mot de passe : ")
    coffre_fort[site] = crypter_donnees(mot_de_passe, cle)
    print("MDP ajouté")


def supprimer_mot_de_passe(coffre_fort):
    site = input("Entrez le nom du site/service à supprimer : ")
    if site in coffre_fort:
        del coffre_fort[site]
        print("MDP supprimé")
    else:
        print("Aucun mot de passe trouvé pour ce site/service.")


def lire_mot_de_passe(coffre_fort, cle):
    site = input("Entrez le nom du site/service : ")
    if site in coffre_fort:
        mot_de_passe_crypte = coffre_fort[site]
        mot_de_passe = decrypter_donnees(mot_de_passe_crypte, cle)
        print(f"Site/Service : {site} | Mot de passe : {mot_de_passe}")
    else:
        print("Aucun mot de passe trouvé pour ce site.")


def afficher_menu():
    print("1. Ajouter un mot de passe")
    print("2. Supprimer un mot de passe")
    print("3. Lire un mot de passe")
    print("4. Quitter")


def main():
    fichier_cle = "cle.key"
    fichier_donnees = "coffre_fort.dat"
    try:
        cle = charger_cle(fichier_cle)
    except FileNotFoundError:
        cle = generer_cle()
        sauvegarder_cle(cle, fichier_cle)

    try:
        donnees_cryptees = open(fichier_donnees, 'rb').read()
        donnees = decrypter_donnees(donnees_cryptees, cle)
        coffre_fort = eval(donnees)
    except (FileNotFoundError, SyntaxError):
        coffre_fort = {}

    if verifier_phrase_secrete():
        while True:
            afficher_menu()
            choix = input("Entrez votre choix : ")

            if choix == "1":
                ajouter_mot_de_passe(coffre_fort, cle)
            elif choix == "2":
                supprimer_mot_de_passe(coffre_fort)
            elif choix == "3":
                lire_mot_de_passe(coffre_fort, cle)
            elif choix == "4":
                donnees = str(coffre_fort)
                donnees_cryptees = crypter_donnees(donnees, cle)
                with open(fichier_donnees, 'wb') as file:
                    file.write(donnees_cryptees)
                print("Les données du coffre-fort ont été sauvegardées.")
                break
            else:
                print("Veuillez réessayer")
    else:
        print("Phrase secrète erronée. Accès refusé.")


if __name__ == '__main__':
    main()
