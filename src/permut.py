import sys
from itertools import permutations


def permute(s: str)->list:
    d = set(permutations(s, len(s)))
    w = ["".join(v) for v in d]
    return sorted(w)


s = sys.argv[1]
# s='123'
# s='LOVE'
print(permute(s))
