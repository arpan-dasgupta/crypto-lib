from mac.mac import *

class CCA:
    """
    Complete class for performing the complete procedure from key generation, 
    encryption and decryption for a cpa-secure communication. The previously defined
    MAC, PRG and PRF classes are used. CCA-secure implies that an adversary with access to 
    encryption server and the decryption server cannot break the encryption scheme.
    """
    def __init__(self, type=1):
        self.type = type

    def key_gen(self, n):
        """
        Generate an n-bit key for performing communication using PRG.
        """
        g = PRG(type = self.type)
        g.init_val(format(432,'b'))

        mac = CBC_MAC(type=self.type)
        
        return (g.gen_n_bit(n), mac.key_gen(n))

    def encrypt(self, message, key):
        """
        Given a message and a key, return the encrypted cipher text (along with the tag).
        """
        g = PRG(type=self.type)
        f = PRF(type=self.type)
        mac = CBC_MAC(type=self.type)
        m = []

        key_1, key_2 = key
        for mb in message:
            g.init_val(format(432,'b'))
            r = g.gen_n_bit(len(key_1))
            x = int(mb, 2) ^ int(f.func(key_1, r),2)
            m.append((r, bin(x)[2:].zfill(len(key_1))))

        return (m, mac.mac(message, key_2))

    def decrypt(self, cipher, key):
        """
        Given a ciphertext and the key, generate the message which was encrypted. Also 
        verify if the cipher and the tag match.
        """
        key_1, key_2 = key
        m = []
        for c in cipher[0]:
            f = PRF(type=self.type)
            x = int(c[1], 2) ^ int(f.func(key_1, c[0]),2)
            m.append(bin(x)[2:].zfill(len(c[1])))
        mac = CBC_MAC(type=self.type)
        if mac.verify(m, key_2, cipher[1]):
            return m
        else:
            return []

if __name__ == "__main__":
    cca = CCA()
    # print()
    k = cca.key_gen(7)
    print(message_encoder("Hello World"))
    print(cca.encrypt(message_encoder("Hello World"),k))
    print(cca.decrypt(cca.encrypt(message_encoder("Hello World"),cca.key_gen(7)),k))
    print(message_decoder(cca.decrypt(cca.encrypt(message_encoder("Hello World"),cca.key_gen(7)),k)))
    