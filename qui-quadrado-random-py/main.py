import random as rd
import numpy as np

def main ():
    i=0
    vetor = np.zeros(100)
    
    for i in range(100):
        aleatorio = rd.uniform(0,1)
        vetor[int(aleatorio*100)] +=1
        # print("inseriu " + str(aleatorio) + " na posicao " + str(int(aleatorio*100)) + " ficando com " + str(vetor[int(aleatorio*100)]) + "\n")

    soma = np.zeros(10)
    for i in range(10):
        for j in range(10):
            soma[i] += vetor[i*10+j] 
        
        soma[i] = (soma[i] - 10)**2 / 10

    print(sum(soma))


main()