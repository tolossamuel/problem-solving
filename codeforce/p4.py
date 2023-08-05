n = int(input())
num = list(map(int,(input().split())))
checker = num.copy()
for i in range(n-1):
    for y in range(i+1,n,+1):
        checker[i],checker[y] = checker[y], checker[i]
        if checker:
            print(f"YES\n{checker[y]} {checker[i]}")
            quit()
        checker = num.copy()
print("NO")