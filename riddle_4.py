# ln(x)^pi = 4*sqrt(3^2)
# from wolfram alpha: e ^ (12 ^ (1 / pi))

import mpmath
mpmath.dps = 100

overpi = 1 / mpmath.pi
tothepow = 12 ** overpi
powe = mpmath.e ** tothepow
print(powe)