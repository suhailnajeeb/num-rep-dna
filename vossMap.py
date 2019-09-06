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