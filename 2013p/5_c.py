# Funkcja generuje listę liczb Fibonacciego
def fibonacci():
    fib = [1, 1]

    while fib[-1] + fib[-2] < 1000000000:
        fib.append(fib[-1] + fib[-2])

    return fib


fib = fibonacci()

file = open("dane.txt")

data = file.read().split("\n")

file.close()

found = []   # Lista znalezionych liczb fibonacciego z danych

for el in data:
    number = int(el)  # Zamieniamy tekst na liczbę
    if number in fib:
        found.append(number)  # Dodajemy liczbę do listy found

max_length = 1   # Szukamy maksymalnej długości ciągu
current_length = 1  # Długość obecnego ciągu
current_index = 0  # Indeks początkowy obecnego ciągu
max_index = 0  # Indeks początkowy maksymalnego ciągu

for i in range(1, len(found)):
    if found[i] > found[i-1]:
        # Tutaj mamy kolejny element ciągu rosnącego
        current_length += 1   # Zwiększamy obecną długość
        if current_length > max_length:
            max_length = current_length
            max_index = current_index
    else:
        # Skończył się ciąg rosnący
        # Zaczynamy liczyć od nowa
        current_length = 1
        current_index = i

print("Max długość:", max_length)
print("Indeks początkowy:", max_index)

begin_index = max_index
end_index = begin_index + max_length
print(found[begin_index:end_index])

