"""
    https://rosalind.info/problems/ba1a/

    Synopsis:
    The solution first assumes that length of pattern < length of text. 
    Loop through all indexes from 0 to length of text - length of pattern.
    Check if the substring of current index to current index + length of pattern
    equals pattern. If so, increment the count. Return the count.
"""

def pattern_count(text, pattern) -> int:
    count = 0
    # Loop through each sequence of characters of length pattern
    for i in range(len(text) - len(pattern) + 1):
        # Check if the current sequence is pattern. If so, increment the count.
        if text[i: i + len(pattern)] == pattern:
            count += 1
    return count
