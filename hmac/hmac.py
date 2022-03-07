from merkle_damgard.merkle_damgard import MerkleDamgard
from fixed_len_hash.fixed_length_hash_func import FixedLenHash
from cpa_secure.cpa_secure import *
from copy import deepcopy

class H_MAC:
    """
    Class for making a hash based MAC for genrating a tag in CCA-secure 
    encryption schemes. These are faster than the CBC MAC.
    """
    def __init__(self, type = 1):
        """
        Initialize the type of the one way function.
        """
        self.prf = PRF(type=1)

    def key_gen(self, n):
        """
        Generate an n-bit key for performing MAC using PRG.
        """
        g = PRG()
        g.init_val(format(432,'b'))
        return g.gen_n_bit(n)

    def mac(self, message, key):
        """
        Genrate a tag for a given message and a key. The tag is a fixed length value 
        genrated by taking the hash in two stps using the previously defined MerkleDamgard
        function.
        """
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
        """
        Verify if the message and the tag generated match up.
        """
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