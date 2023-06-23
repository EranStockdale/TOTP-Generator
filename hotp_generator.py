from hmac_generator import hmac, sha1

def to_bits(_bytes: bytes):
    return bin(int(_bytes.hex(), base=16)).removeprefix('0b').ljust(len(_bytes) * 8, '0')

def bitstring_to_bytes(s): # Thanks https://stackoverflow.com/questions/32675679/convert-binary-string-to-bytearray-in-python-3/32676625#32676625
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])

def extract31(mac: bytes, i: int):
    return bitstring_to_bytes(to_bits(mac)[i * 8 + 1:i * 8 + 4 * 8 - 1])

def truncate(mac: bytes):
    return extract31(
        mac,
        int(to_bits(mac)[19 * 8 + 4:19 * 8 + 7], base=2)
    )

def hotp(key: bytes, message: bytes):
    return truncate(hmac(key, message, sha1, 64, 20))

def hotp_value(key: bytes, message: bytes, d: int):
    return int(hotp(key, message).hex(), base=16) % (10 ** d)

if __name__ == '__main__':
    mac = hmac("key".encode(), "this is a message".encode(), sha1, 64, 20)
    print(len(mac))
    print(len(to_bits(mac)) / 8)
    print(mac.hex())
    print(to_bits(mac))
    print(int(to_bits(mac)[19 * 8 + 4:19 * 8 + 7], base=2))
    print(extract31(
        mac,
        int(to_bits(mac)[19 * 8 + 4:19 * 8 + 7], base=2)
    ))
    print(truncate(mac))

    print(hotp_value('hello'.encode(), 'message'.encode(), 6))