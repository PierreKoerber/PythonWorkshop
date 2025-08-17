Super question 👍
On reprend doucement et **pas à pas**, comme tu pourras l’expliquer à ton fils.

---

# 📦 Manipuler du JSON dans un fichier en Python

---

## 1️⃣ Qu’est-ce que JSON ?

- **JSON = JavaScript Object Notation**
- C’est juste du **texte formaté** pour représenter des données.
- Ressemble beaucoup aux dictionnaires et listes Python.

Exemple de JSON (dans un fichier `contacts.json`) :

```json
[
  {
    "nom": "Alex",
    "age": 14,
    "tel": "123"
  },
  {
    "nom": "Marie",
    "age": 15,
    "tel": "456"
  }
]
```

---

## 2️⃣ Sauvegarder du JSON dans un fichier

### Exemple en Python

```python
import json

# Une liste de dictionnaires (contacts)
contacts = [
    {"nom": "Alex", "age": 14, "tel": "123"},
    {"nom": "Marie", "age": 15, "tel": "456"}
]

# On ouvre un fichier en mode écriture
with open("contacts.json", "w", encoding="utf-8") as f:
    json.dump(contacts, f, indent=2, ensure_ascii=False)
```

### Résultat dans `contacts.json`

```json
[
  {
    "nom": "Alex",
    "age": 14,
    "tel": "123"
  },
  {
    "nom": "Marie",
    "age": 15,
    "tel": "456"
  }
]
```

💡 Paramètres utiles :

- `indent=2` → rend le fichier lisible (espaces indentés)
- `ensure_ascii=False` → garde les accents (utile pour le français)

---

## 3️⃣ Relire du JSON depuis un fichier

### Exemple

```python
import json

with open("contacts.json", "r", encoding="utf-8") as f:
    contacts = json.load(f)

print(contacts)           # affiche la liste complète
print(contacts[0]["nom"]) # affiche "Alex"
```

---

## 4️⃣ Résumé visuel

1. **Python → JSON (sauvegarde)**

   - `json.dump(objet_python, fichier)`

2. **JSON → Python (lecture)**

   - `json.load(fichier)`

---

## 5️⃣ Mini-exercice

1. Crée une liste de jeux vidéo (titre + note).
2. Sauvegarde-la en JSON.
3. Relis le fichier et affiche la note du premier jeu.
