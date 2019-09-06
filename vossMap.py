import requests

def vossMap(s):
    def voss(s,c):
        return 1 if s == c else 0

    Cn = [ voss(s,'C') for s in S ]
    Gn = [ voss(s,'G') for s in S ]
    An = [ voss(s,'A') for s in S ]
    Tn = [ voss(s,'T') for s in S ]

    return Cn, Gn, An, Tn

SEQUENCES_URL = 'https://raw.githubusercontent.com/abidlabs/deep-learning-genomics-primer/master/sequences.txt'
sequences = requests.get(SEQUENCES_URL).text.split('\n')
sequences = list(filter(None, sequences))  # This removes empty sequences.

n = 1000
sequence = sequences[n]

print("Sequence no " + str(n) + ": " + sequence)
print("Voss Mapping of Sequence: ")
S = [s for s in sequence]
C, G, A, T = vossMap(S)

print(" Xc : ") 
print(C)

print(" Xg : ") 
print(G)

print(" Xa : ") 
print(A)

print(" Xt : ") 
print(T)

# STDFT


import cmath

def stdft(x, L = 50):
    X = []
    for K in range(L-1):
        S = 0
        for n in range(L-1):
            S = S + x[n]*cmath.exp(-1j*2*math.pi/L*K*n)
        X.append(S)
    return X
        
Xc = stdft(C)
Xa = stdft(A)
Xt = stdft(T)
Xg = stdft(G)

P = []

for p in range

a = 3 + 2j
cmath.polar(a)[0]


