# def int_to_bin(int: int, bits: int):
    # out_bytes = bytearray()
    # for _ in range(bits)

def to_base32(string: str) -> bytes:
    values = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
    encoded_ints = [values.index(char) for char in string]
    print(bytearray(encoded_ints).hex())

if __name__ == '__main__':
    import base64
    from totp_generator import totp, get_time_steps, get_decimal_time_steps
    from hotp_generator import to_bits
    import math
    time_step_size = 30

    key = input("Enter your TOTP key: ")
    # key = key.encode('ascii')
    key = base64.b32decode(key.upper())
    # for i in range(get_time_steps(time_step_size) - 100, get_time_steps(time_step_size)):
    #     print(totp(key = key, counter = i))
    
    while True: 
        print(totp(key), f"Updating in {math.floor(time_step_size * (1 - (get_decimal_time_steps(time_step_size) % 1))) + 1} second(s)")