from math import floor, sqrt

def decode(z):
    # Rosenberg-Strong decoding function
    m = floor(sqrt(z))
    if z-m*m < m:
        return (z-m*m, m)
    else:
        return (m, m*m+2*m-z)

def encode(x,y):
    # Encoding for Rosenberg-Strong
    return max(x,y)**2 + max(x,y) + x - y

def mod_encode(x,y,m):
    return x+m*y

def mod_decode(z,m):
    if m == 0:
        return (z,0)
    else:
        return ((z-(z%m)) // m, z%m)
