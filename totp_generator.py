import time
from hotp_generator import hotp_value
import base64

def totp(key: bytes):
    counter = int(time.time() // 30)
    return hotp_value(key, counter.to_bytes((counter.bit_length() + 7) // 8, 'big'), 6)

if __name__ == '__main__':
    key = input("Enter your TOTP key: ")
    key = base64.b32encode(bytearray(key, 'ascii'))
    while True:
        print(totp(key))