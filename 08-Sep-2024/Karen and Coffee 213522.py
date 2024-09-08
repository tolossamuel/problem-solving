# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

def solve(n,k,q):
    arr = [0] * 200001
    for x in range(n):
        a,b = map(int, input().split())
        arr[a-1] += 1
        arr[b] -= 1
   
    for x in range(len(arr)-1):
        arr[x+1] += arr[x]
 
    counter = [0] * 200001
    for x in range(len(arr)):
        if arr[x] >= q:
            counter[x] = 1
    for x in range(1,len(counter)):
        counter[x] += counter[x-1]
    # print(counter)
    for x in range(k):
        a,b = map(int, input().split())
        if a == 1:
            print(counter[b-1])
        else:
            print(counter[b-1] - counter[a-2])
n,q,k = map(int, input().split())

solve(n,k,q)