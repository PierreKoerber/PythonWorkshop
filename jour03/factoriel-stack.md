Parfait 👍
Je vais te faire un **schéma texte** simple qui montre la **pile d’appels** (_call stack_) quand on exécute une fonction récursive.

---

# 📚 Schéma texte : Call Stack & Fonction récursive

## Exemple : Factorielle

```python
def factorielle(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorielle(n - 1)

print(factorielle(3))
```

---

## 🔍 Étapes dans l’ordinateur

La **call stack** est comme une pile d’assiettes :

- On **empile** chaque appel de fonction.
- Quand une fonction finit, on la **retire** (on “dépile”).

---

### **1. Appel initial**

```
Appel: factorielle(3)
```

- `n = 3`, pas ≤ 1 → doit calculer `3 * factorielle(2)`
- Empile un nouvel appel.

---

### **2. Nouvelle pile après factorielle(3) → factorielle(2)**

```
[ Haut de la pile ]
factorielle(2)   # en cours
factorielle(3)   # en attente du résultat de factorielle(2)
[ Bas de la pile ]
```

- `n = 2`, pas ≤ 1 → doit calculer `2 * factorielle(1)`

---

### **3. Nouvelle pile après factorielle(2) → factorielle(1)**

```
[ Haut de la pile ]
factorielle(1)   # en cours
factorielle(2)   # en attente du résultat de factorielle(1)
factorielle(3)   # en attente du résultat de factorielle(2)
[ Bas de la pile ]
```

- `n = 1` → **cas de base** : retourne `1`.

---

### **4. Retour des valeurs (dépilement)**

1. `factorielle(1)` retourne `1` → dépile :

```
factorielle(2) reçoit 1 → calcule 2 * 1 = 2
```

2. `factorielle(2)` retourne `2` → dépile :

```
factorielle(3) reçoit 2 → calcule 3 * 2 = 6
```

3. `factorielle(3)` retourne `6` → pile vide.

---

### **5. Résultat final**

```
print(factorielle(3))  # 6
```

---

## 📌 Schéma visuel simplifié

```
--- Empilement ---
factorielle(3)
  → factorielle(2)
       → factorielle(1)
--- Retour ---
factorielle(1) → 1
factorielle(2) → 2 * 1 = 2
factorielle(3) → 3 * 2 = 6
```

---

💡 On peut facilement adapter ce schéma à d’autres récursions comme **compte à rebours**, **parcours de répertoire**, etc.

Si tu veux, je peux te préparer **une version graphique A4** avec des flèches pour illustrer visuellement la pile d’appels récursive — ce serait parfait pour ton cours Jour 3.
Veux-tu que je te fasse cette version graphique ?
