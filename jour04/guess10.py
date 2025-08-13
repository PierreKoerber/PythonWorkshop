# Jour 4 — Mini-jeu devinettes (1..10, 3 essais)
import random
secret = random.randint(1, 10)
tries = 3
while tries > 0:
    guess = int(input("Devine (1..10) : "))
    if guess == secret:
        print("Gagné !")
        break
    else:
        tries -= 1
        print("Raté. Reste", tries, "essai(s).")
if tries == 0:
    print("Perdu. C'était", secret)