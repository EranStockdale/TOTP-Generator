import hashlib

def sha1(inp: bytes):
    m = hashlib.sha1()
    m.update(inp)
    return m.digest()

def computeBlockSizedKey(key: bytes, hash_function, blockSize: int):
    if len(bytearray(key)) > blockSize:
        key = hash_function(key)
    
    if len(bytearray(key)) < blockSize:
        return (b"\0" * (blockSize - len(bytearray(key)))) + key
    
    return key

def hmac(key: bytes, message: bytes, hash_function, blockSize: int, outputSize: int):
    block_sized_key = computeBlockSizedKey(key, hash_function, blockSize)

    o_key_pad = (int.from_bytes(block_sized_key, 'big') ^ int.from_bytes(bytes([0x5c] * blockSize), 'big')).to_bytes(blockSize, 'big')
    i_key_pad = (int.from_bytes(block_sized_key, 'big') ^ int.from_bytes(bytes([0x36] * blockSize), 'big')).to_bytes(blockSize, 'big')

    # print(block_sized_key)
    # print(o_key_pad)
    # print(i_key_pad)
    # print(i_key_pad + message)

    return hash_function(bytearray(o_key_pad) + bytearray(hash_function(bytearray(i_key_pad) + bytearray(message))))

if __name__ == '__main__':
    mac = hmac("key".encode(), "this is a message".encode(), sha1, 64, 20)
    print(len(mac))