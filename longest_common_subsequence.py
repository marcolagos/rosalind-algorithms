"""
    https://rosalind.info/problems/ba5c/

    Find the longest common subsequence of two strings.

    Synopsis:
    Using DP, we can find the longest common subsequence in O(mn) time.
    The idea is to create a table L[m+1][n+1] where L[i][j] represents the length of the LCS of the strings X[0...i-1] and Y[0...j-1].
    If the last characters of both sequences match (X[i-1] == Y[j-1]), then L[i][j] = L[i-1][j-1] + 1.
    Otherwise, L[i][j] = max(L[i-1][j], L[i][j-1]).
"""

def read_input(file_path: str) -> list[str]:
    """Reads the input file and returns the list of lines."""
    with open(file_path, "r") as input_file:
        return input_file.readlines()

def lcs(X, Y):
    m, n = len(X), len(Y)
    
    L = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build L[m][n] in bottom up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
                
    index = L[m][n]
    
    lcs = [''] * (index + 1)
    lcs[index] = ''
    
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(lcs)


def main():
    """Main call. Parses, runs, and saves problem specific data."""
    # Reading the input file
    input = read_input('datasets/rosalind_ba5c.txt')

    subseq = lcs(input[0], input[1])
    # Printing and saving answer
    with open('solutions/rosalind_ba5c.txt', 'w') as output_file:
        output_file.write(subseq)

if __name__ == "__main__":
    main()