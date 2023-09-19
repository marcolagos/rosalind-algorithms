"""
    https://rosalind.info/problems/ba3c/

    Construct the overlap graph of a collection of k-mers.
    Given: A collection Patterns of k-mers.
    Return: The overlap graph Overlap(Patterns), in the form of an adjacency list.

    Synopsis:
    Run through each kmer in patterns and find the suffix of the kmer.
    Run through each kmer in patterns and find the prefix of the kmer.
    If the suffix of the first kmer is equal to the prefix of the second kmer,
    add the kmer to the adjacency list.
"""

def read_input(file_path: str) -> list[str]:
    """Reads the input file and returns the list of lines."""
    with open(file_path, "r") as input_file:
        return input_file.readlines()
    
def overlap_graph(patterns: list[str]) -> dict[str, list[str]]:
    """Returns the overlap graph of a collection of k-mers."""
    adjacency_list = {}
    for i in range(len(patterns)):
        suffix = patterns[i][1:]
        for j in range(len(patterns)):
            prefix = patterns[j][:-1]
            if suffix == prefix:
                if patterns[i] not in adjacency_list:
                    adjacency_list[patterns[i]] = []
                adjacency_list[patterns[i]].append(patterns[j])
    return adjacency_list

def main():
    """Main call. Parses, runs, and saves problem specific data."""
    # Reading the input file
    patterns = read_input('datasets/rosalind_ba3c.txt')
    patterns = [pattern.strip() for pattern in patterns]
    rc = overlap_graph(patterns)

    # Printing and saving answer
    print(rc)
    with open('solutions/rosalind_ba3c.txt', 'w') as output_file:
        for key, values in rc.items():
            for value in values:
                kmer = key + ' -> ' + value
                output_file.write(kmer + '\n')
    
if __name__ == "__main__":
    main()
