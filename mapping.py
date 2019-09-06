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

def intm(s):
    if s == 'A':
        return 2
    if s == 'C':
        return 1
    if s == 'G':
        return 3
    if s == 'T':
        return 0

I = [intm(s) for s in S]


# Real

def real(s):
    if s == 'A':
        return -1.5
    if s == 'C':
        return 0.5
    if s == 'G':
        return -0.5
    if s == 'T':
        return 1.5

R = [real(s) for s in S]

# Complex

def complexM(s):
    if s == 'A':
        return 1+1j
    if s == 'C':
        return -1+1j
    if s == 'G':
        return -1-1j
    if s == 'T':
        return 1-1j

C = [complexM(s) for s in S]

# Quarternion

def quarter(s):
    if s == 'A':
        return (1,1,1)
    if s == 'C':
        return (1,-1,-1)
    if s == 'G':
        return (-1,-1,1)
    if s == 'T':
        return (-1,1,-1)

Q = [quarter(s) for s in S]

# EIIP

def EIIP(s):
    if s == 'A':
        return 0.1260
    if s == 'C':
        return 0.1340
    if s == 'G':
        return 0.0806
    if s == 'T':
        return 0.1335

E = [EIIP(s) for s in S]

# Atomnic Number

def atomic(s):
    if s == 'A':
        return 70
    if s == 'C':
        return 58
    if s == 'G':
        return 78
    if s == 'T':
        return 66

A = [atomic(s) for s in S]

# Paired Numeric

def pairedNum1(s):
    if s == 'A':
        return 1
    if s == 'C':
        return -1
    if s == 'G':
        return -1
    if s == 'T':
        return 1

P1 = [pairedNum1(s) for s in S]

def pairedNum21(s):
    if s == 'A':
        return 0
    if s == 'C':
        return -1
    if s == 'G':
        return -1
    if s == 'T':
        return 0

def pairedNum22(s):
    if s == 'A':
        return 1
    if s == 'C':
        return 0
    if s == 'G':
        return 0
    if s == 'T':
        return 1

P21 = [pairedNum21(s) for s in S]
P22 = [pairedNum22(s) for s in S]

# DNA Walk

def dnaWalk(s,x):
    if s == 'A':
        return x - 1
    if s == 'C':
        return x + 1
    if s == 'G':
        return x - 1
    if s == 'T':
        return x + 1

x = 0
D = []
for s in S:
    x = dnaWalk(s,x)
    D.append(x)    

# Z-curve



