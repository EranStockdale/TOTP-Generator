# def int_to_bin(int: int, bits: int):
    # out_bytes = bytearray()
    # for _ in range(bits)

def to_base32(string: str) -> bytes:
    values = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
    encoded_ints = [values.index(char) for char in string]
    print(bytearray(encoded_ints).hex())

if __name__ == '__main__':
    from totp_generator import generate_totp, get_time_steps, get_decimal_time_steps
    from hotp_generator import to_bits
    import math
    time_step_size = 30

    key = input("Enter your TOTP key: ")
    prev_totp = None
    for i in range(get_time_steps(time_step_size) - 100, get_time_steps(time_step_size)):
        new_totp = generate_totp(key, counter=i - 1)
        if prev_totp != new_totp:
            print(i - 1, new_totp)
            prev_totp = new_totp
    
    while True:
        new_totp = generate_totp(key)
        if prev_totp != new_totp:
            prev_totp = new_totp
            # print(prev_totp)
        print(new_totp, f"Updating in {math.floor(time_step_size * (1 - (get_decimal_time_steps(time_step_size) % 1))) + 1} second(s)", end=('\r' if prev_totp == new_totp else '\n'))