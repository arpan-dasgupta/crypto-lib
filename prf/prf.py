from prg.prg import *

class PRF:
    def __init__(self, type=1):
        if type==1:
            self.prg = PRG(type=1)
    
    def func(self, key, val):
        z = key
        for bit in val:
            self.prg.init_val(z)
            x = self.prg.gen_n_bit(2*len(key))
            # print(x, end=' ')
            if bit == '0':
                z = x[:len(key)]
            else:
                z = x[-len(key):]
        return z

if __name__ == "__main__":
    f = PRF()
    k = '0110010110'
    v = '1100110010'
    for i in range(800, 810):
        v = format(i, 'b').zfill(10)
        print(f.func(k, v))