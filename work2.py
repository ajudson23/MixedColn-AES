def multiply(a, b):
    result = 0
    while a and b:
        if b & 1:
            result ^= a
        a <<= 1
        # if 9th bit is set to ensure that bit is within 2^8 bit
        if a & 0x100:
            a ^= 0x11B  # 0x11B is the Irreducible polynomial (x^8 + x^4 + x^3 + x + 1)
        b >>= 1
    return result

def matrix_multiply(opperator, stateArray):
    result = [[0 for _ in range(4)] for _ in range(4)]
    
    for i in range(4):
        for j in range(4):
            for k in range(4):
                result[i][j] ^= multiply(opperator[i][k], stateArray[k][j])
    
    return result


opperator = [
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03,0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02]
]

stateArray = [
    [0x87, 0xf2, 0x4d, 0x97],
    [0x6e, 0x4c, 0x90, 0xec],
    [0x46, 0xe7, 0x4a, 0xc3],
    [0xa6, 0x8c, 0xd8, 0x95]
]

newState = matrix_multiply(opperator, stateArray)

for row in newState:
    print(' '.join(f'{byte:02x}' for byte in row))
