
from Encoding import decode, mod_decode

# Store integers as a stack integers
class IntegerizedStack:
    def __init__(self, v=0):
        self.value = v

    def pop(self):
        # assume the integer pairs
        self.value, ret = decode(self.value)
        return ret

    def modpop(self, modulus):
        self.value, ret = mod_decode(self.value, modulus)
        return ret

    def split(self, n):
        # Assume value codes exactly n integers, nothing more
        out = [self.pop() for _ in range(n-1)]
        out.append(self.value)
        self.value = 0
        return out



