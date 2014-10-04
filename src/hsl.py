import sys
from math import *

# http://psychology.wikia.com/wiki/HSL_and_HSV


def to_hsl(R, G, B):
  M = max(R,G,B)
  m = min(R,G,B)
  C = M - m

  if C == 0:
    Hp = 0
  elif M == R and G >= B:
    Hp = ((G-B)/C)
  elif M == R and G < B:
    Hp = ((G-B)/C) + 6
  elif M == G:
    Hp = ((B-R)/C) + 2
  elif M == B:
    Hp = ((R-G)/C) + 4

  H = 60 * Hp
  L = 0.5*(M+m)
  if (L <= 0.50):
    S = C/(2*L)
  else:
    S = C/(2-2*L)

  return [H, S, L]

def to_rgb(H, S, L):
  q = L * (1 + S) if (L < 0.5) else L + S - (L*S)
  p = 2 * L - q
  hk = H/360.

  t = [hk + 1/3., hk, hk - 1/3.]

  ret = []
  t = [(x + 1.0 if x < 0 else x - 1.0 if x > 1 else x) for x in t]
  for c in t:
    if c < 1/6.:
      C = p + ((q - p) * 6 * c)
    elif 1/6. <= c and c < 1/2.:
      C = q
    elif 1/2. <= c and c < 2/3.:
      C = p + ((q - p) * 6 * (2/3. - c))
    else:
      C = p
    ret.append(C)
  return ret

R = int(sys.argv[1][0:2], 16)/255.
G = int(sys.argv[1][2:4], 16)/255.
B = int(sys.argv[1][4:6], 16)/255.
a = float(sys.argv[2])

[H, S, L] = to_hsl(R,G,B)
print H
print S
print "%f + %f = %f" % (L, a, L+a)

[r, g, b] = [int(round(255*x)) for x in to_rgb(H, S, L + a)]
print "%.2x%.2x%.2x" % (r,g,b)
  
