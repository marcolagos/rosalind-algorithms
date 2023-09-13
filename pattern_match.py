"""
    https://rosalind.info/problems/ba1d/

    Synopsis:
    Iterate through the Genome from index 0 to length of Genome - length of pattern.
    Check if the substring of current index to current index + length of pattern.
    If so, append the index to the list of indices. Return the list of indices.
"""

def read_input(file_path: str) -> list[str]:
    """Reads the input file and returns the list of lines."""
    with open(file_path, "r") as input_file:
        return input_file.readlines()

def pattern_match(genome: str, pattern: str) -> list[int]:
    """Returns the list of indices where pattern matches genome."""
    indices = []
    # Iterate through the Genome from index 0 to length of Genome - length of pattern.
    for i in range(len(genome) - len(pattern) + 1):
        # Check if the substring of current index to current index + length of pattern.
        if genome[i: i + len(pattern)] == pattern:
            indices.append(i)
    return indices

def main():
    """Main call. Parses, runs, and saves problem specific data."""
    # Reading the input file
    pattern, genome = read_input('datasets/rosalind_ba1d.txt')
    pattern = pattern.strip()
    genome = genome.strip()

    indices = pattern_match(genome, pattern)

    # Printing and saving answer
    print(' '.join(map(str, indices)))
    with open('solutions/rosalind_ba1d.txt', 'w') as output_file:
        output_file.write(' '.join(map(str, indices)))

if __name__ == "__main__":
    main()
