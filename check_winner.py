#!/usr/bin/env python3

import sys
from scipy.stats import chi2

p = [int(x) for x in sys.argv[1:]]
p = sorted(p, reverse=True)
n = len(p)

if (p[0]-p[1])**2 / (p[0]+p[1]) > chi2.isf(0.05, n-1):
    print('winner is unquestionable')
else:
    print('winner might have been just lucky')
