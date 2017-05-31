import mpmath as ap

ap.mp.dps = 30

def error(x):
  if x == 0: return 1000
  return abs(2 * ap.sqrt(x) - x ** 2 / 2)

def approximate(errfunc, startsize = 1, startnum = 0): # peice of shit is broken
  estim = ap.mpf(startnum)
  while error(estim) != 0 and startnum > -ap.mp.dps:
    value = ap.mpf(10)**startsize
    for d in range(10):
      print((d+1)*value)
      print(f"value {estim} vs {estim + value}")
      print(f"errone is {error(estim)}")
      print(f"errtwo is {error(estim + value)}")
      if error(estim + value) > error(estim):
        print("break")
        input()
        break
      input()
      estim += value
    startsize -= 1
  return estim

#print(approximate(error, 0, 2.5))

# fuck this

# (2 * sqrt(x)) - (x ^ 2 / 2) = 0
# from wolfram alpha: 2 * cuberoot(2)
print(str(2 * ap.cbrt(2)))
