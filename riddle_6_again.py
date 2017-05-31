import mpmath
mpmath.mp.dps = 20

rt5 = mpmath.sqrt(5)
overrt5 = 1 / rt5

def fib(n):
  return overrt5 * mpmath.phi ** n

print(int(fib(1_000_000_000)))