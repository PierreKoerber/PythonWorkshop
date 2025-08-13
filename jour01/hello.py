#!/usr/bin/env python3

# Jour 1 — Hello + version Python
import platform
print("Hello 👋")
print("Python :", platform.python_version())
print("Système :", platform.system(), platform.release())

name = input("Ton prénom ? ")
print("Bienvenue,", name, "!")