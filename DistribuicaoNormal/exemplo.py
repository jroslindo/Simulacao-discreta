import random as rd
import numpy as np
import matplotlib.pyplot as plt

vetor_saida = np.zeros(100)


j = 0
for i in range(100):
    if j<25:
        vetor_saida[i] = rd.uniform(0,100) * 0.25
    elif j >75:
        vetor_saida[i] = rd.uniform(0,100) * 0.25
    else:
        vetor_saida[i] = rd.uniform(0,100)
    j+=1

print(vetor_saida)

plt.bar(np.arange(100),vetor_saida)

plt.show()