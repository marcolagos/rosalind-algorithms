"""
    https://rosalind.info/problems/ba1b/

    Synopsis:
    Go through each seq_len sequence in the given text. For each
    of these call pattern_count. If the count returned is matches the 
    current max count or exceeds it, then update the max count and 
    patterns list appropriately. 
"""

from pattern_count import pattern_count

def frequent_words(text, seq_len) -> list:
    # Initialize the seen patterns, the max count seen, and the patterns corresponding to the max count
    patterns = set()
    max_count = 0
    max_patterns = []
    # Loop through indexes 0 through length of text - sequence length
    for i in range(len(text) - seq_len + 1):
        # Find substring of length seq_len for pattern
        new_pattern = text[i: i + seq_len]
        # If the pattern has not been seen, proceed
        if new_pattern not in patterns:
            patterns.add(new_pattern)
            # Find the count of the new pattern
            new_count = pattern_count(text, new_pattern)
            # Update the max count and max patterns accordingly
            if new_count == max_count:
                max_patterns.append(new_pattern)
            elif new_count > max_count:
                max_patterns = [new_pattern]
                max_count = new_count
    return max_patterns 