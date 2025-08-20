---

# 🔧 Ajout : paramètres dans `__main__` (CLI)

## Pourquoi ?

- Lancer des **actions rapides** sans passer par le menu (ex. ajouter un contact en 1 ligne).
- **Changer le chemin** du fichier de données.
- Faire des **imports/exports** automatisés.

## Outils

- `if __name__ == "__main__":` : point d’entrée du script.
- `argparse` : parseur d’arguments.
- (optionnel) `sys.argv` pour montrer la base, mais on privilégie `argparse`.

## Modèle d’arguments (exemples)

- `--file contacts.json` : choisir le fichier de données
- `--add "Nom,Age,Tel"` : ajouter un contact depuis la CLI
- `--search "Nom"` : rechercher et afficher
- `--export-csv contacts.csv` : exporter en CSV
- `--quiet` : mode silencieux (moins de prints)
- Sans argument → **mode menu interactif** (comportement par défaut)

### Exemple prêt à coller (`main.py`)

```python
# main.py
import argparse
from storage import charger, sauvegarder
from contacts import ajouter_contact, afficher_contacts, chercher_contact

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Carnet numérique (CLI + menu)")
    p.add_argument("--file", default="contacts.json", help="Chemin du fichier JSON")
    p.add_argument("--add", help='Ajouter un contact "Nom,Age,Tel"')
    p.add_argument("--search", help='Rechercher par nom (affiche et quitte)')
    p.add_argument("--export-csv", dest="export_csv", help="Exporter en CSV (chemin)")
    p.add_argument("--quiet", action="store_true", help="Mode silencieux")
    return p

def export_csv(contacts, path):
    import csv
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["nom","age","tel"])
        for c in contacts:
            w.writerow([c.get("nom",""), c.get("age",""), c.get("tel","")])

def run_menu(contacts, datafile):
    while True:
        print("\n=== Carnet numérique ===")
        print("1) Ajouter un contact")
        print("2) Afficher tous les contacts")
        print("3) Rechercher un contact")
        print("4) Quitter")
        choix = input("> ").strip()
        if choix == "1":
            nom = input("Nom : ")
            age = int(input("Âge : "))
            tel = input("Téléphone : ")
            ajouter_contact(contacts, nom, age, tel)
            print("✅ Ajouté.")
        elif choix == "2":
            afficher_contacts(contacts)
        elif choix == "3":
            q = input("Nom à chercher : ")
            c = chercher_contact(contacts, q)
            print(c if c else "Non trouvé.")
        elif choix == "4":
            sauvegarder(contacts, datafile)  # ← version storage acceptant un chemin
            print("💾 Données sauvegardées. À bientôt !")
            break
        else:
            print("Choix invalide.")

def main():
    parser = build_parser()
    args = parser.parse_args()

    # Charger avec chemin personnalisé
    contacts = charger(args.file)

    # Mode non-interactif si des flags sont fournis
    if args.add or args.search or args.export_csv:
        if args.add:
            try:
                nom, age, tel = [x.strip() for x in args.add.split(",", 2)]
                ajouter_contact(contacts, nom, int(age), tel)
                if not args.quiet:
                    print(f"Ajouté: {nom} ({age}) {tel}")
            except Exception as e:
                parser.error(f'--add doit être "Nom,Age,Tel" (erreur: {e})')
        if args.search:
            c = chercher_contact(contacts, args.search)
            if not args.quiet:
                print(c if c else "Non trouvé.")
        if args.export_csv:
            export_csv(contacts, args.export_csv)
            if not args.quiet:
                print(f"Exporté vers {args.export_csv}")
        # Sauvegarder si on a modifié
        if args.add:
            sauvegarder(contacts, args.file)
        return

    # Sinon, mode menu interactif
    run_menu(contacts, args.file)

if __name__ == "__main__":
    main()
```

> ⚠️ Mets à jour `storage.py` pour accepter un **chemin** :

```python
# storage.py
import json
from pathlib import Path
from typing import Any

def charger(path: str | Path) -> list[dict[str, Any]]:
    p = Path(path)
    if not p.exists():
        return []
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def sauvegarder(contacts: list[dict[str, Any]], path: str | Path) -> None:
    p = Path(path)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)
```

---

# 🔁 Plan régénéré (Jours 8 & 9 avec CLI)

## 📚 Jour 8 — Organisation en modules + Entrée CLI basique

**Objectifs**

- Modules & imports ; point d’entrée `__main__`.
- Séparer `main.py`, `contacts.py`, `storage.py`.
- **Introduire `argparse`** et un flag simple : `--file`.

**Déroulé (1h)**

1. (10’) Rappel modules / `__main__`.
2. (15’) Refactor : `storage.py` (charger/sauvegarder avec chemin).
3. (15’) `main.py` : `argparse` minimal (`--file`).
4. (20’) Test : lancer avec un fichier custom, vérifier lecture/écriture.

**Exercices**

- E1 : Ajouter `--quiet` (réduire les prints).
- E2 : Afficher le nombre de contacts chargés au démarrage.

---

## 📚 Jour 9 — Robustesse + CLI avancée (actions sans menu)

**Objectifs**

- Exceptions, validation.
- **Flags d’action** : `--add`, `--search`, `--export-csv`.
- Sauvegarde sûre, logs, petits tests.

**Déroulé (1h)**

1. (10’) Exceptions & validation (rappel selon ton plan existant).
2. (20’) Ajouter flags : `--add "Nom,Age,Tel"`, `--search`, `--export-csv`.
3. (15’) Sauvegarde et logs (si modifié → sauvegarder).
4. (15’) Tests rapides (ajout, recherche, export).

**Exercices**

- E1 : `--import-json fichier.json` (fusionner avec les contacts).
- E2 : Conflits nom → demander stratégie (`--on-duplicate keep|replace|skip`).
- E3 : Erreurs contrôlées si format `--add` incorrect.

---

## 🧪 Exemples d’utilisation

- Menu normal :

  ```bash
  python main.py
  ```

- Fichier custom + ajout direct :

  ```bash
  python main.py --file data/contacts.json --add "Alex,14,123"
  ```

- Recherche silencieuse (utilisable dans un script) :

  ```bash
  python main.py --search "Alex" --quiet
  ```

- Export CSV :

  ```bash
  python main.py --export-csv contacts.csv
  ```
