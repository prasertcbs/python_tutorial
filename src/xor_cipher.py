# https://en.wikipedia.org/wiki/XOR_cipher
from itertools import cycle


def string_to_bin(s):
    # b = []
    # for c in s:
    #     b.append("{:08b}".format(ord(c)))
    # return b
    return ["{:08b}".format(ord(c)) for c in s]

def xor_cipher(text, key):
    # x = []
    # for t, k in zip(text, cycle(key)):
    #     x.append(chr(ord(t) ^ ord(k)))
    # return "".join(x)
    x = [chr(ord(t) ^ ord(k)) for t, k in zip(text, cycle(key))]
    return "".join(x)

# print(string_to_bin("Wiki"))
# print(" ".join(string_to_bin("Wiki")))
t = "somewhere over the rainbow"
k = "snake"
encrypted = xor_cipher(t, k)
print(encrypted)
print(" ".join(string_to_bin(t)))
print(" ".join(string_to_bin(k * len(t))))
print(" ".join(string_to_bin(encrypted)))

decrypted = xor_cipher(encrypted, k)
print(decrypted)