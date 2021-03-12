# W pliku owoce2.txt w każdej linii są dwie wartości
# Tekst i liczba
# Oznaczają nazwę owocu i jego ilość na magazynie
# Dla każdego owocu policz, ile jest jego sztuk na magazynie łącznie

file = open("owoce2.txt")
lines = file.read().split("\n")
file.close()

fruits = dict()

for line in lines:
    values = line.split(" ")
    #print(values)
    fruit_name = values[0]
    fruit_value = int(values[1])
    if fruit_name in fruits:
        fruits[fruit_name] += fruit_value
    else:
        fruits[fruit_name] = fruit_value

for fruit_name in fruits:
    print(fruit_name, fruits[fruit_name])