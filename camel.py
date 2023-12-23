string = input("Верблюжий стиль: ")
string = string[0].lower() + string[1: ]
for i in string:
    if i.isupper():
        string = string.replace(i, f"_{i.lower()}")
print(string)
