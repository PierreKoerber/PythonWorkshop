Très bonnes questions 👌 Tu touches là à un point important : en Python, il existe à la fois des **exceptions génériques** (valables partout) et des **exceptions spécifiques** (propres à une fonction, un module ou une opération).

---

# 🔹 1. Exceptions génériques

- **`Exception`** : la classe de base de toutes les exceptions _utilisables_ (sauf cas très rares).
- **`BaseException`** : racine de **tout** (y compris `SystemExit`, `KeyboardInterrupt`…), en pratique on ne l’attrape presque jamais.

👉 Typiquement, on écrit :

```python
try:
    x = int("abc")
except Exception as e:
    print("Erreur attrapée :", e)
```

Cela capture **toutes les erreurs courantes**, quelle que soit leur nature (`ValueError`, `TypeError`, etc.).

⚠️ Mais c’est **trop large** si on ne sait pas quoi faire → on risque de masquer des vrais bugs.
Bonne pratique : capturer d’abord les **exceptions précises** qu’on attend.

---

# 🔹 2. Exceptions spécifiques

Chaque type d’erreur Python a sa propre exception. Quelques classiques :

| Exception                             | Quand ça arrive                      |
| ------------------------------------- | ------------------------------------ |
| `ValueError`                          | Conversion impossible (`int("abc")`) |
| `TypeError`                           | Mauvais type (`"a" + 3`)             |
| `IndexError`                          | Index hors limites d’une liste       |
| `KeyError`                            | Clé absente d’un dictionnaire        |
| `FileNotFoundError`                   | Fichier inexistant à l’ouverture     |
| `ZeroDivisionError`                   | Division par zéro                    |
| `ImportError` / `ModuleNotFoundError` | Problème d’import                    |
| `JSONDecodeError` (module `json`)     | Fichier JSON invalide                |

---

# 🔹 3. Comment savoir quelle exception une fonction peut lever ?

### 📌 Méthodes pratiques

1. **Lire la doc officielle** :
   Exemple : [`int()`](https://docs.python.org/3/library/functions.html#int)
   → “Raises `ValueError` if invalid literal for int() with base 10.”

2. **Essayer / tester** avec des cas limites :

```python
try:
    int("abc")
except Exception as e:
    print(type(e), e)
# <class 'ValueError'> invalid literal for int() with base 10: 'abc'
```

3. **Lire le code source** si c’est un module standard (open source).

4. **IDE / Linter** : certains IDE comme PyCharm ou VS Code indiquent les exceptions courantes dans l’auto-complétion ou les tooltips.

---

# 🔹 4. Hiérarchie des exceptions

Python organise les exceptions en arbre :

- `BaseException`

  - `Exception`

    - `ArithmeticError`

      - `ZeroDivisionError`

    - `ValueError`
    - `TypeError`
    - `LookupError`

      - `IndexError`
      - `KeyError`

    - etc.

👉 On peut donc capturer **une famille entière** :

```python
try:
    lst = [1, 2]
    print(lst[10])
except LookupError as e:
    print("Erreur d’accès (index ou clé) :", e)
```

---

# 🔹 5. Bonnes pratiques

✅ Attraper les exceptions **spécifiques** attendues.
✅ Utiliser `except Exception as e:` comme “filet de sécurité” seulement à la fin.
✅ Éviter `except:` tout court (ça attrape aussi `KeyboardInterrupt` !).
✅ Pour le debug, afficher **type + message**.
✅ Structurer avec plusieurs blocs si besoin :

```python
try:
    with open("data.json") as f:
        data = json.load(f)
except FileNotFoundError:
    print("⚠️ Fichier introuvable")
except json.JSONDecodeError:
    print("⚠️ JSON corrompu")
except Exception as e:
    print("Erreur inattendue:", type(e), e)
```
