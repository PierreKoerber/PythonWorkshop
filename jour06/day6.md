# 📚 Jour 6 — Lire et écrire des fichiers en Python

---

## 🎯 Objectifs pédagogiques

1. Comprendre **ce qu’est un fichier** et comment l’ordinateur l’utilise.
2. Savoir **lire** un fichier texte en Python.
3. Savoir **écrire** ou **ajouter** des données dans un fichier texte.
4. Comprendre la différence entre **modes d’ouverture** (`"r"`, `"w"`, `"a"`, `"x"`).
5. Manipuler des fichiers **JSON** pour stocker des données structurées.

---

## 1️⃣ Théorie

### 1.1 Ouverture et fermeture

```python
f = open("test.txt", "r")
contenu = f.read()
f.close()
```

⚠️ **Bonne pratique** : utiliser `with` pour fermer automatiquement :

```python
with open("test.txt", "r") as f:
    contenu = f.read()
```

---

### 1.2 Modes d’ouverture

| Mode  | Signification | Effet                                             |
| ----- | ------------- | ------------------------------------------------- |
| `"r"` | Read          | Lecture seule (erreur si le fichier n’existe pas) |
| `"w"` | Write         | Écriture (efface le contenu existant)             |
| `"a"` | Append        | Écriture en ajout à la fin                        |
| `"x"` | Create        | Crée un nouveau fichier (erreur si existe déjà)   |

---

### 1.3 Lire un fichier

```python
with open("test.txt", "r", encoding="utf-8") as f:
    contenu = f.read()
print(contenu)
```

Lire **ligne par ligne** :

```python
with open("test.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(ligne.strip())  # strip() enlève les \n
```

---

### 1.4 Écrire dans un fichier

```python
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Bonjour\n")
```

Ajouter à la fin :

```python
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("Nouvelle ligne\n")
```

---

### 1.5 Sauvegarde en JSON

```python
import json

data = {"nom": "Alex", "age": 14}

with open("profil.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
```

Lecture JSON :

```python
with open("profil.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(data["nom"])
```

---

## 2️⃣ Exemple guidé

Sauvegarder une **liste de joueurs** dans un fichier texte :

```python
joueurs = ["Alex", "Marie", "Sam"]

with open("joueurs.txt", "w", encoding="utf-8") as f:
    for j in joueurs:
        f.write(j + "\n")
```

Lire et afficher :

```python
with open("joueurs.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(ligne.strip())
```

---

## 3️⃣ Mini-projet du jour — Carnet d’adresses

**Objectif :**

1. Demander nom, prénom, téléphone.
2. Les stocker dans un fichier `contacts.json`.
3. Pouvoir relire et afficher tous les contacts.

---

## 4️⃣ Exercices supplémentaires

1. Lire un fichier texte et compter le nombre de lignes.
2. Écrire 10 nombres dans un fichier, un par ligne.
3. Lire un fichier et afficher toutes les lignes qui contiennent un mot donné.

---

## 5️⃣ Bonus possible

- Découvrir `os.path.exists()` pour vérifier si un fichier existe.
- Faire un **backup automatique** avant de modifier un fichier.
