def fibonacci():
  a, b = 1, 1
  yield a
  yield b
  while True:
    a, b = b, a + b
    yield b

fib = fibonacci()

"""
for i in range(1_000_000_000 - 1):
  v = next(fib)
  if i % 100000 == 0:
    print(i//100000, "of", 10_000)

print(str(next(fib))[-10:]) 
"""
# scratch that, too slow

# need to rethink this
# is there a pattern?
# lets look at the lowest 10 digits of the numbers and see if something pops up

"""for i, v in enumerate(fib):
  input(str(i) + ", " + str(v)[-10:])"""

# the one's place repeats every 120th number
# ...no, every 60th number
# hmm
# do the other places repeat too?
# lets experiment

"""for i, v in enumerate(fib):
  input(str(i) + ", " + str(v)[-2:-1])"""

# lots of sevens
# the sequence '077' seems to occur a lot
# it appears at 45, 94, and... 247
# i'll set up a pattern finder to get all occurrances

"""accumulator = ""
for i, v in enumerate(fib):
  accumulator += str(v)[-2:-1]
  if len(accumulator) > 3:
    accumulator = accumulator[1:]
  if accumulator == "077":
    input(i)"""

# 47, 96, 102, 249, 347, 396, 402, 549, 647, 696, 702
# it definitely repeats regularly
# this is promising
# i should find the period
# i can start with a longer string, maybe the first couple digits
# lets try 123583

"""accumulator = ""
for i, v in enumerate(fib):
  accumulator += str(v)[-2:-1]
  if len(accumulator) > 6:
    accumulator = accumulator[1:]
  if accumulator == "123584":
    input(i)"""

# 11, 289, 311, 589, 611, 889, 911, 1189
# subtract 11 from all of those: 0, 277, 300, 577, 600, 877, 900, 1177
# period of 300, minus the anomolies
# lets use a longer string to confirm it: 123584371898

"""accumulator = ""
stringtofind = "123584371898"
for i, v in enumerate(fib):
  accumulator += str(v)[-2:-1]
  if len(accumulator) > len(stringtofind):
    accumulator = accumulator[1:]
  if accumulator == stringtofind:
    input(i)"""

# yep, every 300
# what about the third digit?
# lets just print out the first 50 third digits

"""for i in range(50):
  print(str(next(fib))[-3:-2], end="")"""

# 1236955179763034
# that should do
# lets plug it into our substring finder

"""accumulator = ""
stringtofind = "1236955179763034"
for i, v in enumerate(fib):
  accumulator += str(v)[-3:-2]
  if len(accumulator) > len(stringtofind):
    accumulator = accumulator[1:]
  if accumulator == stringtofind:
    input(i)"""

# period of 1500
# these are getting much bigger
# but they do repeat
# do the period expansions follow a pattern?
# 60, 300, 1500
# divide all by 60, you get: 1, 5, 25
# powers of 5, times 60
# who'd bet the fourth digit has a period of 125 * 60?
# thats 7500
# lets test it

"""for i in range(50):
  print(str(next(fib))[-4:-3], end="")"""

"""accumulator = ""
stringtofind = "124607865167426842707"
for i, v in enumerate(fib):
  accumulator += str(v)[-4:-3]
  if len(accumulator) > len(stringtofind):
    accumulator = accumulator[1:]
  if accumulator == stringtofind:
    input(i)"""

# wait, no? 
# it's 15000
# 60 * 250
# that's unexpected
# well, better keep it in mind
# i can automate this process somewhat
# have it use the first 10 or so digits maybe, that should be more than enough

def findfibpattern(digit, patternsize=20, periods=2):
  stringtofind = ""
  fib = fibonacci()
  offset = -1
  while len(stringtofind) < patternsize:
    offset += 1
    stringtofind += str(next(fib))[-1-digit:-digit]

  fib = fibonacci()
  accumulator = ""
  for i, v in enumerate(fib):
    accumulator += str(v)[-1-digit:-digit]
    if len(accumulator) > len(stringtofind):
      accumulator = accumulator[1:]
    if accumulator == stringtofind:
      print(i - offset, end=", ")
      periods -= 1
      if periods == 0:
        break
  print()

# lets test it with digits 2-4
#findfibpattern(1)
#findfibpattern(2)
#findfibpattern(3)

# now for the remaining 6 digits
# this may also be slow

for i in range(1, 11):
  findfibpattern(i)

# periods: 300, 1500, 15000, ...
# .......................
# ...it's not showing up
# is the period really that large for the remaining digits?
# what kind of expansion is this?
# it grows so fast

# this is a very hard problem



# ...



# ...150000.

# that was only the fifth digit.
# i'm starting to think this would have been easier the original way.
# at this point it would probably be too slow to calculate the nth digits just by these repetitions
