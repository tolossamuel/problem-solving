a, b=map(int, input().split())
list1=list(map(int, input().split()))
list2=list(map(int, input().split()))
list1.sort()
j=0 
count=0

for i in list2:
    while j < a and list1[j] <= i:
        count+= 1
        j+= 1
    print(count, end=" ")

