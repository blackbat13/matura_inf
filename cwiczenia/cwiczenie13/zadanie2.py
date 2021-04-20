file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

# Pomysł: sprawdzamy, czy dwie ostatnie cyfra liczby są równe 0
# Liczymy, ile jest takich liczb

count = 0  # Licznik liczb parzystych

for binary in binary_numbers:
    if binary[-1] == "0" and binary[-2] == "0":
        count += 1  # Zwiększamy licznik liczb parzystych

print(count)