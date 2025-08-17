# 📚 Jour 7 — Dictionnaires & Données structurées

---

## 🎯 Objectifs pédagogiques

1. Comprendre ce qu’est un **dictionnaire** (`dict`) en Python.
2. Savoir stocker des **paires clé/valeur**.
3. Manipuler des **listes de dictionnaires** (comme une mini-base de données).
4. Relier ça avec les fichiers JSON.
5. Construire une **première “base de contacts”** avec recherche simple.

---

## 1️⃣ Théorie

### 1.1 Le dictionnaire (`dict`)

Un **dictionnaire** associe une **clé** à une **valeur**.

```python
# Exemple
personne = {
    "nom": "Alex",
    "age": 14,
    "ville": "Lausanne"
}
print(personne["nom"])   # Alex
```

💡 Différence avec une liste :

- Liste = ordre, index (`[0]`, `[1]`…)
- Dictionnaire = clé descriptive (`["nom"]`, `["age"]`)

---

### 1.2 Ajouter / modifier

```python
personne["hobby"] = "Minecraft"   # ajout
personne["age"] = 15              # modification
```

---

### 1.3 Parcourir un dictionnaire

```python
for cle, valeur in personne.items():
    print(f"{cle} : {valeur}")
```

---

### 1.4 Listes de dictionnaires

Un **carnet de contacts** :

```python
contacts = [
    {"nom": "Alex", "age": 14, "tel": "123"},
    {"nom": "Marie", "age": 15, "tel": "456"}
]

print(contacts[0]["nom"])  # Alex
```

---

### 1.5 Recherche simple

```python
nom_recherche = "Marie"
for c in contacts:
    if c["nom"] == nom_recherche:
        print(f"Trouvé : {c['tel']}")
```

---

### 1.6 Avec JSON

```python
import json

# Sauvegarde
with open("contacts.json", "w", encoding="utf-8") as f:
    json.dump(contacts, f, indent=2, ensure_ascii=False)

# Lecture
with open("contacts.json", "r", encoding="utf-8") as f:
    contacts = json.load(f)
```

---

## 2️⃣ Exemple guidé

Créer une **petite base de données** :

```python
contacts = []

def ajouter_contact(nom, age, tel):
    contacts.append({"nom": nom, "age": age, "tel": tel})

ajouter_contact("Alex", 14, "123")
ajouter_contact("Marie", 15, "456")

print(contacts)
```

---

## 3️⃣ Mini-projet du jour — Carnet d’adresses évolué

1. Ajouter plusieurs contacts avec une fonction `ajouter_contact`.
2. Sauvegarder automatiquement en `contacts.json`.
3. Pouvoir rechercher un contact par nom.
4. Afficher tous les contacts joliment.

---

## 4️⃣ Exercices

1. Crée un dictionnaire `drone` avec `marque`, `poids`, `autonomie`. Affiche toutes ses infos.
2. Crée une **liste de jeux vidéo** avec leur `nom` et `note`. Affiche la moyenne des notes.
3. Modifie un contact dans la liste en changeant son numéro.
4. Ajoute une fonction `supprimer_contact(nom)` qui enlève une entrée.

---

## 5️⃣ Bonus (si motivé)

- Trier les contacts par âge (`sorted`).
- Exporter la base en `.json` et la rouvrir dans un autre programme.

---

👉 Cette journée est très importante car elle montre à ton fils qu’il peut manipuler des **collections d’objets complexes** comme le font les “vrais” programmes (inventaires de jeux, bases de données de joueurs, etc.).
