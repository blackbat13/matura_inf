import random


def f(x):
    return x


a = 0
b = 5

n = 100000

ile_pod_wykresem = 0

for i in range(n):
    x = (random.random() * 5)
    y = (random.random() * 5)

    if y < f(x):
        ile_pod_wykresem += 1

# P_wyk / P_pr ~= ile_pod_wykresem / n

p_pr = 5*5
p_wyk = (p_pr * ile_pod_wykresem) / n

print("Pole pod wykresem: ", p_wyk)