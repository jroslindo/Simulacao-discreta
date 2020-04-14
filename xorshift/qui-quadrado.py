from xorshift import *
import numpy as np

def main ():
    i=0
    vetor = np.zeros(100)
    rand = XORShift()
    
    for i in range(100):
        aleatorio = rand.nextInt(100)
        vetor[int(aleatorio)] +=1
        # print("inseriu " + str(aleatorio) + " na posicao " + str(int(aleatorio)) + " ficando com " + str(vetor[int(aleatorio)]) + "\n")

    soma = np.zeros(10)
    for i in range(10):
        for j in range(10):
            soma[i] += vetor[i*10+j] 
        
        soma[i] = (soma[i] - 10)**2 / 10

    print(sum(soma))


main()