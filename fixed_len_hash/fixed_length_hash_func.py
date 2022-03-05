class FixedLenHash:
    def __init__(self) -> None:
        # self.q = 1000000007
        # self.g = 58756776
        # self.h = 43245436
        self.q = 127
        self.g = 31
        self.h = 71
    
    def compute(self, x1, x2):
        return format((pow(self.g, int(x1,2), self.q)*pow(self.h, int(x2,2), self.q))%self.q,'b').zfill(len(x1))


if __name__=="__main__":
    hsh = FixedLenHash()
    print(hsh.compute('1010110', '1011010'))
    