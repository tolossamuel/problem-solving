# Problem: E - Word Transformation - https://codeforces.com/gym/543431/problem/E

def solve(s,d):
    heap = {}
    y = len(d) - 1
    x = len(s) - 1
    while(x >= 0 and y >= 0):
        # print(x,y,'========')
        if d[y] == s[x]:
            if (y == len(d)-1):
                
                y -= 1
                x -= 1
            else:
                if (d[y] not in heap):
                    y -= 1
                    x -= 1
                else:
                    y = len(d) - 1
        else:
            if (s[x] not in heap):
                heap[s[x]] = 0
            heap[s[x]] += 1
            x -= 1
        # print(x,y)
    if y < 0:
        print("YES")
    else:
        print("NO")
                    
t = int(input())
for _ in range(t):
    s = input().split()
    solve(s[0],s[1])  
    