'''
References:
 - https://www.youtube.com/watch?v=WPz4Kzz6vk4
'''
opperator = [
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03,0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02]
]

''' Multiplication in GF(2^8)
In this function we mutliply the binary values together, if the value becomes (x^7) <  then 
take the mod of the output of 2^8 which is the polynomial of 11b
'''  
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

''' 
(1) function does matrix multiplication // aka first row of opperatorMatrix gets opperated on the first column of stateMatrix
(2) Send the values to the multiply() to do polynomial multiplication in GF(2^8)
(3) XOR each row for the value being solved, if uneven # of 1s then remain 1 else 0
'''
def mixColumns(state):
    # applying 4 rounds of matrix multiplication
    mixed_state = []
    for i in range(4):
        # {0x01} means mult by 1 // aka stays the same 
        # {0x02} means mult by x
        # {0x03} means mult by x + 1
        mixed_column = [
            multiply(0x02, state[0][i]) ^ multiply(0x03, state[1][i]) ^ state[2][i] ^ state[3][i],
            state[0][i] ^ multiply(0x02, state[1][i]) ^ multiply(0x03, state[2][i]) ^ state[3][i],
            state[0][i] ^ state[1][i] ^ multiply(0x02, state[2][i]) ^ multiply(0x03, state[3][i]),
            multiply(0x03, state[0][i]) ^ state[1][i] ^ state[2][i] ^ multiply(0x02, state[3][i])
        ]
        mixed_state.append(mixed_column)
    
    print("mixed_state", mixed_state)       # delete
    return mixed_state

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def printMatrix(state):
    for row in state:
        print(' '.join(f'{byte:02x}' for byte in row))

# Example usage:
stateArray = [
    [0x87, 0xf2, 0x4d, 0x97],
    [0x6e, 0x4c, 0x90, 0xec],
    [0x46, 0xe7, 0x4a, 0xc3],
    [0xa6, 0x8c, 0xd8, 0x95]
]

print("Original state:")
printMatrix(stateArray)

newState = mixColumns(stateArray)

print("\nNew State Array:")
newState = transpose(newState)
printMatrix(newState)
