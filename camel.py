camelcase = input("camelCase: ")
for letter in camelcase:
    if letter.isupper():
        _ = camelcase.split(letter)
        _.insert(1, "_" + letter.lower())
        camelcase = "".join(_)
print("snake_case:", camelcase)
