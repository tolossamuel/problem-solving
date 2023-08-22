n = int(input())
list1 = list(map(int,input().split()))
list1.sort()
index = len(list1)
if list1[index-2] + list1[index-3] > list1[index-1]:
    list1[index-2], list1[index-3] = list1[index-3] , list1[index-2]
    print("YES")
    print(* list1)
else:
    print("NO")