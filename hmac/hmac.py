from merkle_damgard.merkel_damgard import MerkleDamgard
from fixed_len_hash.fixed_length_hash_func import FixedLenHash
from cpa_secure.cpa_secure import *
from copy import deepcopy

class H_MAC:
    def __init__(self, type = 1):
        self.prf = PRF(type=1)

    def key_gen(self, n):
        g = PRG()
        g.init_val(format(432,'b'))
        return g.gen_n_bit(n)

    def mac(self, message, key):
        md = MerkleDamgard()
        ipad = "0110110"
        opad = "1011100"
        ki = format(int(ipad,2)^int(key,2),'b').zfill(len(message[0]))
        ko = format(int(opad,2)^int(key,2),'b').zfill(len(message[0]))
        inp = deepcopy(message)
        inp.append(bin(len(message))[2:].zfill(len(message[0])))
        inp[:0] = [ki]
        v1 = [md.hash(inp)]
        v1[:0] = [ko]
        ans = md.hash(v1)
        return ans
    
    def verify(self, message, key, tag):
        md = MerkleDamgard()
        ipad = "0110110"
        opad = "1011100"
        ki = format(int(ipad,2)^int(key,2),'b').zfill(len(message[0]))
        ko = format(int(opad,2)^int(key,2),'b').zfill(len(message[0]))
        inp = deepcopy(message)
        inp.append(bin(len(message))[2:].zfill(len(message[0])))
        inp[:0] = [ki]
        v1 = [md.hash(inp)]
        v1[:0] = [ko]
        ans = md.hash(v1)
        return ans == tag

if __name__=="__main__":
    mac = H_MAC()
    k = mac.key_gen(7)
    print(mac.mac(message_encoder("Hello World"), k))
    print(mac.verify(message_encoder("Hello World"), k, mac.mac(message_encoder("Hello World"), k)))
    print(mac.verify(message_encoder("Hello World"), k, mac.mac(message_encoder("Hello rl"), k)))
    print(mac.verify(message_encoder("Hello World"), k, mac.mac(message_encoder("Hello World"), '0101011')))