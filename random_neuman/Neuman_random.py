semente = 6519
qtt_digitos = 4

for i in range(10   ):
    digitos = semente**2

    x = []
    for j in range(qtt_digitos*2):
        x.insert(0, int(digitos%10))
        digitos = digitos/10

    
    semente= x[2]*1000
    semente+= x[3]*100
    semente+= x[4]*10
    semente+= x[5]
    print(semente)