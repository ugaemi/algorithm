def checkMagazine(magazine, note):
    from collections import Counter

    # Count the frequency of each word in the magazine and the note
    magazine_count = Counter(magazine)
    note_count = Counter(note)

    # Check if each word in the note can be formed from the magazine
    for word in note_count:
        if note_count[word] > magazine_count.get(word, 0):
            print("No")
            return

    print("Yes")


if __name__ == '__main__':
    import sys

    input = sys.stdin.read
    data = input().splitlines()

    # Read the first line for the number of words in magazine and note
    m, n = map(int, data[0].split())

    # Read the second line for the magazine words
    magazine = data[1].split()

    # Read the third line for the note words
    note = data[2].split()

    # Check if the note can be formed from the magazine
    checkMagazine(magazine, note)
