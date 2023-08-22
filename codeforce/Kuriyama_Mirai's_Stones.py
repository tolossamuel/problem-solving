n = int(input())
list_num1 = list(map(int, input().split()))
list_num = list_num1.copy()
list_num.sort()
list1 = list()
list2 = list()
list1.append(list_num1[0])
list2.append(list_num[0])
for i in range(1, n):
    list1.append(list1[i - 1] + list_num1[i])
    list2.append(list2[i - 1] + list_num[i])
for _ in range(int(input())):
    t, l, r = map(int, input().split())
    if t == 1:
        if l == 1:
            print(list1[r - 1])
        else:
            print(list1[r - 1] - list1[l - 2])
    else:
        if l == 1:
            print(list2[r - 1])
        else:
            print(list2[r - 1] - list2[l - 2])