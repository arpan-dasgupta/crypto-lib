from fixed_len_hash.fixed_length_hash_func import FixedLenHash
from message_encoder import message_encoder

class MerkleDamgard:
    def __init__(self) -> None:
        self.iv = '1001010'

    def hash(self, message):
        prev = self.iv
        f = FixedLenHash()
        for m in message:
            prev = f.compute(prev, m)
        return prev

if __name__=="__main__":
    m = MerkleDamgard()
    message = message_encoder("Hello World")
    print(m.hash(message))