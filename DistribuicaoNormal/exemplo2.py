import random as rd
import numpy as np
import matplotlib.pyplot as plt

vetor_saida = np.zeros(100)


j = 0
for i in range(100):
    if j<25:
        vetor_saida[i] = rd.uniform(0,100) * i/100
    elif j >75:
        vetor_saida[i] = rd.uniform(0,100) * (1-i/100)
    else:
        vetor_saida[i] = rd.uniform(0,100) * i/100
    j+=1

plt.bar(np.arange(100),vetor_saida)

plt.show()