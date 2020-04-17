s1 = 5
s2 = 659
s3 = 15600

def wichmann_hill():
    global s1
    global s2
    global s3
    s1 = 171*s1 % 30269 # primeiro congruente
    s2 = 172*s2 % 30307 # segundo congruente
    s3 = 173*s3 % 30323 # terceiro congruente

    result = (s1/30269.0 + s2/30307.0 + s3*30323.0) % 1

    return result

def verificador():
    Oi = [0]*10
    for i in range(0, 100):
        numero = wichmann_hill()
        print("Numero:", "{:.2f}".format(numero))
        
        if numero < 0.1:
            Oi[0] += 1
        elif numero < 0.2:
            Oi[1] += 1
        elif numero < 0.3:
            Oi[2] += 1
        elif numero < 0.4:
            Oi[3] += 1
        elif numero < 0.5:
            Oi[4] += 1
        elif numero < 0.6:
            Oi[5] += 1
        elif numero < 0.7:
            Oi[6] += 1
        elif numero < 0.8:
            Oi[7] += 1
        elif numero < 0.9:
            Oi[8] += 1
        elif numero < 1.0:
            Oi[9] += 1
    
    print("Intervalo | Oi\t| Ei | Oi-Ei\t|Oi-Ei^2| Oi-Ei^2/Ei")
    
    soma = 0
    soma_divisao = 0
    for i in range(1, 11):
        print((i-1)/10,"-", i/10,"|",Oi[i-1],"\t| 10 |",Oi[i-1]-10,"\t|",(Oi[i-1]-10)**2,"\t|",(Oi[i-1]-10)**2/10)
        soma += Oi[i-1]
        soma_divisao += (Oi[i-1]-10)**2/10

    print("Oi = ",soma," Ei = 100")
    print("(Oi - Ei)^2 / Ei = ", "{:.2f}".format(soma_divisao))

verificador()
