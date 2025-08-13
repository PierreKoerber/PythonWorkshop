Parfait, on va enrichir la **leçon du Jour 2** avec une **partie découverte hardware** pour montrer les **connecteurs courants** de l’ordinateur et leurs usages.
Ça permettra à ton fils de relier la programmation au côté concret de la machine.

---

# 📚 Jour 2 — Variables, Calculs, Fonctions & Découverte Hardware

---

## 🎯 Objectifs du jour

1. Manipuler des variables et faire des calculs simples.
2. Comprendre et utiliser des fonctions.
3. Savoir mettre des fonctions dans un fichier réutilisable.
4. Découvrir les connecteurs principaux d’un ordinateur et leur rôle.

---

## 1. Rappel : Variable & Calcul

💡 Une variable = une boîte avec un nom qui contient une valeur.

```python
a = 7
b = 5
print(a + b)  # 12
```

Types de données fréquents :

* **int** → nombre entier (`42`)
* **float** → nombre décimal (`3.14`)
* **str** → texte (`"Bonjour"`)

---

## 2. Fonctions : organiser son code

### 2.1 Définir une fonction

```python
def saluer():
    print("Bonjour !")
```

### 2.2 Paramètres

```python
def saluer_nom(nom):
    print("Bonjour", nom)
```

### 2.3 Retourner une valeur

```python
def addition(a, b):
    return a + b
```

---

## 3. Fichier mutualisé (module Python)

**utils.py**

```python
def addition(a, b):
    return a + b
```

**main.py**

```python
from utils import addition
print(addition(4, 5))
```

---

## 4. 💻 Découverte de l’ordinateur — Connecteurs

### 4.1 USB (Universal Serial Bus)

* **USB-A** : le format rectangulaire classique, souvent bleu en USB 3.0 (plus rapide).
* **USB-B** : carré, surtout pour imprimantes ou appareils audio.
* **USB-C** : réversible, plus petit, peut transmettre données + vidéo + alimentation.

  * Utilisé pour les téléphones récents, certains PC, écrans portables.

📌 Particularités :

* Vitesse : USB 2.0 (480 Mbps) → USB 3.0 (5 Gbps) → USB 3.2 / 4 (40 Gbps).
* Peut fournir l’alimentation (**Power Delivery**).

---

### 4.2 HDMI (High-Definition Multimedia Interface)

* Transmet **vidéo + audio** dans un seul câble.
* Formats :

  * **HDMI standard** : taille normale pour PC/TV.
  * **Mini-HDMI** : plus petit, utilisé sur certaines tablettes ou caméras.
  * **Micro-HDMI** : encore plus petit, souvent sur appareils photo.

📌 Particularités :

* Supporte vidéo jusqu’à 8K selon la version.
* Pratique pour brancher à une TV.

---

### 4.3 DisplayPort

* Connecteur vidéo pour PC, souvent sur les cartes graphiques.
* Version **mini DisplayPort** sur certains laptops Apple/Surface.
* Avantage : meilleure bande passante que HDMI pour écrans haute fréquence (144 Hz et +).

---

### 4.4 Autres connecteurs utiles

* **Jack audio 3,5 mm** : écouteurs/casque/micro.
* **Ethernet (RJ45)** : connexion réseau filaire.
* **Lecteur de carte SD/microSD** : transfert de photos/vidéos.

---

## 5. Exemple visuel des connecteurs

💡 Idée : apporter un câble de chaque type et lui faire deviner :

* Nom du connecteur
* Usage principal
* S’il transmet données, vidéo, ou les deux.

---

## 6. Mini-exercice

1. Lancer `jour2/variables.py` → changer les valeurs de `a` et `b`.
2. Créer une fonction `soustraction(a, b)` dans `utils.py` et l’appeler depuis `main.py`.
3. Repérer sur le Lenovo :

   * 2 ports USB différents
   * sortie HDMI
   * prise casque

---

Si tu veux, je peux te préparer **un schéma illustré des connecteurs** avec les formes et tailles, pour qu’il puisse les reconnaître facilement sur son PC et à l’arrière de la TV.
Veux-tu que je te fasse ce schéma ?
