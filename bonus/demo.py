import time
import random

# 1. Afficheur de mots qui grossissent
def mot_grossissant():
    mot = input("Entre un mot : ")
    for i in range(1, len(mot) + 1):
        print(mot[:i])
        time.sleep(0.3)

# 2. Compteur narratif
def compteur_narratif():
    histoires = [
        "Prépare-toi...",
        "Attention, ça arrive...",
        "Le suspense est insoutenable...",
        "C’est presque là...",
        "BOUM !"
    ]
    for i in range(len(histoires), 0, -1):
        print(f"{i}... {histoires[len(histoires) - i]}")
        time.sleep(1)

# 3. Répétiteur farceur
def repetiteur_farceur():
    phrase = input("Entre une phrase : ").split()
    mots = ["banane", "tortue", "poulet", "poney", "chaussette"]
    for _ in range(5):
        phrase_modifiee = phrase[:]
        index = random.randint(0, len(phrase) - 1)
        phrase_modifiee[index] = random.choice(mots)
        print(" ".join(phrase_modifiee))
        time.sleep(0.5)

# 4. Texte en escargot
def texte_escargot():
    texte = input("Entre un mot ou une phrase : ")
    for _ in range(3):
        print(texte)
        time.sleep(0.3)
        print(texte[::-1])
        time.sleep(0.3)

# 5. Progression ASCII
def progression_ascii():
    total = 20
    for i in range(total + 1):
        barre = "█" * i + "-" * (total - i)
        print(f"[{barre}] {int((i/total)*100)}%", end="\r")
        time.sleep(0.1)
    print("\nChargement terminé !")

# 6. Effet machine à écrire (bonus)
def machine_a_ecrire():
    texte = input("Tape une phrase : ")
    for lettre in texte:
        print(lettre, end="", flush=True)
        time.sleep(0.05)
    print()

# Menu pour tester
def menu():
    options = {
        "1": ("Mot grossissant", mot_grossissant),
        "2": ("Compteur narratif", compteur_narratif),
        "3": ("Répétiteur farceur", repetiteur_farceur),
        "4": ("Texte en escargot", texte_escargot),
        "5": ("Progression ASCII", progression_ascii),
        "6": ("Machine à écrire", machine_a_ecrire),
        "q": ("Quitter", None)
    }

    while True:
        print("\n--- Menu Ludique ---")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")
        choix = input("Choisis une option : ")

        if choix == "q":
            break
        elif choix in options:
            options[choix][1]()
        else:
            print("Option invalide.")

if __name__ == "__main__":
    menu()
