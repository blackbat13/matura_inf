# W pliku owoce.txt wpisane są różne owoce w dowolnej kolejności
# Zadanie: Policz ile razy występuje każdy owoc w pliku
# Dla każdego owocu wypisz jaką część całego zbioru stanowi (w %)

file = open("owoce.txt")

lines = file.read().split("\n")

file.close()

fruits = dict()
count = len(lines)

for fr in lines:
    if fr in fruits:
        fruits[fr] += 1
    else:
        fruits[fr] = 1

for fr in sorted(fruits):
    print(fr, (fruits[fr] / count) * 100)