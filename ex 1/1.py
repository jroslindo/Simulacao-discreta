from random import randrange

def main ():
    duzias_dia = 0
    vet_duzia = []
    clientes_dia = 0
    chance_pao = 0
    for i in range (15):
        chance_cliente = randrange(1,100)
        
        if chance_cliente <= 10:
            clientes_dia = 14
        elif chance_cliente > 10 and chance_cliente<=35:
            clientes_dia = 12
        elif chance_cliente > 35 and chance_cliente<=65:
            clientes_dia = 10
        else:
            clientes_dia = 8

        # print(clientes_dia)
        duzias_dia = 0
        for j in range(clientes_dia):
            chance_pao = randrange(1,100)

            if chance_cliente <= 10:
                duzias_dia += 4
            elif chance_cliente > 10 and chance_cliente<=30:
                duzias_dia += 3
            elif chance_cliente > 30 and chance_cliente<=60:
                duzias_dia += 2
            else:
                duzias_dia += 1
        
        vet_duzia.append(int(duzias_dia))

    print(vet_duzia)
    print(sum(vet_duzia)/15)






main()