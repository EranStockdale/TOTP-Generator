import time
from hotp_generator import hotp_value
import math
import base64

def get_decimal_time_steps(step_size = 30):
    return time.time() / step_size

def get_time_steps(step_size = 30):
    return math.floor(get_decimal_time_steps(step_size))

def totp(key: bytes, counter: int = None, code_length: int = 6):
    if counter == None:
        counter = get_time_steps()
    
    return hotp_value(key, counter.to_bytes(8, 'big'), code_length)

def generate_totp(key: str, counter: int = None, code_length: int = 6):
    if counter == None:
        counter = get_time_steps()

    key = base64.b32decode(key.upper() + '=' * ((8 - len(key)) % 8))
    
    return totp(key, counter, code_length)