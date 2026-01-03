 #dizionari
persona1: dict[str, str] = {
    "nome": "Mario",
    "cognome": "Rossi",
    "email": "mario.rossi@example.com"
}
print(persona1)
print(persona1["email"])









#liste
'''
stringhe: list[str | int] = ["Pippo", 1, "Pluto", "Paperino"]
stringhe.append("Topolino") 
stringhe.append("Minnie")
# for x in stringhe:
#     print(x)

print(stringhe)
# print(stringhe[1]) 
deleted_values: list[str] = []

value_to_check_and_delete: str = "aperino"

is_value_in_the_list: bool = value_to_check_and_delete in stringhe
print(is_value_in_the_list)

if is_value_in_the_list:
    index_value_to_delete = stringhe.index(value_to_check_and_delete)
    print(index_value_to_delete)
    deleted_value = stringhe.pop(index_value_to_delete)
    deleted_values.append(deleted_value)
else:
    print(f" {value_to_check_and_delete} non esiste nella lista {stringhe}")

print("*"*30)
print(stringhe)
print(deleted_values)
'''