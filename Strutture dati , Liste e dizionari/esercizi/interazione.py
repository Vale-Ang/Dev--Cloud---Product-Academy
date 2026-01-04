utenti: dict[str, str] = {
    "alice": "admin",
    "bob": "user",
    "charlie": "guest"
}

for username, ruolo in utenti.items():
    print(f"Username: {username}, Ruolo: {ruolo}")

username_to_check: str = "bob"
if username_to_check in utenti:
    print(f"{username_to_check} presente: True")
else:
    print(f"{username_to_check} presente: False")

dict_keys: list[str] = list(utenti.keys())
print(f"Usernames: dict_keys {dict_keys}")
dict_values: list[str] = list(utenti.values())
print(f"Ruoli: dict_values {dict_values}")