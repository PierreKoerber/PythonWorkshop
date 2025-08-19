# Pack Ultra Simple — 10 jours (14 ans)

Zéro dépendance externe. Tout en Python standard (Tkinter inclus).  
Lancez chaque jour :

```bash
python jour1/hello.py
```

## Conversion d'un md ne présentation powerpoint

pandoc chapitres.md -t pptx -o presentation.pptx

## Bonus - jupyter notebook

https://jupyter.org/try-jupyter/lab/

## Contenu rapide

---

### 📚 Jour 1 — Découvrir Python & l’ordinateur

- Comprendre comment un programme est lancé.
- Savoir ce qu’est un **hashbang** sur Linux.
- Apprendre la notion d’**entrée** et de **sortie** dans un programme.
- Utiliser `print()` et `input()`.

---

### 📚 Jour 2 — Variables, Calculs, Fonctions & Découverte Hardware

1. Manipuler des variables et faire des calculs simples.
2. Comprendre et utiliser des fonctions.
3. Savoir mettre des fonctions dans un fichier réutilisable.
4. Découvrir les connecteurs principaux d’un ordinateur et leur rôle.

---

### 📚 Jour 3 — Fichiers, Types, Fonctions avancées, Boucles

1. Lire et écrire dans un fichier (`config.json` ou `.txt`).
2. Comprendre le **typage** des paramètres dans une fonction.
3. Retourner **plusieurs valeurs** depuis une fonction.
4. Découvrir les **fonctions récursives**.
5. Introduction aux **boucles** (`for`, `while`).
6. Connaître les **types de base** de Python.

---

### 📚 Jour 4 — Conditions, Opérateurs logiques, Mini-projet "Jeu du nombre"

1. Comprendre **les conditions** (`if`, `elif`, `else`).
2. Découvrir les **opérateurs logiques** (`and`, `or`, `not`).
3. Utiliser les **opérateurs de comparaison** (`==`, `!=`, `<`, `>`, `<=`, `>=`).
4. Introduire les **conditions imbriquées**.
5. Réaliser un **mini-projet interactif** pour appliquer ces notions.

---

### 📚 Jour 5 — Listes et Dictionnaires

1. Comprendre ce qu’est une **liste** (`list`) et comment l’utiliser.
2. Comprendre ce qu’est un **dictionnaire** (`dict`) et son intérêt.
3. Savoir **ajouter, modifier, supprimer** des éléments.
4. Parcourir ces structures avec une **boucle `for`**.
5. Appliquer tout ça dans un **mini-projet concret**.

---

### 📚 Jour 6 — Lire et écrire des fichiers en Python

1. Comprendre **ce qu’est un fichier** et comment l’ordinateur l’utilise.
2. Savoir **lire** un fichier texte en Python.
3. Savoir **écrire** ou **ajouter** des données dans un fichier texte.
4. Comprendre la différence entre **modes d’ouverture** (`"r"`, `"w"`, `"a"`, `"x"`).
5. Manipuler des fichiers **JSON** pour stocker des données structurées.

---

### 📚 Jour 7 — Dictionnaires & Données structurées

1. Comprendre ce qu’est un **dictionnaire** (`dict`) en Python.
2. Savoir stocker des **paires clé/valeur**.
3. Manipuler des **listes de dictionnaires** (comme une mini-base de données).
4. Relier ça avec les fichiers JSON.
5. Construire une **première “base de contacts”** avec recherche simple.

---

### 📚 Jour 8 — Organiser le projet en modules (multifichiers)

1. Comprendre **modules** et **imports** (`import`, `from … import …`).
2. Structurer un petit projet en **plusieurs fichiers** : séparer **logique**, **accès fichiers**, **interface (menu)**.
3. Utiliser le point d’entrée `if __name__ == "__main__":` pour lancer l’app.
4. Ajouter **docstrings** et quelques **annotations de type** pour clarifier.

---

### 📚 Jour 9 — Robustesse : erreurs, validation, sauvegarde sûre, tests

1. Comprendre les **exceptions** et `try / except / else / finally`.
2. Valider proprement les **entrées utilisateur** (nombres, champs obligatoires, formats).
3. Sécuriser la **sauvegarde des fichiers** (backup, écriture atomique).
4. Ajouter un **journal** (_logging_) simple pour diagnostiquer.
5. Écrire **quelques tests** de base pour vérifier les fonctions clés.
