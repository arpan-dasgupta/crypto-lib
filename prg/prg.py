class DiscreteLog:
    """
    Class for performing dicrete log computation and finding the hardcore predicate.
    """
    def __init__(self):
        """
        Initialize prime and generator
        """
        self.p = 37975227936943673922808872755445627854565536638199
        self.g = 17075227936943673922808872755445627854565536638199
        # self.p = 1000000007
        # self.g = 67849

    def evaluate(self, val):
        """
        Performs the discrete log computation for the assigned prime and generator
        """
        g = self.g
        p = self.p
        return pow(g, val, p) 

    def hardcore_pred(self, val):
        """
        Returns the hardcore predicate given the output of dicrete log (The MSB)
        """
        g = self.g
        p = self.p
        if val>p/2:
            return 1
        else:
            return 0

class OneWayFunc:
    """
    General function adaptible to any one way function or permutation to be added in the future
    """
    def __init__(self, type=1):
        """
        Initialize type of one way function used
        """
        if type==1:
            self.ow_func = DiscreteLog()

    def evaluate(self, val):
        """
        Compute the one way function
        """
        return self.ow_func.evaluate(val)
    
    def hardcore_pred(self, val):
        """
        Return the hardcore predicate given the output
        """
        return self.ow_func.hardcore_pred(val)

class PRG:
    """
    Class for generating a n-bit pseudo random number
    """
    def __init__(self, type=1):
        """
        Initialize initial value and the type of one-way function
        """
        self.val = "11" # Initial Value
        self.type = 1
        self.output = ""

    def init_val(self, val):
        """
        Initialize the value of the PRG using some seed
        """
        self.val = val
        self.output = ""

    def add_bit(self, bit):
        """
        Internal function for genrating an extra bit of the prg
        """
        self.output = self.output + str(bit)
        return self.output

    def gen_n_bit(self, n):
        """
        Generate a random n-bit (pseudo)random number using the one way function and return it.
        """
        f = OneWayFunc(type=self.type)
        for i in range(n):
            x = f.evaluate(int(self.val, 2))
            self.add_bit(f.hardcore_pred(int(self.val,2)))
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