#inputSeed = "59312054"
#vectorSeed = list(map(int, inputSeed))

# semente
vectorSeed = [82, 10, 75, 4, 13, 33, 22, 41, 50, 71, 99]

operationType = input("Tipo de operação(sum, mult ou sub): ")

j = 7 # setima posição do vetor da semente
k = 10 # decima posição do vetor da semente
mod = 100
cicles = 1000 # numero de numeros aleatorios

# variaveis para o teste do X²
randomNumbers = []
obtainedRatio = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
expectedRatio = 100
rangeValues = [0.1*mod, 0.2*mod, 0.3*mod, 0.4*mod, 0.5*mod, 0.6*mod, 0.7*mod, 0.8*mod, 0.9*mod, 1*mod]


# função que calculo o proximo numero
def calculateNextNumber():
    if(operationType == "sum"):
        return (vectorSeed[j-1] + vectorSeed[k-1]) % mod
    elif(operationType == "sub"):
        return (vectorSeed[j-1] - vectorSeed[k-1]) % mod
    elif(operationType == "mult"):
        return (vectorSeed[j-1] * vectorSeed[k-1]) % mod
    else:
        return None

# loop onde é calculado todos os numeros aleatorios
for x in range(cicles):
    newValue = calculateNextNumber()
    print(vectorSeed, "->", newValue)
    vectorSeed.pop(0)
    vectorSeed.append(newValue)
    randomNumbers.append(newValue)

print(randomNumbers)


# codigo para o teste do x²
for x in range(len(randomNumbers)):
    for z in range(len(rangeValues)):
            if(randomNumbers[x] < rangeValues[z]):
                obtainedRatio[z] += 1
                break

def getXSquare():
    xResult = 0.0
    for x in range(len(obtainedRatio)):
        xResult = xResult + ((obtainedRatio[x] - expectedRatio)*(obtainedRatio[x] - expectedRatio))/expectedRatio
    return xResult


print(obtainedRatio)
print('X²:', getXSquare())

