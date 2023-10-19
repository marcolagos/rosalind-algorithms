"""
    https://rosalind.info/problems/ba3e/

    Construct the de Bruijn graph from a collection of k-mers.
    Given: A collection of k-mers Patterns.
    Return: The de Bruijn graph DeBruijn(Patterns), in the form of an adjacency list.

    Synopsis:
    Run through each kmer in patterns and find the suffix of the kmer.
    Run through each kmer in patterns and find the prefix of the kmer.
    If the suffix of the first kmer is equal to the prefix of the second kmer,
    add the kmer to the adjacency list. 
"""
from collections import defaultdict

def read_input(file_path: str) -> list[str]:
    """Reads the input file and returns the list of lines."""
    with open(file_path, "r") as input_file:
        return input_file.readlines()

def construct_debruijn(kmers):
    graph = defaultdict(list)
    # Run through each kmer in patterns and find the suffix of the kmer.
    # Run through each kmer in patterns and find the prefix of the kmer.
    # If the suffix of the first kmer is equal to the prefix of the second kmer,
    # add the kmer to the adjacency list.
    for i in range(len(kmers)):
        graph[kmers[i][:-1]].append(kmers[i][1:])
    return graph

def main():
    """Main call. Parses, runs, and saves problem specific data."""
    # Reading the input file
    patterns = read_input('datasets/rosalind_ba3e.txt')
    patterns = [pattern.strip() for pattern in patterns]

    graph = construct_debruijn(patterns)

    # Printing and saving answer
    with open('solutions/rosalind_ba3e.txt', 'w') as output_file:
        for key, values in graph.items():
            value_str = ','.join(map(str, values))
            edge = key + ' -> ' + value_str
            output_file.write(edge + '\n')

if __name__ == "__main__":
    main()