fruits = dict()
fruits = {"apple": 2.9}
fruits["banana"] = 6.23
fruits["banana"] *= 2

print(fruits["banana"])

fruits["ananas"] = 4.5

if "orange" in fruits:
    print(fruits["orange"])

for fr in fruits:
    print(fr, fruits[fr])