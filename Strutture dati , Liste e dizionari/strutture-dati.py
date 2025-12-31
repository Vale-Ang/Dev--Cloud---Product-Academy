stringhe: list[str] = ["pippo", "pluto", "paperino"]
stringhe.append("topolino") 
stringhe.append("minnie")
# for x in stringhe:
#     print(x)

print(stringhe)
# print(stringhe[1])
deleted_values: list[str] = []
deleted_value = stringhe.pop()
deleted_values.append(deleted_value)
print(deleted_values)

