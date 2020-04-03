import random

def LCG(a, c, m, seed):     
    xi = seed
    while True:
        xf = (a * xi + c) % m
        xi = xf
        yield xf

def random_sample(n, interval ):#20200420162000
    seed = random.randrange(0,20200420162009)
    lower, upper = interval[0], interval[1]
    sample = []
    glibc = LCG(1103515245, 12345, 2 ** 32, seed)       # parameters as in GNU C Library

    for i in range(n):
        observation = (upper - lower) * (next(glibc) / (2 ** 32 - 1)) + lower
        sample.append(int(observation))

    return sample

# sample = random_sample(1, [0, 100])   # 100 random numbers between 30 and 90
# print(sample[0])