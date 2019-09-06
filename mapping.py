S = ['C', 'G', 'A', 'T']

# Voss

def voss(s,c):
    return 1 if s == c else 0

def vossMap(s):
    Cn = [ voss(s,'C') for s in S ]
    Gn = [ voss(s,'G') for s in S ]
    An = [ voss(s,'A') for s in S ]
    Tn = [ voss(s,'T') for s in S ]
    return Cn, Gn, An, Tn

# Tetrahedron



'''

def tetra(C,G,A,T):
    xr = math.sqrt(2)/3*(2*T-C-G)
    xg = math.sqrt(6)/3*(C-G)
    xb = 1/3*(3*A-T-C-G)
    return xr,xg,xb

T = [ tetra(voss(s,'C'), voss(s,'G'), voss(s,'A'), voss(s,'T')) for s in S ]

'''
import math

def tetra(s,c,C,G,A,T):
    if c == 'r':
        xr = math.sqrt(2)/3*(2*T-C-G)
        return xr
    if c == 'g':
        xg = math.sqrt(6)/3*(C-G)
        return xg
    if c == 'b':
        xb = 1/3*(3*A-T-C-G)
        return xb

def tetraMap(S):
    xr =  [ tetra(s,'r', voss(s,'C'), voss(s,'G'), voss(s,'A'), voss(s,'T')) for s in S ]
    xg =  [ tetra(s,'g', voss(s,'C'), voss(s,'G'), voss(s,'A'), voss(s,'T')) for s in S ]
    xb =  [ tetra(s,'b', voss(s,'C'), voss(s,'G'), voss(s,'A'), voss(s,'T')) for s in S ]
    return xr, xg, xb

# Integer



# Real



# Complex



# Quarternion



# EIIP



# Atomnic Number



# Paired Numeric



# DNA Walk



# Z-curve



