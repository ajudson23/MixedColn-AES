def parse_input(filename):
    stateArray = []
    with open(filename, 'r') as file:
        for line in file:
            values = line.strip().split()
            row = [int(value, 16) for value in values]
            stateArray.append(row)
    return stateArray

# Example usage:
if __name__ == "__main__":
    filename = "classEx.txt"
    stateArray = parse_input(filename)
    print("Parsed stateArray:")
    for row in stateArray:
        print(row)