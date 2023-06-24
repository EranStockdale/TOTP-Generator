desired_code = input("What code do you want to be generated? ")
desired_time_step = int(input("What time step do you wish this to happen at? "))

d = len(desired_code)
desired_code = int(desired_code)

from totp_generator import generate_totp, totp
import os, random
random_base32 = lambda length: ''.join([random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ234567") for _ in range(length)])

searched = 0
while True:
    key = random_base32(24)
    generated_code = generate_totp(key, desired_time_step, d)
    print(f"Searched {searched} keys", end='\r')
    searched += 1
    if generated_code == desired_code:
        print(key, generated_code)
        break