import time

class XORShift:
    def __init__(self):
        self.init(int(round(time.time() * 1000)))

    def init(self, seed):
        self.last = seed

    def nextInt(self, max):
        self.last ^= (self.last << 21)
        self.last ^= (self.last >> 35)
        self.last ^= (self.last << 4)

        out = self.last % max
        if  out < 0:
            return -out
        else:
            return  out

# rand = XORShift(6504)
# rand = XORShift()
# print(rand.nextInt(255))