import random


def aleatorio_neumann ():
    semente = random.randrange(0,99)
    qtt_digitos = 2

    for i in range(10):
        digitos = semente**2

        x = []
        for j in range(qtt_digitos*2):
            x.insert(0, int(digitos%10))
            digitos = digitos/10

        
        semente= x[2]*10
        semente+= x[3]
        # semente+= x[4]*10
        # semente+= x[5]
    
    # print(semente)
    return semente

