# Ashley J
# HW4 problem 2: Mix Columns


''' Fetch output files input state matrix'''
def readFile(fileName):
    newStateHex = ''                                                                # final state matrix(s) variable 
    with open(fileName, 'r') as infile:
        for line in infile:                                                         # while there is lines to read f/ file:
            line = line.strip()                                                     # strip whitespace
            stateArray = [int(line[i:i+2], 16) for i in range(0, 32, 2)]            # convert hex to byte rep.
            newState = mixColumns(stateArray)                                       # Apply MixColumns to each line of file 
            hexValues = ''.join(''.join(format(x, '02x') for x in row) for row in newState)  # change output f/ byte to hex 
            newStateHex += hexValues
    return newStateHex


''' Print Array & print to file if desired '''
def printArray(newArray):
    print("\n*** New State Array ***\n\n")
    for i in range(0, len(newArray), 32):
        print(newArray[i:i+32].upper())
    userAnswer = input("\n\nPrint to File: Type '1' \nExit program: Type '2'\n    : ")
    while userAnswer not in ['1', '2']:
        print("\nInvalid input.")
        userAnswer = input("Print to File: Type '1' \nExit program: Type '2'\n    : ")
    if userAnswer == '1':
        fileName = input("Filename: ") + ".txt"
        with open(fileName, 'w') as file:
            for i in range(0, len(newArray), 32):
                file.write(newArray[i:i+32].upper() + '\n')
    print("\nExiting program . . .\n")

''' this matrix is used in AES, it is multiplied with the 32 bit state array 
0x01 : multiply by 1
0x02 : multiply by x
0x03 : multiply by (x+1)
'''
opperator = [
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02]
]

''' multiplying #s in GF(2^4), 
checking if degree exceeds GF(2^4) & applying irriducible polynomial (x^8 + x^4 + x^3 + x + 1) '''
def multiply(a, b):
    result = 0
    while a and b:
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x100:                                                               # if 9th bit is set to ensure that bit is within 2^8 bit
            a ^= 0x11B                                                              # 0x11B is the Irreducible polynomial (x^8 + x^4 + x^3 + x + 1)
        b >>= 1
    return result

''' mixColumns takes a 4x4 array, it multiplies each state array element w/ its AES mix columns 'operator function', 
then XOR entire column line together  '''
def mixColumns(state):
    mixedState = [[0 for _ in range(4)] for _ in range(4)]                          # create 4x4 matrix filled w/ 0s
    for i in range(4):                                                              # the two for loops will interate through the 4x4 matrix
        for j in range(4):                                                          
            mixedState[i][j] = (                                                    # each value is multiplied with its AES opperator value
                multiply(opperator[i][0], state[0 + j]) ^                           # after we have retreived the values of the coloumn, XOR the entire column together
                multiply(opperator[i][1], state[4 + j]) ^
                multiply(opperator[i][2], state[8 + j]) ^
                multiply(opperator[i][3], state[12 + j])
            )
    return mixedState

# Main ----------------------------------------------------------------------------

print("********* Welcome to the Mix Columns Program *********")
fileName = input("\n\nPlease input your test file: ") 
newStateArray = readFile(fileName)                                                  # retrieve hex values f/ file & perform Mix columns
printArray(newStateArray)                                                           # print new state array &/OR write to file
