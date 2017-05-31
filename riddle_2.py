import mpmath

mpmath.mp.dps=4

def to_base(n, base=63):
  digitmap = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?"
  nstring = ""
  ndigits = 0
  while True:
    if base ** (ndigits + 1) > n:
      break
    ndigits += 1

  while ndigits >= 0:
    magnitude = base ** ndigits
    d = n // magnitude
    n = n % magnitude
    nstring += digitmap[d]
    ndigits -= 1

  return nstring

def is_palindrome(n):
  nstr = str(n)
  while len(nstr) > 1:
    if nstr[0] != nstr[-1]:
      return False
    nstr = nstr[1:-1]
  return True

i = 0

while True:
  if mpmath.cbrt(i**2) % 1 == 0:
    base = to_base(i)
    if is_palindrome(base):
      print(f"number is {i}")
      print(f"{i}^2 ({i**2}) is cube of {int(mpmath.cbrt(i**2))}")
      print(f"number in base 63 is {base}")
      input()
  i += 1