def gf_mult(a, b):
    p = 0
    for _ in range(4):
        if b & 1:
            p ^= a
        hi_bit_set = a & 0x8
        a <<= 1
        if hi_bit_set:
            a ^= 0x13  # AES modular polynomial: x^4 + x + 1
        b >>= 1
    return p


def aes_gf_mult_table():
    table = [[0 for _ in range(16)] for _ in range(16)]
    for i in range(16):
        for j in range(16):
            table[i][j] = gf_mult(i, j)
    return table


def print_table(table):
    print("AES GF(2^4) Multiplication Table:")
    print("    ", end="")
    for i in range(16):
        print(f"{i:2X} ", end="")
    print()
    print("  " + "-" * 39)
    for i in range(16):
        print(f"{i:2X} |", end="")
        for j in range(16):
            print(f"{table[i][j]:2X} ", end="")
        print()


if __name__ == "__main__":
    mult_table = aes_gf_mult_table()
    print_table(mult_table)
