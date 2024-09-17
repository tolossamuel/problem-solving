# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

def solve(x,s):
    num1 = ["9"] * x
    num2 = ["1"] + ["0"]*(x-1)
    first = 9 * x
    small = 1
    i = len(num1)-1
    while(first > s):
        if (first - s) > 9:
            first -= 9
            num1[i] = "0"
            i -= 1
        else:
            dif = (9 - (first - s))
            first -= (first - s)
            num1[i] = str(dif)
            break
        if i < 0:
            break
    i = len(num2)-1
    while(small < s):
        if (s - small) > 9:
            small += 9
            num2[i] = "9"
            i -= 1
        else:
            dif = (s - small)
            small += (s - small)
            num2[i] = str(dif + int(num2[i]))
            break
        if i < 0:
            break
    num1 = int("".join(num1))
    num2 = int("".join(num2))
    if s == 0 and x == 1:
        print(0,0)
    elif s == 0 and x > 1:
        print(-1,-1)
    elif small != s or first != s:
        print(-1,-1)
    else:
        print(num2,num1)
x,s = map(int,input().split())

solve(x,s)
        