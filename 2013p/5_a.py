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

for el in data:
    number = int(el)  # Zamieniamy tekst na liczbę
    if number in fib:
        print(number)
