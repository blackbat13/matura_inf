file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

# Pomysł: sprawdzamy, czy ostatnia cyfra liczby jest równa 0
# Liczymy, ile jest takich liczb

count = 0 # Licznik liczb parzystych

for binary in binary_numbers:
    if binary[-1] == "0":  # Jeżeli ostatni znak liczby binarnej to 0
        count += 1   # Zwiększamy licznik liczb parzystych
        
print(count)
