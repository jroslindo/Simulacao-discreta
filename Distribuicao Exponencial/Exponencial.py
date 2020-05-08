#feito pelo gustavo, joao e ianael

from scipy.integrate import quad
import numpy as np


valor_minimo = input("valor minio: ")
valor_maximo = input("valor máximo: ")
lamb         = int(input("lambda: "))

def integrand(x):
    return lamb*np.exp(-lamb*x)


if valor_minimo == "i":
    valor_minimo = np.Infinity
else:
    valor_minimo = int(valor_minimo)

if valor_maximo == "i":
    valor_maximo = np.Infinity
else:
    valor_maximo = int(valor_maximo)

ans, err = quad(integrand, valor_minimo, valor_maximo)
print (ans)