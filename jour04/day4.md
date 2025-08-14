---
# 📚 Jour 4 — Conditions, Opérateurs logiques, Mini-projet "Jeu du nombre"
---

## 🎯 Objectifs pédagogiques

1. Comprendre **les conditions** (`if`, `elif`, `else`).
2. Découvrir les **opérateurs logiques** (`and`, `or`, `not`).
3. Utiliser les **opérateurs de comparaison** (`==`, `!=`, `<`, `>`, `<=`, `>=`).
4. Introduire les **conditions imbriquées**.
5. Réaliser un **mini-projet interactif** pour appliquer ces notions.

---

## 1️⃣ Théorie

### 1.1 Structure `if`

```python
age = 14
if age >= 18:
    print("Tu es majeur.")
else:
    print("Tu es mineur.")
```

### 1.2 Avec `elif`

```python
note = 15
if note >= 16:
    print("Très bien")
elif note >= 12:
    print("Bien")
else:
    print("Peut mieux faire")
```

### 1.3 Opérateurs de comparaison

| Opérateur | Signification      |
| --------- | ------------------ |
| `==`      | égal à             |
| `!=`      | différent de       |
| `<`       | plus petit que     |
| `>`       | plus grand que     |
| `<=`      | plus petit ou égal |
| `>=`      | plus grand ou égal |

### 1.4 Opérateurs logiques

```python
if age >= 18 and age <= 25:
    print("Jeune adulte")

if age < 18 or age > 60:
    print("Réduction spéciale")

if not(age < 18):
    print("Tu n’es pas mineur")
```

### 1.5 Conditions imbriquées

```python
if age >= 18:
    if age < 25:
        print("Jeune adulte")
```

---

## 2️⃣ Exemple guidé

```python
nom = input("Nom : ")
age = int(input("Âge : "))

if age >= 18:
    print(f"{nom}, tu peux jouer à ce jeu.")
else:
    print(f"{nom}, tu es trop jeune pour ce jeu.")
```

---

## 3️⃣ Mini-projet du jour — **Jeu du nombre mystère**

### Description

L’ordinateur choisit un nombre entre 1 et 20.
Le joueur doit deviner, avec des indications **trop grand / trop petit**.

### Code

```python
import random

nombre_secret = random.randint(1, 20)
trouve = False

print("🎯 Devine le nombre entre 1 et 20")

while not trouve:
    essai = int(input("Ton essai : "))

    if essai == nombre_secret:
        print("Bravo 🎉 tu as trouvé !")
        trouve = True
    elif essai < nombre_secret:
        print("C'est plus grand !")
    else:
        print("C'est plus petit !")
```

💡 Ce mini-jeu combine :

- **Boucle `while`** (vue au Jour 3)
- **Conditions `if`**
- **Variables** (Jour 2)
- **Entrée utilisateur** (Jour 1)

---

## 4️⃣ Exercices supplémentaires

1. **Test de majorité** : demander âge, afficher si majeur ou mineur.
2. **Classement sportif** : en fonction d’un score donné, afficher un message (“débutant”, “intermédiaire”, “expert”).
3. **Accès au serveur** : demander un mot de passe, vérifier s’il correspond à `"admin123"`.

---

## 5️⃣ Bonus possible

Introduction rapide aux **expressions ternaires** :

```python
age = 20
message = "majeur" if age >= 18 else "mineur"
print(message)
```
