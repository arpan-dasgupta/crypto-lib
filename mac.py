from cpa_secure import *

class CBC_MAC:
    def __init__(self, type = 1):
        self.prf = PRF(type=1)

    def key_gen(self, n):
        g = PRG()
        g.init_val(format(432,'b'))
        return g.gen_n_bit(n)

    def mac(self, message, key):
        init = format(len(message), 'b')
        for m in message:
            x = int(init, 2) ^ int(m,2)
            # print(x, "-", end = ' ')
            init = self.prf.func(bin(x)[2:].zfill(len(init)), key)
            # print(init, "+", end=' ')
        return init
    
    def verify(self, message, key, tag):
        init = format(len(message), 'b')
        for m in message:
            x = int(init, 2) ^ int(m,2)
            init = self.prf.func(bin(x)[2:].zfill(len(init)), key)
        return init == tag


if __name__ == "__main__":
    mac = CBC_MAC(type=1)
    k = mac.key_gen(7)
    print(mac.mac(message_encoder("Hello World"), k))
    print(mac.verify(message_encoder("Hello World"), k, mac.mac(message_encoder("Hello World"), k)))
    print(mac.verify(message_encoder("Hello World"), k, mac.mac(message_encoder("Hello rl"), k)))
    print(mac.verify(message_encoder("Hello World"), k, mac.mac(message_encoder("Hello World"), '0101011')))