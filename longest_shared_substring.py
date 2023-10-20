"""
    https://rosalind.info/problems/ba9e/
"""

def read_input(file_path: str) -> list[str]:
    """Reads the input file and returns the list of lines."""
    with open(file_path, "r") as input_file:
        return input_file.readlines()

def longest_shared_substring(text1, text2):
    if len(text1) > len(text2):
        longer, shorter = text1, text2
    else:
        longer, shorter = text2, text1

    for length in range(len(shorter), 0, -1):
        for i in range(len(shorter) - length + 1):
            substring = shorter[i:i+length]
            if substring in longer:
                return substring

    return ""


def main():
    """Main call. Parses, runs, and saves problem specific data."""
    # Reading the input file
    input = read_input('datasets/rosalind_ba9e.txt')
    
    # Printing and saving answer
    with open('solutions/rosalind_ba9e.txt', 'w') as output_file:
        output_file.write(longest_shared_substring(input[0], input[1]))

if __name__ == "__main__":
    main()