"""
    https://rosalind.info/problems/ba1c/

    Synopsis:
    Iterate through the Genome from index 0 to the length of the Genome.
    Check if the current character is A, T, G, or C. If so, append the complement 
    to the reverse complement. Return the reverse complement.
"""

def read_input(file_path: str) -> list[str]:
    """Reads the input file and returns the list of lines."""
    with open(file_path, "r") as input_file:
        return input_file.readlines()
    
def reverse_complement(genome: str) -> str:
    """Returns the reverse complement of the genome."""
    reverse_complement = ''
    # Iterate through the Genome from index 0 to the length of the Genome.
    for i in range(len(genome)):
        # Check if the current character is A, T, G, or C. 
        if genome[i] == 'A':
            reverse_complement += 'T'
        elif genome[i] == 'T':
            reverse_complement += 'A'
        elif genome[i] == 'G':
            reverse_complement += 'C'
        elif genome[i] == 'C':
            reverse_complement += 'G'
    return reverse_complement

def main():
    """Main call. Parses, runs, and saves problem specific data."""
    # Reading the input file
    genome = read_input('datasets/rosalind_ba1c.txt')

    rc = reverse_complement(genome[0])

    # Printing and saving answer
    print(rc)
    with open('solutions/rosalind_ba1c.txt', 'w') as output_file:
        output_file.write(rc)
    
if __name__ == "__main__":
    main()
