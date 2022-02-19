from prg import *

class PRF:
    def __init__(self, type=1):
        if type==1:
            self.prg = PRG(type=1)
    
    def func(self, key, val):
        z = key
        for bit in val:
            self.prg.init_val(z)
            x = self.prg.gen_n_bit(2*len(key))
            if bit == '0':
                z = x[:len(key)]
            else:
                z = x[-len(key):]
        return z

if __name__ == "__main__":
    f = PRF()
    k = '0110'
    v = '1101'
    print(f.func(k, v))