from prf.prf import *
from message_encoder import *

from datetime import datetime

class CPA:
    """
    Complete class for performing the complete procedure from key generation, 
    encryption and decryption for a cpa-secure communication. The previously defined
    prg and prf classes are used. CPA-secure implies that an adversary with access to 
    encryption server cannot break the encryption scheme.
    """
    def __init__(self):
        pass

    def key_gen(self, n):
        """
        Generate an n-bit key for performing communication using PRG.
        """
        g = PRG()
        g.init_val(format(432,'b'))
        return g.gen_n_bit(n)

    def encrypt(self, message, key):
        """
        Given a message and a key, return the encrypted cipher text.
        """
        g = PRG()
        f = PRF()
        m = []
        for mb in message:
            # print(mb, f.func(key, r))
            g.init_val(format(432,'b'))
            r = g.gen_n_bit(len(key))
            x = int(mb, 2) ^ int(f.func(key, r),2)
            # print(bin(x)[2:].zfill(len(key)))
            m.append((r, bin(x)[2:].zfill(len(key))))
        return m

    def decrypt(self, cipher, key):
        """
        Given a ciphertext and the key, generate the message which was encrypted.
        """
        m = []
        for c in cipher:
            f = PRF()
            x = int(c[1], 2) ^ int(f.func(key, c[0]),2)
            m.append(bin(x)[2:].zfill(len(c[1])))
        return m

if __name__ == "__main__":
    cpa = CPA()

    k = cpa.key_gen(7)
    print(message_encoder("Hello World"))
    print(cpa.encrypt(message_encoder("Hello World"),k))
    print(cpa.decrypt(cpa.encrypt(message_encoder("Hello World"),cpa.key_gen(7)),k))
    print(message_decoder(cpa.decrypt(cpa.encrypt(message_encoder("Hello World"),cpa.key_gen(7)),k)))

    k = cpa.key_gen(10)
    print(int(k,2), k)
    msg = [format(i, 'b').zfill(10) for i in range(800, 810)]
    print(cpa.encrypt(msg, k))
    print(cpa.decrypt(cpa.encrypt(msg, k), k))