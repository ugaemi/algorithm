def makingAnagrams(s1, s2):
    from collections import Counter

    # Count the frequency of each character in both strings
    count1 = Counter(s1)
    count2 = Counter(s2)

    # Calculate the total deletions needed
    deletions = 0

    # Get all unique characters from both strings
    all_chars = set(count1.keys()).union(set(count2.keys()))

    for char in all_chars:
        # Calculate the difference in counts for each character
        deletions += abs(count1[char] - count2[char])

    return deletions


if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()

    result = makingAnagrams(s1, s2)

    print(result)
