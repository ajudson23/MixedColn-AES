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
            hexValues = ''.join(format(x, '02x') for x in newState)                 # change output f/ byte to hex 
            newStateHex += (hexValues)           
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
            file.write(newArray)
    print("\nExiting program . . .\n")


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


''' mixColumns takes a 4x4 array, 
it takes each column of the original state matrix '''
def mixColumns(state):
    for i in range(4):                                                              # for a 4x4 matrix, 4 iterations per column
        column = [state[i], state[4+i], state[8+i], state[12+i]]  
        t = column[0] ^ column[1] ^ column[2] ^ column[3] 
        u = column[0] 
        column[0] ^= t ^ multiply(0x02, column[0] ^ column[1])
        column[1] ^= t ^ multiply(0x02, column[1] ^ column[2])
        column[2] ^= t ^ multiply(0x02, column[2] ^ column[3])
        column[3] ^= t ^ multiply(0x02, column[3] ^ u)
        # rearange the colns for the 
        for j in range(4):
            state[j*4+i] = column[j]
    return state

# Main ----------------------------------------------------------------------------

print("********* Welcome to the Mix Columns Program *********")
fileName = input("\n\nPlease input your test file: ") 
newStateArray = readFile(fileName)                                                  # retrieve hex values f/ file & perform Mix columns
printArray(newStateArray)                                                           # print new state array &/OR write to file
                                                 

