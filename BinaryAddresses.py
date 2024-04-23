from pwnlib.elf import ELF
from pwn import *
# Jeremy Escobar CSE545, Spring 2024 Session A

def analyze_binary(binary_path):
    elf = ELF(binary_path)
    for function in elf.symbols:
        print(f"Function: {function}, Address: {hex(elf.symbols[function])}")


def calculate_offset(binary_path, target_addresses):
    elf = ELF(binary_path)
    offsets = {}
    for target_address in target_addresses:
        if target_address in elf.symbols:
            offset = elf.symbols[target_address] - elf.symbols[target_addresses[0]]
            offsets[target_address] = offset
        else:
            print(f"Function or address {target_address} not found in the binary.")
    return offsets


binary_path = '/challenge/run'

# Analyze the binary to list functions and their addresses
analyze_binary(binary_path)
