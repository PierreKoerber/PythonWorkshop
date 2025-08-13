# Jour 1 — Hello + version Python
import platform
print("Hello 👋")
print("Python :", platform.python_version())
print("Système :", platform.system(), platform.release())

def demandeNom(nom):
    name = input("Ton prénom ? ")
    print(name)
    print("Bienvenue,", name, "!")
