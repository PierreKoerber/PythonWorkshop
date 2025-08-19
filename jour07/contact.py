import json
import os
import utils

utils.affichage("Carnet de contact version 3")

loop = True
filename = "contacts.json"

while loop == True :

    contacts = utils.load_customer(filename)
    utils.affiche_menu()
    status=int(input("Votre choix: "))
    if status == 1 :
        newcontact = utils.saisie_customer()
        contacts.append(newcontact)
        utils.write_customer(contacts)
    
    elif status == 2 :
        utils.affichage_seperator()
        utils.affiche_customers(contacts)

    elif status == 3 :
        utils.affichage_seperator()
        utils.affiche_customers(contacts)
        ret = int(input("le quel voulez vous supprimez ? Entrer le numéro de liste : "))
        contacts = utils.supprime_contact(contacts, ret-1)
        utils.write_customer(contacts)
    
    elif status == 4 :
         loop = False