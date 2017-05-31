import mpmath as ap

# mpmath to the rescue

ap.mp.dps = 1000011

print(str(ap.sqrt(42))[-10:])