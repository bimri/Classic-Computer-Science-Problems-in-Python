"Unbreakable Encryption"

from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    """
    This function creates an int filled with length 
    random bytes. The method int.from_
    bytes() is used to convert from bytes to int.
    """
    # generate length random bytes
    tb: bytes = token_bytes(length)
    # convert those bytes into a bit string and return it
    return int.from_bytes(tb, "big")


'''
In Python, the XOR operator is ^. In the context of the bits of binary numbers,
XOR returns 1 for 0 ^ 1 and 1 ^ 0, but 0 for 0 ^ 0 and 1 ^ 1. If the bits of two numbers
are combined using XOR, a helpful property is that the product can be recombined
with either of the operands to produce the other operand:
A ^ B = C
C ^ B = A
C ^ A = B
'''


def encrypt(original: str) -> Tuple[int, int]:
    """
    int.from_bytes() is being passed two arguments. The first is the
    bytes that we want to convert into an int. The second is the endianness of
    those bytes ("big"). Endianness refers to the byte-ordering used to store data.
    """
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy       # XOR
    return dummy, encrypted

 
def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2                # XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length()+ 7) // 8, "big")
    return temp.decode()
 

if __name__ == "__main__":
    key1, key2 = encrypt("One Time Pad!")
    result: str = decrypt(key1, key2)
    print(result)
