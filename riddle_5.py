import mpmath as ap

# wolfram alpha can't help you this time
# need to perfect my approximation engine

def error(x):
  if x <= 1: return 9 - x
  return abs(x**x - 9)

def approximate(errorfunc, startmagnitude=1, startvalue=0, precision=100):
  estimation = ap.mpf(startvalue)
  magnitude = startmagnitude
  ap.mp.dps = precision

  for i in range(precision):
    significant = ap.mpf(10)**magnitude
    lastvalue = (-10*significant) + estimation
    for offset in range(-9, 11):
      currentvalue = offset * significant + estimation
      if errorfunc(currentvalue) > errorfunc(lastvalue):
        break
      lastvalue = currentvalue
    estimation = lastvalue
    magnitude -= 1

  return estimation

print(approximate(error)) # I love you, approximation engine.