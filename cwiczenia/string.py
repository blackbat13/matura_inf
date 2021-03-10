


wyraz = "abcdefz"

nowy = ""

for i in range(len(wyraz)):
    nowy += chr(ord(wyraz[i]) + 1)

print(nowy)