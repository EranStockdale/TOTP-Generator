factorial = lambda n, depth: factorial(n - 1, depth - 1) * n if n > 1 and depth > 1 else 1

key_len = int(input("How long is the key? "))

charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
possibilities = factorial(len(charset), key_len)
print(f"Calculated that there are {possibilities} possible different keys of length {key_len}")

# from itertools import product
# keys = [''.join(key) for key in product(charset, repeat=key_len)]
# print(len(keys))

print(f"Now, enter some values of the TOTP so that the brute force can begin.")
print(f"These need to be entered in the format [Counter]:[Code] and seperated by commas (,).")
raw_input = input("")
values = raw_input.split(",")
examples = sorted([tuple([int(i) for i in example.split(':')]) for example in values], key=lambda tup: tup[0])

import random
from totp_generator import generate_totp
random_base32 = lambda length: ''.join([random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ234567") for _ in range(length)])
max_checks_matched = -1
best_key = None
import atexit
atexit.register(lambda: print(best_key, max_checks_matched))
while True:
    key = random_base32(key_len)
    for idx, totp in enumerate(examples):
        if generate_totp(key, totp[0]) == totp[1]:
            print(f"Key {key} matches check #{idx + 1}")
            if idx + 1 == len(examples):
                print(f"Found match for all checks: {key}")
            if idx + 1 > max_checks_matched:
                max_checks_matched = idx + 1
                best_key = key
        else:
            if idx > 0:
                print(f"Key {key} does not match all checks. Got to check #{idx}")
            break
    print(f" Crnt Max: {max_checks_matched}", end='\r')