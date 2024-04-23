#!/usr/bin/env python3

# Jeremy Escobar / Spring 545 Session A
import hashlib
import random


def generate_md5_hash_starting_with_null_byte(length):
    """Generates a string of the specified length whose MD5 hash begins with a NULL byte"""
    while True:
        st = ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(length))
        # print("String:",st) # 32 bytes to fill the ring_buffer
        md5_hash = hashlib.md5(st.encode('ascii')).hexdigest()  # 32 bytes to fill the ring_buffer
        # print(md5_hash)
        if md5_hash.startswith('00'):  # Check if the hash starts with a NULL byte (00 in hex) and return the string
            return st

# Generate a string of length 32 whose MD5 hash begins with a NULL byte.
strings = generate_md5_hash_starting_with_null_byte(32)  # 32 bytes to fill the ring_buffer

# Print the string and its MD5 hash.
print(strings)  # 32 bytes to fill the ring_buffer    # 32 bytes to fill the ring_buffer
print(hashlib.md5(strings.encode('ascii')).hexdigest())
