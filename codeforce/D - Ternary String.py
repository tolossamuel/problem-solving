import sys
from sys import maxsize

test_cases = int(sys.stdin.readline().strip())

for _ in range(test_cases):
    input_text = sys.stdin.readline().strip()

    index = [0] * 3
    count = maxsize
    left = 0

    for right in range(len(input_text)):
        pos = ord(input_text[right]) - 49
        index[pos] += 1

        while index[ord(input_text[left]) - 49] > 1:
            index[ord(input_text[left]) - 49] -= 1
            left += 1

        if index[0] != 0 and index[1] != 0 and index[2] != 0:
            count = min(count, right - left + 1)

    print(0 if count == maxsize else count)
