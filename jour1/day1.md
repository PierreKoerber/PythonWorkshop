Jour 1 — Découvrir Python et l’ordinateur

Ouvrir une ordinateur
Pièces d'un ordinateur

Checklist :

    Installer Python et VS Code

    Faire un “Hello World”

    Afficher la version de Python et le nom du système

    Bonus : afficher son nom avec input()

Récap : - Qu'est-ce qu'une fonction ? - Exemple de language informatique ? - Différence language interprêté et compilé ?

OK, je te prépare une **leçon théorique Jour 1** claire et adaptée à ton fils (14 ans), avec juste ce qu’il faut de technique et de concret pour accrocher son intérêt.
On va mêler **explication**, **démonstration Python**, et **mini-exos**.

---

# 📚 Jour 1 — Découvrir Python & l’ordinateur

## 🎯 Objectif du jour

- Comprendre comment un programme est lancé.
- Savoir ce qu’est un **hashbang** sur Linux.
- Apprendre la notion d’**entrée** et de **sortie** dans un programme.
- Utiliser `print()` et `input()`.

---

## 1. Comment un programme fonctionne

Un ordinateur **exécute** des instructions (une suite d’ordres).

- **Entrée** → ce que tu donnes au programme (ex. clavier, souris, fichier…)
- **Traitement** → ce que le programme fait avec ces données.
- **Sortie** → ce que le programme te renvoie (ex. affichage écran, son, fichier…).

**Exemple simple :**

```
Entrée  →  Traitement  →  Sortie
  5         + 3          8
```

En Python, la **sortie** c’est souvent avec `print()` et l’**entrée** avec `input()`.

---

## 2. Le Hashbang (Linux)

Quand on écrit un programme sous Linux, tout en haut du fichier on peut mettre une **ligne spéciale** qui indique **quel interpréteur** doit l’exécuter.

Exemple pour Python :

```python
#!/usr/bin/env python3
```

- `#!` → hashbang (ou shebang).
- `/usr/bin/env python3` → dit au système : “utilise Python 3”.

📌 Si tu mets ça tout en haut, que tu rends ton fichier **exécutable** (`chmod +x monscript.py`), tu peux le lancer directement :

```bash
./monscript.py
```

… au lieu de taper `python monscript.py`.

---

## 3. Lancer un programme Python

**Méthode 1 :** via Python

```bash
python3 monscript.py
```

**Méthode 2 :** en script exécutable (Linux/macOS)

```bash
#!/usr/bin/env python3
print("Bonjour")
```

Puis :

```bash
chmod +x monscript.py
./monscript.py
```

---

## 4. La fonction `print()`

- **Rôle** : afficher un message ou une valeur à l’écran.
- **Syntaxe** :

```python
print("Bonjour le monde")
print(3 + 5)
```

- Tu peux afficher plusieurs choses :

```python
print("Résultat :", 3 + 5)
```

- Tu peux aussi afficher une variable :

```python
nom = "Alex"
print("Bonjour", nom)
```

📌 Par défaut, `print()` ajoute un **retour à la ligne** à la fin.

---

## 5. La fonction `input()`

- **Rôle** : demander une information à l’utilisateur (entrée).
- **Syntaxe** :

```python
nom = input("Quel est ton nom ? ")
print("Bonjour", nom)
```

- Attention : `input()` **retourne toujours une chaîne** (string), même si l’utilisateur tape un nombre.
- Pour transformer en nombre :

```python
age = int(input("Quel âge as-tu ? "))
print("L’année prochaine, tu auras", age + 1, "ans")
```

---

## 6. Exemple complet

```python
#!/usr/bin/env python3

print("=== Programme de bienvenue ===")
nom = input("Quel est ton prénom ? ")
print("Salut", nom, "!")

age = int(input("Quel âge as-tu ? "))
print("Dans 5 ans, tu auras", age + 5, "ans.")
```

---

## 7. Mini-exos à faire ensemble

1. Afficher “Hello, Minecraft!” avec `print()`.
2. Demander à l’utilisateur son pseudo et afficher “Bienvenue <pseudo>”.
3. Demander son âge, calculer l’année de naissance.
4. **Bonus** : afficher une ligne de tirets sous chaque message.

---

Si tu veux, je peux aussi te préparer pour le **Jour 1** :

- le **script Python prêt à exécuter** avec hashbang + exemples de `print` et `input`.
- une **fiche mémo A4** avec les commandes vues aujourd’hui.

Veux-tu que je fasse cette fiche mémo aussi ?
