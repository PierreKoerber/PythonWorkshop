import json
import os


def load_customer(filename="contacts.json") :
    if os.path.exists(filename) == False :
        return [] 
    with open(filename, "r", encoding="utf-8") as f:
        contact = json.load(f)
    return contact

def write_customer(contact, filename="contacts.json") :
    if os.path.exists(filename) == False :
        open(filename, "x", encoding="utf8")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(contact, f, indent=2, ensure_ascii=False)

def saisie_customer():
    nom=input("Entrer le nom de ce contact : ")
    age=input("Entrer l'age de ce contact : ")
    npa=input("Entrer la npa : ")
    rue=input("Entrer la rue : ")
    numm=input("Entrer le numéro de maison : ")
    num=input("Entrer le numéro de telephone : ")
    return {"nom" : nom, "age" : age, "npa" : npa,"rue":rue,"numm":numm,"num":num}

def affiche_customers(contacts):
    i = 0
    for c in contacts :
        print(f"{i+1} : {contacts[i]}")
        i = i + 1
def supprime_contact(contacts, number):
     # on devrait tester que ret est pas trop grand ou trop petit
    contacts.pop(ret-1)
    return contacts 

def affichage(msg):
    print(msg.capitalize())
def affichage_seperator():
    print("---------------------------")


def affiche_menu():
    menu = ["Ajouter un contact", "Lire la liste de contact", "Supprimer un contact", "Sortir du programme"]
    affichage = ""
    index = 0 
    affichage_seperator()
    for li in menu:
        line = str(index+1) + " " + li
        index = index + 1
        print(line)

affichage("carnet de contact version 3")

loop = True
filename = "contacts.json"

while loop == True :

    contacts = load_customer(filename)
    affiche_menu()
    status=int(input("Votre choix: "))
    if status == 1 :
        newcontact = saisie_customer()
        contacts.append(newcontact)
        write_customer(contacts)
    
    elif status == 2 :
        affichage_seperator()
        affiche_customers(contacts)

    elif status == 3 :
        affichage_seperator()
        affiche_customers(contacts)
        ret = int(input("le quel voulez vous supprimez ? Entrer le numéro de liste : "))
        contacts = supprime_contact(contacts, ret-1)
        write_customer(contacts)
    
    elif status == 4 :
         loop = False