---
# 🗂 Projet fil rouge : Carnet numérique
---

## 🎯 Objectif final

Un programme Python qui permet de :

- Ajouter des contacts (nom, prénom, âge, téléphone, email).
- Les sauvegarder automatiquement dans un fichier JSON.
- Relire les contacts au démarrage.
- Rechercher un contact par son nom.
- Afficher tous les contacts.
- Bonus : supprimer un contact, trier les contacts.

---

## 📆 Étapes par jour

### 🔹 Jour 1 : Premiers pas

- **Notions** : print, input, hashbang, exécution d’un programme.
- **Tâche projet** : écrire un programme qui dit _“Bienvenue dans ton carnet numérique”_ et demande ton nom.

---

### 🔹 Jour 2 : Variables et fonctions simples

- **Notions** : variables, calculs, définir une fonction simple.
- **Tâche projet** : créer une fonction `demander_contact()` qui demande le **nom** et l’**âge** d’un contact, puis l’affiche avec `print`.

---

### 🔹 Jour 3 : Types de données + fichiers

- **Notions** : int, string, listes, dict, return, boucles, fonctions récursives.
- **Tâche projet** : améliorer `demander_contact()` pour renvoyer un **dictionnaire** :

  ```python
  {"nom": "Alex", "age": 14}
  ```

  et stocker les contacts dans une liste.

---

### 🔹 Jour 4 : Boucles

- **Notions** : `for`, `while`.
- **Tâche projet** : créer une boucle qui permet d’ajouter **plusieurs contacts** tant que l’utilisateur veut.

---

### 🔹 Jour 5 : Listes et tuples

- **Notions** : opérations sur les listes, tuples.
- **Tâche projet** : écrire une fonction `afficher_contacts()` qui parcourt la liste et affiche chaque contact joliment.

---

### 🔹 Jour 6 : Fichiers + JSON + fonctions réutilisables

- **Notions** : lire/écrire un fichier, JSON, f-strings.
- **Tâche projet** : sauvegarder la liste des contacts dans un fichier `contacts.json`, puis la recharger au lancement.

---

### 🔹 Jour 7 : Dictionnaires et données structurées

- **Notions** : dict, listes de dicts, recherche.
- **Tâche projet** : ajouter une fonction `chercher_contact(nom)` qui affiche le contact si trouvé.

---

### 🔹 Jour 8 : Organisation du code

- **Notions** : séparer le code en plusieurs fichiers (`main.py`, `utils.py`).
- **Tâche projet** : déplacer les fonctions (`ajouter_contact`, `afficher_contacts`, `chercher_contact`) dans `utils.py`.

---

### 🔹 Jour 9 : Gestion d’erreurs

- **Notions** : `try/except`, validation d’entrées.
- **Tâche projet** : vérifier que l’âge saisi est bien un nombre. Si l’utilisateur entre autre chose, afficher un message d’erreur et redemander.

---

### 🔹 Jour 10 : Finalisation et présentation

- **Notions** : revoir l’ensemble, ajouter des bonus (supprimer contact, trier).
- **Tâche projet** : proposer un **menu interactif** :

  ```
  1 - Ajouter un contact
  2 - Afficher tous les contacts
  3 - Rechercher un contact
  4 - Quitter
  ```

- Sauvegarder automatiquement les données quand on quitte.

---

## 🚀 Résultat final

À la fin des 10 jours, il aura une **mini-application console complète** :

- avec un **menu interactif**,
- des **fonctions bien organisées**,
- et des **données persistantes en JSON**.

👉 C’est concret : il pourra montrer son programme à ses amis/famille comme une “vraie app” 🎉
