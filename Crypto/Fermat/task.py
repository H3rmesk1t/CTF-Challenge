from Crypto.Util.number import *
from gmpy import next_prime
from secret import flag

p = getStrongPrime(2048)
q = next_prime(p ^ ((1<<2048)-1))
n = p * q
e = 65537

m = int.from_bytes(bytes(flag, encoding='utf-8'), 'big')
assert m < n
c = pow(m, e, n)

print('n = {}'.format(n))
print('c = {}'.format(c))
