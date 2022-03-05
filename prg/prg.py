class DiscreteLog:
    def __init__(self):
        self.p = 1000000007
        self.g = 67849

    def evaluate(self, val):
        g = self.g
        p = self.p
        return pow(g, val, p) 

    def hardcore_pred(self, val):
        g = self.g
        p = self.p
        if val>p/2:
            return 1
        else:
            return 0

class OneWayFunc:
    def __init__(self, type=1):
        if type==1:
            self.ow_func = DiscreteLog()

    def evaluate(self, val):
        return self.ow_func.evaluate(val)
    
    def hardcore_pred(self, val):
        return self.ow_func.hardcore_pred(val)

class PRG:

    def __init__(self, type=1):
        self.val = "11" # Initial Value
        self.type = 1
        self.output = ""

    def init_val(self, val):
        self.val = val
        self.output = ""

    def add_bit(self, bit):
        self.output = self.output + str(bit)
        return self.output

    def gen_n_bit(self, n):
        f = OneWayFunc(type=self.type)
        for i in range(n):
            x = f.evaluate(int(self.val, 2))
            self.add_bit(f.hardcore_pred(x))
            self.val = format(x, 'b')
        return self.output

if __name__=="__main__":
    # f = OneWayFunc(type=1)
    # for i in range(10):
    #     x = f.evaluate(r.val)
    #     r.add_bit(f.hardcore_pred(x))
    #     print(x, f.hardcore_pred(x), r.val)

    r = PRG()
    for i in range(1, 5):
        # print(format(i, 'b').zfill(10), end=' ')
        r.init_val(format(i, 'b').zfill(10))
        print(r.gen_n_bit(10))

    # dl = DiscreteLog()
    # for i in range(10):
    #     print(dl.evaluate(i))