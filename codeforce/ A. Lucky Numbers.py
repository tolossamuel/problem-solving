def luckiness(x):
    digits = [int(digit) for digit in str(x)]
    return max(digits) - min(digits)

def find_luckiest_starship(l, r):
    max_luckiness = 0
    luckiest_number = l

    for number in range(l, r + 1):
        current_luckiness = luckiness(number)
        if current_luckiness > max_luckiness:
            max_luckiness = current_luckiness
            luckiest_number = number

    return luckiest_number

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    luckiest = find_luckiest_starship(l, r)
    print(luckiest)
