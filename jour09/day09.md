# 📚 Jour 9 — Robustesse : erreurs, validation, sauvegarde sûre, tests

## 🎯 Objectifs pédagogiques

1. Comprendre les **exceptions** et `try / except / else / finally`.
2. Valider proprement les **entrées utilisateur** (nombres, champs obligatoires, formats).
3. Sécuriser la **sauvegarde des fichiers** (backup, écriture atomique).
4. Ajouter un **journal** (_logging_) simple pour diagnostiquer.
5. Écrire **quelques tests** de base pour vérifier les fonctions clés.

---

## 1) Théorie express

### 1.1 Exceptions

- Une **exception** interrompt le programme quand quelque chose ne va pas.
- On la **rattrape** avec `try/except`.

```python
try:
    age = int(input("Âge : "))
    print(2025 - age)
except ValueError:
    print("⚠️ Entre un nombre valide.")
```

`else` s’exécute si **aucune** exception, `finally` s’exécute **toujours**.

```python
try:
    f = open("data.txt")
except FileNotFoundError:
    print("Fichier introuvable")
else:
    print("Lecture OK")
finally:
    try: f.close()
    except: pass
```

### 1.2 Lever une exception

```python
def age_valide(age: int) -> bool:
    if age < 0 or age > 120:
        raise ValueError("Âge incohérent")
    return True
```

---

## 2) Validation d’entrées (module `validators.py`)

Créez un petit module commun pour centraliser vos contrôles.

```python
# validators.py
def not_empty(s: str) -> str:
    s = (s or "").strip()
    if not s:
        raise ValueError("Champ obligatoire")
    return s

def parse_int(s: str) -> int:
    try:
        return int(s.strip())
    except Exception:
        raise ValueError("Nombre invalide")

def age_valide(age: int) -> int:
    if age < 0 or age > 120:
        raise ValueError("Âge incohérent (0-120)")
    return age

def tel_simple(t: str) -> str:
    t = t.strip()
    if len(t) < 3:
        raise ValueError("Téléphone trop court")
    return t
```

**Boucle d’entrée sûre** (réutilisable) :

````python
def demander(prompt: str, parser):
    while True:
        try:
            return parser(input(prompt))
        except ValueError as e:
            print

---

## 3) Sauvegarde sûre (module `storage.py`)

* **Backup** avant écriture (`contacts.backup.json`).
* **Écriture atomique** : écrire dans un fichier **temporaire** puis **renommer**.

```python
# storage.py
import json, os
from pathlib import Path
from typing import Any

FICHIER = Path("contacts.json")
TMP = Path("contacts.tmp.json")
BACKUP = Path("contacts.backup.json")

def charger() -> list[dict[str, Any]]:
    if not FICHIER.exists():
        return []
    with open(FICHIER, "r", encoding="utf-8") as f:
        return json.load(f)

def sauvegarder(contacts: list[dict[str, Any]]) -> None:
    # 1) backup
    if FICHIER.exists():
        FICHIER.replace(BACKUP)
    # 2) écrire dans un temp
    with open(TMP, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)
    # 3) remplacer atomiquement
    os.replace(TMP, FICHIER)
````

---

## 4) Logging simple (module `log.py`)

Un fichier `app.log` avec date/heure pour suivre ce qu’il se passe.

```python
# log.py
from datetime import datetime
from pathlib import Path

LOG = Path("app.log")

def log(msg: str):
    if LOG.exists():
        LOG.open("a", encoding="utf-8").write(f"[{ts}] {msg}\n")
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        LOG.write_text(f"[{ts}] {msg}\n", encoding="utf-8")
```

Utilisation :

```python
from log import log
log("Démarrage de l’application")
log("Sauvegarde réussie")
```

---

## 5) Intégration au menu (`main.py`)

- Entrées **robustes** via `demander()` + `validators`.
- Logs aux moments clés (ajout, recherche, sauvegarde).

```python
from storage import charger, sauvegarder
from contacts import ajouter_contact, afficher_contacts, chercher_contact
from validators import demander, not_empty, parse_int, age_valide, tel_simple
from log import log

def menu():
    contacts = charger()
    log("App lancée")

    while True:
        print("\n=== Carnet numérique ===")
        print("1) Ajouter un contact")
        print("2) Afficher tous les contacts")
        print("3) Chercher un contact")
        print("4) Quitter")
        choix = input("> ").strip()

        if choix == "1":
            nom = demander("Nom : ", not_empty)
            age = age_valide(demander("Âge : ", parse_int))
            tel = demander("Téléphone : ", tel_simple)
            ajouter_contact(contacts, nom, age, tel)
            log(f"Ajout contact: {nom}")
            print("✅ Ajouté.")
        elif choix == "2":
            afficher_contacts(contacts)
        elif choix == "3":
            q = demander("Nom à chercher : ", not_empty)
            c = chercher_contact(contacts, q)
            print(c if c else "Non trouvé.")
        elif choix == "4":
            sauvegarder(contacts)
            log("Sauvegarde et sortie")
            print("💾 Données sauvegardées. À bientôt !")
            break
        else:
            print("Choix invalide.")
```

---

## 6) Mini-tests (sans framework)

Un petit script `tests_smoke.py` pour vérifier les fonctions clés.

```python
# tests_smoke.py
from contacts import ajouter_contact, chercher_contact, afficher_contacts

def run():
    data = []
    ajouter_contact(data, "Alex", 14, "123")
    assert chercher_contact(data, "alex")["tel"] == "123"
    afficher_contacts(data)  # devrait afficher 1 contact
    print("✅ Tests de base OK")

if __name__ == "__main__":
    run()
```

> Si vous voulez aller plus loin : découvrir `unittest` ou `pytest` plus tard.

---

## 7) Déroulé pédagogique (1h)

1. **10 min** — Exceptions & `try/except`, pourquoi valider tôt.
2. **15 min** — Implémenter `validators.py` + intégration dans `main.py`.
3. **15 min** — Sauvegarde sûre (backup + atomique).
4. **10 min** — Logging simple.
5. **10 min** — Mini-tests et démo “erreur maîtrisée”.

---

## 8) Exos “après-cours”

- **E1** : Ajouter validation d’**email** (doit contenir `@` et un `.` après).
- **E2** : Logger les **tentatives invalides** (entrées vides, âge invalide).
- **E3** : Simuler une **erreur de lecture JSON** (fichier corrompu) et gérer proprement en revenant à une liste vide avec un message clair.
- **E4** : Afficher “**X contacts chargés**” au démarrage (avec log).
