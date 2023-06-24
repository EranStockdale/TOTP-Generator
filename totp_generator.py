import time
from hotp_generator import hotp_value
import math

def get_decimal_time_steps(step_size = 30):
    return time.time() / step_size

def get_time_steps(step_size = 30):
    return math.floor(get_decimal_time_steps(step_size))

def totp(key: bytes, counter = None):
    if counter == None:
        counter = get_time_steps()
    
    return hotp_value(key, counter.to_bytes(8, 'big'), 6)