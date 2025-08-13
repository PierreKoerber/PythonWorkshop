Parfait 👍
Voici le **support de cours complet pour le Jour 3** avec toutes les notions que tu veux introduire, en gardant un langage clair et des exemples simples pour ton fils.

---

# 📚 Jour 3 — Fichiers, Types, Fonctions avancées, Boucles

---

## 🎯 Objectifs

1. Lire et écrire dans un fichier (`config.json` ou `.txt`).
2. Comprendre le **typage** des paramètres dans une fonction.
3. Retourner **plusieurs valeurs** depuis une fonction.
4. Découvrir les **fonctions récursives**.
5. Introduction aux **boucles** (`for`, `while`).
6. Connaître les **types de base** de Python.

---

## 1. Lire et écrire un fichier

### Lire

```python
f = open("config.txt", "r", encoding="utf-8")
contenu = f.read()
f.close()
print(contenu)
```

💡 Plus simple avec `with` (fermeture automatique) :

```python
with open("config.txt", "r", encoding="utf-8") as f:
    contenu = f.read()
print(contenu)
```

### Écrire

```python
with open("config.txt", "w", encoding="utf-8") as f:
    f.write("username=Alex\n")
```

---

## 2. Typage des paramètres

En Python, on peut **indiquer** le type attendu dans la définition de la fonction (ce n’est pas obligatoire mais c’est plus clair) :

```python
def addition(a: int, b: int) -> int:
    return a + b

resultat = addition(4, 5)  # 9
```

- `a: int` → paramètre `a` doit être un entier.
- `-> int` → la fonction retourne un entier.

💡 Python ne bloque pas si on met un mauvais type, mais l’éditeur/IDE peut prévenir.

---

## 3. Retourner plusieurs valeurs

Une fonction peut renvoyer **plusieurs résultats** en une seule fois :

```python
def division_et_reste(a: int, b: int) -> tuple[int, int]:
    quotient = a // b
    reste = a % b
    return quotient, reste

q, r = division_et_reste(17, 5)
print("Quotient :", q, "| Reste :", r)
```

💡 Python renvoie en fait un **tuple**.

---

## 4. Fonction récursive

Une **fonction récursive** s’appelle elle-même.

Exemple : **factorielle** (n! = n × (n-1) × … × 1) :

```python
def factorielle(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorielle(n - 1)

print(factorielle(5))  # 120
```

⚠️ Toujours prévoir un **cas de base** pour éviter la boucle infinie.

---

## 5. Introduction aux boucles

### Boucle `for`

Parcourt une séquence (liste, texte, etc.).

```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

### Boucle `while`

Répète tant qu’une condition est vraie.

```python
x = 0
while x < 5:
    print(x)
    x += 1
```

---

## 6. Types de base en Python

| Type    | Description                  | Exemple                      |
| ------- | ---------------------------- | ---------------------------- |
| `int`   | Nombre entier                | `42`                         |
| `float` | Nombre décimal               | `3.14`                       |
| `str`   | Chaîne de caractères (texte) | `"Bonjour"`                  |
| `bool`  | Valeur vraie/faux            | `True`, `False`              |
| `list`  | Liste ordonnée               | `[1, 2, 3]`                  |
| `tuple` | Liste **immuable**           | `(1, 2, 3)`                  |
| `dict`  | Dictionnaire clé → valeur    | `{"nom": "Alex", "age": 14}` |
| `set`   | Ensemble non ordonné         | `{1, 2, 3}`                  |

---

## 7. Exemple complet du jour

```python
# Lecture config
def lire_config() -> dict:
    try:
        with open("config.txt", "r", encoding="utf-8") as f:
            lignes = f.read().splitlines()
        cfg = {}
        for ligne in lignes:
            if "=" in ligne:
                k, v = ligne.split("=", 1)
                cfg[k] = v
        return cfg
    except FileNotFoundError:
        return {}

# Fonction typée + retour multiple
def calcul_stats(a: int, b: int) -> tuple[int, int, int]:
    somme = a + b
    produit = a * b
    diff = a - b
    return somme, produit, diff

# Récursif
def compte_a_rebours(n: int):
    if n == 0:
        print("🚀 Décollage !")
        return
    print(n)
    compte_a_rebours(n - 1)

# --- Utilisation ---
config = lire_config()
print("Config :", config)

s, p, d = calcul_stats(5, 3)
print(f"Somme={s}, Produit={p}, Diff={d}")

compte_a_rebours(5)
```

---

## 8. Mini-exos

1. Créer une fonction `max_et_min` qui retourne le plus grand et le plus petit nombre d’une liste.
2. Créer une fonction récursive `somme_liste` qui additionne tous les éléments d’une liste.
3. Modifier `config.txt` pour y ajouter une clé `theme=clair` et afficher sa valeur.

---

Si tu veux, je peux te préparer **un schéma visuel** qui montre :

- les types de base,
- le flux d’une fonction récursive,
- la boucle `for` et `while`.

Ça rendrait cette leçon plus claire et accrocheuse.
Veux-tu que je te fasse ce schéma pour le Jour 3 ?
