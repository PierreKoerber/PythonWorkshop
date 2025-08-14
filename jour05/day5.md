---
# 📚 Jour 5 — Listes et Dictionnaires
---

## 🎯 Objectifs pédagogiques

1. Comprendre ce qu’est une **liste** (`list`) et comment l’utiliser.
2. Comprendre ce qu’est un **dictionnaire** (`dict`) et son intérêt.
3. Savoir **ajouter, modifier, supprimer** des éléments.
4. Parcourir ces structures avec une **boucle `for`**.
5. Appliquer tout ça dans un **mini-projet concret**.

---

## 1️⃣ Théorie

### 1.1 Les listes (`list`)

- Contiennent **plusieurs valeurs** dans un seul objet.
- Les éléments sont **ordonnés** et accessibles par un index.

```python
fruits = ["pomme", "banane", "cerise"]
print(fruits[0])   # pomme
fruits.append("orange")  # ajoute à la fin
fruits.remove("banane")  # supprime un élément
```

---

### 1.2 Les dictionnaires (`dict`)

- Contiennent des **paires clé/valeur**.
- Accès rapide par **clé** au lieu d’un index.

```python
joueur = {
    "pseudo": "Alex",
    "score": 150,
    "niveau": "débutant"
}

print(joueur["pseudo"])       # Alex
joueur["score"] = 200         # modifie la valeur
joueur["vie"] = 3             # ajoute une nouvelle clé
```

---

### 1.3 Parcourir une liste ou un dictionnaire

```python
# Liste
for fruit in fruits:
    print(fruit)

# Dictionnaire
for cle, valeur in joueur.items():
    print(cle, ":", valeur)
```

---

### 1.4 Longueur et test d’existence

```python
print(len(fruits))           # nombre d’éléments
print("pomme" in fruits)     # True si trouvé
print("score" in joueur)     # True si la clé existe
```

---

## 2️⃣ Exemple guidé

**Liste de scores**

```python
scores = [100, 150, 90]
scores.append(120)
print("Scores :", scores)
print("Score max :", max(scores))
print("Score min :", min(scores))
```

**Dictionnaire de profil**

```python
profil = {"nom": "Alex", "age": 14}
profil["ville"] = "Martigny"
print(profil)
```

---

## 3️⃣ Mini-projet du jour — Gestionnaire de joueurs

### Description

Créer un petit programme qui :

1. Demande plusieurs pseudos et scores.
2. Stocke chaque joueur dans un **dictionnaire**.
3. Les sauvegarde dans une **liste**.
4. Écrit le tout dans un fichier `joueurs.json`.
5. Relit le fichier et affiche tous les joueurs.

### Code

```python
import json

joueurs = []

for i in range(3):
    pseudo = input("Pseudo : ")
    score = int(input("Score : "))
    joueur = {"pseudo": pseudo, "score": score}
    joueurs.append(joueur)

with open("joueurs.json", "w", encoding="utf-8") as f:
    json.dump(joueurs, f, indent=2, ensure_ascii=False)

print("\n--- Lecture du fichier ---")
with open("joueurs.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for j in data:
    print(f"{j['pseudo']} - {j['score']} points")
```

---

## 4️⃣ Exercices supplémentaires

1. Créer une **liste de villes**, afficher la plus courte et la plus longue.
2. Créer un **dictionnaire “PC”** avec processeur, RAM, stockage et afficher chaque info.
3. Demander 5 nombres, stocker dans une liste, afficher la **moyenne**.

---

## 5️⃣ Bonus possible

- Trier une liste (`sorted()`).
- Trier une liste de dictionnaires par valeur (`sorted(liste, key=lambda x: x['score'], reverse=True)`).
- Sauvegarder dans un **CSV** plutôt qu’un JSON.
