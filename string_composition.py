"""
    https://rosalind.info/problems/ba3a/

    Generate the k-mer composition of a string.
    Given: An integer k and a string Text.
    Return: Composition_k(Text) (the k-mers can be provided in any order).

    Synopsis:
    Run through each kmers in text and add it to the list of kmers.
    Return the list of kmers.
"""

def read_input(file_path: str) -> list[str]:
    """Reads the input file and returns the list of lines."""
    with open(file_path, "r") as input_file:
        return input_file.readlines()
    
def string_composition(k: int, text: str) -> list[str]:
    """Returns the k-mer composition of a string."""
    kmers = []
    for i in range(len(text) - k + 1):
        kmers.append(text[i:i+k])
    return kmers

def main():
    """Main call. Parses, runs, and saves problem specific data."""
    # Reading the input file
    output = read_input('datasets/rosalind_ba3a.txt')

    k = int(output[0].strip())
    text = output[1].strip()

    rc = string_composition(k, text)

    # Printing and saving answer
    print(rc)
    with open('solutions/rosalind_ba3a.txt', 'w') as output_file:
        for kmer in rc:
            output_file.write(kmer + '\n')
    
if __name__ == "__main__":
    main()
