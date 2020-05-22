import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import random


def dist_normal (min, max, quantidade_valores):
    x = np.arange(min, max)
    xU, xL = x + 0.5, x - 0.5 
    prob = ss.norm.cdf(xU, scale = max/2) - ss.norm.cdf(xL, scale = max/2)
    prob = prob / prob.sum() #normalize the probabilities so their sum is 1
    nums = np.random.choice(x, size = quantidade_valores, p = prob)

    return nums


def dist_exponencial2(seed, n, limite_inf, med):
    
    soma = 0
    numimp = 0
    u = 0.00
    saida=np.zeros(n)

    alph = 1.0/(med - limite_inf)
    
    for i in range(1, n):
        u = random.randrange(seed)
        
        u = limite_inf - (1/alph) * np.log(u)
        numimp += 1
        
        if (numimp < n+1):
            saida[i]= u*(10**8)
    
    return saida
        
