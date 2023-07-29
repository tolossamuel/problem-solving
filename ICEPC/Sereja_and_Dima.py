# https://codeforces.com/problemset/problem/381/A
num = int(input())
list1 = list(map(int, input().split()))
left = 0
right = num - 1
sereja = 0
dima = 0
even_odd = 0
while(left <= right):
    if (even_odd % 2 == 0):
        if(list1[left]>list1[right]):
                sereja+=list1[left]
                left+=1
        else:
            sereja+=list1[right]
            right-=1
    else:
        if(list1[left]>list1[right]):            
            dima+=list1[left]
            left+=1
            
        else:
            dima+=list1[right]
            right-=1
    even_odd+=1
print(sereja , dima)
            