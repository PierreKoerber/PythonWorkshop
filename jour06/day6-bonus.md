# 🔹 Chapitre complémentaire — Centraliser du code avec des fonctions

---

## 1️⃣ Pourquoi créer des fonctions ?

- **Éviter les répétitions** : au lieu de copier-coller le même bloc plusieurs fois, on écrit une fois et on l’appelle autant qu’on veut.
- **Donner un nom clair** : le programme est plus facile à lire et à comprendre.
- **Pouvoir réutiliser** le même code dans différents projets.
- **Faciliter la maintenance** : si on doit modifier un comportement, on le change à un seul endroit.

---

## 2️⃣ Exemple sans fonction ❌

```python
nom = input("Ton nom : ")
print(f"Salut {nom} !")
age = int(input("Ton âge : "))
print(f"Tu as {age} ans")

nom2 = input("Ton nom : ")
print(f"Salut {nom2} !")
age2 = int(input("Ton âge : "))
print(f"Tu as {age2} ans")
```

Ici, on répète **deux fois** le même code.

---

## 3️⃣ Exemple avec fonction ✅

```python
def demander_infos():
    nom = input("Ton nom : ")
    print(f"Salut {nom} !")
    age = int(input("Ton âge : "))
    print(f"Tu as {age} ans")

# On peut réutiliser la fonction
demander_infos()
demander_infos()
```

Avantages :

- Code plus court
- Facile à modifier (si on change la phrase, ça s’applique partout)

---

## 4️⃣ Paramètres et retour

Une fonction peut **recevoir des paramètres** :

```python
def dire_bonjour(nom):
    print(f"Salut {nom} !")

dire_bonjour("Alex")
dire_bonjour("Marie")
```

Elle peut aussi **retourner une valeur** :

```python
def calculer_annee_naissance(age):
    return 2025 - age

annee = calculer_annee_naissance(14)
print(f"Tu es né en {annee}")
```

---

## 5️⃣ Centraliser dans un fichier séparé

On peut créer un fichier **`utils.py`** :

```python
# utils.py
def dire_bonjour(nom):
    print(f"Salut {nom} !")
```

Et l’utiliser dans notre programme :

```python
# main.py
from utils import dire_bonjour

dire_bonjour("Alex")
```

💡 C’est comme une **boîte à outils** où on range les fonctions qu’on veut réutiliser.

---

## 6️⃣ Comprendre `print(f"Salut {nom}")`

- Les **f-strings** (depuis Python 3.6) permettent **d’insérer directement** des variables dans une chaîne.
- La lettre **`f`** avant les guillemets signifie _format string_.
- Tout ce qui est entre **`{}`** sera remplacé par la valeur de la variable.

```python
nom = "Alex"
age = 14
print(f"Salut {nom}, tu as {age} ans")
# Affiche : Salut Alex, tu as 14 ans
```

💡 Avantages par rapport à `"Salut " + nom` :

- Plus **lisible**
- Plus **rapide à écrire**
- Évite les erreurs de conversion (`str()`)

---

📌 **Mini-exercice pour ton fils**

1. Créer une fonction `demander_nom_age()` qui :

   - Demande un nom
   - Demande un âge
   - Retourne ces deux infos

2. Appeler la fonction et afficher :

   ```
   Bonjour Alex, tu as 14 ans.
   ```

   en utilisant une **f-string**.
