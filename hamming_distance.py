"""
    https://rosalind.info/problems/ba2h/

    Find the distance between a pattern and a set of strings.
    Given: A DNA string Pattern and a collection of DNA strings Dna.
    Return: DistanceBetweenPatternAndStrings(Pattern, Dna).

    Synopsis:
    Run through each string in dna and find the minimum hamming distance
    between pattern and all k-mers in the string. Add the minimum hamming
    distance to the distance variable. Return the distance variable.
"""

def read_input(file_path: str) -> list[str]:
    """Reads the input file and returns the list of lines."""
    with open(file_path, "r") as input_file:
        return input_file.readlines()
    
def find_hamming_distance(pattern: str, kmer: str) -> int:
    """Returns the hamming distance between two strings."""
    hamming_distance = 0
    for i in range(len(pattern)):
        # If the kmer is shorter than the pattern, we assume that the
        # missing nucleotides are different from the pattern.
        if len(kmer) <= i or pattern[i] != kmer[i]:
            hamming_distance += 1
    return hamming_distance
    
def distance_between_pattern_and_strings(pattern: str, dna: list) -> str:
    """Returns the distance between a pattern and a set of strings."""
    k = len(pattern)
    distance = 0
    # For each string in dna, find the minimum hamming distance between
    # pattern and all k-mers in the string.
    for string in dna:
        hamming_distance = float('inf')
        # For each k-mer in the string, find the hamming distance.
        # If the hamming distance is smaller than the previous one,
        # update the hamming distance.
        for i in range(len(string) - k + 1):
            kmer = string[i:i+k]
            if hamming_distance > find_hamming_distance(pattern, kmer):
                hamming_distance = find_hamming_distance(pattern, kmer)
        distance += hamming_distance
    return distance

def main():
    """Main call. Parses, runs, and saves problem specific data."""
    # Reading the input file
    output = read_input('datasets/rosalind_ba2h.txt')

    pattern = output[0].strip()
    dna = output[1].strip().split(' ')

    rc = distance_between_pattern_and_strings(pattern, dna)

    # Printing and saving answer
    print(rc)
    with open('solutions/rosalind_ba2h.txt', 'w') as output_file:
        output_file.write(str(rc))
    
if __name__ == "__main__":
    main()
