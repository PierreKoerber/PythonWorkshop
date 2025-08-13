# Jour 3 — Lire/écrire un fichier config.txt
from pathlib import Path

cfg = Path("config.txt")
if not cfg.exists():
    cfg.write_text("username=Alex
", encoding="utf-8")

text = cfg.read_text(encoding="utf-8")
print("Contenu actuel:", text.strip())

new_name = input("Nouveau username ? ")
cfg.write_text(f"username={new_name}\n", encoding="utf-8")
print("OK, enregistré.")