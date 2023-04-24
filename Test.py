
from Encoding import *
from IntegerizedStack import *

if __name__ == "__main__":

    for i in range(1000000):
        x,y = decode(i)
        print( (x,y), encode(x,y))
        assert( i == encode(x,y) )

        for m in range(1, 25):
            x, y = mod_decode(i,m)
            assert (i == mod_encode(x, y, m))

    print("Encoding and decoding test complete.")
