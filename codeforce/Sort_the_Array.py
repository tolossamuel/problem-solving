# Description of the problem can be found at http://codeforces.com/problemset/problem/451/B

n = input()
num = list(map(int, input().split()))
l = 0
a = 0
x = True

for i in range(1, len(num)):
    if x:
        if num[i] > num[i - 1]:
            if num[l] != num[a]:
                if num[i] < num[l]:
                    print("no")
                    quit()
                else:
                    x = False
            else:
                a = i
                l = i
        else:
            a += 1
    elif num[i] < num[i - 1]:
        print("no")
        quit()

if l > 0 and num[a] < num[l - 1]:
    print("no")
else:
    print("yes")
    print("%d %d" % (l + 1, a + 1))