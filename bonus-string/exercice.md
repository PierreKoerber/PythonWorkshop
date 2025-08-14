génial — voici un paquet d’**exercices progressifs** sur les **chaînes de caractères** qui **écrivent/lisent** aussi des fichiers. Chaque exercice a :

- l’**objectif**,
- un **hint (indice)**,
- un **squelette de code**,
- et parfois un **plus** (extension).

Si tu veux, je peux te fournir ensuite un **corrigé** complet pour chacun.

---

# 🎯 Exercices “strings + fichiers”

## 1) Compter les lettres d’un prénom

**Objectif :** demander un prénom, afficher sa longueur, sauvegarder le résultat.
**Fichier :** `resultats/longueur_prenom.txt`

```python
from pathlib import Path
Path("resultats").mkdir(exist_ok=True)

prenom = input("Ton prénom : ").strip()
longueur = len(prenom)

print(f"Longueur = {longueur}")
(Path("resultats/longueur_prenom.txt")
 .write_text(f"{prenom}:{longueur}\n", encoding="utf-8"))
```

**Plus :** si le fichier existe, ajoute au lieu d’écraser (mode append : `open(..., "a")`).

---

## 2) Nettoyer une phrase et la sauvegarder

**Objectif :** demander une phrase, enlever espaces début/fin, la passer en minuscules et la **sauvegarder propre**.
**Fichier :** `resultats/phrase_propre.txt`
**Hint :** `.strip()`, `.lower()`

```python
from pathlib import Path
phrase = input("Écris une phrase : ")
propre = phrase.strip().lower()

Path("resultats").mkdir(exist_ok=True)
with open("resultats/phrase_propre.txt", "w", encoding="utf-8") as f:
    f.write(propre + "\n")
```

---

## 3) Découper en mots et compter

**Objectif :** lire `resultats/phrase_propre.txt`, afficher le **nombre de mots** et sauvegarder la liste des mots.
**Fichier :** `resultats/mots.txt`
**Hint :** `.split()`, `"\n".join(...)`

```python
from pathlib import Path
texte = Path("resultats/phrase_propre.txt").read_text(encoding="utf-8")
mots = texte.split()
print("Nombre de mots :", len(mots))

Path("resultats/mots.txt").write_text("\n".join(mots), encoding="utf-8")
```

**Plus :** afficher le mot le plus long.

---

## 4) Trouver/Remplacer un mot “interdit”

**Objectif :** demander un mot à censurer, le remplacer par `***`, sauvegarder le texte modifié.
**Fichier :** `resultats/phrase_censuree.txt`
**Hint :** `.replace(old, new)`

```python
from pathlib import Path
texte = Path("resultats/phrase_propre.txt").read_text(encoding="utf-8")
cible = input("Mot à censurer : ").strip().lower()
modifie = texte.replace(cible, "***")
Path("resultats/phrase_censuree.txt").write_text(modifie, encoding="utf-8")
```

**Plus :** ne censurer que des **mots entiers** (piste : `split`, puis reconstruire).

---

## 5) Palindrome simple

**Objectif :** demander un mot, dire s’il se lit pareil à l’endroit et à l’envers, loguer le résultat.
**Fichier (append) :** `resultats/palindromes.log`
**Hint :** `mot[::-1]` (slice inverse)

```python
from pathlib import Path
Path("resultats").mkdir(exist_ok=True)

mot = input("Mot : ").strip().lower()
est_pal = (mot == mot[::-1])
ligne = f"{mot};{est_pal}\n"

with open("resultats/palindromes.log", "a", encoding="utf-8") as f:
    f.write(ligne)

print("Palindrome ?", est_pal)
```

---

## 6) Générer un identifiant à partir nom+prénom

**Objectif :** `prenom.nomYY` (YY = 2 derniers chiffres de l’année de naissance calculée).
**Fichier (append) :** `resultats/users.csv` (CSV “prenom,nom,age,identifiant”)
**Hints :** `.lower()`, `f-strings`, `,`.

