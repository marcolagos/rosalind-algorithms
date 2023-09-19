"""
    https://rosalind.info/problems/ba5g/

    Find the edit distance between two strings.
    Given: Two amino acid strings.
    Return: The edit distance between these strings.

    Synopsis:
    Initialize the dp matrix. Initialize the first row and column.
    Fill in the rest of the matrix. Return the bottom right value.
"""

def read_input(file_path: str) -> list[str]:
    """Reads the input file and returns the list of lines."""
    with open(file_path, "r") as input_file:
        return input_file.readlines()
    
def edit_distance(str1: str, str2:str) -> int:
    """Returns the edit distance between two strings."""
    # Initialize the dp matrix
    matrix = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    # Initialize the first row
    for i in range(len(str1) + 1):
        matrix[i][0] = i
    # Initialize the first column
    for j in range(len(str2) + 1):
        matrix[0][j] = j
    # Fill in the rest of the matrix
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            # If the nucleotides are the same, the cost is 0.
            # Otherwise, the cost is 1.
            insertion = matrix[i][j - 1] + 1
            # Deletion is the same as insertion.
            deletion = matrix[i - 1][j] + 1
            match = matrix[i - 1][j - 1]
            mismatch = matrix[i - 1][j - 1] + 1
            # If the nucleotides are the same, the cost is 0.
            # Otherwise, the cost is 1.
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = min(insertion, deletion, match)
            else:
                matrix[i][j] = min(insertion, deletion, mismatch)
    return matrix[-1][-1]

def main():
    """Main call. Parses, runs, and saves problem specific data."""
    # Reading the input file
    text = read_input('datasets/rosalind_ba5g.txt')

    rc = edit_distance(text[0].strip(), text[1].strip())

    # Printing and saving answer
    print(rc)
    with open('solutions/rosalind_ba5g.txt', 'w') as output_file:
        output_file.write(str(rc))
    
if __name__ == "__main__":
    main()
