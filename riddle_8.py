import mpmath as ap

def error(x):
  return abs(x**3 - 3**x)

# approximation engine to the rescue

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

#print(approximate(error))

# the main issue is that it always finds the local minimum
# kind of frustrating
# have to mutate the function to chop out local minima

def newerror(x):
  if x < 2 or x > 2.75:
    return abs(x - 2.5) + 1
  return abs(x**3 - 3**x)

print(approximate(newerror))