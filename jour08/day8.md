# 📚 Jour 8 — Organiser le projet en modules (multifichiers)

## 🎯 Objectifs pédagogiques

1. Comprendre **modules** et **imports** (`import`, `from … import …`).
2. Structurer un petit projet en **plusieurs fichiers** : séparer **logique**, **accès fichiers**, **interface (menu)**.
3. Utiliser le point d’entrée `if __name__ == "__main__":` pour lancer l’app.
4. Ajouter **docstrings** et quelques **annotations de type** pour clarifier.

---

## 1) Théorie express

### 1.1 Module = fichier `.py`

- Un fichier Python peut être **importé** par un autre.
- Importer tout le module :

  ```python
  import utils
  utils.dire_bonjour("Alex")
  ```

- Importer une fonction précise :

  ```python
  from utils import dire_bonjour
  dire_bonjour("Alex")
  ```

### 1.2 Point d’entrée

```python
def main():
    print("Je lance l’appli")

if __name__ == "__main__":
    main()
```

- Quand on exécute le fichier directement → `main()` est appelé.
- Quand on l’importe → rien ne s’exécute automatiquement.

### 1.3 Docstrings & types

```python
def ajouter_contact(contacts: list[dict], nom: str, age: int, tel: str) -> None:
    """Ajoute un contact au tableau contacts."""
    contacts.append({"nom": nom, "age": age, "tel": tel})
```

---

## 2) Structure de dossiers proposée

```
carnet/
├─ main.py           # point d’entrée (menu)
├─ contacts.py       # logique métier (ajouter, chercher, afficher)
├─ storage.py        # lecture/écriture JSON
└─ typing_helpers.py # (optionnel) types alias
```

> Garde ça simple : 3 fichiers suffisent.

---

## 3) Squelettes de fichiers

### `storage.py` — persistance JSON

```python
import json
from pathlib import Path
from typing import Any

FICHIER = Path("contacts.json")

def charger() -> list[dict[str, Any]]:
    if not FICHIER.exists():
        return []
    with open(FICHIER, "r", encoding="utf-8") as f:
        return json.load(f)

def sauvegarder(contacts: list[dict[str, Any]]) -> None:
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)
```

### `contacts.py` — logique métier

```python
from typing import Any

def ajouter_contact(contacts: list[dict[str, Any]], nom: str, age: int, tel: str) -> None:
    contacts.append({"nom": nom.strip(), "age": int(age), "tel": tel.strip()})

def afficher_contacts(contacts: list[dict[str, Any]]) -> None:
    if not contacts:
        print("Aucun contact.")
        return
    for c in contacts:
        print(f"- {c['nom']} ({c['age']} ans) tel: {c['tel']}")

def chercher_contact(contacts: list[dict[str, Any]], nom: str) -> dict | None:
    nom = nom.strip()
    for c in contacts:
        if c["nom"].lower() == nom.lower():
            return c
    return None
```

### `main.py` — interface (menu)

```python
from storage import charger, sauvegarder
from contacts import ajouter_contact, afficher_contacts, chercher_contact

def menu():
    contacts = charger()
    while True:
        print("\n=== Carnet numérique ===")
        print("1) Ajouter un contact")
        print("2) Afficher tous les contacts")
        print("3) Rechercher un contact")
        print("4) Quitter")
        choix = input("> ").strip()

        if choix == "1":
            nom = input("Nom : ")
            age = input("Âge : ")
            tel = input("Téléphone : ")
            try:
                ajouter_contact(contacts, nom, int(age), tel)
                print("✅ Ajouté.")
            except ValueError:
                print("⚠️ Âge invalide.")
        elif choix == "2":
            afficher_contacts(contacts)
        elif choix == "3":
            nom = input("Nom à chercher : ")
            c = chercher_contact(contacts, nom)
            print(c if c else "Non trouvé.")
        elif choix == "4":
            sauvegarder(contacts)
            print("💾 Données sauvegardées. À bientôt !")
            break
        else:
            print("Choix invalide.")

def main():
    menu()

if __name__ == "__main__":
    main()
```

---

## 4) Déroulé pédagogique (1h)

1. **5–10 min** — Rappel (JSON, fonctions, f-strings).
2. **10–15 min** — Théorie modules/imports + `__main__`.
3. **20–25 min** — Refactor pas à pas :

   - créer `storage.py` (charger/sauvegarder),
   - déplacer la logique dans `contacts.py`,
   - alléger `main.py` (menu uniquement).

4. **10 min** — Test complet + petite amélioration (try/except sur âge).
5. **5 min** — Debrief : pourquoi c’est plus clair/maintenable.

---

## 5) Exos “après-cours”

- **E1** : Ajouter une option 5) **Supprimer un contact** par nom.
- **E2** : Ajouter une option 6) **Trier** l’affichage par nom.
- **E3** : Dans `storage.py`, faire un **backup** automatique `contacts.backup.json` avant sauvegarde.

---

## 6) Bonus (si à l’aise)

- Ajouter un **module `validators.py`** (valider tel/âge).
- Ajouter un **champ email** et un contrôle simple (`"@" in email`).
- Afficher un **compteur** : “X contacts chargés”.

.
