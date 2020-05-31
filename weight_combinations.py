import itertools
import numpy as np

# T1
a = list(np.array(range(1,6)) * 800)

# T2
b = list(np.array(range(1,2)) * 800 * 2)
c = list(np.array(range(1,2)) * 800 * 3)

# T3
d = list(np.array(range(1,4)) * 900 * 1)
e = list(np.array(range(1,4)) * 900 * 2)
f = list(np.array(range(1,4)) * 900 * 3)

# T4
g = list(np.array(range(1,6)) * 1000 * 2)

# T5
h = list(np.array(range(1,4)) * 1000)


n = a + b + c + d + e + f + g + h

for c in range(1,4):
    comb = list(itertools.combinations(n,c))

    for combi in comb:
        a = np.array(combi)
        s = a.sum()
        if s >= 20000 and s < 21500:
            print("%s = %d" % (combi,s))


#print(comb)