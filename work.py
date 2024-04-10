import os


def lines_to_matrix(lines):
    matrix = []
    for line in lines:
        row = [f"0x{line[i:i+2].upper()}" for i in range(0, len(line.strip()), 2)]
        matrix.append(row)
    return matrix


# Function to read lines from a text file and create 4x4 matrices
def read_lines_from_file(filename):
    filePath = os.path.abspath(filename)
    if os.path.exists(filePath):
        with open(filePath, 'r') as file:
            while True:
                # Read one line
                lines = [file.readline().strip()]
                if not lines[0]:  # If the line is empty, there are no more lines to read
                    break
                matrix = lines_to_matrix(lines)
                print("Matrix:\n", matrix)
                print()  
    else:
        print(f"File '{filename}' not found.")

# Main function
def main():
    print("********* Reading Lines and Creating Matrices from Text File *********")
    fileName = input("\nPlease input the filename: ")
    read_lines_from_file(fileName)

if __name__ == "__main__":
    main()
