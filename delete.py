def gf256_mul(a, b):
    # Multiply two numbers in the GF(2^8) finite field defined
    # by the polynomial x^8 + x^4 + x^3 + x + 1.
    p = 0
    while a and b:
        if b & 1:  # If the lowest bit of b is set
            p ^= a  # Add (XOR) a to the result
        if a & 0x80:  # If the highest bit of a is set
            a = (a << 1) ^ 0x11b  # Left shift a and reduce by the AES modulus
        else:
            a <<= 1  # Otherwise, just left shift a
        b >>= 1  # Right shift b
    return p


def mix_single_column(a):
    # Mix a single column of the state matrix using the AES MixColumns transformation.
    t = a[0] ^ a[1] ^ a[2] ^ a[3]  # XOR of all column bytes
    u = a[0]  # Copy of the first element
    # Mix using the AES polynomial
    a[0] ^= t ^ gf256_mul(0x02, a[0] ^ a[1])
    a[1] ^= t ^ gf256_mul(0x02, a[1] ^ a[2])
    a[2] ^= t ^ gf256_mul(0x02, a[2] ^ a[3])
    a[3] ^= t ^ gf256_mul(0x02, a[3] ^ u)
    return a


def mix_columns(state):
    # Apply the MixColumns step to the state matrix.
    for i in range(4):
        column = [state[i], state[4+i], state[8+i], state[12+i]]  # Extract the column
        column = mix_single_column(column)  # Mix it
        # Put the mixed column back into the state
        for j in range(4):
            state[j*4+i] = column[j]
    return state


def process_file(input_filename, output_filename):
    # Reads an input file with hexadecimal strings, applies MixColumns, and writes the output.
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            line = line.strip()  # Remove any whitespace
            # Convert the hex string to a byte array
            state = [int(line[i:i+2], 16) for i in range(0, 32, 2)]
            mixed_state = mix_columns(state)  # Apply MixColumns
            # Convert the byte array back to a hex string and write it to the output
            output_hex = ''.join(format(x, '02x') for x in mixed_state)
            outfile.write(output_hex + '\n')


process_file('2a.txt', 'output.txt')
