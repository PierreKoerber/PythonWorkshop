# 📚 Jour 10 — Finalisation, livraison & démo

## 🎯 Objectifs pédagogiques

1. Finaliser les fonctionnalités essentielles du projet
2. Polir l’expérience (messages, erreurs, aide CLI)
3. Préparer une **démo** courte et fluide
4. “Livrer” : README, export, sauvegarde, (optionnel) exécutable

---

## 1) Checklist “prêt à montrer”

### Fonctionnel

- [ ] **Menu interactif** opérationnel (`main.py`)
- [ ] Modules séparés : `contacts.py`, `storage.py`, `validators.py`, `log.py`
- [ ] **Lecture/écriture JSON** fiable (chemin personnalisable `--file`)
- [ ] **CLI** :

  - `--add "Nom,Age,Tel"`
  - `--search "Nom"`
  - `--export-csv chemin.csv`
  - `--quiet`

- [ ] **Validation** d’entrées (âge, champs non vides, tel)
- [ ] **Logs** basiques (démarrage, ajout, sauvegarde, erreurs)

### Qualité

- [ ] Messages utilisateurs clairs (pas de jargon)
- [ ] Aide CLI : `python main.py -h` affiche une description lisible
- [ ] **README.md** minimal (voir modèle ci-dessous)
- [ ] **Données de test** (2–3 contacts) pour la démo

---

## 2) README minimal (copier-coller)

````markdown
# Carnet numérique (projet fil rouge)

Petit programme en Python pour gérer des contacts (ajout, recherche, affichage), avec sauvegarde JSON et options en ligne de commande.

## Lancer (menu)

```bash
python main.py
```

## Fichier de données

Par défaut `contacts.json`. Personnalisable :

```bash
python main.py --file data/mes_contacts.json
```

## Actions rapides (CLI)

- Ajouter :

```bash
python main.py --add "Alex,14,123"
```

- Rechercher :

```bash
python main.py --search "Alex"
```

- Export CSV :

```bash
python main.py --export-csv contacts.csv
```

- Mode silencieux :

```bash
python main.py --search "Alex" --quiet
```

## Structure

- `main.py` — menu + CLI
- `contacts.py` — logique (ajouter, afficher, chercher)
- `storage.py` — lecture/écriture JSON (chemin paramétrable)
- `validators.py` — vérifs d’entrées
- `log.py` — journalisation simple

## Prérequis

Python 3.10+ (aucune dépendance externe)

## Idées d’amélioration

- suppression / édition d’un contact
- champ email + validation
- tri et pagination de l’affichage
````

---

## 3) Script de démo (2–3 minutes)

1. **Intro (10s)** : “Voici mon carnet numérique en Python.”
2. **Menu** : lancer `python main.py`, montrer les 4 choix.
3. **Ajouter** 1 contact via **menu** (Nom/Âge/Tel).
4. **Afficher** tous les contacts.
5. **Recherche** via **CLI** :

   ```bash
   python main.py --search "Alex"
   ```

6. **Ajouter** via **CLI** (montre la vitesse) :

   ```bash
   python main.py --add "Marie,15,456"
   ```

7. **Export CSV** :

   ```bash
   python main.py --export-csv contacts.csv
   ```

8. **Sauvegarde & sortie** (retour menu → Quitter).
9. **Conclusion (10s)** : “Données JSON, modules, validation, logs.”

💡 Astuce : prépare un **contacts.json** initial avec 1–2 entrées pour éviter le “vide”.

---

## 4) Tests “fumée” rapides (1 minute)

Exécuter un mini-script (ou à la main) :

```bash
python - <<'PY'
from contacts import ajouter_contact, chercher_contact
data=[]
ajouter_contact(data,"Test",14,"123")
assert chercher_contact(data,"test")["tel"]=="123"
print("✅ Tests OK")
PY
```

---

## 5) (Optionnel) Packaging exécutable

Si vous voulez un **.exe / binaire** local (Windows/macOS/Linux) :

```bash
pip install pyinstaller
pyinstaller --onefile main.py
# Binaire dans dist/main
```

> Garde le JSON dans le **même dossier** que l’exécutable, et utilise `--file` pour pointer vers un chemin précis si besoin.

---

## 6) Planning 1h (séance Jour 10)

- **10 min** — Revue finale : relire la checklist, corriger 1–2 messages
- **15 min** — Rédiger/peaufiner le **README** (copier-coller + ajuster)
- **15 min** — Répéter **le script de démo** une fois
- **10 min** — (Optionnel) PyInstaller / export CSV / création d’un dossier “release”
- **10 min** — Présentation à la famille (ou capture vidéo)

---

## 7) Dossier “release” (à remettre / montrer)

```
release/
├─ main (ou main.exe)
├─ contacts.json      # données de démo
├─ contacts.csv       # export
└─ README.md
```

---

## 8) Extensions (après le cycle)

- **Supprimer/éditer** un contact
- **Email** et **validation** (regex simple ou vérifs basiques)
- **Tri** par nom/âge (`sorted`)
- **Stats** : nombre de contacts par tranche d’âge
- **Interface graphique** (Tkinter) — réutiliser l’idée du pack simple J7/J10

---