```python
from pathlib import Path
prenom = input("Prénom : ").strip()
nom = input("Nom : ").strip()
age = int(input("Âge : ").strip())

annee = 2025 - age
identifiant = f"{prenom.lower()}.{nom.lower()}{str(annee)[-2:]}"

Path("resultats").mkdir(exist_ok=True)
with open("resultats/users.csv", "a", encoding="utf-8") as f:
    f.write(f"{prenom},{nom},{age},{identifiant}\n")

print("ID généré :", identifiant)
```

**Plus :** empêcher les espaces/accents dans l’identifiant (remplacer par `-`).

---

## 7) “Dictionnaire de profil” → JSON

**Objectif :** demander plusieurs champs et **sauver un dict** en JSON.
**Fichier :** `resultats/profil.json`
**Hints :** module `json`, `json.dump(...)`

```python
import json
from pathlib import Path

profil = {
    "prenom": input("Prénom : ").strip(),
    "nom": input("Nom : ").strip(),
    "ville": input("Ville : ").strip(),
    "centres_interet": input("Centres d'intérêt (séparés par ,) : ").split(",")
}

with open("resultats/profil.json", "w", encoding="utf-8") as f:
    json.dump(profil, f, indent=2, ensure_ascii=False)

print("Profil enregistré.")
```

**Plus :** relire le JSON et afficher joliment chaque champ.

---

## 8) Nettoyer un “journal de chat” et compter les emojis

**Objectif :** demander 3 messages, les **nettoyer** (strip), stocker un par ligne, compter le nombre de `🙂` et `😂`.
**Fichier :** `resultats/chat.txt`

```python
from pathlib import Path
msgs = []
for i in range(3):
    m = input(f"Message {i+1} : ").strip()
    msgs.append(m)

texte = "\n".join(msgs)
Path("resultats/chat.txt").write_text(texte, encoding="utf-8")

nb_smile = texte.count("🙂")
nb_lol = texte.count("😂")
print("🙂 :", nb_smile, "| 😂 :", nb_lol)
```

**Plus :** convertir tout en minuscules sauf les emojis.

---

## 9) Index des mots → positions

**Objectif :** lire `resultats/phrase_propre.txt`, construire un **index** {mot: position(s)}, sauver en JSON.
**Fichier :** `resultats/index_mots.json`
**Hints :** `enumerate`, `dict.setdefault`

```python
import json
from pathlib import Path
texte = Path("resultats/phrase_propre.txt").read_text(encoding="utf-8")
mots = texte.split()

index = {}
for pos, mot in enumerate(mots):
    index.setdefault(mot, []).append(pos)

with open("resultats/index_mots.json", "w", encoding="utf-8") as f:
    json.dump(index, f, indent=2, ensure_ascii=False)

print("Index créé.")
```

**Plus :** ignorer la ponctuation (piste : `str.strip(",.;!?")` avant d’indexer).

---

## 10) Template de “carte joueur” avec f-string

**Objectif :** demander pseudo, jeu préféré, niveau (texte), générer un **fichier carte** formaté joliment.
**Fichier :** `resultats/carte_joueur.txt`

```python
from pathlib import Path
pseudo = input("Pseudo : ").strip()
jeu = input("Jeu préféré : ").strip()
niveau = input("Niveau (débutant/intermédiaire/expert) : ").strip().lower()

modele = f"""
========== CARTE JOUEUR ==========
Pseudo      : {pseudo}
Jeu préféré : {jeu}
Niveau      : {niveau.title()}
==================================
"""

Path("resultats/carte_joueur.txt").write_text(modele.strip()+"\n", encoding="utf-8")
print("Carte générée.")
```

**Plus :** ajouter la date/heure (piste : `from datetime import datetime`).

---

## Bonus “thème Minecraft/CS”

- **Pseudo safe** : remplace espaces/accents → `-` ; tout en minuscules.
- **Fichier de “whitelist”** : ajoute un pseudo par ligne dans `whitelist.txt`, évite les doublons (relis, teste `if pseudo in texte`).
- **Stats** : à partir de lignes `kill:3, death:2`, extraire les valeurs avec `split(",")` puis `split(":")`, calculer K/D et sauvegarder.

---

Si tu veux, je peux te livrer un **petit bundle “exos_strings” prêt à exécuter** (un fichier `.py` par exercice + un `README.md`) pour que ton fils puisse les faire sans rien retaper. Tu veux que je te génère ce pack ?
