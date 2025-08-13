def lire_config() -> dict:
    try:
        with open("config.txt", "r", encoding="utf-8") as f:
            lignes = f.read().splitlines()
        cfg = {}
        for ligne in lignes:
            if "=" in ligne:
                k, v = ligne.split("=", 1)
                cfg[k] = v
        return cfg
    except FileNotFoundError:
        return {}

x = lire_config()

print(x)
print(x["nom"])