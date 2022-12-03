
from math import sqrt, log10

x = set(str('123456789'))

a = (1+sqrt(5))/2

c = 1/sqrt(5)

f = 1

fp = 1

i = 2

mod = 10**9


def fibcalc(n): return str(
    int(pow(10, n*log10(a) - log10(sqrt(5)) - int(n*log10(a) - log10(sqrt(5))-8))))


while not ((set(str(f)) == x) and (set(fibcalc(i)) == x)):
    f, fp, i = (f+fp) % mod, f, i+1
print(i, f)
