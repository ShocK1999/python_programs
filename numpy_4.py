import numpy as np

tab = np.random.randint(101, size=(10, 10))
print(tab)

for x in range(np.size(tab, 1)):
    for y in range(np.size(tab, 0)):
        if y%2 != 0:
            tab[x][y] = 0

print(tab)