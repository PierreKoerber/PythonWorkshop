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

#### 1.1.1 LISTE

Oui 👍, je vais te faire une description claire et complète pour bien expliquer à ton fils la différence entre **`list`** et **`tuple`**, dans un format simple à intégrer dans ton support de cours.

---

##### 📦 Comparaison `list` vs `tuple` en Python

| Type        | Description                                                                                                                 | Exemple                         | Peut être modifié ? | Quand l’utiliser                                                                           |
| ----------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------------------- | ------------------------------------------------------------------------------------------ |
| **`list`**  | Collection **ordonnée** et **modifiable** d’éléments. On peut **ajouter, supprimer ou changer** des valeurs après création. | `["pomme", "banane", "cerise"]` | ✅ Oui              | Quand les données peuvent **changer** pendant l’exécution (ex : liste de joueurs, scores). |
| **`tuple`** | Collection **ordonnée** mais **immuable** (on ne peut pas modifier, ajouter ou supprimer un élément après création).        | `("pomme", "banane", "cerise")` | ❌ Non              | Quand les données doivent **rester fixes** (ex : coordonnées GPS, date, configuration).    |

---

##### 📌 Exemple concret

```python
# Liste
fruits = ["pomme", "banane"]
fruits.append("cerise")  # OK
fruits[0] = "orange"     # OK

# Tuple
coordonnees = (45.76, 4.84)
# coordonnees[0] = 50.0  # ❌ Erreur : tuple immuable
```

---

##### 📍 Particularités des tuples

1. **Plus rapide** à manipuler que les listes (car fixe).
2. Peut être utilisé comme **clé dans un dictionnaire** (les listes ne peuvent pas).
3. Peut contenir **des listes** à l’intérieur (mais alors ces listes restent modifiables).
4. Pour créer un tuple avec un seul élément :

   ```python
   t = (5,)  # la virgule est obligatoire
   ```

---

💡 **Astuce pédagogique**
Je te conseille de montrer un exemple **réaliste** :

- **Liste** : liste des pseudos connectés à un serveur → change tout le temps.
- **Tuple** : taille d’écran en pixels `(1920, 1080)` → ne change pas.

---

Si tu veux, je peux te préparer un **schéma mémoire** qui montre que la liste a un "conteneur extensible" alors que le tuple est "verrouillé" une fois créé, pour l’ajouter à ton Jour 5.
Veux-tu que je te fasse ce schéma ?

---

Voici la réponse structurée pour que ce soit clair dans ton support de cours du **Jour 5** :

---

### 🔄 Conversions entre types en Python

#### 1️⃣ Tuple → Liste

```python
t = (1, 2, 3)
ma_liste = list(t)
print(ma_liste)  # [1, 2, 3]
```

💡 Utilise `list()` pour transformer un **tuple** en **liste modifiable**.

---

#### 2️⃣ Liste → Tuple

```python
ma_liste = [1, 2, 3]
t = tuple(ma_liste)
print(t)  # (1, 2, 3)
```

💡 Utilise `tuple()` pour rendre la collection **immuable**.

---

#### 3️⃣ Dictionnaire → Liste

Il faut décider **ce que tu veux extraire** :

```python
d = {"a": 1, "b": 2}

cles = list(d.keys())      # ['a', 'b']
valeurs = list(d.values()) # [1, 2]
paires = list(d.items())   # [('a', 1), ('b', 2)]
```

💡 `.items()` donne une liste de **tuples** `(clé, valeur)`.

---

#### 4️⃣ Peut-on mélanger les types dans une liste ?

✅ Oui, une liste peut contenir **différents types** :

```python
melange = [42, "texte", 3.14, True, [1, 2], {"a": 1}]
print(melange)
```

⚠️ **Conseil** : c’est possible, mais souvent il vaut mieux garder **un type cohérent** pour éviter les erreurs.

---

#### 📌 Astuce pour ton fils

Pour qu’il retienne :

- **`list()`** : transforme en liste
- **`tuple()`** : transforme en tuple
- **`dict.keys()` / `.values()` / `.items()`** : pour extraire du dictionnaire

---

Si tu veux, je peux te faire **une fiche visuelle** avec un tableau de toutes les conversions Python courantes (`list`, `tuple`, `dict`, `set`, `str`) à coller dans le cours.
Veux-tu que je te prépare ça ?

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
