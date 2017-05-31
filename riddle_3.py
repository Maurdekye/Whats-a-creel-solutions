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

googolb2 = to_base(10**100, 2)
print(googolb2.count("1"))