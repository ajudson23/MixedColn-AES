import os

opperator = [
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03,0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02]
]

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

def makeFile(newText):
    fileName = input("Filename: ") + ".txt"
    with open(fileName, 'w') as file:
        file.write(newText)
'''
def readFile():
    fileName = input("\n\nInput your test file: ")
    filePath = os.path.abspath(fileName)
    if os.path.exists(filePath):
        with open(filePath, 'r') as file:
            #
    else:
        print(f"File '{filePath}' not found.")
        return None, None, None
'''

def printMatrix(newState):
    for row in newState:
        print(' '.join(f'{byte:02x}'.upper() for byte in row))


# Main -----------------------------------------------------------------

stateArray = [
    [0xEA, 0x04, 0x65, 0x85],
    [0x45, 0x5d, 0x96, 0x83],
    [0x98, 0xb0, 0x5c, 0x33],
    [0xc5, 0xf0, 0x2d, 0xad]
]
print("Original State Matrix:")
printMatrix(stateArray)

# Provide Mixed Columns
newState = matrix_multiply(opperator, stateArray)
print("\nNew State Matrix:")
printMatrix(newState)

# userAnswer = input("\n\nPrint to File: Type '1' \nExit program: Type '2'\n    : ")
# while userAnswer not in ['1', '2']:
#     print("\nInvalid input.")
#     userAnswer = input("Print to File: Type '1' \nExit program: Type '2'\n    : ")
# if userAnswer == '1':
#     makeFile(newState)

